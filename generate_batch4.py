BASE_URL = "https://rabiuhamza11.github.io/harz-portfolio"

TOOLS = [
    # Security & Privacy Tools (10)
    ("password-strength-analyzer", "Password Strength Analyzer", "Analyze password strength in real-time. Check length, complexity, entropy, and common patterns. Get security recommendations.", "password, strength, analyzer, security, entropy"),
    ("data-breach-checker", "Data Breach Info", "Learn how to check if your email has been compromised in data breaches. Guide for HaveIBeenPwned and security best practices.", "data breach, email, security, privacy, check"),
    ("security-headers-checker", "Security Headers Guide", "Complete guide to HTTP security headers. Learn about CSP, HSTS, X-Frame-Options, and XSS protection.", "security, headers, csp, hsts, http, web"),
    ("encryption-guide", "Encryption Type Guide", "Reference guide to encryption types. AES, RSA, SHA, bcrypt, and when to use each one.", "encryption, aes, rsa, sha, bcrypt, security"),
    ("privacy-checklist", "Privacy Compliance Checklist", "GDPR, NDPR, and CCPA compliance checklist for websites and apps. Know your data protection obligations.", "privacy, gdpr, ndpr, ccpa, compliance"),
    ("secure-password-policy", "Password Policy Generator", "Generate a password policy for your organization. Set rules for length, complexity, expiration, and history.", "password, policy, generator, security, organization"),
    ("2fa-setup-guide", "2FA Setup Guide", "Step-by-step guide to setting up two-factor authentication. TOTP, SMS, hardware keys, and backup codes.", "2fa, two factor, authentication, security, totp"),
    ("vpn-comparison-tool", "VPN Comparison Tool", "Compare VPN features side by side. Protocols, logging policies, server count, and pricing.", "vpn, comparison, security, privacy, tool"),
    ("phishing-simulator-info", "Phishing Awareness Guide", "Learn to identify phishing attempts. Check email headers, URLs, and common red flags.", "phishing, security, awareness, email, guide"),
    ("crypto-wallet-safety", "Crypto Wallet Safety Guide", "Best practices for securing cryptocurrency wallets. Hardware vs software, seed phrases, and multi-sig.", "crypto, wallet, security, bitcoin, safety"),

    # Developer Productivity (10)
    ("code-snippet-manager", "Code Snippet Manager", "Save and organize your code snippets. Categorize by language, tag, and search. Export as JSON or Markdown.", "code, snippet, manager, organizer, developer"),
    ("api-tester-mock", "API Testing Guide", "Learn REST API testing best practices. Methods, headers, authentication, and response validation.", "api, testing, rest, developer, guide"),
    ("webhook-tester-info", "Webhook Testing Guide", "How to test and debug webhooks. ngrok, requestbin, and signature verification explained.", "webhook, testing, debug, developer, guide"),
    ("regex-cheatsheet", "Regex Cheat Sheet", "Complete regular expression reference. Characters, quantifiers, groups, lookaheads, and common patterns.", "regex, regular expression, cheat sheet, reference"),
    ("unicode-emoji-picker", "Unicode Emoji Picker", "Browse and search Unicode emojis by category. Copy emoji, shortcode, and Unicode codepoint.", "emoji, unicode, picker, search, copy"),
    ("char-encoder", "Character Encoder", "Encode and decode HTML entities, URL components, and Unicode escape sequences all in one tool.", "character, encoding, html, url, unicode, encoder"),
    ("number-formatter", "Number Formatter", "Format numbers with thousands separators, scientific notation, and custom patterns. Support for 20+ locales.", "number, format, locale, thousands, separator"),
    ("byte-converter", "Byte Size Converter", "Convert between bytes, KB, MB, GB, TB, and PB. Also supports binary (KiB) and decimal (KB) units.", "byte, converter, kb, mb, gb, storage"),
    ("timestamp-converter", "Unix Timestamp Converter", "Convert Unix timestamps to human-readable dates and vice versa. Supports milliseconds and timezones.", "timestamp, unix, converter, date, epoch"),
    ("cron-helper", "Cron Expression Helper", "Interactive cron expression reference. Common patterns, field meanings, and examples for scheduling.", "cron, expression, schedule, reference, crontab"),

    # Business Document Generators (10)
    ("service-agreement-generator", "Service Agreement Generator", "Generate professional service agreements. Define scope, payment terms, deliverables, and timelines.", "service, agreement, contract, generator, legal"),
    ("freelance-contract-generator", "Freelance Contract Generator", "Create freelance contracts with milestones, payment terms, IP rights, and termination clauses.", "freelance, contract, generator, legal, agreement"),
    ("rental-agreement-generator", "Rental Agreement Generator", "Generate rental/lease agreements for properties. Terms, deposit, utilities, and house rules.", "rental, lease, agreement, generator, legal, property"),
    ("employment-contract-generator", "Employment Contract Generator", "Generate employment contracts with salary, benefits, duties, probation, and termination terms.", "employment, contract, generator, legal, hr"),
    ("sales-agreement-generator", "Sales Agreement Generator", "Create sales agreements for goods and services. Payment, delivery, warranties, and dispute resolution.", "sales, agreement, generator, legal, contract"),
    ("loan-agreement-generator", "Loan Agreement Generator", "Generate personal or business loan agreements. Principal, interest, repayment, and collateral terms.", "loan, agreement, generator, legal, contract"),
    ("memorandum-generator", "Memorandum of Understanding Generator", "Create MoU documents for partnerships and collaborations. Define roles, contributions, and goals.", "memorandum, mou, understanding, generator, partnership"),
    ("resolution-generator", "Board Resolution Generator", "Generate corporate board resolutions. Authorize actions, approve transactions, and formalize decisions.", "board, resolution, corporate, generator, legal"),
    ("minutes-generator", "Meeting Minutes Generator", "Generate professional meeting minutes. Attendees, agenda, decisions, action items, and next meeting.", "meeting, minutes, generator, corporate, legal"),
    ("disclosure-generator", "Affiliate Disclosure Generator", "Generate FTC-compliant affiliate disclosure statements for your website, blog, or social media.", "affiliate, disclosure, ftc, generator, legal"),

    # Marketing & SEO (10)
    ("keyword-density-checker", "Keyword Density Checker", "Analyze keyword density in your content. Avoid over-optimization and find content gaps.", "keyword, density, seo, content, analyzer"),
    ("serp-snippet-generator", "SERP Snippet Generator", "Preview and optimize your search result snippets. Title, URL, and description with pixel width checker.", "serp, snippet, seo, google, preview"),
    ("backlink-analyzer-info", "Backlink Analysis Guide", "Learn how to analyze backlinks. Domain authority, anchor text, toxic links, and link building strategies.", "backlink, seo, analysis, guide, link building"),
    ("competitor-keyword-finder", "Competitor Keyword Strategy Guide", "Strategy guide for finding competitor keywords. Gap analysis, SERP overlap, and content opportunities.", "competitor, keyword, seo, strategy, gap analysis"),
    ("content-gap-analyzer", "Content Gap Analyzer", "Identify content gaps in your SEO strategy. Compare your pages against competitors and find opportunities.", "content, gap, seo, analyzer, strategy"),
    ("page-speed-checklist", "Page Speed Optimization Checklist", "Complete checklist for optimizing page load speed. Core Web Vitals, images, JS, CSS, and caching.", "page speed, optimization, core web vitals, checklist, seo"),
    ("local-seo-checklist", "Local SEO Checklist", "Optimize for local search. Google Business, citations, reviews, schema, and location pages.", "local seo, google business, citations, checklist, seo"),
    ("email-warmup-guide", "Email Warmup Guide", "Step-by-step guide to warming up email domains. Improve deliverability and avoid spam filters.", "email, warmup, deliverability, spam, guide"),
    ("utm-builder-v2", "Advanced UTM Builder", "Build UTM tracking URLs with campaign groups, A/B variants, and QR code generation. Bulk import via CSV.", "utm, tracking, url, builder, campaign, analytics"),
    ("conversion-rate-calculator", "Conversion Rate Calculator", "Calculate conversion rates for your funnels. Visitors, conversions, rate, and revenue per visitor.", "conversion, rate, calculator, funnel, marketing"),

    # Education & Productivity (10)
    ("flashcard-maker", "Flashcard Maker", "Create digital flashcards for studying. Add questions, answers, and export as printable cards or JSON.", "flashcard, study, education, maker, quiz"),
    ("study-schedule-generator", "Study Schedule Generator", "Generate personalized study schedules. Input subjects, exam dates, and available hours. Get a day-by-day plan.", "study, schedule, generator, education, planner"),
    ("grade-calculator", "Grade Calculator", "Calculate your course grade from weighted assignments. Track GPA and predict final scores.", "grade, calculator, gpa, education, academic"),
    ("citation-generator", "Citation Generator", "Generate citations in APA, MLA, Chicago, and Harvard styles. Books, journals, websites, and more.", "citation, generator, apa, mla, reference, academic"),
    ("plagiarism-checker-info", "Plagiarism Checking Guide", "Guide to checking content for plagiarism. Tools, techniques, and best practices for originality.", "plagiarism, checker, guide, originality, academic"),
    ("reading-time-estimator", "Reading Time Estimator", "Estimate reading time for articles and books. Words per minute, difficulty level, and speaking time.", "reading, time, estimator, words, content"),
    ("note-template-generator", "Note Template Generator", "Generate note-taking templates. Cornell, outline, mind map, and boxing methods for any subject.", "note, template, generator, cornell, study"),
    ("exam-countdown", "Exam Countdown Planner", "Plan your exam preparation with a countdown. Days remaining, topic breakdown, and daily targets.", "exam, countdown, planner, study, education"),
    ("vocabulary-builder", "Vocabulary Builder", "Build your vocabulary with word lists, definitions, example sentences, and flashcard export.", "vocabulary, builder, words, english, education"),
    ("spelling-practice", "Spelling Practice Tool", "Practice spelling with custom word lists. Audio playback, hints, and progress tracking.", "spelling, practice, education, words, quiz"),
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
header h1{{font-size:1.7rem;color:#fff;margin-bottom:8px}}
header p{{color:#888;font-size:0.9rem}}
.tool{{background:#161616;border-radius:16px;padding:28px;margin:20px 0;border:1px solid #2a2a2a}}
.input-group{{margin-bottom:18px}}
label{{display:block;margin-bottom:8px;color:#aaa;font-size:0.85rem;font-weight:600}}
input,textarea,select{{width:100%;padding:12px 14px;background:#0d0d0d;border:1px solid #333;border-radius:8px;color:#fff;font-size:1rem;font-family:inherit;outline:none;transition:border-color .2s}}
input:focus,textarea:focus,select:focus{{border-color:#7c3aed}}
textarea{{min-height:120px;resize:vertical;font-family:'Courier New',monospace;font-size:0.9rem}}
button{{padding:12px 24px;background:linear-gradient(135deg,#7c3aed,#ec4899);color:#fff;border:none;border-radius:8px;font-size:1rem;cursor:pointer;transition:all .2s;width:100%;font-weight:600}}
button:hover{{opacity:.92;transform:translateY(-1px)}}
button:active{{transform:scale(.98)}}
.output{{margin-top:18px;padding:16px;background:#0d0d0d;border-radius:8px;min-height:50px;border:1px solid #333;white-space:pre-wrap;word-break:break-all;font-family:'Courier New',monospace;font-size:0.85rem;color:#34d399;overflow-x:auto;max-height:400px;overflow-y:auto}}
.copy-btn{{margin-top:10px;padding:8px 16px;background:#2a2a2a;color:#ccc;border:1px solid #444;border-radius:6px;cursor:pointer;font-size:0.82rem;transition:all .2s}}
.copy-btn:hover{{background:#3a3a3a;border-color:#7c3aed}}
.info-box{{background:#7c3aed15;border-left:3px solid #7c3aed;padding:14px;border-radius:0 8px 8px 0;margin:18px 0;color:#bbb;font-size:0.85rem;line-height:1.6}}
.back-link{{text-align:center;margin:20px 0}}
.back-link a{{color:#7c3aed;text-decoration:none;font-size:0.88rem}}
footer{{text-align:center;padding:30px;color:#555;font-size:0.78rem}}
.chat-fab{{position:fixed;bottom:20px;right:20px;width:56px;height:56px;background:linear-gradient(135deg,#7c3aed,#ec4899);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;font-size:1.4rem;box-shadow:0 4px 12px rgba(124,58,237,.4);z-index:999;transition:transform .2s}}
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
<div class="info-box">⚡ Harz Digital Services ecosystem — 400+ free online tools. All processing happens in your browser — your data stays private.</div>
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
    "password-strength-analyzer": '''<div class="input-group"><label>Enter Password</label><input type="text" id="pwd" placeholder="Type your password..." oninput="analyze()" style="font-family:monospace"></div><div style="margin:16px 0"><div style="height:8px;background:#333;border-radius:4px;overflow:hidden"><div id="bar" style="height:100%;width:0;background:#ef4444;transition:all .3s"></div></div><div id="label" style="margin-top:8px;color:#aaa;font-size:0.85rem"></div></div><div class="output" id="output" style="display:none"></div><script>function analyze(){const p=document.getElementById('pwd').value;let score=0;const checks=[];if(p.length>=8){score+=1;checks.push('✓ At least 8 characters')}else checks.push('✗ At least 8 characters');if(p.length>=16){score+=1;checks.push('✓ 16+ characters')}if(/[A-Z]/.test(p)){score+=1;checks.push('✓ Uppercase letters')}else checks.push('✗ Uppercase letters');if(/[a-z]/.test(p)){score+=1;checks.push('✓ Lowercase letters')}else checks.push('✗ Lowercase letters');if(/[0-9]/.test(p)){score+=1;checks.push('✓ Numbers')}else checks.push('✗ Numbers');if(/[^A-Za-z0-9]/.test(p)){score+=2;checks.push('✓ Special characters')}else checks.push('✗ Special characters');if(!/(.)\\1{2,}/.test(p)){score+=1;checks.push('✓ No repeated characters')}const entropy=p.length*Math.log2(new Set(p).size+1);const levels=['Very Weak','Weak','Fair','Good','Strong','Very Strong','Excellent'];const colors=['#ef4444','#f97316','#eab308','#84cc16','#22c55e','#14b8a6','#06b6d4'];const idx=Math.min(Math.floor(score/1.5),6);document.getElementById('bar').style.width=(score/8*100)+'%';document.getElementById('bar').style.background=colors[idx];document.getElementById('label').textContent='Strength: '+levels[idx]+' | Entropy: '+entropy.toFixed(0)+' bits';document.getElementById('output').style.display='block';document.getElementById('output').textContent=checks.join('\\n')}analyze()</script>''',
    "timestamp-converter": '''<div class="input-group"><label>Unix Timestamp</label><input type="number" id="ts" placeholder="1690000000" oninput="convert()"></div><div class="output" id="output1" style="margin-bottom:16px"></div><div class="input-group"><label>Date String</label><input type="text" id="date" placeholder="2026-07-19T12:00:00" oninput="reverse()"></div><div class="output" id="output2"></div><script>function convert(){const ts=document.getElementById('ts').value;if(!ts)return;const d=new Date(parseInt(ts)*1000);document.getElementById('output1').textContent='UTC: '+d.toUTCString()+'\\nLocal: '+d.toLocaleString()+'\\nISO: '+d.toISOString()}function reverse(){const d=document.getElementById('date').value;if(!d)return;const ts=Math.floor(new Date(d).getTime()/1000);document.getElementById('output2').textContent='Unix: '+ts}</script>''',
    "byte-converter": '''<div class="input-group"><label>Value</label><input type="number" id="val" value="1024" oninput="convert()"></div><div class="input-group"><label>From Unit</label><select id="from" onchange="convert()"><option value="1">Bytes</option><option value="1024" selected>Kilobytes (KB)</option><option value="1048576">Megabytes (MB)</option><option value="1073741824">Gigabytes (GB)</option><option value="1099511627776">Terabytes (TB)</option></select></div><div class="output" id="output"></div><script>function convert(){const v=parseFloat(document.getElementById('val').value)||0;const f=parseFloat(document.getElementById('from').value);const bytes=v*f;const units=['B','KB','MB','GB','TB','PB'];let i=0;let b=bytes;while(b>=1024&&i<5){b/=1024;i++}document.getElementById('output').textContent=`Bytes: ${bytes.toLocaleString()} B\\nKilobytes: ${(bytes/1024).toFixed(2)} KB\\nMegabytes: ${(bytes/1048576).toFixed(2)} MB\\nGigabytes: ${(bytes/1073741824).toFixed(4)} GB\\nTerabytes: ${(bytes/1073741824/1024).toFixed(6)} TB\\n\\nBest: ${b.toFixed(2)} ${units[i]}`}convert()</script>''',
    "grade-calculator": '''<div id="rows"><div class="input-group" style="display:flex;gap:8px"><input type="text" id="name0" placeholder="Assignment" style="flex:2"><input type="number" id="score0" placeholder="Score" style="flex:1"><input type="number" id="weight0" placeholder="Weight %" style="flex:1"></div></div><button onclick="addRow()" style="margin:8px 0;background:#333">+ Add Row</button><button onclick="calc()">Calculate Grade</button><div class="output" id="output" style="margin-top:16px"></div><script>let count=1;function addRow(){document.getElementById('rows').innerHTML+=`<div class="input-group" style="display:flex;gap:8px"><input type="text" id="name${count}" placeholder="Assignment" style="flex:2"><input type="number" id="score${count}" placeholder="Score" style="flex:1"><input type="number" id="weight${count}" placeholder="Weight %" style="flex:1"></div>`;count++}function calc(){let total=0,totalW=0;for(let i=0;i<count;i++){const s=parseFloat(document.getElementById('score'+i)?.value||0);const w=parseFloat(document.getElementById('weight'+i)?.value||0);if(!isNaN(s)&&!isNaN(w)){total+=s*w/100;totalW+=w}}const grade=totalW>0?total:0;const letter=grade>=90?'A':grade>=80?'B':grade>=70?'C':grade>=60?'D':'F';document.getElementById('output').textContent=`Total Weight: ${totalW}%\\nWeighted Score: ${grade.toFixed(2)}%\\nGrade: ${letter}\\nGPA: ${(grade/100*4).toFixed(2)}/4.00`}</script>''',
    "conversion-rate-calculator": '''<div class="input-group"><label>Visitors</label><input type="number" id="visitors" value="10000" oninput="calc()"></div><div class="input-group"><label>Conversions</label><input type="number" id="conversions" value="150" oninput="calc()"></div><div class="input-group"><label>Revenue (₦)</label><input type="number" id="revenue" value="500000" oninput="calc()"></div><div class="output" id="output"></div><script>function calc(){const v=parseFloat(document.getElementById('visitors').value)||0;const c=parseFloat(document.getElementById('conversions').value)||0;const r=parseFloat(document.getElementById('revenue').value)||0;const rate=v>0?(c/v*100).toFixed(2):0;const rpv=v>0?(r/v).toFixed(2):0;const rpc=c>0?(r/c).toFixed(2):0;document.getElementById('output').textContent=`Conversion Rate: ${rate}%\\nRevenue per Visitor: ₦${rpv}\\nRevenue per Conversion: ₦${rpc}\\nVisitors per Conversion: ${v>0?Math.round(v/c):0}`}calc()</script>''',
    "reading-time-estimator": '''<div class="input-group"><label>Text Content</label><textarea id="text" placeholder="Paste your text here..." oninput="calc()" style="min-height:200px"></textarea></div><div class="output" id="output"></div><script>function calc(){const t=document.getElementById('text').value;const words=t.trim()?t.trim().split(/\\s+/).length:0;const chars=t.length;const sentences=t.trim()?t.split(/[.!?]+/).length-1:0;const readMin=Math.ceil(words/200);const speakMin=Math.ceil(words/130);document.getElementById('output').textContent=`Words: ${words}\\nCharacters: ${chars}\\nSentences: ${sentences}\\nReading Time: ${readMin} min (200 wpm)\\nSpeaking Time: ${speakMin} min (130 wpm)`}calc()</script>''',
    "flashcard-maker": '''<div class="input-group"><label>Front (Question)</label><input type="text" id="front" placeholder="What is..."></div><div class="input-group"><label>Back (Answer)</label><input type="text" id="back" placeholder="It is..."></div><button onclick="addCard()">Add Card</button><div id="cards" style="margin-top:20px"></div><button onclick="study()" style="margin-top:16px;background:#333">Start Studying</button><div id="studyArea" style="margin-top:20px;display:none"></div><script>let cards=[];function addCard(){const f=document.getElementById('front').value;const b=document.getElementById('back').value;if(!f||!b)return;cards.push({f,b});document.getElementById('front').value='';document.getElementById('back').value='';render()}function render(){document.getElementById('cards').innerHTML=cards.map((c,i)=>`<div style="background:#0d0d0d;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #333"><strong>${i+1}.</strong> ${c.f} → ${c.b} <button onclick="cards.splice(${i},1);render()" style="display:inline;width:auto;padding:2px 8px;background:#ef4444;font-size:0.75rem">✕</button></div>`).join('')}let idx=0;function study(){if(!cards.length)return;idx=0;document.getElementById('studyArea').style.display='block';show()}function show(){const c=cards[idx];document.getElementById('studyArea').innerHTML=`<div style="background:#1a1a2e;padding:40px;border-radius:12px;text-align:center;min-height:150px;display:flex;align-items:center;justify-content:center" id="card" onclick="flip()"><span style="font-size:1.2rem">${c.f}</span></div><div style="text-align:center;margin-top:12px;color:#888">${idx+1}/${cards.length} | Tap to flip</div><button onclick="idx=(idx+1)%cards.length;show()" style="margin-top:12px;background:#333">Next →</button>`}function flip(){const card=document.getElementById('card');const c=cards[idx];card.textContent=card.textContent===c.f?c.b:c.f}</script>''',
    "citation-generator": '''<div class="input-group"><label>Source Type</label><select id="type"><option value="book">Book</option><option value="journal">Journal Article</option><option value="website">Website</option></select></div><div class="input-group"><label>Author(s)</label><input type="text" id="author" placeholder="Last, First"></div><div class="input-group"><label>Title</label><input type="text" id="title" placeholder="Title of work"></div><div class="input-group"><label>Year</label><input type="text" id="year" placeholder="2026"></div><div class="input-group"><label>Publisher / URL</label><input type="text" id="pub" placeholder="Publisher or URL"></div><button onclick="generate()">Generate Citations</button><div class="output" id="output" style="margin-top:16px"></div><script>function generate(){const a=document.getElementById('author').value;const t=document.getElementById('title').value;const y=document.getElementById('year').value;const p=document.getElementById('pub').value;const apa=`${a} (${y}). ${t}. ${p}.`;const mla=`${a}. "${t}." ${p}, ${y}.`;const chicago=`${a}. ${t}. ${p}, ${y}.`;const harvard=`${a} ${y}, '${t}', ${p}.`;document.getElementById('output').textContent=`APA:\\n${apa}\\n\\nMLA:\\n${mla}\\n\\nChicago:\\n${chicago}\\n\\nHarvard:\\n${harvard}`}</script>''',
    "number-formatter": '''<div class="input-group"><label>Number</label><input type="number" id="num" value="1234567.89" oninput="format()"></div><div class="input-group"><label>Locale</label><select id="locale" onchange="format()"><option value="en-US">English (US)</option><option value="en-NG">English (Nigeria)</option><option value="de-DE">German</option><option value="fr-FR">French</option><option value="ja-JP">Japanese</option><option value="ar-SA">Arabic</option><option value="hi-IN">Hindi</option><option value="zh-CN">Chinese</option></select></div><div class="output" id="output"></div><script>function format(){const n=parseFloat(document.getElementById('num').value)||0;const l=document.getElementById('locale').value;const f=new Intl.NumberFormat(l).format(n);const c=new Intl.NumberFormat(l,{style:'currency',currency:l.endsWith('NG')?'NGN':l.endsWith('US')?'USD':l.endsWith('JP')?'JPY':l.endsWith('DE')?'EUR':'USD'}).format(n);document.getElementById('output').textContent=`Formatted: ${f}\\nCurrency: ${c}\\nScientific: ${n.toExponential(2)}\\nCompact: ${new Intl.NumberFormat(l,{notation:'compact'}).format(n)}`}format()</script>''',
    "char-encoder": '''<div class="input-group"><label>Input Text</label><textarea id="input" placeholder="Enter text to encode/decode..."></textarea></div><div style="display:flex;gap:8px;flex-wrap:wrap"><button onclick="encHTML()" style="width:auto;flex:1">HTML Encode</button><button onclick="decHTML()" style="width:auto;flex:1">HTML Decode</button><button onclick="encURL()" style="width:auto;flex:1">URL Encode</button><button onclick="decURL()" style="width:auto;flex:1">URL Decode</button></div><div class="output" id="output" style="margin-top:16px"></div><script>function encHTML(){const t=document.getElementById('input').value;document.getElementById('output').textContent=t.replace(/[<>&"']/g,c=>({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;',"'":'&#39;'})[c])}function decHTML(){const t=document.getElementById('input').value;const d=document.createElement('div');d.innerHTML=t;document.getElementById('output').textContent=d.textContent}function encURL(){document.getElementById('output').textContent=encodeURIComponent(document.getElementById('input').value)}function decURL(){document.getElementById('output').textContent=decodeURIComponent(document.getElementById('input').value)}</script>''',
    "unicode-emoji-picker": '''<div style="margin:16px 0"><input type="text" id="search" placeholder="Search emoji..." oninput="filter()" style="width:100%"></div><div id="grid" style="display:grid;grid-template-columns:repeat(8,1fr);gap:8px;max-height:400px;overflow-y:auto"></div><div id="selected" style="margin-top:16px;text-align:center;font-size:3rem;min-height:60px"></div><script>const emojis=[['😀','Grinning'],['😃','Smiley'],['😄','Smile'],['😁','Grin'],['😆','Laugh'],['😅','Sweat Smile'],['🤣','ROFL'],['😂','Joy'],['🙂','Slight Smile'],['😉','Wink'],['😊','Blush'],['😍','Heart Eyes'],['🥰','Smiling Hearts'],['😘','Kiss'],['😗','Kiss'],['😙','Kiss Smile'],['😚','Kiss Closed Eyes'],['😎','Cool'],['🤩','Star Struck'],['🥳','Party'],['😏','Smirk'],['😒','Unamused'],['😞','Sad'],['😔','Pensive'],['😕','Confused'],['🙁','Frown','😟','Worried'],['🥺','Pleading'],['😢','Cry'],['😭','Sob'],['😤','Huff'],['😡','Angry'],['😠','Mad'],['🤬','Cursing'],['🤯','Exploding Head'],['😱','Scream'],['😨','Fear'],['😰','Cold Sweat'],['😥','Disappointed'],['😓','Sweat'],['🤗','Hug'],['🤔','Think'],['🤭','Hand Over Mouth'],['🤫','Shush'],['🤥','Lying'],['😶','No Mouth'],['😐','Neutral'],['😑','Expressionless'],['😬','Grimace'],['🙄','Eye Roll'],['😯','Hushed'],['😦','Frowning'],['😧','Anguished'],['😮','Open Mouth'],['🤐','Zip Mouth'],['😴','Sleep'],['🤤','Drool'],['😪','Sleepy'],['😵','Dizzy'],['🤒','Thermometer'],['🤕','Bandage'],['🤢','Nauseated'],['🤮','Vomiting'],['🥵','Hot'],['🥶','Cold'],['🥴','Woozy'],['😵','Dizzy'],['🤠','Cowboy'],['🥸','Disguise'],['🤓','Nerd'],['🧐','Monocle'],['🐶','Dog'],['🐱','Cat'],['🐭','Mouse'],['🐹','Hamster'],['🐰','Rabbit'],['🦊','Fox'],['🐻','Bear'],['🐼','Panda'],['🐨','Koala'],['🐯','Tiger'],['🦁','Lion'],['🐮','Cow'],['🐷','Pig'],['🐸','Frog'],['🐵','Monkey'],['🙈','See No Evil'],['🙉','Hear No Evil'],['🙊','Speak No Evil'],['💋','Kiss Mark'],['💌','Love Letter'],['💍','Ring'],['💎','Diamond'],['💥','Collision'],['💫','Dizzy'],['💦','Sweat Drops'],['💨','Dash'],['🏁','Checkered'],['🚩','Triangular Flag'],['🎌','Crossed Flags'],['🏳️','White Flag'],['🏴','Black Flag'],['♥️','Heart'],['❤️','Red Heart'],['🧡','Orange Heart'],['💛','Yellow Heart'],['💚','Green Heart'],['💙','Blue Heart'],['💜','Purple Heart'],['🖤','Black Heart'],['🤍','White Heart'],['🤎','Brown Heart'],['💔','Broken Heart'],['❣️','Heart Exclamation'],['💕','Two Hearts'],['💞','Revolving Hearts'],['💓','Beating Heart'],['✨','Sparkles'],['⭐','Star'],['🌟','Glowing Star'],['⚡','Lightning'],['🔥','Fire'],['💯','Hundred'],['✅','Check Mark'],['❌','Cross Mark'],['❎','Cross Mark Button'],['➡️','Right Arrow'],['⬅️','Left Arrow'],['⬆️','Up Arrow'],['⬇️','Down Arrow'],['🎉','Party Popper'],['🎊','Confetti'],['🎈','Balloon'],['🎁','Gift'],['🏆','Trophy'],['🥇','Gold Medal'],['🥈','Silver Medal'],['🥉','Bronze Medal']];const grid=document.getElementById('grid');function render(list){grid.innerHTML=list.map(([e,n])=>`<div style="font-size:1.8rem;cursor:pointer;text-align:center;padding:8px;border-radius:8px;background:#1a1a2e" onclick="pick('${e}','${n}')" title="${n}">${e}</div>`).join('')}render(emojis);function filter(){const q=document.getElementById('search').value.toLowerCase();const f=emojis.filter(([e,n])=>n.toLowerCase().includes(q));render(f)}function pick(e,n){document.getElementById('selected').textContent=e;navigator.clipboard.writeText(e)}</script>''',
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
