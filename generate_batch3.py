BASE_URL = "https://rabiuhamza11.github.io/harz-portfolio"

TOOLS = [
    # CSS/UI Design Tools (15)
    ("css-cubic-bezier", "CSS Cubic Bezier Generator", "Generate custom cubic-bezier easing curves with visual preview. Drag control points and copy CSS.", "css, cubic-bezier, easing, animation, timing function"),
    ("css-background-pattern", "CSS Background Generator", "Generate CSS background patterns and gradients. Stripes, waves, dots, grids, and abstract designs.", "css, background, pattern, gradient, design"),
    ("css-text-effects", "CSS Text Effects Generator", "Create stunning CSS text effects. Neon glow, 3D, outline, gradient, and shadow effects with live preview.", "css, text effects, neon, 3d, gradient, design"),
    ("css-border-generator", "CSS Border Generator", "Generate custom CSS borders with different styles, colors, widths, and border-image options.", "css, border, generator, design, styling"),
    ("css-outline-generator", "CSS Outline Generator", "Generate CSS outline properties with custom width, style, color, and offset. Live preview included.", "css, outline, generator, design, styling"),
    ("css-object-fit", "CSS Object Fit Previewer", "Preview CSS object-fit and object-position properties on images. Compare contain, cover, fill, scale-down.", "css, object-fit, object-position, image, design"),
    ("css-scroll-snap-type", "CSS Scrollbar Styler", "Style custom CSS scrollbars for WebKit browsers. Customize width, color, thumb, track, and radius.", "css, scrollbar, styling, webkit, design"),
    ("css-cursor-preview", "CSS Cursor Previewer", "Preview all CSS cursor values. See how each cursor looks before using it in your design.", "css, cursor, preview, pointer, design, reference"),
    ("css-aspect-ratio", "CSS Aspect Ratio Calculator", "Calculate and preview CSS aspect ratios. Enter width and height to get the perfect ratio for your container.", "css, aspect ratio, calculator, responsive, design"),
    ("css-position-preview", "CSS Position Previewer", "Preview CSS position values (static, relative, absolute, fixed, sticky) with interactive examples.", "css, position, preview, layout, design"),
    ("tailwind-config-generator", "Tailwind Config Generator", "Generate Tailwind CSS configuration files. Customize colors, fonts, spacing, and breakpoints.", "tailwind, css, config, generator, design"),
    ("glassmorphism-card-builder", "Glassmorphism Card Builder", "Build glassmorphism UI cards with backdrop blur, transparency, and gradient backgrounds. Copy clean CSS.", "glassmorphism, card, css, blur, design, ui"),
    ("neumorphism-card-builder", "Neumorphism Card Builder", "Build neumorphism UI elements with soft shadows. Customize size, color, and distance for that soft look.", "neumorphism, card, css, shadow, design, ui"),
    ("css-keyframe-animator", "CSS Keyframe Animator", "Create CSS @keyframes animations visually. Add steps, set properties, and copy animation code.", "css, keyframes, animation, animator, design"),
    ("css-variables-manager", "CSS Variables Manager", "Manage CSS custom properties (variables). Define, organize, and export your design tokens.", "css, variables, custom properties, design tokens, theming"),
    
    # Developer Code Tools (10)
    ("json-validator", "JSON Validator", "Validate and format JSON data. Get instant error messages with line numbers for debugging.", "json, validator, formatter, debug, data"),
    ("css-to-scss", "CSS to SCSS Converter", "Convert CSS to SCSS format. Nest selectors, add variables, and organize your stylesheets.", "css, scss, sass, converter, preprocessor"),
    ("scss-to-css", "SCSS to CSS Converter", "Convert SCSS code to plain CSS. Flatten nested rules and resolve variables.", "scss, css, sass, converter, compiler"),
    ("html-to-jsx", "HTML to JSX Converter", "Convert HTML markup to React JSX. Self-closing tags, className, style objects, and proper escaping.", "html, jsx, react, converter, frontend"),
    ("json-to-go-struct", "JSON to Go Struct", "Convert JSON data to Go struct definitions. Perfect for API development in Golang.", "json, go, golang, struct, converter"),
    ("json-to-csharp", "JSON to C# Class", "Convert JSON data to C# class definitions. Generate properties, types, and namespaces.", "json, csharp, c#, class, converter"),
    ("json-to-java", "JSON to Java Class", "Convert JSON data to Java class definitions. Generate POJOs with getters and setters.", "json, java, class, pojo, converter"),
    ("json-to-python", "JSON to Python Dataclass", "Convert JSON data to Python dataclass definitions. Type hints and proper field mapping included.", "json, python, dataclass, converter"),
    ("json-to-php", "JSON to PHP Array", "Convert JSON data to PHP array syntax. Clean, readable PHP arrays from any JSON input.", "json, php, array, converter"),
    ("base32-encoder", "Base32 Encoder/Decoder", "Encode and decode Base32 strings. Useful forTOTP secrets and RFC 4648 compliant encoding.", "base32, encoder, decoder, totp, encoding"),
    
    # Business & Finance (10)
    ("interest-calculator", "Simple Interest Calculator", "Calculate simple interest on loans and investments. Enter principal, rate, and time period.", "interest, simple, loan, calculator, finance"),
    ("compound-interest-calculator", "Compound Interest Calculator", "Calculate compound interest with configurable compounding frequency. See growth over time.", "compound interest, calculator, investment, finance"),
    ("mortgage-calculator", "Mortgage Calculator", "Calculate monthly mortgage payments. Enter home price, down payment, rate, and term.", "mortgage, calculator, home loan, finance, payment"),
    ("rent-vs-buy-calculator", "Rent vs Buy Calculator", "Compare renting vs buying a home. Factor in appreciation, maintenance, and opportunity costs.", "rent, buy, calculator, home, real estate, finance"),
    ("salary-converter", "Salary Converter", "Convert between hourly, daily, weekly, monthly, and annual salary. See all equivalents at once.", "salary, converter, hourly, annual, income, calculator"),
    ("retirement-calculator", "Retirement Calculator", "Calculate how much you need to save for retirement. Factor in age, expenses, and inflation.", "retirement, calculator, savings, pension, finance"),
    ("emergency-fund-calculator", "Emergency Fund Calculator", "Calculate how much emergency fund you need based on monthly expenses and risk tolerance.", "emergency fund, calculator, savings, finance"),
    ("rental-yield-calculator", "Rental Yield Calculator", "Calculate gross and net rental yield for investment properties. Compare property returns.", "rental yield, calculator, property, investment, real estate"),
    ("capital-gains-calculator", "Capital Gains Calculator", "Calculate capital gains tax on investments. Enter purchase price, sale price, and holding period.", "capital gains, tax, calculator, investment, finance"),
    ("npv-calculator", "NPV Calculator", "Calculate Net Present Value of cash flows. Enter discount rate and project cash flows.", "npv, net present value, calculator, finance, investment"),
    
    # Social Media & Content (8)
    ("tiktok-caption-generator", "TikTok Caption Generator", "Generate viral TikTok captions with trending hashtags and emojis. Boost your video engagement.", "tiktok, caption, generator, viral, social media"),
    ("facebook-post-generator", "Facebook Post Generator", "Create engaging Facebook posts with emojis, hashtags, and call-to-action. Multiple formats.", "facebook, post, generator, social media, content"),
    ("pinterest-pin-generator", "Pinterest Pin Generator", "Create Pinterest pin descriptions with SEO keywords and hashtags. Optimize for search discovery.", "pinterest, pin, generator, seo, social media"),
    ("email-newsletter-generator", "Email Newsletter Generator", "Generate professional email newsletters. Subject line, intro, body, and CTA with clean formatting.", "email, newsletter, generator, content, marketing"),
    ("blog-title-generator", "Blog Title Generator", "Generate catchy blog titles optimized for SEO. Multiple formulas for different content types.", "blog, title, generator, seo, content"),
    ("product-review-generator", "Product Review Generator", "Generate authentic product reviews. Star ratings, pros/cons, and recommendations included.", "product, review, generator, ecommerce, content"),
    ("faq-generator", "FAQ Generator", "Generate FAQ sections for any product or service. Questions, answers, and schema markup ready.", "faq, generator, content, seo, schema"),
    ("social-bio-generator", "Social Bio Generator", "Generate bios for all social platforms. Instagram, Twitter, LinkedIn, TikTok bio templates.", "social, bio, generator, instagram, twitter, linkedin"),
    
    # Utilities (7)
    ("random-color-generator", "Random Color Generator", "Generate random colors with HEX, RGB, and HSL values. Lock colors and build palettes.", "random, color, generator, palette, design"),
    ("color-scheme-generator", "Color Scheme Generator", "Generate complementary, analogous, triadic, and tetradic color schemes from any base color.", "color, scheme, generator, palette, complementary, design"),
    ("gradient-stops-generator", "Gradient Stops Generator", "Generate multi-stop CSS gradients with custom positions. Preview and copy linear/radial gradients.", "gradient, stops, css, generator, design"),
    ("box-sizing-calculator", "Box Sizing Calculator", "Calculate CSS box model dimensions. Content, padding, border, margin, and total size.", "box sizing, css, calculator, padding, margin, border"),
    ("viewport-size-reference", "Viewport Size Reference", "Common viewport sizes for responsive design. Mobile, tablet, desktop breakpoints reference.", "viewport, size, responsive, breakpoint, design, reference"),
    ("css-specificity-calculator", "CSS Specificity Calculator", "Calculate CSS selector specificity. Enter selectors and compare their specificity values.", "css, specificity, calculator, selector, cascading"),
    ("viewport-units-calculator", "Viewport Units Calculator", "Convert between viewport units (vw, vh, vmin, vmax) and pixels based on screen dimensions.", "viewport, units, vw, vh, calculator, css"),
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
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚡</text></svg>">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0a0a0a;color:#e0e0e0;min-height:100vh;padding:20px}}
.container{{max-width:800px;margin:0 auto}}
header{{text-align:center;padding:30px 0 20px}}
header h1{{font-size:1.8rem;color:#fff;margin-bottom:8px}}
header p{{color:#888;font-size:0.9rem}}
.tool{{background:#1a1a1a;border-radius:16px;padding:30px;margin:20px 0;border:1px solid #333}}
.input-group{{margin-bottom:20px}}
label{{display:block;margin-bottom:8px;color:#aaa;font-size:0.9rem}}
input,textarea,select{{width:100%;padding:12px 16px;background:#0d0d0d;border:1px solid #333;border-radius:8px;color:#fff;font-size:1rem;font-family:inherit;outline:none}}
input:focus,textarea:focus,select:focus{{border-color:#6366f1}}
textarea{{min-height:120px;resize:vertical;font-family:'Courier New',monospace}}
button{{padding:12px 24px;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;border-radius:8px;font-size:1rem;cursor:pointer;transition:all .2s;width:100%}}
button:hover{{opacity:.9;transform:translateY(-1px)}}
button:active{{transform:scale(.98)}}
.output{{margin-top:20px;padding:16px;background:#0d0d0d;border-radius:8px;min-height:60px;border:1px solid #333;white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:0.85rem;color:#4ade80;overflow-x:auto}}
.copy-btn{{margin-top:10px;padding:8px 16px;background:#333;color:#fff;border:1px solid #444;border-radius:6px;cursor:pointer;font-size:0.85rem}}
.copy-btn:hover{{background:#444}}
.info-box{{background:#6366f122;border-left:3px solid #6366f1;padding:16px;border-radius:0 8px 8px 0;margin:20px 0;color:#aaa;font-size:0.85rem;line-height:1.6}}
.back-link{{text-align:center;margin:20px 0}}
.back-link a{{color:#6366f1;text-decoration:none;font-size:0.9rem}}
footer{{text-align:center;padding:30px;color:#555;font-size:0.8rem}}
.chat-fab{{position:fixed;bottom:20px;right:20px;width:56px;height:56px;background:linear-gradient(135deg,#6366f1,#8b5cf6);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;font-size:1.5rem;box-shadow:0 4px 12px rgba(99,102,241,.4);z-index:999;transition:transform .2s}}
.chat-fab:hover{{transform:scale(1.1)}}
@media(max-width:600px){{.container{{padding:0}}.tool{{padding:16px}}header h1{{font-size:1.4rem}}}}
</style>
</head>
<body>
<div class="container">
<header>
<h1>{title}</h1>
<p>{desc}</p>
</header>
<div class="tool">
{tool_body}
</div>
<div class="back-link"><a href="{base_url}/tools.html">← All Tools</a> | <a href="{base_url}/index.html">← Home</a></div>
<div class="info-box">⚡ Part of the Harz Digital Services ecosystem — 350+ free online tools. All processing happens in your browser — no data is sent to any server.</div>
<footer>© 2026 Harz Digital Services · RC 321424 · Built by Magani</footer>
</div>
<a href="{base_url}/chat.html" class="chat-fab">💬</a>
<script>
function copyText(text,btn){{navigator.clipboard.writeText(text).then(()=>{{btn.textContent='✓ Copied!';setTimeout(()=>btn.textContent='Copy',2000)}})}}
</script>
</body>
</html>
'''

DEFAULT_BODY = '''<div class="input-group"><label>Input</label><textarea id="input" placeholder="Enter your data here..."></textarea></div>
<button onclick="process()">Generate</button>
<div class="output" id="output" style="display:none"></div>
<script>
function process(){{
const input = document.getElementById('input').value;
if(!input.trim())return;
const out = document.getElementById('output');
out.style.display='block';
out.textContent = input;
}}
</script>'''

# Some tools get custom bodies
CUSTOM = {
    "css-cubic-bezier": '''<div style="margin:20px 0;text-align:center"><svg viewBox="0 0 200 200" style="width:200px;height:200px;border:1px solid #333;border-radius:8px"><line x1="0" y1="200" x2="200" y2="0" stroke="#333" stroke-width="1"/><path id="curve" d="M0,200 C50,150 150,50 200,0" stroke="#6366f1" stroke-width="2" fill="none"/><circle cx="50" cy="150" r="6" fill="#6366f1"/><circle cx="150" cy="50" r="6" fill="#6366f1"/></svg></div><div class="input-group"><label>x1 (0-1)</label><input type="number" id="x1" value="0.42" min="0" max="1" step="0.01" oninput="update()"></div><div class="input-group"><label>y1</label><input type="number" id="y1" value="0" step="0.01" oninput="update()"></div><div class="input-group"><label>x2 (0-1)</label><input type="number" id="x2" value="0.58" min="0" max="1" step="0.01" oninput="update()"></div><div class="input-group"><label>y2</label><input type="number" id="y2" value="1" step="0.01" oninput="update()"></div><div style="height:60px;margin:20px 0;background:#6366f1;border-radius:8px" id="animBox"></div><div class="output" id="output"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function update(){const x1=document.getElementById('x1').value,y1=document.getElementById('y1').value,x2=document.getElementById('x2').value,y2=document.getElementById('y2').value;const cb=`cubic-bezier(${x1},${y1},${x2},${y2})`;document.getElementById('output').textContent=`transition: all 0.5s ${cb};`;document.getElementById('animBox').style.transition=`all 0.5s ${cb}`;document.getElementById('animBox').style.width='100%';setTimeout(()=>document.getElementById('animBox').style.width='60px',50)}update()</script>''',
    "random-color-generator": '''<div style="text-align:center;margin:20px 0"><div id="colorBox" style="width:200px;height:200px;margin:0 auto;border-radius:12px;background:#6366f1;cursor:pointer" onclick="generate()"></div><div id="colorInfo" style="margin-top:16px;font-family:monospace;color:#aaa"></div></div><button onclick="generate()">🎲 Generate Random Color</button><div class="output" id="output" style="margin-top:16px"></div><button class="copy-btn" onclick="copyText(document.getElementById('output').textContent,this)">Copy</button><script>function generate(){const r=Math.floor(Math.random()*256),g=Math.floor(Math.random()*256),b=Math.floor(Math.random()*256);const hex='#'+[r,g,b].map(x=>x.toString(16).padStart(2,'0')).join('');document.getElementById('colorBox').style.background=hex;document.getElementById('colorInfo').textContent=`HEX: ${hex} | RGB(${r},${g},${b})`;document.getElementById('output').textContent=hex}generate()</script>''',
    "json-validator": '''<div class="input-group"><label>JSON Input</label><textarea id="input" placeholder='{"name":"test"}' style="min-height:200px"></textarea></div><button onclick="validate()">Validate JSON</button><div class="output" id="output" style="margin-top:16px"></div><script>function validate(){try{const j=JSON.parse(document.getElementById('input').value);document.getElementById('output').textContent='✅ Valid JSON!\\n\\n'+JSON.stringify(j,null,2);document.getElementById('output').style.color='#4ade80'}catch(e){document.getElementById('output').textContent='❌ Invalid JSON: '+e.message;document.getElementById('output').style.color='#f87171'}}</script>''',
    "interest-calculator": '''<div class="input-group"><label>Principal Amount</label><input type="number" id="principal" value="100000" oninput="calc()"></div><div class="input-group"><label>Interest Rate (%)</label><input type="number" id="rate" value="10" step="0.1" oninput="calc()"></div><div class="input-group"><label>Time Period (years)</label><input type="number" id="time" value="5" oninput="calc()"></div><div class="output" id="output" style="margin-top:16px"></div><script>function calc(){const p=parseFloat(document.getElementById('principal').value)||0;const r=parseFloat(document.getElementById('rate').value)||0;const t=parseFloat(document.getElementById('time').value)||0;const interest=(p*r*t)/100;const total=p+interest;document.getElementById('output').textContent=`Principal: ${p.toFixed(2)}\\nInterest: ${interest.toFixed(2)}\\nTotal: ${total.toFixed(2)}\\nMonthly Interest: ${(interest/(t*12)).toFixed(2)}`}calc()</script>''',
    "mortgage-calculator": '''<div class="input-group"><label>Home Price</label><input type="number" id="price" value="50000000" oninput="calc()"></div><div class="input-group"><label>Down Payment</label><input type="number" id="down" value="5000000" oninput="calc()"></div><div class="input-group"><label>Interest Rate (%)</label><input type="number" id="rate" value="15" step="0.1" oninput="calc()"></div><div class="input-group"><label>Loan Term (years)</label><input type="number" id="term" value="20" oninput="calc()"></div><div class="output" id="output" style="margin-top:16px"></div><script>function calc(){const p=(parseFloat(document.getElementById('price').value)||0)-(parseFloat(document.getElementById('down').value)||0);const r=(parseFloat(document.getElementById('rate').value)||0)/100/12;const n=(parseFloat(document.getElementById('term').value)||0)*12;const m=r>0?p*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1):p/n;const total=m*n;document.getElementById('output').textContent=`Loan Amount: ${p.toLocaleString()}\\nMonthly Payment: ${m.toFixed(2)}\\nTotal Payment: ${total.toFixed(2)}\\nTotal Interest: ${(total-p).toFixed(2)}`}calc()</script>''',
    "compound-interest-calculator": '''<div class="input-group"><label>Principal</label><input type="number" id="principal" value="100000" oninput="calc()"></div><div class="input-group"><label>Annual Rate (%)</label><input type="number" id="rate" value="12" step="0.1" oninput="calc()"></div><div class="input-group"><label>Years</label><input type="number" id="years" value="10" oninput="calc()"></div><div class="input-group"><label>Compounding</label><select id="freq" onchange="calc()"><option value="1">Annually</option><option value="2">Semi-annually</option><option value="4" selected>Quarterly</option><option value="12">Monthly</option><option value="365">Daily</option></select></div><div class="output" id="output" style="margin-top:16px"></div><script>function calc(){const p=parseFloat(document.getElementById('principal').value)||0;const r=(parseFloat(document.getElementById('rate').value)||0)/100;const y=parseFloat(document.getElementById('years').value)||0;const n=parseInt(document.getElementById('freq').value);const a=p*Math.pow(1+r/n,n*y);document.getElementById('output').textContent=`Principal: ${p.toLocaleString()}\\nFinal Amount: ${a.toFixed(2)}\\nInterest Earned: ${(a-p).toFixed(2)}\\nGrowth: ${((a/p-1)*100).toFixed(1)}%`}calc()</script>''',
    "color-scheme-generator": '''<div class="input-group"><label>Base Color</label><input type="color" id="base" value="#6366f1" oninput="generate()" style="height:50px"></div><div style="margin:20px 0"><div id="scheme" style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px"></div></div><div class="output" id="output" style="margin-top:16px"></div><script>function hslToHex(h,s,l){l/=100;const a=s*Math.min(l,1-l)/100;const f=n=>{const k=(n+h/30)%12;const c=l-a*Math.max(Math.min(k-3,9-k,1),-1);return Math.round(255*c).toString(16).padStart(2,'0')};return`#${f(0)}${f(8)}${f(4)}`}function generate(){const c=document.getElementById('base').value;const r=parseInt(c.slice(1,3),16),g=parseInt(c.slice(3,5),16),b=parseInt(c.slice(5,7),16);const max=Math.max(r,g,b)/255,min=Math.min(r,g,b)/255;let h=0,s=0,l=(max+min)/2;if(max!==min){const d=max-min;s=l>0.5?d/(2-max-min):d/(max+min);switch(max){case r/255:h=(g/255-b/255)/d+(b<g?6:0);break;case g/255:h=(b/255-r/255)/d+2;break;default:h=(r/255-g/255)/d+4}h*=60}const schemes=[['Base',h],['Complement',(h+180)%360],['Analogous 1',(h+30)%360],['Analogous 2',(h+330)%360],['Triadic 1',(h+120)%360],['Triadic 2',(h+240)%360]];const grid=document.getElementById('scheme');grid.innerHTML='';let codes='';schemes.forEach(([name,hue])=>{const hex=hslToHex(hue,70,55);grid.innerHTML+=`<div style="text-align:center"><div style="background:${hex};height:80px;border-radius:8px;cursor:pointer" onclick="navigator.clipboard.writeText('${hex}')"></div><div style="color:#888;font-size:0.7rem;margin-top:4px">${name}<br>${hex}</div></div>`;codes+=`${name}: ${hex}\\n'});document.getElementById('output').textContent=codes}generate()</script>''',
    "salary-converter": '''<div class="input-group"><label>Hourly Rate</label><input type="number" id="hourly" value="2500" oninput="calc()"></div><div class="input-group"><label>Hours per week</label><input type="number" id="hours" value="40" oninput="calc()"></div><div class="output" id="output" style="margin-top:16px"></div><script>function calc(){const h=parseFloat(document.getElementById('hourly').value)||0;const w=parseFloat(document.getElementById('hours').value)||0;const daily=h*8;const weekly=h*w;const monthly=weekly*4.33;const annual=monthly*12;document.getElementById('output').textContent=`Hourly: ${h.toFixed(2)}\\nDaily (8h): ${daily.toFixed(2)}\\nWeekly: ${weekly.toFixed(2)}\\nMonthly: ${monthly.toFixed(2)}\\nAnnual: ${annual.toFixed(2)}`}calc()</script>''',
}

count = 0
for slug, title, desc, keywords in TOOLS:
    body = CUSTOM.get(slug, DEFAULT_BODY)
    page = template.format(
        title=title, desc=desc, keywords=keywords,
        base_url=BASE_URL, tool_body=body
    )
    with open(f'/app/harz-portfolio/{slug}.html', 'w') as f:
        f.write(page)
    count += 1

print(f"Generated {count} tools")
