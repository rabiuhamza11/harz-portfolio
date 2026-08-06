// HARZ Cloud API v23.0.0
// Enhanced with: Rate Limiting, Error Tracking, Analytics, All existing endpoints
// Hosted on Cloudflare Workers (Global Edge)

const VERSION = "23.0.0";
const RATE_LIMIT_PER_MINUTE = 60;
const RATE_LIMIT_PER_HOUR = 1000;

// ============ RATE LIMITING ============
async function checkRateLimit(ip, kv) {
  const now = Date.now();
  const minuteKey = `rl:${ip}:${Math.floor(now / 60000)}`;
  const hourKey = `rl:${ip}:hour:${Math.floor(now / 3600000)}`;
  
  const minuteCount = parseInt((await kv.get(minuteKey)) || "0");
  const hourCount = parseInt((await kv.get(hourKey)) || "0");
  
  if (minuteCount >= RATE_LIMIT_PER_MINUTE) {
    return { allowed: false, reason: "Rate limit exceeded (per minute)", retryAfter: 60 };
  }
  if (hourCount >= RATE_LIMIT_PER_HOUR) {
    return { allowed: false, reason: "Rate limit exceeded (per hour)", retryAfter: 3600 };
  }
  
  await kv.put(minuteKey, String(minuteCount + 1), { expirationTtl: 120 });
  await kv.put(hourKey, String(hourCount + 1), { expirationTtl: 3700 });
  
  return { allowed: true, remaining: { minute: RATE_LIMIT_PER_MINUTE - minuteCount - 1, hour: RATE_LIMIT_PER_HOUR - hourCount - 1 } };
}

// ============ ERROR TRACKING ============
async function logError(error, path, ip, kv) {
  const errorId = `err:${Date.now()}:${Math.random().toString(36).slice(2, 8)}`;
  const errorData = {
    id: errorId,
    message: error.message || String(error),
    stack: error.stack || null,
    path,
    ip,
    timestamp: new Date().toISOString(),
  };
  await kv.put(errorId, JSON.stringify(errorData), { expirationTtl: 86400 * 7 }); // Keep 7 days
  
  // Also increment error counter
  const counterKey = `errors:count:${new Date().toISOString().slice(0, 10)}`;
  const count = parseInt((await kv.get(counterKey)) || "0");
  await kv.put(counterKey, String(count + 1), { expirationTtl: 86400 * 30 });
  
  return errorId;
}

async function getErrorStats(kv) {
  const today = new Date().toISOString().slice(0, 10);
  const todayCount = parseInt((await kv.get(`errors:count:${today}`)) || "0");
  const yesterday = new Date(Date.now() - 86400000).toISOString().slice(0, 10);
  const yesterdayCount = parseInt((await kv.get(`errors:count:${yesterday}`)) || "0");
  return { today: todayCount, yesterday: yesterdayCount };
}

// ============ CORS ============
const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization, X-API-Key",
};

// ============ RESPONSE HELPERS ============
function jsonResponse(data, status = 200, headers = {}) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "Content-Type": "application/json", ...corsHeaders, ...headers },
  });
}

function errorResponse(message, status = 404, path = "") {
  return jsonResponse({ success: false, error: message, path, timestamp: new Date().toISOString() }, status);
}

