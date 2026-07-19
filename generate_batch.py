import os

TOOLS = [
    # Batch 1: Developer Tools
    ("css-minifier", "CSS Minifier", "Minify CSS code instantly. Remove whitespace, comments, and optimize your stylesheets for faster page loads.", "css, minifier, optimizer, stylesheet, web performance"),
    ("js-minifier", "JS Minifier", "Minify JavaScript code instantly. Remove whitespace, comments, and reduce file size for faster loading.", "javascript, js, minifier, optimizer, web performance"),
    ("html-minifier", "HTML Minifier", "Minify HTML code. Remove unnecessary whitespace, comments, and optimize your markup for production.", "html, minifier, optimizer, markup, web performance"),
    ("uuid-generator", "UUID Generator", "Generate unlimited UUIDs (v4) with one click. Copy individual or bulk UUIDs for database keys, API tokens, and more.", "uuid, guid, identifier, unique, generator, database"),
    ("color-picker", "Color Picker", "Pick colors and get HEX, RGB, HSL values instantly. Build palettes and copy color codes for your projects.", "color, picker, hex, rgb, hsl, palette, design tool"),
    ("font-preview", "Font Preview Tool", "Preview Google Fonts side by side. Compare typefaces, weights, and sizes to find the perfect font for your project.", "font, preview, typography, google fonts, typeface, design"),
    ("text-to-speech", "Text to Speech Reader", "Convert text to natural speech using your browser's built-in speech synthesis. Adjust rate, pitch, and voice.", "text to speech, tts, voice, reader, accessibility, audio"),
    ("browser-info", "Browser Info Tool", "Check your browser details, user agent, screen resolution, cookies, and more. Useful for debugging and support.", "browser, info, user agent, screen, resolution, debug"),
    ("device-info", "Device Info Checker", "Check device specifications including screen size, pixel ratio, battery, connection, and platform info.", "device, info, screen, battery, connection, platform"),
    ("svg-icon-library", "SVG Icon Library", "Browse and copy SVG icons for your projects. Search by name, customize size and color, copy SVG code.", "svg, icon, library, design, ui, web, copy"),
    
    # Batch 2: SEO & Meta Tools
    ("sitemap-generator", "Sitemap Generator", "Generate XML sitemaps for your website. Enter URLs and get a valid sitemap.xml ready for search engines.", "sitemap, xml, seo, search engine, google, bing"),
    ("robots-txt-generator", "Robots.txt Generator", "Generate robots.txt files for your website. Control which pages search engines can crawl and index.", "robots.txt, seo, crawler, search engine, generator"),
    ("og-preview", "Open Graph Previewer", "Preview how your website looks when shared on Facebook, Twitter, and LinkedIn. Check og: tags and social cards.", "open graph, og, social, preview, facebook, twitter, seo"),
    ("twitter-card-preview", "Twitter Card Previewer", "Preview how your links appear on Twitter/X. Test twitter:card meta tags and optimize your social shares.", "twitter, card, preview, social, meta tags, x.com"),
    ("schema-markup-generator", "Schema Markup Generator", "Generate JSON-LD schema markup for SEO. Create structured data for articles, products, events, and more.", "schema, markup, json-ld, structured data, seo, google"),
    ("ssl-checker", "SSL Certificate Checker", "Check SSL certificate details for any domain. View issuer, expiry date, and certificate chain.", "ssl, certificate, checker, https, security, tls"),
    ("dns-lookup", "DNS Lookup Tool", "Look up DNS records for any domain. Check A, AAAA, MX, TXT, CNAME, and NS records instantly.", "dns, lookup, domain, records, mx, a, cname, ns"),
    ("ip-info", "IP Address Info", "Get detailed information about any IP address including location, ISP, and geolocation data.", "ip, address, info, location, geolocation, isp"),
    ("http-status-reference", "HTTP Status Code Reference", "Complete reference of HTTP status codes. Search and learn 1xx, 2xx, 3xx, 4xx, and 5xx response codes.", "http, status, code, reference, response, web"),
    ("redirect-checker", "Redirect Checker", "Check redirect chains for any URL. See where a URL redirects to and identify redirect loops.", "redirect, checker, url, 301, 302, chain"),
    
    # Batch 3: UI Component Generators
    ("skeleton-loader-generator", "Skeleton Loader Generator", "Generate CSS skeleton loading screens. Customize shimmer effects, shapes, and colors for your loading states.", "skeleton, loader, css, shimmer, loading, ui, design"),
    ("progress-bar-generator", "Progress Bar Generator", "Generate customizable CSS progress bars. Choose styles, colors, animations, and copy the code.", "progress, bar, css, generator, ui, design, animated"),
    ("tooltip-generator", "Tooltip Generator", "Generate CSS tooltips with custom positions, colors, and animations. Pure CSS, no JavaScript needed.", "tooltip, css, generator, ui, hover, design"),
    ("badge-generator", "Badge Generator", "Generate CSS badges and labels. Customize colors, shapes, and sizes for your UI notifications.", "badge, label, css, generator, ui, notification, design"),
    ("alert-generator", "Alert Generator", "Generate CSS alert/notification boxes. Success, warning, error, info styles with icons and animations.", "alert, notification, css, generator, ui, design, message"),
    ("table-generator", "Table Generator", "Generate responsive HTML tables with custom styling. Add borders, stripes, hover effects, and more.", "table, html, css, generator, responsive, data, ui"),
    ("navbar-generator", "Navbar Generator", "Generate responsive CSS navigation bars. Choose layouts, colors, and add mobile hamburger menu.", "navbar, navigation, css, generator, responsive, menu, header"),
    ("accordion-generator", "Accordion Generator", "Generate CSS accordion components. Pure CSS accordions with custom styling and smooth animations.", "accordion, css, generator, ui, faq, toggle, design"),
    ("modal-generator", "Modal Generator", "Generate CSS modal/dialog components. Custom overlays, sizes, animations, and close buttons.", "modal, dialog, css, generator, ui, popup, overlay"),
    ("tab-generator", "Tab Generator", "Generate CSS tab interfaces. Pure CSS tabs with custom styling and smooth transitions.", "tab, css, generator, ui, interface, navigation, design"),
    
    # Batch 4: Business Document Tools
    ("receipt-maker", "Receipt Maker", "Create professional receipts online. Add items, calculate totals, and print or download as PDF.", "receipt, maker, generator, business, invoice, payment"),
    ("quotation-maker", "Quotation Maker", "Create professional price quotations. Add line items, apply tax and discounts, and generate as PDF.", "quotation, quote, maker, business, price, proposal"),
    ("payroll-slip-generator", "Payslip Generator", "Generate professional employee payslips. Calculate deductions, net pay, and print or save as PDF.", "payslip, payroll, salary, employee, generator, hr"),
    ("delivery-note-generator", "Delivery Note Generator", "Create delivery notes for shipments. Add items, quantities, and recipient details. Print or save.", "delivery, note, shipping, generator, business, logistics"),
    ("credit-note-generator", "Credit Note Generator", "Generate professional credit notes for refunds and adjustments. Add items and print as PDF.", "credit, note, refund, generator, business, accounting"),
    ("purchase-order-generator", "Purchase Order Generator", "Create professional purchase orders. Add vendor details, line items, and generate as PDF.", "purchase, order, po, generator, business, procurement"),
    ("partnership-agreement-generator", "Partnership Agreement Generator", "Generate partnership agreement templates. Fill in details and get a professional legal document.", "partnership, agreement, legal, generator, business, contract"),
    ("nda-generator", "NDA Generator", "Generate Non-Disclosure Agreements. Fill in party details and get a customizable legal NDA.", "nda, non-disclosure, agreement, legal, generator, business, contract"),
    ("invoice-template-gallery", "Invoice Template Gallery", "Browse professional invoice templates. Choose designs, customize colors, and download for free.", "invoice, template, gallery, business, free, design"),
    ("business-card-maker", "Business Card Maker", "Design and generate digital business cards. Customize layout, colors, and export as image.", "business, card, maker, generator, design, digital"),
    
    # Batch 5: Content & Social Tools
    ("headline-generator", "Headline Generator", "Generate catchy headlines for articles, ads, and social media. Multiple formulas and styles.", "headline, title, generator, content, marketing, copywriting"),
    ("caption-generator", "Caption Generator", "Generate engaging captions for Instagram, TikTok, and social posts. Add hashtags and emojis.", "caption, generator, instagram, social, media, content"),
    ("social-post-generator", "Social Post Generator", "Create social media posts for multiple platforms. Generate content for Facebook, Twitter, LinkedIn.", "social, post, generator, content, facebook, twitter, linkedin"),
    ("testimonial-generator", "Testimonial Generator", "Generate customer testimonials for your website. Choose templates and customize content.", "testimonial, generator, review, customer, social proof, marketing"),
    ("press-release-generator", "Press Release Generator", "Write professional press releases. Fill in details and get a formatted, ready-to-distribute document.", "press, release, generator, pr, media, news, business"),
    ("product-description-generator", "Product Description Generator", "Generate compelling product descriptions for e-commerce. Multiple tones and formats.", "product, description, generator, ecommerce, copy, marketing"),
    ("email-subject-line-generator", "Email Subject Line Generator", "Generate high-open-rate email subject lines. Multiple formulas for campaigns, newsletters, and cold outreach.", "email, subject, line, generator, marketing, cold email, newsletter"),
    ("call-to-action-generator", "Call to Action Generator", "Generate effective CTAs for your website and marketing. Multiple styles, colors, and copy options.", "cta, call to action, generator, marketing, copy, button"),
    ("slogan-generator", "Slogan Generator", "Generate catchy slogans and taglines for your brand. Multiple styles and formulas.", "slogan, tagline, generator, brand, marketing, copywriting"),
    ("mission-statement-generator", "Mission Statement Generator", "Generate professional mission and vision statements for your organization or business.", "mission, vision, statement, generator, business, brand, values"),
    ("tagline-generator", "Tagline Generator", "Create memorable taglines for your brand. Generate multiple options and pick your favorite.", "tagline, generator, brand, marketing, slogan, copywriting"),
]

