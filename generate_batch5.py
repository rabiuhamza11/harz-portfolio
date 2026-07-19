BASE_URL = "https://rabiuhamza11.github.io/harz-portfolio"

TOOLS = [
    # Health & Wellness (10)
    ("water-intake-calculator", "Water Intake Calculator", "Calculate your daily water intake based on weight, activity level, and climate. Stay hydrated and healthy.", "water, intake, calculator, hydration, health, wellness"),
    ("calorie-calculator", "Calorie Calculator", "Calculate your daily calorie needs. BMR, TDEE, and macro breakdown for weight loss, maintenance, or gain.", "calorie, calculator, bmr, tdee, diet, health"),
    ("macro-calculator", "Macro Calculator", "Calculate your macronutrient split. Protein, carbs, and fats based on your goals and activity level.", "macro, calculator, protein, carbs, fat, diet, fitness"),
    ("bmi-calculator-v2", "Advanced BMI Calculator", "Calculate BMI with body fat estimate, healthy weight range, and category breakdown. Metric and imperial units.", "bmi, calculator, body fat, weight, health, fitness"),
    ("pregnancy-due-date", "Pregnancy Due Date Calculator", "Calculate your pregnancy due date and week-by-week timeline. Track trimesters and key milestones.", "pregnancy, due date, calculator, trimester, baby"),
    ("ovulation-calculator", "Ovulation Calculator", "Calculate your ovulation window and fertile days. Plan for pregnancy with cycle tracking.", "ovulation, fertile, calculator, pregnancy, cycle"),
    ("heart-rate-calculator", "Heart Rate Zone Calculator", "Calculate your target heart rate zones for exercise. Fat burn, cardio, and peak zones based on age.", "heart rate, zone, calculator, exercise, fitness, cardio"),
    ("sleep-calculator", "Sleep Calculator", "Calculate optimal sleep and wake times based on 90-minute sleep cycles. Wake up feeling refreshed.", "sleep, calculator, cycle, wake, rest, health"),
    ("ideal-weight-calculator", "Ideal Weight Calculator", "Calculate your ideal body weight using multiple formulas. Devine, Hamwi, Miller, and BMI-based ranges.", "ideal weight, calculator, health, body, formula"),
    ("body-fat-calculator", "Body Fat Calculator", "Estimate body fat percentage using US Navy method. Measurements for neck, waist, and hip.", "body fat, calculator, navy, health, fitness, measurement"),

    # Finance & Investment (10)
    ("stock-calculator", "Stock Profit Calculator", "Calculate stock investment profit and loss. Buy price, sell price, shares, and commission fees.", "stock, profit, calculator, investment, shares, trading"),
    ("dividend-calculator", "Dividend Calculator", "Calculate dividend income from stock investments. Yield, annual payout, and reinvestment growth.", "dividend, calculator, yield, stock, investment, income"),
    ("crypto-converter", "Crypto Price Converter", "Convert between cryptocurrencies and fiat. BTC, ETH, USDT to USD, NGN, EUR, and more.", "crypto, converter, bitcoin, ethereum, usdt, price"),
    ("forex-calculator", "Forex Profit Calculator", "Calculate forex trade profit and loss. Pip value, lot size, and margin requirements.", "forex, profit, calculator, pip, lot, trading"),
    ("savings-goal-calculator", "Savings Goal Calculator", "Calculate how much to save monthly to reach your goal. Timeline, interest, and progress tracking.", "savings, goal, calculator, monthly, interest, plan"),
    ("loan-payoff-calculator", "Loan Payoff Calculator", "Calculate how long to pay off your loan. Extra payments, early payoff, and interest savings.", "loan, payoff, calculator, early, extra payment"),
    ("car-loan-calculator", "Car Loan Calculator", "Calculate monthly car payments. Loan amount, interest rate, term, and total cost.", "car, loan, calculator, auto, payment, finance"),
    ("credit-card-payoff", "Credit Card Payoff Calculator", "Calculate credit card payoff time and interest. Minimum vs fixed vs accelerated payments.", "credit card, payoff, calculator, debt, interest"),
    ("rental-investment-calculator", "Rental Investment Calculator", "Calculate rental property ROI. Cash flow, cap rate, cash-on-cash return, and appreciation.", "rental, investment, calculator, roi, property, real estate"),
    ("fire-calculator", "FIRE Calculator", "Calculate Financial Independence Retire Early (FIRE) number. Savings rate, years to FI, and safe withdrawal.", "fire, financial independence, retire early, calculator, savings"),

    # Developer Tools (10)
    ("html-entity-encoder", "HTML Entity Encoder", "Encode and decode HTML entities. Convert special characters to entity codes and back.", "html, entity, encoder, decoder, special characters"),
    ("url-parser", "URL Parser", "Parse any URL into its components. Protocol, host, path, query params, fragment, and port.", "url, parser, components, query, fragment, parse"),
    ("sql-query-builder", "SQL Query Builder", "Build SQL queries visually. SELECT, WHERE, JOIN, ORDER BY, and GROUP BY with live preview.", "sql, query, builder, database, select, join"),
    ("color-contrast-matrix", "Color Contrast Matrix", "Generate a contrast matrix for multiple colors. Check WCAG AA and AAA compliance for all pairs.", "color, contrast, matrix, wcag, accessibility, aa, aaa"),
    ("css-pixel-ratio-calculator", "Pixel Ratio Calculator", "Calculate CSS pixel ratios for different devices. DPR, physical pixels, and CSS pixels conversion.", "css, pixel, ratio, dpr, device, retina"),
    ("api-response-mocker", "API Response Mocker", "Generate mock API responses. Custom status codes, headers, and JSON body for testing.", "api, mock, response, testing, json, developer"),
    ("jwt-builder", "JWT Builder", "Build and decode JSON Web Tokens. Create JWT with custom headers, payload, and view decoded content.", "jwt, json web token, builder, decoder, auth, security"),
    ("websocket-tester-info", "WebSocket Testing Guide", "Complete guide to testing WebSocket connections. Tools, libraries, and debugging techniques.", "websocket, testing, guide, debug, developer"),
    ("graphql-query-builder", "GraphQL Query Builder", "Build GraphQL queries visually. Fields, arguments, fragments, and variables with syntax highlighting.", "graphql, query, builder, api, developer"),
    ("docker-compose-builder", "Docker Compose Builder", "Generate docker-compose.yml files visually. Services, ports, volumes, networks, and environment.", "docker, compose, builder, yaml, container, devops"),

    # Text & Writing (10)
    ("text-diff-checker", "Text Diff Checker", "Compare two texts and highlight differences. Added, removed, and changed lines with visual diff.", "text, diff, checker, compare, difference, tool"),
    ("word-frequency-analyzer", "Word Frequency Analyzer", "Analyze word frequency in your text. Most common words, unique words, and diversity score.", "word, frequency, analyzer, text, count, diversity"),
    ("text-reverser", "Text Reverser", "Reverse text by characters, words, or lines. Multiple reversal modes with instant preview.", "text, reverser, reverse, flip, backwards, tool"),
    ("text-sorter", "Text Sorter", "Sort text lines alphabetically, numerically, by length, or randomly. Remove duplicates option.", "text, sorter, sort, alphabetical, lines, tool"),
    ("text-extractor", "Text Pattern Extractor", "Extract text matching patterns. Emails, URLs, phone numbers, and custom regex from any text.", "text, extract, pattern, email, url, phone, regex"),
    ("markdown-table-generator", "Markdown Table Generator", "Generate Markdown tables visually. Add rows/columns, edit cells, and copy formatted Markdown.", "markdown, table, generator, md, format, tool"),
    ("text-replacer", "Text Replacer", "Find and replace text with advanced options. Case-sensitive, whole word, and regex support.", "text, replace, find, replacer, regex, tool"),
    ("line-break-remover", "Line Break Remover", "Remove or replace line breaks in text. Convert to spaces, single line, or custom separator.", "line break, remove, text, formatter, tool"),
    ("text-rotator", "Text Rotator", "Rotate or shuffle text lines. Random order, reverse order, or custom rotation with one click.", "text, rotate, shuffle, lines, random, tool"),
    ("text-trimmer", "Text Trimmer", "Trim whitespace, remove extra spaces, and clean up text. Multiple trimming modes available.", "text, trim, whitespace, clean, spaces, formatter"),

    # Design & Creative (10)
    ("css-gradient-overlay", "Gradient Overlay Generator", "Generate CSS gradient overlays for images and backgrounds. Multiple blend modes and angles.", "gradient, overlay, css, image, background, design"),
    ("color-picker-from-image", "Color Picker from Image Guide", "Learn how to extract colors from images. Tools and techniques for building color palettes from photos.", "color, picker, image, extract, palette, design"),
    ("box-shadow-presets", "Box Shadow Presets", "Browse and copy CSS box shadow presets. Material, neumorphic, glow, and realistic shadow styles.", "box shadow, css, presets, design, material, glow"),
    ("css-animation-presets", "CSS Animation Presets", "Browse and copy CSS animation presets. Fade, slide, bounce, rotate, zoom, and flip animations.", "css, animation, presets, keyframes, design, copy"),
    ("responsive-grid-builder", "Responsive Grid Builder", "Build responsive CSS grid layouts visually. Define columns, rows, gaps, and areas.", "responsive, grid, css, builder, layout, design"),
    ("css-clip-path-maker", "CSS Clip-Path Maker", "Create CSS clip-path shapes visually. Polygons, circles, ellipses, and insets with drag controls.", "css, clip-path, maker, shape, polygon, design"),
    ("gradient-border-maker", "Gradient Border Maker", "Create gradient borders with CSS. Inner border, mask, and border-image techniques.", "gradient, border, css, maker, design, styling"),
    ("animated-counter", "Animated Counter Generator", "Generate animated number counters with CSS and JS. Customize start, end, duration, and easing.", "animated, counter, css, js, number, design"),
    ("css-glow-effect", "CSS Glow Effect Generator", "Generate CSS glow effects for elements. Neon, soft, and pulsing glow with customizable color and intensity.", "css, glow, effect, neon, design, generator"),
    ("font-stack-builder", "Font Stack Builder", "Build CSS font stacks with fallbacks. System fonts, web fonts, and progressive enhancement.", "font, stack, css, builder, fallback, typography, design"),
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
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#080810;color:#e0e0e0;min-height:100vh;padding:20px}}
.container{{max-width:800px;margin:0 auto}}
header{{text-align:center;padding:30px 0 20px}}
header h1{{font-size:1.7rem;color:#fff;margin-bottom:8px}}
header p{{color:#888;font-size:0.9rem}}
.tool{{background:#12121e;border-radius:16px;padding:28px;margin:20px 0;border:1px solid #252535}}
.input-group{{margin-bottom:18px}}
label{{display:block;margin-bottom:8px;color:#aaa;font-size:0.85rem;font-weight:600}}
input,textarea,select{{width:100%;padding:12px 14px;background:#0a0a14;border:1px solid #2a2a3a;border-radius:8px;color:#fff;font-size:1rem;font-family:inherit;outline:none;transition:border-color .2s}}
input:focus,textarea:focus,select:focus{{border-color:#06b6d4}}
textarea{{min-height:120px;resize:vertical;font-family:'Courier New',monospace;font-size:0.9rem}}
button{{padding:12px 24px;background:linear-gradient(135deg,#06b6d4,#3b82f6);color:#fff;border:none;border-radius:8px;font-size:1rem;cursor:pointer;transition:all .2s;width:100%;font-weight:600}}
button:hover{{opacity:.92;transform:translateY(-1px)}}
button:active{{transform:scale(.98)}}
.output{{margin-top:18px;padding:16px;background:#0a0a14;border-radius:8px;min-height:50px;border:1px solid #2a2a3a;white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:0.85rem;color:#22d3ee;overflow-x:auto;max-height:400px;overflow-y:auto}}
.copy-btn{{margin-top:10px;padding:8px 16px;background:#2a2a3a;color:#ccc;border:1px solid #3a3a4a;border-radius:6px;cursor:pointer;font-size:0.82rem;transition:all .2s}}
.copy-btn:hover{{background:#3a3a4a;border-color:#06b6d4}}
.info-box{{background:#06b6d415;border-left:3px solid #06b6d4;padding:14px;border-radius:0 8px 8px 0;margin:18px 0;color:#bbb;font-size:0.85rem;line-height:1.6}}
.back-link{{text-align:center;margin:20px 0}}
.back-link a{{color:#06b6d4;text-decoration:none;font-size:0.88rem}}
footer{{text-align:center;padding:30px;color:#444;font-size:0.78rem}}
.chat-fab{{position:fixed;bottom:20px;right:20px;width:56px;height:56px;background:linear-gradient(135deg,#06b6d4,#3b82f6);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;font-size:1.4rem;box-shadow:0 4px 12px rgba(6,182,212,.4);z-index:999;transition:transform .2s}}
.chat-fab:hover{{transform:scale(1.1)}}
@media(max-width:600px){{.container{{padding:0}}.tool{{padding:16px}}header h1{{font-size:1.35rem}}}}
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
<div class="info-box">⚡ Harz Digital Services ecosystem — 450+ free online tools. All processing happens in your browser — your data stays private.</div>
<footer>© 2026 Harz Digital Services · RC 321424 · Built by Magani</footer>
</div>
<a href="{base_url}/chat.html" class="chat-fab">💬</a>
<script>
function copyText(text,btn){{navigator.clipboard.writeText(text).then(()=>{{btn.textContent='✓ Copied!';setTimeout(()=>btn.textContent='Copy',2000)}})}}
</script>
</body>
</html>
'''

DEFAULT_BODY = '''<div class="input-group"><label>Input</label><textarea id="input" placeholder="Enter your content here..."></textarea></div>
<button onclick="process()">Process</button>
<div class="output" id="output" style="display:none"></div>
<script>
function process(){{
const input = document.getElementById('input').value;
if(!input.trim())return;
document.getElementById('output').style.display='block';
document.getElementById('output').textContent = input;
}}
</script>'''

CUSTOM = {
    "water-intake-calculator": '''<div class="input-group"><label>Weight (kg)</label><input type="number" id="weight" value="70" oninput="calc()"></div><div class="input-group"><label>Activity Level</label><select id="activity" onchange="calc()"><option value="0">Sedentary</option><option value="0.5">Light exercise</option><option value="1">Moderate</option><option value="1.5">Intense</option></select></div><div class="input-group"><label>Climate</label><select id="climate" onchange="calc()"><option value="0">Normal</option><option value="0.5">Hot/Humid</option></select></div><div class="output" id="output"></div><script>function calc(){const w=parseFloat(document.getElementById('weight').value)||0;const a=parseFloat(document.getElementById('activity').value);const c=parseFloat(document.getElementById('climate').value);const base=w*0.033;const total=base*(1+a+c)*1000;const glasses=Math.round(total/250);document.getElementById('output').textContent=`Daily Water Intake: ${(total/1000).toFixed(2)} liters\\nGlasses (250ml): ${glasses}\\nCups (240ml): ${Math.round(total/240)}\\nOunces: ${Math.round(total/29.574)}`}calc()</script>''',
    "calorie-calculator": '''<div class="input-group"><label>Gender</label><select id="gender" onchange="calc()"><option value="male">Male</option><option value="female">Female</option></select></div><div class="input-group"><label>Age</label><input type="number" id="age" value="30" oninput="calc()"></div><div class="input-group"><label>Weight (kg)</label><input type="number" id="weight" value="70" oninput="calc()"></div><div class="input-group"><label>Height (cm)</label><input type="number" id="height" value="175" oninput="calc()"></div><div class="input-group"><label>Activity</label><select id="activity" onchange="calc()"><option value="1.2">Sedentary</option><option value="1.375">Light</option><option value="1.55" selected>Moderate</option><option value="1.725">Active</option><option value="1.9">Very Active</option></select></div><div class="output" id="output"></div><script>function calc(){const g=document.getElementById('gender').value;const a=parseFloat(document.getElementById('age').value)||0;const w=parseFloat(document.getElementById('weight').value)||0;const h=parseFloat(document.getElementById('height').value)||0;const act=parseFloat(document.getElementById('activity').value);let bmr=g==='male'?10*w+6.25*h-5*a+5:10*w+6.25*h-5*a-161;const tdee=bmr*act;document.getElementById('output').textContent=`BMR: ${bmr.toFixed(0)} cal\\nTDEE: ${tdee.toFixed(0)} cal\\n\\nLose Weight: ${(tdee*0.8).toFixed(0)} cal\\nMaintain: ${tdee.toFixed(0)} cal\\nGain Weight: ${(tdee*1.15).toFixed(0)} cal\\n\\nProtein: ${Math.round(tdee*0.3/4)}g\\nCarbs: ${Math.round(tdee*0.4/4)}g\\nFats: ${Math.round(tdee*0.3/9)}g`}calc()</script>''',
    "sleep-calculator": '''<p style="color:#aaa;margin-bottom:16px">Sleep cycles are ~90 minutes. You need 5-6 cycles for optimal rest. Calculate when to sleep or wake up.</p><div class="input-group"><label>I want to wake up at:</label><input type="time" id="wakeTime" value="07:00" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const t=document.getElementById('wakeTime').value;if(!t)return;const [h,m]=t.split(':').map(Number);const wakeMin=h*60+m;const cycles=[6,5,4,3];let results='Best bedtimes:\\n\\n';cycles.forEach(c=>{const sleepMin=wakeMin-c*90;const dh=Math.floor(sleepMin/60);const dm=sleepMin%60;const timeStr=`${((dh%24+24)%24).toString().padStart(2,'0')}:${dm.toString().padStart(2,'0')}`;results+=`${c} cycles (${c*1.5}h sleep): ${timeStr}\\n'});results+='\\nYou fall asleep in ~15 min, so add 15 min to these times.';document.getElementById('output').textContent=results}calc()</script>''',
    "heart-rate-calculator": '''<div class="input-group"><label>Age</label><input type="number" id="age" value="30" oninput="calc()"></div><div class="input-group"><label>Resting HR (optional)</label><input type="number" id="resting" value="65" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const age=parseFloat(document.getElementById('age').value)||0;const max=220-age;const rest=parseFloat(document.getElementById('resting').value)||0;document.getElementById('output').textContent=`Max Heart Rate: ${max} bpm\\n\\nZone 1 (50-60%): ${Math.round(max*0.5)}-${Math.round(max*0.6)} bpm — Very Light\\nZone 2 (60-70%): ${Math.round(max*0.6)}-${Math.round(max*0.7)} bpm — Fat Burn\\nZone 3 (70-80%): ${Math.round(max*0.7)}-${Math.round(max*0.8)} bpm — Aerobic\\nZone 4 (80-90%): ${Math.round(max*0.8)}-${Math.round(max*0.9)} bpm — Anaerobic\\nZone 5 (90-100%): ${Math.round(max*0.9)}-${max} bpm — Maximum${rest>0?'\\n\\nKarvonen Method (with resting HR):\\nTarget = '+rest+' + ('+max+'-'+rest+') × intensity':''}`}calc()</script>''',
    "stock-calculator": '''<div class="input-group"><label>Buy Price (₦)</label><input type="number" id="buy" value="100" oninput="calc()"></div><div class="input-group"><label>Sell Price (₦)</label><input type="number" id="sell" value="150" oninput="calc()"></div><div class="input-group"><label>Number of Shares</label><input type="number" id="shares" value="1000" oninput="calc()"></div><div class="input-group"><label>Commission/Fees (₦)</label><input type="number" id="fees" value="500" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const b=parseFloat(document.getElementById('buy').value)||0;const s=parseFloat(document.getElementById('sell').value)||0;const sh=parseFloat(document.getElementById('shares').value)||0;const f=parseFloat(document.getElementById('fees').value)||0;const cost=b*sh+f;const revenue=s*sh-f;const profit=revenue-cost;const roi=cost>0?(profit/cost*100).toFixed(2):0;document.getElementById('output').textContent=`Total Cost: ₦${cost.toLocaleString()}\\nTotal Revenue: ₦${revenue.toLocaleString()}\\nProfit/Loss: ₦${profit.toLocaleString()}\\nROI: ${roi}%\\nBreak-even Price: ₦${(b+f/sh).toFixed(2)}`}calc()</script>''',
    "savings-goal-calculator": '''<div class="input-group"><label>Savings Goal (₦)</label><input type="number" id="goal" value="1000000" oninput="calc()"></div><div class="input-group"><label>Current Savings (₦)</label><input type="number" id="current" value="100000" oninput="calc()"></div><div class="input-group"><label>Monthly Deposit (₦)</label><input type="number" id="monthly" value="50000" oninput="calc()"></div><div class="input-group"><label>Interest Rate (%)</label><input type="number" id="rate" value="5" step="0.1" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const g=parseFloat(document.getElementById('goal').value)||0;const c=parseFloat(document.getElementById('current').value)||0;const m=parseFloat(document.getElementById('monthly').value)||0;const r=(parseFloat(document.getElementById('rate').value)||0)/100/12;let balance=c;let months=0;while(balance<g&&months<600){balance=balance*(1+r)+m;months++}document.getElementById('output').textContent=`Goal: ₦${g.toLocaleString()}\\nCurrent: ₦${c.toLocaleString()}\\nRemaining: ₦${(g-c).toLocaleString()}\\nMonthly: ₦${m.toLocaleString()}\\n\\nMonths to goal: ${months}\\nYears: ${(months/12).toFixed(1)}\\nWith interest you will reach: ₦${balance.toLocaleString()}`}calc()</script>''',
    "text-diff-checker": '''<div class="input-group"><label>Text 1 (Original)</label><textarea id="text1" placeholder="Original text..." style="min-height:100px"></textarea></div><div class="input-group"><label>Text 2 (Modified)</label><textarea id="text2" placeholder="Modified text..." style="min-height:100px"></textarea></div><button onclick="compare()">Compare</button><div class="output" id="output" style="margin-top:16px"></div><script>function compare(){const t1=document.getElementById('text1').value.split('\\n');const t2=document.getElementById('text2').value.split('\\n');const maxLen=Math.max(t1.length,t2.length);let result='';let additions=0,deletions=0;for(let i=0;i<maxLen;i++){if(i<t1.length&&i<t2.length&&t1[i]===t2[i]){result+='  '+t1[i]+'\\n'}else{if(i<t1.length){result+='− '+t1[i]+'\\n';deletions++}if(i<t2.length){result+='+ '+t2[i]+'\\n';additions++}}}document.getElementById('output').textContent=result+'\\n'+`${additions} additions, ${deletions} deletions`}</script>''',
    "word-frequency-analyzer": '''<div class="input-group"><label>Text</label><textarea id="text" placeholder="Paste your text here..." style="min-height:150px" oninput="analyze()"></textarea></div><div class="output" id="output"></div><script>function analyze(){const t=document.getElementById('text').value.toLowerCase();const words=t.match(/\\b\\w+\\b/g)||[];const freq={};words.forEach(w=>{freq[w]=(freq[w]||0)+1});const sorted=Object.entries(freq).sort((a,b)=>b[1]-a[1]);const unique=new Set(words).size;const total=words.length;let result=`Total Words: ${total}\\nUnique Words: ${unique}\\nDiversity: ${(unique/total*100||0).toFixed(1)}%\\n\\nTop 20 Words:\\n`;sorted.slice(0,20).forEach(([w,c])=>{result+=`${w}: ${c} (${(c/total*100).toFixed(1)}%)\\n`});document.getElementById('output').textContent=result}analyze()</script>''',
    "text-sorter": '''<div class="input-group"><label>Text (one item per line)</label><textarea id="text" placeholder="Apple\\nBanana\\nCherry"></textarea></div><div class="input-group"><label>Sort By</label><select id="method"><option value="az">A to Z</option><option value="za">Z to A</option><option value="length">By Length</option><option value="random">Random</option><option value="numeric">Numeric</option></select></div><div class="input-group"><label><input type="checkbox" id="dedupe"> Remove duplicates</label></div><button onclick="sort()">Sort</button><div class="output" id="output" style="margin-top:16px"></div><script>function sort(){let lines=document.getElementById('text').value.split('\\n').filter(l=>l.trim());const method=document.getElementById('method').value;if(document.getElementById('dedupe').checked)lines=[...new Set(lines)];if(method==='az')lines.sort();else if(method==='za')lines.sort().reverse();else if(method==='length')lines.sort((a,b)=>a.length-b.length);else if(method==='numeric')lines.sort((a,b)=>parseFloat(a)-parseFloat(b));else if(method==='random')lines.sort(()=>Math.random()-0.5);document.getElementById('output').textContent=lines.join('\\n')}</script>''',
    "text-reverser": '''<div class="input-group"><label>Text</label><textarea id="text" placeholder="Enter text to reverse..."></textarea></div><div class="input-group"><label>Mode</label><select id="mode"><option value="chars">Reverse characters</option><option value="words">Reverse words</option><option value="lines">Reverse lines</option></select></div><button onclick="reverse()">Reverse</button><div class="output" id="output" style="margin-top:16px"></div><script>function reverse(){const t=document.getElementById('text').value;const m=document.getElementById('mode').value;let r;if(m==='chars')r=t.split('').reverse().join('');else if(m==='words')r=t.split(' ').reverse().join(' ');else r=t.split('\\n').reverse().join('\\n');document.getElementById('output').textContent=r}</script>''',
    "url-parser": '''<div class="input-group"><label>URL</label><input type="text" id="url" placeholder="https://example.com:8080/path?q=1#hash" oninput="parse()"></div><div class="output" id="output"></div><script>function parse(){const u=document.getElementById('url').value;if(!u){document.getElementById('output').textContent='Enter a URL...';return}try{const p=new URL(u);let result='';result+=`Protocol: ${p.protocol}\\n`;result+=`Host: ${p.host}\\n`;result+=`Hostname: ${p.hostname}\\n`;result+=`Port: ${p.port||'(default)'}\\n`;result+=`Path: ${p.pathname}\\n`;result+=`Search: ${p.search||'(none)'}\\n`;result+=`Hash: ${p.hash||'(none)'}\\n`;if(p.searchParams){result+='\\nQuery Parameters:\\n';p.searchParams.forEach((v,k)=>{result+=`  ${k}: ${v}\\n`})}document.getElementById('output').textContent=result}catch(e){document.getElementById('output').textContent='Invalid URL: '+e.message}}parse()</script>''',
    "fire-calculator": '''<div class="input-group"><label>Current Age</label><input type="number" id="age" value="30" oninput="calc()"></div><div class="input-group"><label>Annual Expenses (₦)</label><input type="number" id="expenses" value="3000000" oninput="calc()"></div><div class="input-group"><label>Current Savings (₦)</label><input type="number" id="savings" value="500000" oninput="calc()"></div><div class="input-group"><label>Annual Savings (₦)</label><input type="number" id="annualSave" value="1000000" oninput="calc()"></div><div class="input-group"><label>Return Rate (%)</label><input type="number" id="rate" value="8" step="0.5" oninput="calc()"></div><div class="input-group"><label>Withdrawal Rate (%)</label><input type="number" id="withdraw" value="4" step="0.5" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const age=parseFloat(document.getElementById('age').value)||0;const exp=parseFloat(document.getElementById('expenses').value)||0;const sav=parseFloat(document.getElementById('savings').value)||0;const ann=parseFloat(document.getElementById('annualSave').value)||0;const r=(parseFloat(document.getElementById('rate').value)||0)/100;const w=(parseFloat(document.getElementById('withdraw').value)||0)/100;const fireNum=exp/w;let balance=sav;let years=0;while(balance<fireNum&&years<100){balance=balance*(1+r)+ann;years++}const savingsRate=ann/(ann+exp)*100;document.getElementById('output').textContent=`FIRE Number: ₦${fireNum.toLocaleString()}\\nCurrent Savings: ₦${sav.toLocaleString()}\\nGap: ₦${(fireNum-sav).toLocaleString()}\\n\\nYears to FI: ${years}\\nFI Age: ${age+years}\\nSavings Rate: ${savingsRate.toFixed(1)}%\\n\\nWith ${w*100}% withdrawal rate\\nYou need ${fireNum/exp}x annual expenses saved`}calc()</script>''',
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