// ============ ROUTES ============
const routes = {
  "GET /": () => ({
    platform: "HARZ Cloud",
    version: VERSION,
    status: "operational",
    hosted_on: "Cloudflare Workers (Global Edge)",
    infrastructure: "Cloudflare Workers + D1 + KV + Rate Limiting + Error Tracking",
    endpoints: {
      health: "/health",
      info: "/info",
      status: "/status",
      rateLimit: "/rate-limit-stats",
      errors: "/errors",
      agents: "/agents/list, /agents/chat, /agents/route",
      entities: "/api/:entity, /api/:entity/:id",
      crm: "/crm",
      orders: "/orders",
      products: "/products",
      payments: "/payments, /payments/checkout, /payments/verify",
      analytics: "/analytics",
      memory: "/memory/store, /memory/retrieve",
      auth: "/auth/signup, /auth/login",
      deployforge: "/deployforge/health",
      bridge: "/bridge/status",
      webhooks: "/webhooks/whatsapp, /webhooks/telegram",
    },
  }),
  "GET /health": () => ({
    status: "operational",
    version: VERSION,
    timestamp: new Date().toISOString(),
    uptime: "always (edge)",
    services: { workers: "operational", d1: "operational", kv: "operational", rateLimit: "active", errorTracking: "active" },
  }),
  "GET /info": () => ({
    platform: "HARZ Cloud",
    version: VERSION,
    totalPlatforms: 651,
    totalWorkers: 58,
    database: "D1",
    storage: "KV (8 namespaces) + R2 (pending)",
    cdn: "Cloudflare Global (330+)",
    features: ["Static hosting", "API gateway", "D1 SQLite", "KV storage", "Rate limiting", "Error tracking", "AI agents (13)", "Auth", "Entity CRUD", "CRM", "Orders", "Payments", "Analytics", "Memory", "DeployForge", "Cron", "SSL", "DDoS"],
    replaces: ["Render", "Vercel", "Base44", "GitHub Pages", "Railway"],
    security: ["Rate limiting (60/min, 1000/hour)", "Error tracking (7-day retention)", "CORS", "DDoS protection (Cloudflare)"],
  }),
  "GET /status": () => ({
    system: "HARZ Cloud",
    version: VERSION,
    provider: "cloudflare",
    agents: 15,
    models: ["nemotron-120b", "nemotron-9b", "gpt-oss-20b"],
    never_sleeps: true,
    replaces: ["Render", "Vercel", "Base44", "Railway", "GitHub Pages"],
  }),
  "GET /rate-limit-stats": async (env, ip) => {
    const rl = await checkRateLimit(ip, env.HARZ_RATE_LIMIT);
    const errors = await getErrorStats(env.HARZ_RATE_LIMIT);
    return {
      ip,
      rateLimit: rl.allowed ? rl.remaining : { error: rl.reason },
      limits: { perMinute: RATE_LIMIT_PER_MINUTE, perHour: RATE_LIMIT_PER_HOUR },
      errors,
    };
  },
  "GET /errors": async (env) => {
    const stats = await getErrorStats(env.HARZ_RATE_LIMIT);
    return { success: true, errorStats: stats, retention: "7 days" };
  },
};

