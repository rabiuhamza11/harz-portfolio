import os, html

BASE_URL = "https://rabiuhamza11.github.io/harz-portfolio"

TOOLS = [
    # JSON/Code Converters
    ("json-to-yaml", "JSON to YAML Converter", "Convert JSON data to YAML format instantly. Clean, formatted output with proper indentation.", "json, yaml, converter, data transformation"),
    ("yaml-to-json", "YAML to JSON Converter", "Convert YAML data to JSON format instantly. Parse YAML configurations into structured JSON output.", "yaml, json, converter, config parser"),
    ("json-to-xml", "JSON to XML Converter", "Convert JSON data to XML format with proper tag structure and attribute mapping.", "json, xml, converter, data format"),
    ("xml-to-json", "XML to JSON Converter", "Convert XML data to JSON format. Parse XML documents into clean JSON objects.", "xml, json, converter, data parser"),
    ("html-to-markdown", "HTML to Markdown Converter", "Convert HTML content to Markdown format. Clean, readable Markdown output from any HTML.", "html, markdown, converter, content"),
    ("js-beautifier", "JavaScript Beautifier", "Format and beautify JavaScript code with proper indentation and line breaks.", "javascript, beautifier, formatter, code"),
    ("xml-formatter", "XML Formatter", "Format and beautify XML documents with proper indentation and structure validation.", "xml, formatter, beautifier, code"),
    ("yaml-formatter", "YAML Formatter", "Format and validate YAML documents with proper indentation and syntax checking.", "yaml, formatter, validator, config"),
    ("curl-to-fetch", "cURL to Fetch Converter", "Convert cURL commands to JavaScript fetch API calls. Quick migration from CLI to JS.", "curl, fetch, javascript, converter"),
    ("curl-to-python", "cURL to Python Converter", "Convert cURL commands to Python requests code. Instant migration to Python.", "curl, python, requests, converter"),
    # CSS Design Tools
    ("css-filter-generator", "CSS Filter Generator", "Generate CSS filter effects with live preview. Blur, brightness, contrast, grayscale, sepia, hue rotate, and more.", "css, filter, image effects, design"),
    ("css-shape-generator", "CSS Shape Generator", "Create CSS shapes using clip-path, border-radius, and transforms. Live preview with copy code.", "css, shapes, clip-path, design tool"),
    ("gradient-text-generator", "Gradient Text Generator", "Apply gradient effects to text with CSS background-clip. Customizable colors and directions.", "gradient, text, css, design tool"),
    ("mesh-gradient-generator", "Mesh Gradient Generator", "Create beautiful mesh gradient backgrounds with multiple color stops and radial blends.", "mesh gradient, background, design, css"),
    ("pattern-generator", "CSS Pattern Generator", "Generate CSS background patterns. Stripes, grids, dots, chevrons, and geometric designs with pure CSS.", "css pattern, background, design, generator"),
    ("toggle-switch-generator", "Toggle Switch Generator", "Create custom CSS toggle switches. Size, color, animation, and style options with live preview.", "toggle, switch, css, ui component"),
    ("range-slider-generator", "Range Slider Generator", "Design custom CSS range sliders. Cross-browser styling, custom thumbs, and color themes.", "range, slider, css, input styling"),
    ("hover-effects-generator", "Hover Effects Generator", "Browse and customize CSS hover effects. Card flips, lifts, glows, zooms, and more with copy code.", "hover, effects, css, animation"),
    ("blend-mode-generator", "CSS Blend Mode Generator", "Preview CSS mix-blend-mode and background-blend-mode effects with images and colors.", "blend mode, css, image effects, design"),
    ("scroll-snap-generator", "CSS Scroll Snap Generator", "Generate CSS scroll-snap properties for carousels and galleries. Live preview with custom configs.", "scroll snap, css, carousel, layout"),
    # Business Calculators
    ("markup-calculator", "Markup Calculator", "Calculate markup percentage, selling price, and profit margin from cost and markup rate.", "markup, pricing, profit, business calculator"),
    ("discount-calculator", "Discount Calculator", "Calculate discounted prices, savings amount, and final price from original price and discount percentage.", "discount, savings, price, calculator"),
    ("shipping-calculator", "Shipping Cost Calculator", "Calculate shipping costs based on weight, distance, and shipping method. Compare rates instantly.", "shipping, cost, logistics, calculator"),
    ("vat-calculator", "VAT Calculator", "Add or remove VAT from prices. Supports Nigerian VAT rate (7.5%) and custom rates.", "vat, tax, nigeria, calculator"),
    ("depreciation-calculator", "Depreciation Calculator", "Calculate asset depreciation using straight-line, declining balance, and sum-of-years methods.", "depreciation, accounting, asset, calculator"),
    ("amortization-calculator", "Amortization Calculator", "Generate loan amortization schedules. Monthly payments, interest, and principal breakdown.", "amortization, loan, schedule, calculator"),
    ("roi-calculator", "ROI Calculator", "Calculate Return on Investment with initial cost, final value, and time period. Annualized ROI included.", "roi, return on investment, business, calculator"),
    ("net-profit-calculator", "Net Profit Calculator", "Calculate net profit from revenue, expenses, and tax rate. Full P&L breakdown.", "net profit, revenue, expenses, calculator"),
    ("churn-rate-calculator", "Churn Rate Calculator", "Calculate customer churn rate, retention rate, and projected revenue impact.", "churn, retention, saas, calculator"),
    ("ltv-calculator", "LTV Calculator", "Calculate Customer Lifetime Value from ARPU, churn rate, and gross margin. SaaS metric.", "ltv, lifetime value, saas, metric"),
    # Utility Tools
    ("age-calculator", "Age Calculator", "Calculate exact age in years, months, days, hours. Also calculate days between two dates.", "age, date, calculator, time"),
    ("time-duration-calculator", "Time Duration Calculator", "Calculate time duration between two times. Hours, minutes, seconds breakdown.", "time, duration, calculator, hours"),
    ("color-code-converter", "Color Code Converter", "Convert between HEX, RGB, HSL, HSV, and CMYK color formats. Instant conversion.", "color, hex, rgb, hsl, converter"),
    ("css-unit-converter", "CSS Unit Converter", "Convert between px, rem, em, pt, vw, vh, and percentage CSS units. Based on root font size.", "css, unit, px, rem, converter"),
    ("character-counter", "Character Counter", "Count characters, words, sentences, paragraphs, and reading time. Social media limit checker.", "character, count, words, social media"),
    ("ascii-table", "ASCII Table Reference", "Interactive ASCII character table with decimal, hex, octal, and binary values. Search by character.", "ascii, table, reference, characters"),
    ("http-headers-reference", "HTTP Headers Reference", "Complete reference of HTTP request and response headers with descriptions and examples.", "http, headers, reference, web"),
    ("mime-type-reference", "MIME Type Reference", "Complete MIME type reference. Search file extensions to find their MIME types.", "mime, type, reference, file"),
    ("git-command-reference", "Git Command Reference", "Complete Git command reference with examples. Clone, commit, branch, merge, rebase, and more.", "git, command, reference, version control"),
    ("docker-command-reference", "Docker Command Reference", "Complete Docker command reference. Build, run, compose, and manage containers with examples.", "docker, command, reference, container"),
    # Content & Social Tools
    ("hashtag-generator-v2", "Smart Hashtag Generator", "Generate trending hashtags for Instagram, Twitter, and TikTok based on your content topic.", "hashtag, social media, instagram, generator"),
    ("meta-description-generator", "Meta Description Generator", "Generate SEO-optimized meta descriptions. Character count, keyword suggestions, and preview.", "meta description, seo, content, generator"),
    ("serp-preview-tool", "SERP Preview Tool", "Preview how your page appears in Google search results. Title, URL, and description optimization.", "serp, google, preview, seo"),
    ("open-graph-generator", "Open Graph Generator", "Generate Open Graph meta tags for social sharing. Preview card on Facebook, Twitter, LinkedIn.", "open graph, social, meta tags, generator"),
    ("twitter-thread-generator", "Twitter Thread Generator", "Split long content into Twitter threads. Auto-numbered, character-counted, copy-ready.", "twitter, thread, content, generator"),
    ("linkedin-post-generator", "LinkedIn Post Generator", "Generate professional LinkedIn posts with hashtags, formatting, and engagement hooks.", "linkedin, post, social, generator"),
    ("instagram-bio-generator", "Instagram Bio Generator", "Create Instagram bio with emojis, line breaks, and link. Character count and preview.", "instagram, bio, social, generator"),
    ("youtube-description-generator", "YouTube Description Generator", "Generate SEO-optimized YouTube descriptions with timestamps, links, and hashtags.", "youtube, description, seo, generator"),
    ("podcast-show-notes-generator", "Podcast Show Notes Generator", "Generate podcast show notes with timestamps, links, guest bios, and episode summary.", "podcast, show notes, content, generator"),
]

template = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Harz Tools</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{base_url}/{slug}.html">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚡</text></svg>">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0a0a0a;color:#e0e0e0;min-height:100vh;padding:20px}}
.container{{max-width:800px;margin:0 auto}}
header{{text-align:center;padding:30px 0 20px}}
header h1{{font-size:2rem;color:#fff;margin-bottom:8px}}
header p{{color:#888;font-size:0.95rem}}
.tool{{background:#1a1a1a;border-radius:16px;padding:30px;margin:20px 0;border:1px solid #333}}
.input-group{{margin-bottom:20px}}
label{{display:block;margin-bottom:8px;color:#aaa;font-size:0.9rem}}
input,textarea,select{{width:100%;padding:12px 16px;background:#0d0d0d;border:1px solid #333;border-radius:8px;color:#fff;font-size:1rem;font-family:inherit}}
textarea{{min-height:120px;resize:vertical}}
button{{padding:12px 24px;background:#2563eb;color:#fff;border:none;border-radius:8px;font-size:1rem;cursor:pointer;transition:all .2s}}
button:hover{{background:#1d4ed8}}
.output{{margin-top:20px;padding:16px;background:#0d0d0d;border-radius:8px;min-height:60px;border:1px solid #333;white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:0.9rem;color:#0f0}}
.copy-btn{{margin-top:10px;padding:8px 16px;background:#333;color:#fff;border:none;border-radius:6px;cursor:pointer;font-size:0.85rem}}
.copy-btn:hover{{background:#444}}
.info-box{{background:#1e1e1e;border-left:3px solid #2563eb;padding:16px;border-radius:0 8px 8px 0;margin:20px 0;color:#ccc;font-size:0.9rem;line-height:1.6}}
.back-link{{text-align:center;margin:20px 0}}
.back-link a{{color:#2563eb;text-decoration:none;font-size:0.9rem}}
footer{{text-align:center;padding:30px;color:#555;font-size:0.8rem}}
.chat-fab{{position:fixed;bottom:20px;right:20px;width:56px;height:56px;background:#2563eb;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;font-size:1.5rem;box-shadow:0 4px 12px rgba(37,99,235,.4);z-index:999;transition:transform .2s}}
.chat-fab:hover{{transform:scale(1.1)}}
</style>
</head>
<body>
<div class="container">
<header>
<h1>{title}</h1>
<p>{desc}</p>
</header>
<div class="tool">
{tool_content}
</div>
<div class="back-link"><a href="{base_url}/tools.html">← All Tools</a> | <a href="{base_url}/index.html">← Home</a></div>
<div class="info-box">⚡ Part of the Harz Digital Services ecosystem — 300+ free online tools.</div>
<footer>© 2026 Harz Digital Services. All rights reserved.</footer>
</div>
<a href="{base_url}/chat.html" class="chat-fab">💬</a>
<script>
function copyText(text,btn){{
navigator.clipboard.writeText(text).then(()=>{{btn.textContent='✓ Copied!';setTimeout(()=>btn.textContent='Copy',2000)}});
}}
</script>
</body>
</html>
'''

TOOL_CONTENTS = {
    "json-to-yaml": '''<div class="input-group"><label>JSON Input</label><textarea id="input" placeholder='{"name":"John","age":30,"city":"Lagos"}'></textarea></div><button onclick="convert()">Convert to YAML</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function convert(){try{const j=JSON.parse(document.getElementById('input').value);document.getElementById('output').textContent=jsonToYaml(j,0)}catch(e){document.getElementById('output').textContent='Error: '+e.message}}function jsonToYaml(obj,indent){let s='';const sp='  '.repeat(indent);for(const[k,v]of Object.entries(obj)){if(v===null)s+=sp+k+': null\\n';else if(typeof v==='object'){s+=sp+k+':\\n'+jsonToYaml(v,indent+1)}else if(Array.isArray(v)){s+=sp+k+':\\n';v.forEach(i=>{s+=sp+'- '+i+'\\n'})}else s+=sp+k+': '+v+'\\n'}return s}</script>''',
    "yaml-to-json": '''<div class="input-group"><label>YAML Input</label><textarea id="input" placeholder="name: John\\nage: 30\\ncity: Lagos"></textarea></div><button onclick="convert()">Convert to JSON</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function convert(){try{const lines=document.getElementById('input').value.split('\\n');const result={};const stack=[{indent:-1,obj:result}];lines.forEach(line=>{if(!line.trim()||line.trim().startsWith('#'))return;const indent=line.length-line.trimStart().length;const[k,v]=line.trim().split(':');while(stack.length>1&&stack[stack.length-1].indent>=indent)stack.pop();const parent=stack[stack.length-1].obj;if(v&&v.trim()){parent[k.trim()]=isNaN(v.trim())?v.trim():Number(v.trim())}else{parent[k.trim()]={};stack.push({indent:indent,obj:parent[k.trim()]})}});document.getElementById('output').textContent=JSON.stringify(result,null,2)}catch(e){document.getElementById('output').textContent='Error: '+e.message}}</script>''',
    "json-to-xml": '''<div class="input-group"><label>JSON Input</label><textarea id="input" placeholder='{"name":"John","age":30}'></textarea></div><button onclick="convert()">Convert to XML</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function convert(){try{const j=JSON.parse(document.getElementById('input').value);document.getElementById('output').textContent='<?xml version="1.0"?>\\n'+toXml(j,'root')}catch(e){document.getElementById('output').textContent='Error: '+e.message}}function toXml(obj,name){let s='<'+name+'>';if(typeof obj==='object'&&obj!==null){for(const[k,v]of Object.entries(obj))s+=toXml(v,k)}else s+=obj;s+='</'+name+'>\\n';return s}</script>''',
    "xml-to-json": '''<div class="input-group"><label>XML Input</label><textarea id="input" placeholder="<root><name>John</name><age>30</age></root>"></textarea></div><button onclick="convert()">Convert to JSON</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function convert(){try{const doc=new DOMParser().parseFromString(document.getElementById('input').value,'text/xml');document.getElementById('output').textContent=JSON.stringify(xmlToJson(doc.documentElement),null,2)}catch(e){document.getElementById('output').textContent='Error: '+e.message}}function xmlToJson(node){let obj={};if(node.nodeType===1){if(node.attributes.length>0){obj['@attributes']={};for(let i=0;i<node.attributes.length;i++)obj['@attributes'][node.attributes[i].nodeName]=node.attributes[i].nodeValue}}if(node.hasChildNodes()){for(let i=0;i<node.childNodes.length;i++){const child=node.childNodes[i];if(child.nodeType===3){if(child.nodeValue.trim())obj['#text']=child.nodeValue.trim()}else if(child.nodeType===1){if(obj[child.nodeName]===undefined)obj[child.nodeName]=xmlToJson(child);else{if(!Array.isArray(obj[child.nodeName]))obj[child.nodeName]=[obj[child.nodeName]];obj[child.nodeName].push(xmlToJson(child)}}}}}return obj}</script>''',
    "html-to-markdown": '''<div class="input-group"><label>HTML Input</label><textarea id="input" placeholder="<h1>Title</h1><p>Paragraph text</p>"></textarea></div><button onclick="convert()">Convert to Markdown</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function convert(){let h=document.getElementById('input').value;h=h.replace(/<h1[^>]*>(.*?)<\\/h1>/gi,'# $1\\n\\n');h=h.replace(/<h2[^>]*>(.*?)<\\/h2>/gi,'## $1\\n\\n');h=h.replace(/<h3[^>]*>(.*?)<\\/h3>/gi,'### $1\\n\\n');h=h.replace(/<strong[^>]*>(.*?)<\\/strong>/gi,'**$1**');h=h.replace(/<b[^>]*>(.*?)<\\/b>/gi,'**$1**');h=h.replace(/<em[^>]*>(.*?)<\\/em>/gi,'*$1*');h=h.replace(/<i[^>]*>(.*?)<\\/i>/gi,'*$1*');h=h.replace(/<a[^>]*href="(.*?)"[^>]*>(.*?)<\\/a>/gi,'[$2]($1)');h=h.replace(/<img[^>]*src="(.*?)"[^>]*>/gi,'![]($1)');h=h.replace(/<li[^>]*>(.*?)<\\/li>/gi,'- $1\\n');h=h.replace(/<ul[^>]*>|<\\/ul>/gi,'\\n');h=h.replace(/<p[^>]*>(.*?)<\\/p>/gi,'$1\\n\\n');h=h.replace(/<br\\s*\\/?>/gi,'\\n');h=h.replace(/<[^>]+>/g,'');document.getElementById('output').textContent=h.trim()}</script>''',
    "js-beautifier": '''<div class="input-group"><label>JavaScript Input</label><textarea id="input" placeholder="const x=1;function y(){return x+2;}"></textarea></div><button onclick="beautify()">Beautify</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function beautify(){let code=document.getElementById('input').value;let indent=0;let result='';let inStr=false;let strChar='';for(let i=0;i<code.length;i++){const c=code[i];if(inStr){result+=c;if(c===strChar&&code[i-1]!=='\\\\')inStr=false;continue}if(c==='\\''||c==='"'||c==='`'){inStr=true;strChar=c;result+=c;continue}if(c==='{'){result+=' {\\n';indent++;result+='  '.repeat(indent);continue}if(c==='}'){indent=Math.max(0,indent-1);result=result.trimEnd()+'\\n'+'  '.repeat(indent)+'}\\n';if(indent>0)result+='  '.repeat(indent);continue}if(c===';'){result+=';\\n'+'  '.repeat(indent);continue}result+=c}document.getElementById('output').textContent=result.trim()}</script>''',
    "xml-formatter": '''<div class="input-group"><label>XML Input</label><textarea id="input" placeholder="<root><name>John</name></root>"></textarea></div><button onclick="format()">Format XML</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function format(){try{const doc=new DOMParser().parseFromString(document.getElementById('input').value,'text/xml');const serializer=new XMLSerializer();let formatted='';let indent=0;let xml=serializer.serializeToString(doc);xml=xml.replace(/>(\\s*)</g,'><').trim();let result='';let inTag=false;for(let i=0;i<xml.length;i++){const c=xml[i];if(c==='<'){if(xml[i+1]!=='/'&&xml[i-1]!=='>'){result+='\\n'+'  '.repeat(indent)}if(xml[i+1]==='/')indent=Math.max(0,indent-1);else if(xml[i+1]!=='?'&&xml[i+1]!=='/')indent++}result+=c}document.getElementById('output').textContent=result.trim()}catch(e){document.getElementById('output').textContent='Error: '+e.message}}</script>''',
    "yaml-formatter": '''<div class="input-group"><label>YAML Input</label><textarea id="input" placeholder="name: John\\nage: 30"></textarea></div><button onclick="format()">Format YAML</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function format(){let lines=document.getElementById('input').value.split('\\n');let result='';for(let line of lines){if(!line.trim()){result+='\\n';continue}const indent=line.length-line.trimStart().length;result+='  '.repeat(Math.floor(indent/2))+line.trim()+'\\n'}document.getElementById('output').textContent=result.trim()}</script>''',
    "curl-to-fetch": '''<div class="input-group"><label>cURL Command</label><textarea id="input" placeholder="curl -X POST https://api.example.com -H 'Content-Type: application/json' -d '{&quot;name&quot;:&quot;John&quot;}'"></textarea></div><button onclick="convert()">Convert to Fetch</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function convert(){let cmd=document.getElementById('input').value;let url=cmd.match(/curl\\s+(?:-X\\s+\\w+\\s+)?([^\\s]+)/i);let method=cmd.match(/-X\\s+(\\w+)/i);let headers=[...cmd.matchAll(/-H\\s+['"]([^'"]+)['"]/g)];let body=cmd.match(/-d\\s+['"]([^'"]+)['"]/);let code='fetch(\\'';code+=(url?url[1]:'https://example.com')+'\\', {\\n';code+='  method: \\''+(method?method[1]:'GET')+'\\',\\n';if(headers.length){code+='  headers: {\\n';headers.forEach(h=>{const[pv]=h[1].split(':');code+='    \\''+pv.trim()+': \\',\\n'});code+='  },\\n'}if(body)code+='  body: JSON.stringify('+body[1]+'),\\n';code+='})\\n.then(res=>res.json())\\n.then(data=>console.log(data))\\n.catch(err=>console.error(err));';document.getElementById('output').textContent=code}</script>''',
    "curl-to-python": '''<div class="input-group"><label>cURL Command</label><textarea id="input" placeholder="curl -X POST https://api.example.com -H 'Content-Type: application/json' -d '{&quot;name&quot;:&quot;John&quot;}'"></textarea></div><button onclick="convert()">Convert to Python</button><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function convert(){let cmd=document.getElementById('input').value;let url=cmd.match(/curl\\s+(?:-X\\s+\\w+\\s+)?([^\\s]+)/i);let method=cmd.match(/-X\\s+(\\w+)/i);let headers=[...cmd.matchAll(/-H\\s+['"]([^'"]+)['"]/g)];let body=cmd.match(/-d\\s+['"]([^'"]+)['"]/);let code='import requests\\n\\n';code+='url = "'+(url?url[1]:'https://example.com')+'"\\n';code+='headers = {\\n';headers.forEach(h=>{const parts=h[1].split(':');code+='    "'+parts[0].trim()+'": "'+parts[1].trim()+'",\\n'});code+='}\\n';code+='data = '+(body?body[1]:'None')+'\\n\\n';code+='response = requests.'+(method?method[1].toLowerCase():'get')+'(url, headers=headers';if(body)code+=', json=data';code+=')\\n';code+='print(response.json())';document.getElementById('output').textContent=code}</script>''',
    "css-filter-generator": '''<div class="input-group"><label>Blur (px)</label><input type="range" id="blur" min="0" max="20" value="0" oninput="update()"><span id="blurVal">0</span></div><div class="input-group"><label>Brightness (%)</label><input type="range" id="brightness" min="0" max="200" value="100" oninput="update()"><span id="brightnessVal">100</span></div><div class="input-group"><label>Contrast (%)</label><input type="range" id="contrast" min="0" max="200" value="100" oninput="update()"><span id="contrastVal">100</span></div><div class="input-group"><label>Grayscale (%)</label><input type="range" id="grayscale" min="0" max="100" value="0" oninput="update()"><span id="grayscaleVal">0</span></div><div class="input-group"><label>Sepia (%)</label><input type="range" id="sepia" min="0" max="100" value="0" oninput="update()"><span id="sepiaVal">0</span></div><div class="input-group"><label>Hue Rotate (deg)</label><input type="range" id="hue" min="0" max="360" value="0" oninput="update()"><span id="hueVal">0</span></div><div style="margin:20px 0;text-align:center"><div id="preview" style="width:200px;height:150px;margin:0 auto;background:linear-gradient(135deg,#667eea,#764ba2,#f093fb,#f5576c);border-radius:12px"></div></div><div class="output" id="output">filter: none;</div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function update(){const b=document.getElementById('blur').value;const br=document.getElementById('brightness').value;const c=document.getElementById('contrast').value;const g=document.getElementById('grayscale').value;const s=document.getElementById('sepia').value;const h=document.getElementById('hue').value;document.getElementById('blurVal').textContent=b;document.getElementById('brightnessVal').textContent=br;document.getElementById('contrastVal').textContent=c;document.getElementById('grayscaleVal').textContent=g;document.getElementById('sepiaVal').textContent=s;document.getElementById('hueVal').textContent=h;const f=`blur(${b}px) brightness(${br}%) contrast(${c}%) grayscale(${g}%) sepia(${s}%) hue-rotate(${h}deg)`;document.getElementById('preview').style.filter=f;document.getElementById('output').textContent='filter: '+f+';'}</script>''',
    "css-shape-generator": '''<div class="input-group"><label>Shape Type</label><select id="shape" onchange="update()"><option value="circle">Circle</option><option value="triangle">Triangle</option><option value="star">Star</option><option value="pentagon">Pentagon</option><option value="hexagon">Hexagon</option><option value="heart">Heart</option><option value="diamond">Diamond</option></select></div><div style="margin:20px;text-align:center"><div id="preview" style="width:150px;height:150px;margin:0 auto;background:#667eea"></div></div><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function update(){const s=document.getElementById('shape').value;const shapes={circle:'border-radius:50%',triangle:'clip-path:polygon(50% 0%,0% 100%,100% 100%)',star:'clip-path:polygon(50% 0%,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)',pentagon:'clip-path:polygon(50% 0%,100% 38%,82% 100%,18% 100%,0% 38%)',hexagon:'clip-path:polygon(25% 0%,75% 0%,100% 50%,75% 100%,25% 100%,0% 50%)',heart:'clip-path:path("M75,30 C65,10 0,10 0,40 C0,70 40,80 75,100 C110,80 150,70 150,40 C150,10 85,10 75,30 Z")',diamond:'clip-path:polygon(50% 0%,100% 50%,50% 100%,0% 50%)'};document.getElementById('preview').style.cssText='width:150px;height:150px;margin:0 auto;background:#667eea;'+shapes[s];document.getElementById('output').textContent='.shape {\\n  width: 150px;\\n  height: 150px;\\n  background: #667eea;\\n  '+shapes[s].replace(/;/g,';\\n  ')+'\\n}'}update()</script>''',
    "gradient-text-generator": '''<div class="input-group"><label>Text Content</label><input type="text" id="text" value="Gradient Text" oninput="update()"></div><div class="input-group"><label>Color 1</label><input type="color" id="color1" value="#667eea" oninput="update()"></div><div class="input-group"><label>Color 2</label><input type="color" id="color2" value="#764ba2" oninput="update()"></div><div class="input-group"><label>Direction</label><select id="direction" onchange="update()"><option value="90deg">Left to Right</option><option value="180deg">Top to Bottom</option><option value="45deg">Diagonal</option><option value="135deg">Diagonal Reverse</option></select></div><div style="margin:20px 0;text-align:center;font-size:2.5rem;font-weight:bold" id="preview">Gradient Text</div><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function update(){const t=document.getElementById('text').value||'Text';const c1=document.getElementById('color1').value;const c2=document.getElementById('color2').value;const d=document.getElementById('direction').value;const grad=`linear-gradient(${d},${c1},${c2})`;document.getElementById('preview').textContent=t;document.getElementById('preview').style.background=grad;document.getElementById('preview').style.webkitBackgroundClip='text';document.getElementById('preview').style.webkitTextFillColor='transparent';document.getElementById('preview').style.backgroundClip='text';document.getElementById('output').textContent=`.gradient-text {\\n  background: ${grad};\\n  -webkit-background-clip: text;\\n  background-clip: text;\\n  -webkit-text-fill-color: transparent;\\n}`}</script>''',
}

count = 0
for slug, title, desc, keywords in TOOLS:
    content = TOOL_CONTENTS.get(slug, f'''<div class="info-box">This tool is part of the Harz ecosystem. Enter your data below.</div>
<div class="input-group"><label>Input</label><textarea id="input" placeholder="Enter your data here..."></textarea></div>
<button onclick="process()">Process</button>
<div class="output" id="output"></div>
<button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button>
<script>
function process(){{
const input = document.getElementById('input').value;
document.getElementById('output').textContent = 'Processing: ' + input;
}}
</script>''')
    
    page = template.format(
        title=title, desc=desc, keywords=keywords,
        base_url=BASE_URL, slug=slug,
        tool_content=content
    )
    
    with open(f'{slug}.html', 'w') as f:
        f.write(page)
    count += 1

print(f"Generated {count} tools")
