/* HARZ QR — zero-dependency QR Code encoder (byte mode, ECC level L, versions 1-9)
 * Same file is used by the browser app and the node test harness (byte-identical).
 * Placement algorithms follow the reference qrcode-generator layout (Arase),
 * re-implemented from scratch for HARZ. Sep 2026.
 */
(function (root, factory) {
  if (typeof module !== 'undefined' && module.exports) { module.exports = factory(); }
  else { root.HarzQR = factory(); }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // ---- GF(256) arithmetic (primitive poly 0x11d, alpha=2) ----
  var EXP = new Array(512), LOG = new Array(256);
  (function () {
    var x = 1;
    for (var i = 0; i < 255; i++) { EXP[i] = x; LOG[x] = i; x <<= 1; if (x & 0x100) x ^= 0x11d; }
    for (var j = 255; j < 512; j++) EXP[j] = EXP[j - 255];
  })();
  function gmul(a, b) { if (a === 0 || b === 0) return 0; return EXP[LOG[a] + LOG[b]]; }
  function polyMul(a, b) {
    var r = new Array(a.length + b.length - 1).fill(0);
    for (var i = 0; i < a.length; i++) for (var j = 0; j < b.length; j++) r[i + j] ^= gmul(a[i], b[j]);
    return r;
  }
  function rsGen(n) { var g = [1]; for (var i = 0; i < n; i++) g = polyMul(g, [1, EXP[i]]); return g; }
  function rsRem(data, nEc) {
    var g = rsGen(nEc);
    var buf = data.slice().concat(new Array(nEc).fill(0));
    for (var i = 0; i < data.length; i++) {
      var c = buf[i];
      if (c !== 0) { for (var j = 1; j < g.length; j++) buf[i + j] ^= gmul(g[j], c); }
    }
    return buf.slice(data.length);
  }

  // ---- tables: ECC level L ----
  // version -> [numBlocks, dataCwPerBlock, eccCwPerBlock]
  // verified against the reference block table (qrcode.base.rs_blocks, ECC L), Sep 11
  var L_BLOCKS = {
    1: [1, 19, 7], 2: [1, 34, 10], 3: [1, 55, 15],
    4: [1, 80, 20], 5: [1, 108, 26], 6: [2, 68, 18],
    7: [2, 78, 20], 8: [2, 97, 24], 9: [2, 116, 30]
  };
  var ALIGN = {
    2: [6, 18], 3: [6, 22], 4: [6, 26], 5: [6, 30], 6: [6, 34],
    7: [6, 22, 38], 8: [6, 24, 42], 9: [6, 26, 46]
  };
  function dataCwTotal(v) { var b = L_BLOCKS[v]; return b[0] * b[1]; }
  function byteCapacity(v) { return dataCwTotal(v) - 2; } // 12-bit header for v1-9
  function pickVersion(len) {
    for (var v = 1; v <= 9; v++) if (len <= byteCapacity(v)) return v;
    throw new Error('payload too large for QR v9-L: ' + len + ' bytes (max ' + byteCapacity(9) + ')');
  }

  // ---- bit stream (byte mode, ECC L, terminator + padding) ----
  function buildCodewords(bytes, v) {
    var b = L_BLOCKS[v], nBlocks = b[0], dPer = b[1], ePer = b[2];
    var dTotal = nBlocks * dPer;
    var bits = [];
    function push(val, n) { for (var i = n - 1; i >= 0; i--) bits.push((val >> i) & 1); }
    push(4, 4); push(bytes.length, 8);
    for (var i = 0; i < bytes.length; i++) push(bytes[i], 8);
    var capBits = dTotal * 8;
    for (var t = 0; t < 4 && bits.length < capBits; t++) bits.push(0);
    while (bits.length % 8 !== 0) bits.push(0);
    var padToggle = 0;
    while (bits.length < capBits) { push(padToggle ? 0x11 : 0xEC, 8); padToggle ^= 1; }
    var dataCw = [];
    for (var k = 0; k < bits.length; k += 8) {
      var by = 0; for (var q = 0; q < 8; q++) by = (by << 1) | bits[k + q];
      dataCw.push(by);
    }
    var blocks = [], eccs = [];
    for (var bl = 0; bl < nBlocks; bl++) {
      var chunk = dataCw.slice(bl * dPer, (bl + 1) * dPer);
      blocks.push(chunk);
      eccs.push(rsRem(chunk, ePer));
    }
    var out = [];
    for (var c = 0; c < dPer; c++) for (var bl2 = 0; bl2 < nBlocks; bl2++) out.push(blocks[bl2][c]);
    for (var c2 = 0; c2 < ePer; c2++) for (var bl3 = 0; bl3 < nBlocks; bl3++) out.push(eccs[bl3][c2]);
    return out;
  }

  // ---- BCH helpers (reference algorithm) ----
  function bchDigit(x) { var n = 0; while (x !== 0) { n++; x >>>= 1; } return n; }
  function bchTypeInfo(data) {
    var d = data << 10;
    while (bchDigit(d) - bchDigit(0x537) >= 0) { d ^= (0x537 << (bchDigit(d) - bchDigit(0x537))); }
    return ((data << 10) | d) ^ 0x5412;
  }
  function bchTypeNumber(data) {
    var d = data << 12;
    while (bchDigit(d) - bchDigit(0x1f25) >= 0) { d ^= (0x1f25 << (bchDigit(d) - bchDigit(0x1f25))); }
    return ((data << 12) | d);
  }

  function encode(text) {
    var bytes = (typeof TextEncoder !== 'undefined')
      ? new TextEncoder().encode(text)
      : Buffer.from(text, 'utf8');
    var v = pickVersion(bytes.length);
    var size = 17 + 4 * v;
    var codewords = buildCodewords(bytes, v);

    // ---- matrix ----
    var m = []; for (var r = 0; r < size; r++) m.push(new Array(size).fill(null));

    // finder + separators
    function finder(top, left) {
      for (var dr = -1; dr <= 7; dr++) for (var dc = -1; dc <= 7; dc++) {
        var r0 = top + dr, c0 = left + dc;
        if (r0 < 0 || r0 >= size || c0 < 0 || c0 >= size) continue;
        var dark = (dr >= 0 && dr <= 6 && dc >= 0 && dc <= 6) &&
          (dr === 0 || dr === 6 || dc === 0 || dc === 6 || (dr >= 2 && dr <= 4 && dc >= 2 && dc <= 4));
        m[r0][c0] = dark ? 1 : 0;
      }
    }
    finder(0, 0); finder(0, size - 7); finder(size - 7, 0);

    // timing
    for (var i = 8; i < size - 8; i++) {
      m[6][i] = (i % 2 === 0) ? 1 : 0;
      m[i][6] = (i % 2 === 0) ? 1 : 0;
    }

    // alignment
    var ap = ALIGN[v] || [];
    for (var a1 = 0; a1 < ap.length; a1++) for (var a2 = 0; a2 < ap.length; a2++) {
      var cr = ap[a1], cc = ap[a2];
      if ((cr <= 8 && cc <= 8) || (cr <= 8 && cc >= size - 9) || (cr >= size - 9 && cc <= 8)) continue;
      for (var dr2 = -2; dr2 <= 2; dr2++) for (var dc2 = -2; dc2 <= 2; dc2++) {
        m[cr + dr2][cc + dc2] = (dr2 === 0 && dc2 === 0) ? 1 :
          ((Math.abs(dr2) === 2 || Math.abs(dc2) === 2) ? 1 : 0);
      }
    }

    // free-cell map (true = data region) — reserved cells get false
    var freeMap = []; for (var r2 = 0; r2 < size; r2++) freeMap.push(new Array(size).fill(true));
    function mark(rw, cl) { if (rw >= 0 && rw < size && cl >= 0 && cl < size) freeMap[rw][cl] = false; }
    for (var fr = -1; fr <= 7; fr++) for (var fc = -1; fc <= 7; fc++) {
      mark(fr, fc); mark(fr, size - 7 + fc); mark(size - 7 + fr, fc);
    }
    for (var t2 = 8; t2 < size - 8; t2++) { mark(6, t2); mark(t2, 6); }
    var ap2 = ALIGN[v] || [];
    for (var b1 = 0; b1 < ap2.length; b1++) for (var b2 = 0; b2 < ap2.length; b2++) {
      var ar = ap2[b1], ac2 = ap2[b2];
      if ((ar <= 8 && ac2 <= 8) || (ar <= 8 && ac2 >= size - 9) || (ar >= size - 9 && ac2 <= 8)) continue;
      for (var dr3 = -2; dr3 <= 2; dr3++) for (var dc3 = -2; dc3 <= 2; dc3++) mark(ar + dr3, ac2 + dc3);
    }
    // format areas (both copies) + dark module
    for (var f1 = 0; f1 < 15; f1++) {
      if (f1 < 6) mark(f1, 8);
      else if (f1 < 8) mark(f1 + 1, 8);
      else mark(size - 15 + f1, 8);
    }
    for (var f2 = 0; f2 < 15; f2++) {
      if (f2 < 8) mark(8, size - 1 - f2);
      else if (f2 === 8) mark(8, 7);
      else mark(8, 14 - f2);
    }
    mark(size - 8, 8);
    // version areas (v >= 7)
    if (v >= 7) {
      for (var vi = 0; vi < 18; vi++) {
        mark(Math.floor(vi / 3), vi % 3 + size - 11);
        mark(vi % 3 + size - 11, Math.floor(vi / 3));
      }
    }

    // data placement (zigzag) + mask 0 applied during placement
    var totalBits = codewords.length * 8, bitIdx = 0;
    var col = size - 1, up = true;
    while (col > 0) {
      if (col === 6) col = 5; // skip timing column
      for (var rr = 0; rr < size; rr++) {
        var row = up ? (size - 1 - rr) : rr;
        for (var cOff = 0; cOff < 2; cOff++) {
          var c2 = col - cOff;
          if (freeMap[row][c2]) {
            var bit = (bitIdx < totalBits) ? ((codewords[bitIdx >> 3] >> (7 - (bitIdx & 7))) & 1) : 0;
            if ((row + c2) % 2 === 0) bit ^= 1; // mask pattern 0
            m[row][c2] = bit;
            bitIdx++;
          }
        }
      }
      up = !up; col -= 2;
    }

    // format info: ECC L (01) + mask 0 -> data = (1 << 3) | 0 = 8
    var fmt = bchTypeInfo(8);
    for (var fi = 0; fi < 15; fi++) {
      var fb = (fmt >> fi) & 1;
      if (fi < 6) m[fi][8] = fb;
      else if (fi < 8) m[fi + 1][8] = fb;
      else m[size - 15 + fi][8] = fb;
      if (fi < 8) m[8][size - 1 - fi] = fb;
      else if (fi === 8) m[8][7] = fb;
      else m[8][14 - fi] = fb;
    }

    // version info blocks (v >= 7)
    if (v >= 7) {
      var vb = bchTypeNumber(v);
      for (var vj = 0; vj < 18; vj++) {
        var vbit = (vb >> vj) & 1;
        m[Math.floor(vj / 3)][vj % 3 + size - 11] = vbit;
        m[vj % 3 + size - 11][Math.floor(vj / 3)] = vbit;
      }
    }

    // dark module
    m[size - 8][8] = 1;

    return {
      version: v, size: size, modules: m,
      capacityUsed: bytes.length, capacityMax: byteCapacity(v)
    };
  }

  return {
    encode: encode,
    byteCapacity: byteCapacity,
    pickVersion: pickVersion
  };
});