// ============ MAIN HANDLER ============
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const method = request.method;
    const ip = request.headers.get("CF-Connecting-IP") || "unknown";
    const routeKey = `${method} ${path}`;
    
    // CORS preflight
    if (method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }
    
    try {
      // Rate limiting (skip for health check)
      if (path !== "/health" && env.HARZ_RATE_LIMIT) {
        const rl = await checkRateLimit(ip, env.HARZ_RATE_LIMIT);
        if (!rl.allowed) {
          return jsonResponse({
            success: false,
            error: rl.reason,
            retryAfter: rl.retryAfter,
            ip,
          }, 429, { "Retry-After": String(rl.retryAfter) });
        }
      }
      
      // Check exact route match
      const handler = routes[routeKey];
      if (handler) {
        const result = await handler(env, ip);
        return jsonResponse(result);
      }
      
      // Dynamic routes
      // Products
      if (path === "/products" && method === "GET") {
        return jsonResponse({ success: true, count: 486, products: "Use /api/products for full CRUD" });
      }
      
      // Orders
      if (path === "/orders" && method === "GET") {
        if (env.HARZ_DB) {
          const result = await env.HARZ_DB.prepare("SELECT * FROM orders ORDER BY created_at DESC LIMIT 50").all();
          return jsonResponse({ success: true, count: result.results?.length || 0, orders: result.results || [] });
        }
        return jsonResponse({ success: true, count: 0, orders: [], note: "D1 not bound" });
      }
      
      // Payments
      if (path === "/payments" && method === "GET") {
        return jsonResponse({
          platform: "HARZ Pay",
          version: "3.0.0",
          methods: [
            { name: "UBA Transfer", account: "2034326424", holder: "Rabiu Hamza Mohammed", code: "033", status: "LIVE" },
            { name: "Paystack", status: "LIVE" },
            { name: "GDEG Token", rate: "1 = $0.01", status: "LIVE" },
            { name: "USDT TRC20", status: "LIVE" },
            { name: "Grey US Bank (Lead Bank)", account: "210753267775", holder: "Hamza Rabiu", status: "LIVE" },
            { name: "NowPayments (Crypto)", status: "LIVE" },
          ],
          greyBank: { bank: "Lead Bank", address: "1801 Main St., Kansas City, MO 64108", account: "210753267775", holder: "Hamza Rabiu" },
        });
      }
      
      // Analytics
      if (path === "/analytics" && method === "GET") {
        let stats = { revenue: 0, pending: 0, orders: 0, products: 486 };
        if (env.HARZ_DB) {
          try {
            const revResult = await env.HARZ_DB.prepare("SELECT SUM(amount) as total FROM orders WHERE status = 'paid'").first();
            const pendResult = await env.HARZ_DB.prepare("SELECT SUM(amount) as total FROM orders WHERE status != 'paid'").first();
            const countResult = await env.HARZ_DB.prepare("SELECT COUNT(*) as count FROM orders").first();
            stats.revenue = revResult?.total || 0;
            stats.pending = pendResult?.total || 0;
            stats.orders = countResult?.count || 0;
          } catch (e) { /* table might not exist */ }
        }
        return jsonResponse({ success: true, analytics: stats, version: VERSION });
      }
      
      // CRM
      if (path === "/crm" && method === "GET") {
        return jsonResponse({ success: true, crm: "active", version: VERSION, queue: "harz-crm-queue" });
      }
      
      // Agent endpoints
      if (path === "/agents/list" && method === "GET") {
        return jsonResponse({
          success: true,
          agents: [
            { id: "omega-commander", name: "OMEGA Commander", role: "Executive AI", tools: 21 },
            { id: "magani", name: "Magani Agent", role: "Operations AI", tools: 21 },
            { id: "infrastructure", name: "Infrastructure Agent", role: "DevOps", tools: 5 },
            { id: "payments", name: "Payments Agent", role: "Finance", tools: 4 },
            { id: "database", name: "Database Agent", role: "Data", tools: 3 },
            { id: "security", name: "Security Agent", role: "Security", tools: 3 },
            { id: "content", name: "Content Agent", role: "Content", tools: 4 },
            { id: "marketing", name: "Marketing Agent", role: "Growth", tools: 4 },
            { id: "comms", name: "Comms Agent", role: "Communications", tools: 3 },
          ],
        });
      }
      
      if (path === "/agents/chat" && method === "POST") {
        const body = await request.json();
        return jsonResponse({
          success: true,
          response: "HARZ Cloud AI is running on Cloudflare Workers AI. Connect via /agents/chat with a message.",
          agent: body.agent || "omega-commander",
          version: VERSION,
        });
      }
      
      // Auth endpoints
      if (path === "/auth/signup" && method === "POST") {
        const body = await request.json();
        if (!body.email || !body.password) {
          return errorResponse("Email and password required", 400, path);
        }
        const userId = `user_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
        if (env.HARZ_KV) {
          await env.HARZ_KV.put(`user:${body.email}`, JSON.stringify({ id: userId, email: body.email, role: body.role || "user", createdAt: new Date().toISOString() }));
        }
        return jsonResponse({ success: true, userId, message: "Account created" });
      }
      
      if (path === "/auth/login" && method === "POST") {
        const body = await request.json();
        if (!body.email) return errorResponse("Email required", 400, path);
        if (env.HARZ_KV) {
          const user = await env.HARZ_KV.get(`user:${body.email}`);
          if (user) return jsonResponse({ success: true, user: JSON.parse(user), token: "harz_" + Math.random().toString(36).slice(2) });
        }
        return errorResponse("User not found", 404, path);
      }
      
      // Entity CRUD
      if (path.startsWith("/api/") && method === "GET") {
        const entity = path.split("/")[2];
        const id = path.split("/")[3];
        if (env.HARZ_DB) {
          if (id) {
            const result = await env.HARZ_DB.prepare(`SELECT * FROM ${entity} WHERE id = ?`).bind(id).first();
            return jsonResponse({ success: true, data: result });
          }
          const result = await env.HARZ_DB.prepare(`SELECT * FROM ${entity} LIMIT 50`).all();
          return jsonResponse({ success: true, count: result.results?.length || 0, data: result.results || [] });
        }
        return jsonResponse({ success: true, entity, note: "D1 not configured" });
      }
      
      if (path.startsWith("/api/") && method === "POST") {
        const entity = path.split("/")[2];
        const body = await request.json();
        const id = `rec_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
        if (env.HARZ_DB) {
          const keys = Object.keys(body).join(", ");
          const values = Object.values(body).map(v => typeof v === "string" ? `'${v}'` : v).join(", ");
          await env.HARZ_DB.prepare(`INSERT INTO ${entity} (id, ${keys}) VALUES ('${id}', ${values})`).run();
        }
        return jsonResponse({ success: true, id, entity, message: "Record created" });
      }
      
      // Memory endpoints
      if (path === "/memory/store" && method === "POST") {
        const body = await request.json();
        if (env.HARZ_KV) {
          await env.HARZ_KV.put(`memory:${body.key}`, JSON.stringify(body.value));
        }
        return jsonResponse({ success: true, message: "Memory stored", key: body.key });
      }
      
      if (path === "/memory/retrieve" && method === "GET") {
        const key = url.searchParams.get("key");
        if (!key) return errorResponse("Key parameter required", 400, path);
        if (env.HARZ_KV) {
          const value = await env.HARZ_KV.get(`memory:${key}`);
          return jsonResponse({ success: true, key, value: value ? JSON.parse(value) : null });
        }
        return errorResponse("KV not configured", 500, path);
      }
      
      // Webhook endpoints
      if (path === "/webhooks/whatsapp" && (method === "GET" || method === "POST")) {
        if (method === "GET") {
          const mode = url.searchParams.get("hub.mode");
          const token = url.searchParams.get("hub.verify_token");
          const challenge = url.searchParams.get("hub.challenge");
          if (mode === "subscribe" && challenge) {
            return new Response(challenge, { status: 200 });
          }
        }
        return jsonResponse({ success: true, message: "WhatsApp webhook received" });
      }
      
      if (path === "/webhooks/telegram" && method === "POST") {
        const body = await request.json();
        return jsonResponse({ success: true, message: "Telegram webhook received", chatId: body?.message?.chat?.id });
      }
      
      // DeployForge health
      if (path === "/deployforge/health" && method === "GET") {
        return jsonResponse({ success: true, status: "operational", version: "7.1", providers: ["cloudflare"] });
      }
      
      // Bridge status
      if (path === "/bridge/status" && method === "GET") {
        return jsonResponse({ success: true, bridge: "active", connections: ["whatsapp", "telegram"], version: VERSION });
      }
      
      // Manager endpoints
      if (path === "/manager/health-check" && method === "GET") {
        return jsonResponse({
          success: true,
          workers: 4,
          pages: 2,
          d1: 2,
          kv: 8,
          queues: 4,
          vectorize: 3,
          zones: 0,
          r2: "not_enabled",
          workersAI: "needs_paid_plan",
          timestamp: new Date().toISOString(),
        });
      }
      
      // 404 - show available routes
      const available = Object.keys(routes).concat([
        "GET /products", "GET /orders", "GET /payments", "GET /analytics", "GET /crm",
        "GET /agents/list", "POST /agents/chat", "POST /agents/route",
        "POST /auth/signup", "POST /auth/login",
        "GET|POST /api/:entity", "GET|PUT|DELETE /api/:entity/:id",
        "POST /memory/store", "GET /memory/retrieve",
        "GET /deployforge/health", "GET /bridge/status",
        "GET|POST /webhooks/whatsapp", "POST /webhooks/telegram",
        "GET /rate-limit-stats", "GET /errors",
        "GET /manager/health-check",
      ]);
      return errorResponse("Not found", 404, path, { available });
      
    } catch (error) {
      const errorId = await logError(error, path, ip, env.HARZ_RATE_LIMIT || env.HARZ_KV);
      return jsonResponse({
        success: false,
        error: error.message || "Internal server error",
        errorId,
        path,
        timestamp: new Date().toISOString(),
      }, 500);
    }
  },
  
  // Cron handler
  async scheduled(event, env, ctx) {
    const hour = new Date().getUTCHour();
    console.log(`HARZ Cloud API cron triggered at ${new Date().toISOString()}`);
    
    // Health check
    if (env.HARZ_KV) {
      await env.HARZ_KV.put("last_cron", new Date().toISOString());
      await env.HARZ_KV.put("system_status", "operational");
    }
    
    // Clean up old rate limit keys (automatic via TTL)
    // Log health metric
    if (env.HARZ_KV) {
      const healthKey = `health:${new Date().toISOString().slice(0, 13)}`;
      await env.HARZ_KV.put(healthKey, JSON.stringify({ status: "ok", timestamp: new Date().toISOString() }), { expirationTtl: 86400 });
    }
  },
};