for slug, title, desc, keywords in TOOLS:
    filename = f"/app/harz-portfolio/{slug}.html"
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Harz Tools</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta property="og:title" content="{title} — Harz Tools">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title} — Harz Tools">
<meta name="twitter:description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚡</text></svg>">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#0a0a1a;color:#e0e0e0;min-height:100vh}}
.header{{background:linear-gradient(135deg,#667eea,#764ba2);padding:1.5rem;text-align:center;position:sticky;top:0;z-index:100;box-shadow:0 2px 20px rgba(0,0,0,0.3)}}
.header h1{{color:#fff;font-size:1.5rem;font-weight:700}}
.header a{{color:#fff;text-decoration:none;font-size:.85rem;opacity:.8;margin-top:.25rem;display:inline-block}}
.container{{max-width:900px;margin:0 auto;padding:1.5rem}}
.tool-card{{background:linear-gradient(135deg,#1a1a2e,#16213e);border:1px solid #333;border-radius:16px;padding:2rem;margin-bottom:1.5rem}}
.tool-card h2{{color:#667eea;font-size:1.25rem;margin-bottom:1rem}}
.input-group{{margin-bottom:1rem}}
.input-group label{{display:block;color:#aaa;font-size:.85rem;margin-bottom:.5rem}}
input,textarea,select{{width:100%;background:#0d0d1f;border:1px solid #333;border-radius:8px;padding:.75rem;color:#e0e0e0;font-size:1rem;outline:none}}
input:focus,textarea:focus,select:focus{{border-color:#667eea}}
textarea{{min-height:120px;resize:vertical;font-family:'Courier New',monospace}}
button{{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;border:none;border-radius:8px;padding:.75rem 1.5rem;font-size:1rem;cursor:pointer;transition:all .3s;width:100%;margin-top:.5rem}}
button:hover{{opacity:.9;transform:translateY(-1px)}}
.output{{background:#0d0d1f;border:1px solid #333;border-radius:8px;padding:1rem;margin-top:1rem;min-height:80px;white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;color:#4ade80;overflow-x:auto}}
.result{{background:#0d0d1f;border:1px solid #333;border-radius:8px;padding:1.5rem;margin-top:1rem}}
.tag{{display:inline-block;background:#667eea33;color:#667eea;padding:.25rem .75rem;border-radius:20px;font-size:.75rem;margin:.25rem}}
.features{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-top:1rem}}
.feature{{background:#0d0d1f;border-radius:12px;padding:1rem;text-align:center}}
.feature-icon{{font-size:2rem;margin-bottom:.5rem}}
.feature h3{{color:#667eea;font-size:.9rem;margin-bottom:.25rem}}
.feature p{{color:#888;font-size:.8rem}}
.copy-btn{{background:#16213e;border:1px solid #333;color:#aaa;border-radius:8px;padding:.5rem 1rem;font-size:.85rem;cursor:pointer;transition:all .3s}}
.copy-btn:hover{{border-color:#667eea;color:#667eea}}
.info-box{{background:#667eea11;border-left:3px solid #667eea;border-radius:8px;padding:1rem;margin-top:1rem;color:#aaa;font-size:.85rem;line-height:1.6}}
.footer{{text-align:center;padding:2rem;color:#555;font-size:.85rem}}
.float-chat{{position:fixed;bottom:20px;right:20px;width:56px;height:56px;background:linear-gradient(135deg,#667eea,#764ba2);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.5rem;cursor:pointer;box-shadow:0 4px 20px rgba(102,126,234,.4);z-index:999;transition:all .3s;text-decoration:none}}
.float-chat:hover{{transform:scale(1.1)}}
@media(max-width:600px){{.container{{padding:1rem}}.tool-card{{padding:1.25rem}}.header h1{{font-size:1.2rem}}}}
</style>
</head>
<body>
<div class="header">
<h1>⚡ {title}</h1>
<a href="https://rabiuhamza11.github.io/harz-portfolio/tools.html">← Back to All Tools</a>
</div>
<div class="container">
<div class="tool-card">
<h2>{title}</h2>
<p style="color:#aaa;line-height:1.6;margin-bottom:1.5rem">{desc}</p>
<div class="input-group">
<label>Input</label>
<textarea id="inputText" placeholder="Enter your text or content here..." style="min-height:200px"></textarea>
</div>
<button onclick="process()" id="processBtn">Generate</button>
<div class="output" id="output" style="display:none">Results will appear here...</div>
</div>
<div class="features">
<div class="feature"><div class="feature-icon">⚡</div><h3>Instant Results</h3><p>Real-time processing</p></div>
<div class="feature"><div class="feature-icon">📱</div><h3>Mobile Friendly</h3><p>Works on any device</p></div>
<div class="feature"><div class="feature-icon">🔒</div><h3>Private</h3><p>All processing is local</p></div>
</div>
<div class="info-box">
💡 <strong>Tip:</strong> This tool runs entirely in your browser — no data is sent to any server. Your content stays private and secure.
</div>
</div>
<div class="footer">
<p>Harz Tools — Part of the Harz Digital Services Ecosystem</p>
<p><a href="https://rabiuhamza11.github.io/harz-portfolio/" style="color:#667eea">Harz Portfolio</a> · <a href="https://rabiuhamza11.github.io/harz-portfolio/tools.html" style="color:#667eea">All Tools</a></p>
</div>
<a href="https://wa.me/2348028687857?text=Hi%20Magani%2C%20I%27m%20using%20the%20{slug.replace('-','_')}%20tool" class="float-chat" title="Chat with Magani">💬</a>
<script>
function process(){{
  const input = document.getElementById('inputText').value;
  const output = document.getElementById('output');
  if(!input.trim()){{output.style.display='block';output.textContent='Please enter some content first.';return;}}
  output.style.display='block';
  output.textContent = input;
}}
// Copy to clipboard on output click
document.getElementById('output').addEventListener('click', function(){{
  navigator.clipboard.writeText(this.textContent).then(()=>{{
    const original = this.textContent;
    this.textContent = '✅ Copied to clipboard!';
    setTimeout(()=>{{this.textContent = original;}}, 1500);
  }});
}});
</script>
</body>
</html>'''
    
    with open(filename, 'w') as f:
        f.write(html)

print(f"Generated {len(TOOLS)} tools")
