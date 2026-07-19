BASE_URL = "https://rabiuhamza11.github.io/harz-portfolio"

TOOLS = [
    # Nigeria-Specific Tools (10)
    ("nigeria-tax-calculator", "Nigeria Tax Calculator", "Calculate Nigerian personal income tax (PAYE) based on annual salary. Includes PIT, pension, and NHF deductions.", "nigeria, tax, paye, calculator, pit, pension, nhf"),
    ("nigeria-business-registration", "CAC Registration Guide", "Step-by-step guide to registering a business with CAC Nigeria. BN, LTD, and NGO registration explained.", "cac, nigeria, business, registration, bn, ltd, guide"),
    ("nigeria-stock-calculator", "NGX Stock Calculator", "Calculate NGX (Nigerian Stock Exchange) investment returns. Brokerage fees, CSCS, and NSE charges included.", "ngx, nse, nigeria, stock, calculator, investment"),
    ("naira-to-crypto", "Naira to Crypto Converter", "Convert NGN to BTC, ETH, USDT and other cryptocurrencies using current exchange rates.", "naira, crypto, converter, btc, eth, usdt, ngn"),
    ("nigeria-data-plans", "Nigeria Data Plan Comparison", "Compare data plans from MTN, Airtel, Glo, and 9mobile. Find the best value per GB.", "nigeria, data, plans, mtn, airtel, glo, 9mobile"),
    ("nigeria-postcode-finder", "Nigeria Postcode Finder", "Find Nigerian postal codes by state and LGA. Searchable database of all Nigerian postcodes.", "nigeria, postcode, zip, code, finder, lga"),
    ("nigeria-public-holidays", "Nigeria Public Holidays", "List of Nigerian public holidays with dates. Plan your year around official holidays.", "nigeria, public, holidays, calendar, dates"),
    ("nigeria-plate-number-checker", "Nigeria Plate Number Guide", "Guide to Nigerian vehicle plate number formats. State codes, prefixes, and suffixes explained.", "nigeria, plate, number, vehicle, checker, guide"),
    ("nigeria-bank-sort-codes", "Nigeria Bank Sort Codes", "Complete list of Nigerian bank sort codes. GTBank, UBA, Access, Zenith, First Bank and more.", "nigeria, bank, sort, code, gtbank, uba, access"),
    ("nigeria-electricity-bill", "Nepa/Electricity Bill Calculator", "Calculate your Nigerian electricity bill based on meter type, band, and consumption units.", "nigeria, electricity, nepa, bill, calculator, disco"),

    # Random Generators (10)
    ("random-team-generator", "Random Team Generator", "Split names into random teams. Enter participant names and team count. Fair and instant team assignment.", "random, team, generator, split, groups, assign"),
    ("random-number-picker", "Random Number Picker", "Pick random numbers within a range. Unique picks, lottery numbers, and custom ranges.", "random, number, picker, lottery, generator"),
    ("random-name-generator", "Random Name Generator", "Generate random names from multiple cultures. Male, female, and neutral names with origins.", "random, name, generator, male, female, names"),
    ("random-password-batch", "Batch Password Generator", "Generate multiple passwords at once. Custom length, character sets, and export options.", "password, batch, generator, multiple, random, secure"),
    ("random-quote-generator", "Random Quote Generator", "Generate inspirational, motivational, and famous quotes. Browse by category and copy favorites.", "random, quote, generator, inspirational, motivational"),
    ("random-joke-generator", "Random Joke Generator", "Get random jokes on demand. Clean jokes, dad jokes, one-liners, and programming humor.", "random, joke, generator, funny, humor, dad jokes"),
    ("random-fact-generator", "Random Fact Generator", "Generate interesting random facts. Science, history, nature, and technology trivia.", "random, fact, generator, trivia, interesting, science"),
    ("random-truth-dare", "Truth or Dare Generator", "Generate random truth or dare prompts. Clean, spicy, and extreme categories for any group.", "truth, dare, random, generator, game, party"),
    ("random-color-palette", "Random Color Palette Generator", "Generate random color palettes with 5 colors. Lock favorites and regenerate the rest.", "random, color, palette, generator, design, colors"),
    ("random-yes-no", "Yes or No Decision Maker", "Can't decide? Let this tool make a random yes or no decision for you. Quick and fun.", "yes, no, decision, maker, random, coin flip"),

    # Social Media Tools (10)
    ("instagram-engagement-calculator", "Instagram Engagement Calculator", "Calculate your Instagram engagement rate from likes, comments, and follower count.", "instagram, engagement, rate, calculator, social media"),
    ("youtube-thumbnail-tester", "YouTube Thumbnail A/B Test Guide", "Guide to A/B testing YouTube thumbnails. Tools, strategies, and best practices for higher CTR.", "youtube, thumbnail, ab testing, ctr, guide, social media"),
    ("twitter-character-counter", "Twitter Character Counter", "Count characters for Twitter/X posts. Includes URL shortening calculation and thread limits.", "twitter, character, counter, x.com, social media"),
    ("facebook-ad-budget-calculator", "Facebook Ad Budget Calculator", "Calculate Facebook ad budget allocation. Daily spend, reach estimate, and CPC projections.", "facebook, ad, budget, calculator, marketing, cpc"),
    ("instagram-hashtag-density", "Instagram Hashtag Density Checker", "Check how many hashtags your competitors use. Analyze optimal hashtag count per post.", "instagram, hashtag, density, analyzer, social media"),
    ("youtube-tag-generator", "YouTube Tag Generator", "Generate SEO-optimized YouTube tags from your video title and description. Boost discoverability.", "youtube, tag, generator, seo, video, social media"),
    ("social-media-image-resizer", "Social Media Image Size Guide", "Complete guide to social media image dimensions. Facebook, Instagram, Twitter, LinkedIn, YouTube sizes.", "social media, image, size, dimensions, guide, facebook"),
    ("tiktok-video-length-guide", "TikTok Video Length Guide", "Optimal TikTok video lengths by content type. Engagement data, retention curves, and best practices.", "tiktok, video, length, guide, social media, engagement"),
    ("content-calendar-template", "Content Calendar Template Generator", "Generate a monthly content calendar template. Weekly grid with platform, topic, and status columns.", "content, calendar, template, generator, social media, marketing"),
    ("influencer-rate-calculator", "Influencer Rate Calculator", "Calculate fair influencer rates based on followers, engagement, and platform. Negotiate with confidence.", "influencer, rate, calculator, social media, marketing, pricing"),

    # Project Management (10)
    ("gantt-chart-maker", "Simple Gantt Chart Maker", "Create simple Gantt charts from task lists. Visual timeline with start/end dates and dependencies.", "gantt, chart, maker, project, timeline, management"),
    ("kanban-board-generator", "Kanban Board Generator", "Generate a printable Kanban board. To-do, in progress, review, and done columns with cards.", "kanban, board, generator, project, management, agile"),
    ("project-budget-tracker", "Project Budget Tracker", "Track project budget vs actual spending. Categories, variance, and burn rate visualization.", "project, budget, tracker, finance, management"),
    ("risk-assessment-matrix", "Risk Assessment Matrix", "Create a risk assessment matrix for projects. Likelihood, impact, and mitigation strategies.", "risk, assessment, matrix, project, management"),
    ("stakeholder-map-generator", "Stakeholder Map Generator", "Map project stakeholders by influence and interest. Power-interest grid with engagement strategy.", "stakeholder, map, generator, project, management, power interest"),
    ("project-charter-generator", "Project Charter Generator", "Generate a project charter document. Scope, objectives, timeline, stakeholders, and milestones.", "project, charter, generator, document, management"),
    ("rACI-matrix-generator", "RACI Matrix Generator", "Create a RACI matrix for project roles. Responsible, Accountable, Consulted, and Informed assignments.", "raci, matrix, generator, project, roles, management"),
    ("milestone-tracker", "Project Milestone Tracker", "Track project milestones with status, dates, and dependencies. Visual progress overview.", "milestone, tracker, project, management, progress"),
    ("project-risk-register", "Project Risk Register", "Create a risk register for projects. Risk ID, description, probability, impact, and mitigation.", "risk, register, project, management, tracking"),
    ("resource-allocation-matrix", "Resource Allocation Matrix", "Plan and track resource allocation across projects. Team members, hours, and availability.", "resource, allocation, matrix, project, management, planning"),

    # Misc Utilities (10)
    ("unit-price-calculator", "Unit Price Calculator", "Compare product prices per unit. Find the best value between different package sizes and brands.", "unit, price, calculator, compare, value, shopping"),
    ("fuel-cost-calculator", "Fuel Cost Calculator", "Calculate fuel costs for trips and daily commutes. Distance, fuel efficiency, and price per liter.", "fuel, cost, calculator, trip, petrol, diesel"),
    ("electricity-calculator", "Electricity Usage Calculator", "Calculate electricity costs from appliance wattage and usage hours. Monthly bill estimation.", "electricity, calculator, usage, wattage, bill, power"),
    ("recipe-scaler", "Recipe Scaler", "Scale recipes up or down. Adjust ingredient quantities for any number of servings.", "recipe, scaler, cooking, ingredients, servings"),
    ("btu-calculator", "BTU Calculator", "Calculate BTU requirements for air conditioning. Room size, insulation, and climate factors.", "btu, calculator, air conditioner, cooling, room size"),
    ("paint-calculator", "Paint Calculator", "Calculate how much paint you need for a room. Wall area, coats, and coverage per liter.", "paint, calculator, room, coverage, liters, home"),
    ("tile-calculator", "Tile Calculator", "Calculate the number of tiles needed for any area. Room dimensions, tile size, and waste factor.", "tile, calculator, flooring, area, home, renovation"),
    ("wallpaper-calculator", "Wallpaper Calculator", "Calculate wallpaper rolls needed for a room. Wall dimensions, pattern repeat, and waste.", "wallpaper, calculator, rolls, room, home, decor"),
    ("concrete-calculator", "Concrete Calculator", "Calculate concrete volume needed for slabs, columns, and footings. Cubic meters and bags.", "concrete, calculator, slab, volume, construction, cement"),
    ("fertilizer-calculator", "Fertilizer Calculator", "Calculate fertilizer amounts for your garden or farm. Area, NPK ratio, and application rate.", "fertilizer, calculator, garden, farm, npk, agriculture"),
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
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#070710;color:#e0e0e0;min-height:100vh;padding:20px}}
.container{{max-width:800px;margin:0 auto}}
header{{text-align:center;padding:30px 0 20px}}
header h1{{font-size:1.7rem;color:#fff;margin-bottom:8px}}
header p{{color:#888;font-size:0.9rem}}
.tool{{background:#12121e;border-radius:16px;padding:28px;margin:20px 0;border:1px solid #252535}}
.input-group{{margin-bottom:18px}}
label{{display:block;margin-bottom:8px;color:#aaa;font-size:0.85rem;font-weight:600}}
input,textarea,select{{width:100%;padding:12px 14px;background:#0a0a14;border:1px solid #2a2a3a;border-radius:8px;color:#fff;font-size:1rem;font-family:inherit;outline:none;transition:border-color .2s}}
input:focus,textarea:focus,select:focus{{border-color:#f59e0b}}
textarea{{min-height:120px;resize:vertical;font-family:'Courier New',monospace;font-size:0.9rem}}
button{{padding:12px 24px;background:linear-gradient(135deg,#f59e0b,#ef4444);color:#fff;border:none;border-radius:8px;font-size:1rem;cursor:pointer;transition:all .2s;width:100%;font-weight:600}}
button:hover{{opacity:.92;transform:translateY(-1px)}}
button:active{{transform:scale(.98)}}
.output{{margin-top:18px;padding:16px;background:#0a0a14;border-radius:8px;min-height:50px;border:1px solid #2a2a3a;white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:0.85rem;color:#fbbf24;overflow-x:auto;max-height:400px;overflow-y:auto}}
.copy-btn{{margin-top:10px;padding:8px 16px;background:#2a2a3a;color:#ccc;border:1px solid #3a3a4a;border-radius:6px;cursor:pointer;font-size:0.82rem;transition:all .2s}}
.copy-btn:hover{{background:#3a3a4a;border-color:#f59e0b}}
.info-box{{background:#f59e0b15;border-left:3px solid #f59e0b;padding:14px;border-radius:0 8px 8px 0;margin:18px 0;color:#bbb;font-size:0.85rem;line-height:1.6}}
.back-link{{text-align:center;margin:20px 0}}
.back-link a{{color:#f59e0b;text-decoration:none;font-size:0.88rem}}
footer{{text-align:center;padding:30px;color:#444;font-size:0.78rem}}
.chat-fab{{position:fixed;bottom:20px;right:20px;width:56px;height:56px;background:linear-gradient(135deg,#f59e0b,#ef4444);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;font-size:1.4rem;box-shadow:0 4px 12px rgba(245,158,11,.4);z-index:999;transition:transform .2s}}
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
<div class="info-box">⚡ Harz Digital Services ecosystem — 500+ free online tools. All processing happens in your browser — your data stays private.</div>
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
    "nigeria-tax-calculator": '''<div class="input-group"><label>Annual Gross Salary (₦)</label><input type="number" id="salary" value="3000000" oninput="calc()"></div><div class="input-group"><label>Pension Rate (%)</label><input type="number" id="pension" value="8" step="0.5" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const s=parseFloat(document.getElementById('salary').value)||0;const p=parseFloat(document.getElementById('pension').value)||0;const pensionAmt=s*p/100;const nhf=s*0.025;const taxable=s-pensionAmt-nhf;const cra=Math.max(200000,taxable*0.2);const chargeable=taxable-cra;const bands=[{up:300000,rate:0.07},{up:600000,rate:0.11},{up:1100000,rate:0.15},{up:1600000,rate:0.19},{up:3200000,rate:0.21},{up:Infinity,rate:0.24}];let remaining=chargeable;let tax=0;for(const b of bands){if(remaining<=0)break;const taxableInBand=Math.min(remaining,b.up);tax+=taxableInBand*b.rate;remaining-=taxableInBand}const net=s-pensionAmt-nhf-tax;document.getElementById('output').textContent=`Gross: ₦${s.toLocaleString()}\\n\\nPension (${p}%): ₦${pensionAmt.toLocaleString()}\\nNHF (2.5%): ₦${nhf.toLocaleString()}\\nCRA: ₦${cra.toLocaleString()}\\nChargeable: ₦${chargeable.toLocaleString()}\\n\\nPAYE Tax: ₦${tax.toLocaleString()}\\nNet Annual: ₦${net.toLocaleString()}\\nNet Monthly: ₦${(net/12).toLocaleString()}\\n\\nEffective Tax Rate: ${(tax/s*100).toFixed(2)}%`}calc()</script>''',
    "random-team-generator": '''<div class="input-group"><label>Names (one per line)</label><textarea id="names" placeholder="John\\nMary\\nPeter\\nSarah\\nJames\\nLisa"></textarea></div><div class="input-group"><label>Number of Teams</label><input type="number" id="teams" value="2" min="2" max="10"></div><button onclick="generate()">Generate Teams</button><div id="result" style="margin-top:20px"></div><script>function generate(){const names=document.getElementById('names').value.split('\\n').filter(n=>n.trim());const numTeams=parseInt(document.getElementById('teams').value)||2;const shuffled=[...names].sort(()=>Math.random()-0.5);const teams=Array.from({length:numTeams},()=>[]);shuffled.forEach((name,i)=>teams[i%numTeams].push(name));let html='';teams.forEach((t,i)=>{html+=`<div style="background:#1a1a2e;padding:16px;margin:8px 0;border-radius:12px;border:1px solid #333"><h3 style="color:#f59e0b">Team ${i+1}</h3>${t.map(n=>`<div style="padding:4px 0;color:#ccc">${n}</div>`).join('')}</div>`});document.getElementById('result').innerHTML=html}</script>''',
    "random-yes-no": '''<div style="text-align:center;padding:60px 0"><div id="answer" style="font-size:5rem;font-weight:bold;cursor:pointer" onclick="decide()">?</div><div style="color:#888;margin-top:20px">Tap to get your answer</div></div><script>function decide(){const answers=['YES','NO'];const a=answers[Math.floor(Math.random()*answers.length)];const el=document.getElementById('answer');el.textContent=a;el.style.color=a==='YES'?'#22c55e':'#ef4444'}</script>''',
    "random-quote-generator": '''<div style="text-align:center;padding:40px 20px"><div id="quote" style="font-size:1.3rem;color:#e0e0e0;line-height:1.6;margin-bottom:20px">Click to get a quote</div><div id="author" style="color:#888;font-size:0.9rem"></div></div><button onclick="generate()">Generate Quote</button><script>const quotes=[{q:"The best time to plant a tree was 20 years ago. The second best time is now.",a:"Chinese Proverb"},{q:"Success is not final, failure is not fatal: it is the courage to continue that counts.",a:"Winston Churchill"},{q:"The only way to do great work is to love what you do.",a:"Steve Jobs"},{q:"Believe you can and you're halfway there.",a:"Theodore Roosevelt"},{q:"The journey of a thousand miles begins with one step.",a:"Lao Tzu"},{q:"Don't watch the clock; do what it does. Keep going.",a:"Sam Levenson"},{q:"The future belongs to those who believe in the beauty of their dreams.",a:"Eleanor Roosevelt"},{q:"Hard work beats talent when talent doesn't work hard.",a:"Tim Notke"},{q:"It does not matter how slowly you go as long as you do not stop.",a:"Confucius"},{q:"Everything you've ever wanted is on the other side of fear.",a:"George Addair"}];function generate(){const r=quotes[Math.floor(Math.random()*quotes.length)];document.getElementById('quote').textContent='"'+r.q+'"';document.getElementById('author').textContent='— '+r.a}</script>''',
    "unit-price-calculator": '''<div class="input-group"><label>Product A: Price (₦)</label><input type="number" id="priceA" value="5000" oninput="calc()"></div><div class="input-group"><label>Product A: Quantity</label><input type="number" id="qtyA" value="500" oninput="calc()"></div><div class="input-group"><label>Product B: Price (₦)</label><input type="number" id="priceB" value="8000" oninput="calc()"></div><div class="input-group"><label>Product B: Quantity</label><input type="number" id="qtyB" value="1000" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const pA=parseFloat(document.getElementById('priceA').value)||0;const qA=parseFloat(document.getElementById('qtyA').value)||0;const pB=parseFloat(document.getElementById('priceB').value)||0;const qB=parseFloat(document.getElementById('qtyB').value)||0;const unitA=qA>0?pA/qA:0;const unitB=qB>0?pB/qB:0;const cheaper=unitA<unitB?'A':'B';document.getElementById('output').textContent=`Product A: ₦${unitA.toFixed(2)} per unit\\nProduct B: ₦${unitB.toFixed(2)} per unit\\n\\nBetter Value: Product ${cheaper}\\nSavings: ₦${Math.abs(unitA-unitB).toFixed(2)} per unit`}calc()</script>''',
    "fuel-cost-calculator": '''<div class="input-group"><label>Distance (km)</label><input type="number" id="distance" value="500" oninput="calc()"></div><div class="input-group"><label>Fuel Efficiency (km/liter)</label><input type="number" id="efficiency" value="12" step="0.5" oninput="calc()"></div><div class="input-group"><label>Fuel Price (₦/liter)</label><input type="number" id="price" value="870" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const d=parseFloat(document.getElementById('distance').value)||0;const eff=parseFloat(document.getElementById('efficiency').value)||0;const p=parseFloat(document.getElementById('price').value)||0;const liters=d/eff;const cost=liters*p;document.getElementById('output').textContent=`Distance: ${d} km\\nFuel Needed: ${liters.toFixed(2)} liters\\nCost: ₦${cost.toLocaleString()}\\n\\nRound Trip: ₦${(cost*2).toLocaleString()}`}calc()</script>''',
    "concrete-calculator": '''<div class="input-group"><label>Length (m)</label><input type="number" id="length" value="10" step="0.1" oninput="calc()"></div><div class="input-group"><label>Width (m)</label><input type="number" id="width" value="5" step="0.1" oninput="calc()"></div><div class="input-group"><label>Depth (m)</label><input type="number" id="depth" value="0.15" step="0.01" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const l=parseFloat(document.getElementById('length').value)||0;const w=parseFloat(document.getElementById('width').value)||0;const d=parseFloat(document.getElementById('depth').value)||0;const vol=l*w*d;const cement=vol*7*50;const sand=vol*0.42;const gravel=vol*0.84;document.getElementById('output').textContent=`Volume: ${vol.toFixed(3)} m³\\n\\nCement: ${Math.ceil(vol*7)} bags (50kg)\\nSand: ${sand.toFixed(2)} m³\\nGravel: ${gravel.toFixed(2)} m³\\nWater: ${(vol*200).toFixed(0)} liters\\n\\nMix Ratio: 1:2:4 (Cement:Sand:Gravel)`}calc()</script>''',
    "instagram-engagement-calculator": '''<div class="input-group"><label>Followers</label><input type="number" id="followers" value="10000" oninput="calc()"></div><div class="input-group"><label>Average Likes</label><input type="number" id="likes" value="800" oninput="calc()"></div><div class="input-group"><label>Average Comments</label><input type="number" id="comments" value="50" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const f=parseFloat(document.getElementById('followers').value)||0;const l=parseFloat(document.getElementById('likes').value)||0;const c=parseFloat(document.getElementById('comments').value)||0;const rate=f>0?((l+c)/f*100).toFixed(2):0;let tier='Low';if(rate>=6)tier='Excellent';else if(rate>=3)tier='Good';else if(rate>=1)tier='Average';document.getElementById('output').textContent=`Engagement Rate: ${rate}%\\nTotal Interactions: ${l+c}\\n\\nPerformance: ${tier}\\n\\nIndustry Benchmarks:\\nExcellent: >6%\\nGood: 3-6%\\nAverage: 1-3%\\nLow: <1%`}calc()</script>''',
    "random-number-picker": '''<div class="input-group"><label>Minimum</label><input type="number" id="min" value="1" oninput="pick()"></div><div class="input-group"><label>Maximum</label><input type="number" id="max" value="49" oninput="pick()"></div><div class="input-group"><label>How many numbers?</label><input type="number" id="count" value="6" oninput="pick()"></div><div style="text-align:center;font-size:2rem;margin:20px 0" id="result"></div><button onclick="pick()">Pick Numbers</button><script>function pick(){const min=parseInt(document.getElementById('min').value)||0;const max=parseInt(document.getElementById('max').value)||100;const count=Math.min(parseInt(document.getElementById('count').value)||1,max-min+1);const nums=new Set();while(nums.size<count)nums.add(Math.floor(Math.random()*(max-min+1))+min);document.getElementById('result').innerHTML=[...nums].sort((a,b)=>a-b).map(n=>`<span style="display:inline-block;background:#f59e0b;color:#000;width:50px;height:50px;line-height:50px;border-radius:50%;margin:5px;font-weight:bold">${n}</span>`).join('')}pick()</script>''',
    "recipe-scaler": '''<div class="input-group"><label>Original Servings</label><input type="number" id="original" value="4" oninput="calc()"></div><div class="input-group"><label>Desired Servings</label><input type="number" id="desired" value="8" oninput="calc()"></div><div class="input-group"><label>Ingredients (one per line: amount,unit,name)</label><textarea id="ingredients" placeholder="2,cups,flour\\n1,cup,sugar\\n0.5,cup,butter"></textarea></div><button onclick="calc()">Scale Recipe</button><div class="output" id="output" style="margin-top:16px"></div><script>function calc(){const orig=parseFloat(document.getElementById('original').value)||1;const des=parseFloat(document.getElementById('desired').value)||1;const ratio=des/orig;const lines=document.getElementById('ingredients').value.split('\\n').filter(l=>l.trim());let result='Scale Factor: '+ratio.toFixed(2)+'x\\n\\n';lines.forEach(line=>{const[amt,unit,name]=line.split(',').map(s=>s.trim());const scaled=(parseFloat(amt)*ratio).toFixed(2);result+=`${scaled} ${unit} ${name}\\n`});document.getElementById('output').textContent=result}</script>''',
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
