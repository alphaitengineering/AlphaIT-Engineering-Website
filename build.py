"""Reproducible static site generator. Only public customer-profile content is imported."""
from pathlib import Path
import ast, html, json, re
from PIL import Image

ROOT = Path(__file__).parent
OUT = ROOT / 'dist'
SOURCE = Path(r'C:\Users\alpha\OneDrive\Desktop\AlphaIT Engineering')
PROFILE = SOURCE / '00_COMMERCIAL_COMMAND/05_COMMERCIAL_DOCUMENTS/01_ALPHAIT/_build_company_profile_and_proposal_20260911.py'
if PROFILE.exists():
 tree = ast.parse(PROFILE.read_text(encoding='utf-8-sig'))
 expr = next(n.value for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'PRODUCTS' for t in n.targets))
 products = eval(compile(ast.Expression(expr), '<profile data>', 'eval'), {'__builtins__': {}}, {'FLOW_ORANGE':'F67411','COBALT':'2F5BFF'})
else:
 products = json.loads((ROOT/'products.json').read_text(encoding='utf-8'))
products.sort(key=lambda p: 0 if p['name']=='Verdika' else 1)
SLUGS = {'Verdika':'verdika','Varren':'varren','Varren Aegis':'varren-aegis','Varren Herald':'varren-herald','LisBon Signal Infrastructure (LSI)':'lisbon-signal','LisBon Trust Infrastructure (LTI)':'lisbon-trust','LisCredit Marketplace':'liscredit','Trust App':'trust-app','LisBon Flow Infrastructure (LFI)':'lisbon-flow','Flow App':'flow-app','Pollenair':'pollenair','Focused AlphaIT Build':'business-systems-engineering'}
ICONS = {'verdika':'verdika-mark','varren':'varren-mark','aegis':'varren-aegis-mark','herald':'varren-herald-mark','lsi':'lsi-mark','lisbon':'lisbon-icon','liscredit':'liscredit-mark','lfi':'lfi-mark','flow':'flow-mark','pollenair':'pollenair-mark','alphait':'alphait-mark'}
BUYERS = {
 'Verdika':'Businesses, institutions and public bodies that need to understand customer, employee or public experience.',
 'Varren':'Organisations that need research, plans, content, approvals and authorised commercial action to work together.',
 'Varren Aegis':'Teams responsible for live websites, platforms and digital services.',
 'Varren Herald':'Service businesses and platform teams that want to bring customers back for a useful, timely reason.',
 'LisBon Signal Infrastructure (LSI)':'Banks, lenders, fintechs and teams that need reliable signals from financial records.',
 'LisBon Trust Infrastructure (LTI)':'Banks, lenders, fintechs and capital providers assessing individuals, businesses or institutions.',
 'LisCredit Marketplace':'Banks, fintechs and funds looking for relevant, evidence-backed credit applications.',
 'Trust App':'Lenders and institutions that need a clear financial-profile and credit-application journey for customers.',
 'LisBon Flow Infrastructure (LFI)':'Transport, logistics and delivery businesses that want connected operations under their own brand.',
 'Flow App':'Transport and logistics businesses that need a connected booking and service experience for customers and drivers.',
 'Pollenair':'Institutions, employers and sponsors running practical skills programmes.',
 'Focused AlphaIT Build':'Organisations whose service, process or new offering cannot be served fully by an existing system.'}
MEASURES = ['Feedback reaching the right stakeholder; time to respond; recurring issues.','Time from brief to approval; completed actions; verified delivery records.','Time to detect issues; time to resolve them; successful repeat checks.','Recovered customer journeys; contact quality; response and opt-out rates.','Review time; records requiring investigation; completeness of decision evidence.','Decision turnaround; policy consistency; affordability and exposure records.','Relevant applications; time to review; progress through provider decisions.','Profile completion; application completion; customer support requests.','Booking completion; delivery time; dispatch effort; settlement exceptions.','Booking completion; status enquiries; completed journeys.','Participation; progress; completion; learners needing support.','The agreed change in cost, time, service quality, visibility or revenue opportunity.']
for p,m in zip(products,MEASURES):
 p['slug']=SLUGS[p['name']]; p['icon']=ICONS[p['icon_key']]+'.png'; p['buyer']=BUYERS[p['name']];p['measure']=m

# Website copy is intentionally maintained here rather than inherited blindly from
# an older document build. These statements reflect the founder-approved product
# briefs and preserve the distinction between product capability and deployment proof.
PRODUCT_OVERRIDES = {
 'Verdika': {
  'promise':'See what people experience. Fix what matters next.',
  'description':'Verdika turns ratings, reviews, feedback and participation into a clear view of what people experience, what keeps going wrong and what needs attention. It connects recurring patterns with the responsible team, the response and what people experience afterwards.',
  'situation':'Customers, employees, members, service users or the public experience something an organisation needs to understand.',
  'system':'Verdika structures each contribution, reveals recurring patterns and puts the relevant finding in front of the responsible team.',
  'visible':'Leaders can see what people experienced, what requires attention, what the organisation did and what changed afterwards.',
  'index':'Experience intelligence and accountability',
  'measure':'Participation quality; recurring patterns; response ownership; time to act; follow-up experience.'},
 'Varren': {
  'promise':'Tell Varren what needs to happen.',
  'description':'Varren is the governed operator AlphaIT is building to turn organisational intent into planned, authorised, executed and verified work. It brings intelligence, connected tools, approvals, evidence and continuous improvement into one operating experience.',
  'situation':'Important work is spread across people, models, tools, accounts and channels, while the organisation still has to coordinate every step.',
  'system':'Varren organises the work, selects the right intelligence and tools, performs authorised actions, pauses for judgement and verifies the result.',
  'visible':'The organisation sees the objective, plan, approvals, completed work, evidence, cost and the next recommended action in one record.',
  'index':'Governed organisational execution',
  'measure':'Time from intent to verified result; approval time; completed work; cost; evidence quality; improved next actions.'},
 'Varren Aegis': {
  'promise':'Attack your platform before anyone else does, then prove it is fixed.',
  'display_promise':'Attack your platform first. Prove the fix.',
  'description':'Varren Aegis watches, attacks and witnesses a digital platform, then holds every finding open until the check that found it passes again. It can examine security, performance, integrations, user experience, business logic, billing and releases.',
  'situation':'A platform can look healthy while a security boundary, payment, journey, integration or pricing rule is already failing.',
  'system':'Sentinel watches. Crucible attacks. Witness sees what real users hit. Warden keeps the finding open until a repeat check proves the fix.',
  'visible':'Teams see the verdict, the exact finding, its cause, priority, responsible role, recommended fix and verified closure.',
  'index':'Platform assurance',
  'measure':'Time to find; time to verified fix; repeat checks passing; customer-visible issues prevented; commercial leaks found.'},
 'Varren Herald': {
  'promise':'Bring customers back with something true to say.',
  'description':'Varren Herald finds people who stopped partway, waits for a real reason to return, checks permission, uses approved wording and measures what came back against a group left alone.',
  'situation':'People start an application, purchase, enrolment or service journey and stop, while the organisation cannot tell who may be contacted or what would genuinely matter.',
  'system':'Herald finds where they stopped, identifies a true occasion, checks lawful contact rules, locks approved wording and holds back a comparison group.',
  'visible':'The organisation sees who was reachable, what was sent or refused, why, and how many reached the goal compared with people left alone.',
  'index':'Measured customer re-engagement',
  'measure':'Goal reached against held-back group; movement past the stalled step; lawful reachability; refusals; withdrawals.'},
 'LisBon Signal Infrastructure (LSI)': {
  'promise':'Turn financial records into evidence systems can trust.',
  'display_promise':'Make financial records trustworthy.',
  'description':'LSI ingests, validates and structures financial records before they influence a consequential decision. It checks source integrity, identifies financial activity and produces governed signals with clear confidence.',
  'situation':'A bank, lender or platform receives raw financial records that cannot safely move straight into a decision.',
  'system':'LSI checks the source, structures transactions and periods, evaluates integrity and produces governed financial signals.',
  'visible':'The authorised downstream system receives structured evidence with its source, confidence and issues requiring review.',
  'index':'Financial data-truth infrastructure',
  'measure':'Records processed; validation exceptions; review time; signal completeness; evidence confidence.'},
 'LisBon Trust Infrastructure (LTI)': {
  'promise':'Turn governed evidence into decisions you can explain, control and replay.',
  'display_promise':'Make every credit decision explainable.',
  'description':'LTI is deterministic infrastructure for governing financial trust, eligibility, authorisation, exposure and credit obligations. It preserves the evidence, rules, state and history behind each consequential decision.',
  'situation':'A bank, lender, fintech or capital provider must know what it is authorised to do, why and what happens after the decision.',
  'system':'LTI applies governed evidence and approved policy to trust, eligibility, exposure and obligation states, with replayable decision history.',
  'visible':'The institution sees the evidence, applicable rule, decision path, exposure and obligation lifecycle together.',
  'index':'Trust and credit decision infrastructure',
  'measure':'Decision consistency; time to decision; replayability; exposure visibility; obligation-state accuracy.'},
 'LisCredit Marketplace': {
  'promise':'Bring qualified demand and the right capital together.',
  'description':'LisCredit is marketplace infrastructure for bringing multiple sources of qualified demand and multiple capital providers into one controlled operating environment. It can be deployed as a marketplace, embedded in an existing platform or connected to participating providers.',
  'situation':'Qualified people and businesses need suitable capital, while providers need relevant demand that fits their own products and rules.',
  'system':'LisCredit brings qualified demand, applicable products, provider routes, offers and origination workflows into one governed marketplace journey.',
  'visible':'Operators see both sides of the market, providers see relevant opportunities and qualified applicants see the routes available to them.',
  'index':'Credit marketplace infrastructure',
  'buyer':'Marketplace operators, banks, lenders, funds, fintechs and platforms that want to launch, embed or participate in a controlled credit marketplace.',
  'measure':'Qualified demand; provider participation; relevant matches; time to provider decision; origination progress.'},
 'Trust App': {
  'promise':'Your bank statement, turned into trust.',
  'description':'LisBon Trust App gives people a clear way to submit or connect financial evidence, see their Trust Profile and carry that context into credit-access journeys. It is the consumer surface of the LisBon financial infrastructure.',
  'situation':'A person or microbusiness has financial activity, but the evidence remains trapped in documents and difficult for institutions to understand.',
  'system':'The app connects the user to governed financial evidence, a Trust Profile and the relevant next action without taking over the provider decision.',
  'visible':'The user sees what evidence was accepted, the trust context available and which action is possible next.',
  'index':'Consumer financial trust application',
  'measure':'Evidence completion; Trust Profile completion; eligible next steps; application progress; support demand.'},
 'LisBon Flow Infrastructure (LFI)': {
  'promise':'Give recurring physical operations one operating truth.',
  'description':'LFI coordinates route-based work across operators, jobs, assets, locations, execution states and completion records. It gives transport, logistics, delivery and field-service organisations one authoritative view of what should move and what actually happened.',
  'situation':'Routes, jobs and field work are split across calls, messages, paper, spreadsheets and disconnected systems.',
  'system':'LFI maintains the operating state behind scheduled work, assignments, execution, completion, exceptions and history.',
  'visible':'Managers and field teams see the same operation from the view appropriate to their role.',
  'index':'Route operations infrastructure',
  'measure':'Assignment clarity; execution visibility; completion evidence; exception time; reconciliation effort.'},
 'Flow App': {
  'promise':'Run work on the move from one operating view.',
  'description':'LisBon Flow is the role-specific operating application for organisations using LFI. Managers, dispatchers, drivers and field operators see the work, ownership, current state, completion and exceptions relevant to them.',
  'situation':'Different people in a movement operation need different views of the same work, but still need one shared operating truth.',
  'system':'Flow gives each authorised role the appropriate view while every action remains connected to the state held in LFI.',
  'visible':'A field update changes the manager view immediately because both roles work against the same operation.',
  'index':'Operations application',
  'measure':'Work accepted; state updates; completion; exceptions resolved; status enquiries reduced.'},
 'Pollenair': {
  'promise':'Make practical learning and capability visible.',
  'description':'Pollenair turns learning activity, practical work and demonstrated progress into a clearer record of what someone is learning, practising and becoming capable of doing.',
  'situation':'Attendance and course completion show that learning happened, but do not show what a learner can actually do.',
  'system':'Pollenair connects concepts, tests, corrections, practical tasks and submitted evidence into a continuing capability record.',
  'visible':'Learners and sponsoring organisations see practical progress, demonstrated work and the capabilities supported by that evidence.',
  'index':'Practical capability infrastructure',
  'measure':'Practical tasks completed; evidence quality; capability progression; consistency; support required.'},
 'Focused AlphaIT Build': {
  'promise':'Engineer the missing system behind your next opportunity.',
  'description':'When an existing AlphaIT system does not fully fit, we map the real operation, find the missing capability or connection and engineer the focused system required to improve the work or launch the new service.',
  'situation':'An organisation sees an opportunity or operating gap that cannot be carried completely by an existing product.',
  'system':'AlphaIT defines the outcome, maps the people and systems involved, architects the missing layer and builds it around measurable acceptance checks.',
  'visible':'The organisation receives a working connected route it can operate, measure and extend.',
  'index':'Focused product engineering',
  'measure':'The agreed change in service, revenue opportunity, cost, time, visibility, control or launch readiness.'}
}
for p in products:
 p.update(PRODUCT_OVERRIDES[p['name']])
 if p.get('display_promise'):
  p['full_promise'],p['promise']=p['promise'],p['display_promise']

e = html.escape
arrow = '<span aria-hidden="true">↗</span>'
def action(label, href, style='primary'):
 return f'<a class="button {style}" href="{e(href)}">{label}{arrow}</a>'
def header(current=''):
 def link(name, href): return f'<a href="{href}"'+(' aria-current="page"' if current==name else '')+f'>{name}</a>'
 return '<a class="skip" href="#main">Skip to content</a><header class="header" data-header><a class="identity" href="index.html" aria-label="AlphaIT Engineering home"><img src="assets/brand/AlphaIT_Alpha_Aperture_Mono_Carbon.svg" alt="" width="30" height="30"><span>AlphaIT Engineering</span></a><button class="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="main-nav">Menu <span aria-hidden="true">＋</span></button><nav id="main-nav" aria-label="Main navigation">'+link('Our systems','platforms.html')+link('How we work','engagements.html')+link('Company','company.html')+link('Founder','founder.html')+'<a class="nav-contact" href="contact.html">Let’s talk '+arrow+'</a></nav></header>'

def close(title='What could work better?', text='Show us the operation, missed opportunity or new service you have in mind. We will help you find the right starting point.'):
 return f'<section class="closing"><div class="closing-kicker"><img src="assets/brand/AlphaIT_Alpha_Aperture_Reverse_Pearl.svg" width="38" height="38" alt=""><p class="eyebrow">Your next step</p></div><h2>{title}</h2><p>{text}</p><div class="actions">{action("Show us the opportunity","contact.html","light")}<a class="text-link" href="engagements.html">See how we work <span aria-hidden="true">↗</span></a></div><div class="closing-rule"></div><a class="closing-email" href="mailto:projects@alphaitengineering.com">projects@alphaitengineering.com {arrow}</a></section>'
def footer():
 return '<footer><div class="footer-top"><a class="footer-brand" href="index.html">AlphaIT Engineering</a><p>Product Engineering.<br>Without Limits.</p><div><a href="AlphaIT-Company-and-Product-Profile.pdf" target="_blank" rel="noopener">Company &amp; product profile ↗</a><a href="founder.html">Founder ↗</a><a href="https://wa.me/254792989676" target="_blank" rel="noopener">WhatsApp ↗</a><a href="contact.html">Start a conversation ↗</a></div></div><div class="addresses"><div><h3><a href="uae.html">United Arab Emirates ↗</a></h3><p>Alpha Innovation Technologies - F.Z.C<br>B.C. 1301279, Ajman Free Zone C1 Building<br>Ajman Free Zone, Ajman<br>United Arab Emirates</p></div><div><h3><a href="kenya.html">Kenya ↗</a></h3><p>Neptune, Mararo Road<br>Lavington, Nairobi<br>Kenya</p></div><div><h3><a href="nigeria.html">Nigeria ↗</a></h3><p>Polaris Bank Building<br>30 Marina Street, CMS Bus Stop<br>Lagos Island, Nigeria</p></div></div><div class="footer-bottom"><span>© 2026 AlphaIT Engineering</span><a href="mailto:projects@alphaitengineering.com">projects@alphaitengineering.com</a><a href="privacy.html">Privacy notice</a><a href="terms.html">Terms of use</a><a href="https://alphaitengineering.com">alphaitengineering.com ↗</a></div></footer>'

SITE='https://alphaitengineering.com/'
SHARE=SITE+'assets/brand/AlphaIT_Aether_Mineral_OpenGraph.png'
# Google Analytics 4, property alphaitengineering.com under alphaitengineering@gmail.com.
# The privacy page describes exactly what this collects; change one and change the other.
GA_ID='G-E42PBM7MCL'
ANALYTICS=f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag("js",new Date());gtag("config","{GA_ID}");</script>'

# Search and assistant titles are written toward the phrase a buyer actually types.
# The page heading stays the brand sentence; the title tag does the ranking work.
# Each title carries the search phrase first, the product or company name last.
SEO = {
 'index.html':('AlphaIT Engineering | Product Engineering in Kenya and Nigeria','Product engineering company serving Kenya, Nigeria and the UAE. We deploy ready systems, connect your existing tools and engineer the capability you are missing.'),
 'platforms.html':('Enterprise Software Systems and Platforms | AlphaIT','Twelve engineered systems for feedback, operations, platform security, credit decisioning, logistics and training. License, deploy, integrate or extend each one.'),
 'company.html':('About AlphaIT Engineering | Nairobi, Lagos and Ajman','AlphaIT Engineering builds and deploys the systems businesses, institutions and governments run on. Registered in the UAE and Nigeria, operating across Kenya.'),
 'engagements.html':('How We Work: Deploy, Connect, Engineer | AlphaIT','Three delivery routes: deploy a ready AlphaIT system, connect the tools you already run, or engineer the missing capability. Measures agreed before work starts.'),
 'contact.html':('Contact AlphaIT Engineering | Kenya, Nigeria, UAE','Tell us the service, revenue opportunity or operation you want to improve. Enquiries answered from Nairobi, Lagos and Ajman. Email, WhatsApp or the form below.'),
 'founder.html':('Alpha Lucky Chukwunwike Okechukwu | Founder, AlphaIT','Infrastructure and enterprise architect. Founder of AlphaIT Engineering, LisBon Platforms and LisBonFARM, sponsor of a 1,200 TPD cassava processing facility.'),
 'kenya.html':('Software and Product Engineering Company in Kenya | AlphaIT','AlphaIT Engineering builds and deploys business systems for organisations in Kenya and East Africa, from Nairobi. Feedback platforms, credit infrastructure, logistics and custom builds.'),
 'nigeria.html':('Software and Product Engineering Company in Nigeria | AlphaIT','AlphaIT Engineering builds and deploys business systems for lenders, institutions and operators in Nigeria and West Africa, from Lagos. Credit decisioning, feedback, logistics, custom builds.'),
 'uae.html':('Software and Product Engineering Company in the UAE | AlphaIT','AlphaIT Engineering builds and deploys business systems for organisations in Dubai, Abu Dhabi and the wider Gulf. Licensed in Ajman Free Zone. Platform assurance, credit infrastructure, custom builds.'),
 'privacy.html':('Privacy Notice | AlphaIT Engineering','What AlphaIT Engineering collects through this website, why, who it is shared with and the rights you have over it. Contact projects@alphaitengineering.com.'),
 'terms.html':('Website Terms of Use | AlphaIT Engineering','The terms on which AlphaIT Engineering makes this website available, what the content means and does not mean, and the limits of what is published here.'),
 'proof.html':('Systems Built by AlphaIT Engineering','Every system AlphaIT Engineering has engineered, with what each one carries and who it is built for.'),
 '404.html':('Page Not Found | AlphaIT Engineering','That page is not here. Explore the systems AlphaIT Engineering has built, or tell us what you need.'),
 'verdika.html':('Customer and Citizen Feedback Platform Kenya | Verdika','Verdika turns ratings, reviews and feedback into a clear view of what people experience, who owns each recurring problem and whether the response changed anything.'),
 'varren.html':('Governed AI Operations Platform | Varren by AlphaIT','Varren turns organisational intent into planned, authorised, executed and verified work. Research, content, outreach, build and operations under one approval trail.'),
 'varren-aegis.html':('Platform Security and Assurance Testing | Varren Aegis','Varren Aegis watches, attacks and witnesses your live platform, then holds every finding open until the check that found it passes again. Security, billing and journeys.'),
 'varren-herald.html':('Customer Win-Back and Re-engagement | Varren Herald','Varren Herald finds customers who stopped partway, waits for a true reason to contact them, checks every permission and proves the return against a held-back group.'),
 'lisbon-signal.html':('Bank Statement Analysis Infrastructure | LisBon LSI','LSI validates and structures financial records before they reach a lending decision. Source integrity, transaction identification and governed signals with confidence.'),
 'lisbon-trust.html':('Credit Decisioning Infrastructure for Lenders | LisBon LTI','LTI governs trust, eligibility, authorisation, exposure and credit obligations for banks, lenders and fintechs, and keeps every decision explainable and replayable.'),
 'liscredit.html':('Credit Marketplace Software for Lenders | LisCredit','LisCredit brings qualified borrowers and participating capital providers into one governed marketplace. Deploy it, embed it in your platform, or join as a provider.'),
 'trust-app.html':('Financial Profile and Credit Access App | Trust App','Trust App lets people submit or connect financial evidence, see their Trust Profile and carry that context into a credit application. The consumer side of LisBon.'),
 'lisbon-flow.html':('Transport and Logistics Operations Software | LisBon Flow','LFI coordinates route-based work across operators, jobs, assets and locations, giving transport, logistics and field-service businesses one authoritative view.'),
 'flow-app.html':('Driver and Dispatch App for Logistics | Flow App','Flow App gives managers, dispatchers, drivers and field operators the view of the work that belongs to their role, against one shared operating state.'),
 'pollenair.html':('Skills Training and Capability Tracking | Pollenair','Pollenair turns learning activity, practical work and demonstrated progress into a record of what a person can actually do, for employers, sponsors and institutions.'),
 'business-systems-engineering.html':('Custom Software Engineering in Kenya and Nigeria | AlphaIT','When no existing system fits, AlphaIT maps the real operation, finds the missing capability and engineers it around acceptance checks you agree before the build.'),
}

ORG_ID=SITE+'#organization'
FOUNDER_ID=SITE+'founder.html#person'

def org_schema():
 return {'@type':'Organization','@id':ORG_ID,'name':'AlphaIT Engineering','legalName':'Alpha Innovation Technologies - F.Z.C','alternateName':['AlphaIT','Alpha Innovation Technologies'],'url':SITE,'logo':SITE+'assets/brand/AlphaIT_Alpha_Aperture_Mono_Carbon.svg','image':SHARE,'email':'projects@alphaitengineering.com','telephone':'+254792989676','foundingDate':'2024-01-31','slogan':'Product Engineering. Without Limits.','description':'AlphaIT Engineering builds, deploys and licenses the systems businesses, institutions and governments run on, across experience, operations, platform assurance, financial trust, movement and capability.','founder':{'@id':FOUNDER_ID},'identifier':[{'@type':'PropertyValue','name':'Ajman Free Zone licence and registration number','value':'33549'},{'@type':'PropertyValue','name':'CAC registration number (Nigeria)','value':'7450573'}],'address':[{'@type':'PostalAddress','streetAddress':'B.C. 1301279, Ajman Free Zone C1 Building, Ajman Free Zone','addressLocality':'Ajman','addressCountry':'AE'},{'@type':'PostalAddress','streetAddress':'Neptune, Mararo Road, Lavington','addressLocality':'Nairobi','addressCountry':'KE'},{'@type':'PostalAddress','streetAddress':'Polaris Bank Building, 30 Marina Street, CMS Bus Stop, Lagos Island','addressLocality':'Lagos','addressCountry':'NG'}],'areaServed':[{'@type':'Country','name':'Kenya'},{'@type':'Country','name':'Nigeria'},{'@type':'Country','name':'United Arab Emirates'},{'@type':'Country','name':'Saudi Arabia'}],'knowsAbout':['Product engineering','Enterprise architecture','Credit decisioning infrastructure','Platform security assurance','Customer experience intelligence','Logistics operations software','Identity verification'],'sameAs':['https://www.instagram.com/alphaitengineering/','https://www.youtube.com/@alphaitengineering','https://www.tiktok.com/@alphaitengineering','https://www.linkedin.com/company/alphait-engineering/','https://x.com/AlphaITEng'],'contactPoint':{'@type':'ContactPoint','contactType':'sales','email':'projects@alphaitengineering.com','telephone':'+254792989676','availableLanguage':['en'],'areaServed':['KE','NG','AE','SA']}}

def website_schema():
 return {'@type':'WebSite','@id':SITE+'#website','url':SITE,'name':'AlphaIT Engineering','inLanguage':'en','publisher':{'@id':ORG_ID}}

def webpage_schema(file,title,description,canonical):
 return {'@type':'WebPage','@id':canonical+'#webpage','url':canonical,'name':title,'description':description,'inLanguage':'en','isPartOf':{'@id':SITE+'#website'},'about':{'@id':ORG_ID}}

def breadcrumbs(items):
 return {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i,'name':n,'item':SITE+(u if not u.endswith('.html') else route(u))} for i,(n,u) in enumerate(items,1)]}

def faq_schema(pairs):
 return {'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in pairs]}

def software_schema(p):
 return {'@type':'SoftwareApplication','@id':SITE+p['slug']+'#software','name':p['name'],'applicationCategory':'BusinessApplication','applicationSubCategory':p['index'],'operatingSystem':'Web','url':SITE+p['slug'],'description':p['description'],'audience':{'@type':'Audience','audienceType':p['buyer']},'publisher':{'@id':ORG_ID},'author':{'@id':ORG_ID},'offers':{'@type':'Offer','availability':'https://schema.org/InStock','priceSpecification':{'@type':'PriceSpecification','description':'Licensing, deployment and support are quoted per organisation.'}}}

# Cloudflare Pages serves `foo.html` at `/foo` and permanently redirects `/foo.html`
# to it. There is no way to switch that off, so the site speaks in the URLs the host
# actually serves: canonical tags, Open Graph, the sitemap, llms.txt and every internal
# link drop the extension. The files on disk keep their `.html` names because that is
# what Pages reads. Leaving the extension in would have put a redirect on every click
# and pointed every canonical at a URL that redirects somewhere else.
def route(file):
 return '' if file=='index.html' else file[:-5]

INTERNAL_LINK=re.compile(r'href="(?!https?:|mailto:|#)([A-Za-z0-9._-]+)\.html(#[^"]*)?"')
def clean_links(text):
 def swap(m):
  name,frag=m.group(1),m.group(2) or ''
  return f'href="{"index.html" if False else ("/" if name=="index" else name)}{frag}"'
 return INTERNAL_LINK.sub(swap,text)

def page(file,title=None,description=None,body='',current='',schema=None):
 canonical=SITE+route(file)
 seo=SEO.get(file)
 title=seo[0] if seo else title
 description=seo[1] if seo else description
 graph=[org_schema(),website_schema(),webpage_schema(file,title,description,canonical)]+(schema or [])
 ld=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False,separators=(',',':'))
 text=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(description)}"><meta name="theme-color" content="#f7f3ec"><meta name="google-site-verification" content="-JqnNTZhqYh5QK5QHDFkJa1HnYm9St2_NLLwIKCQtO8"><meta name="msvalidate.01" content="88FC7D77598749E72F6C4ECA833929ED"><meta property="og:type" content="website"><meta property="og:site_name" content="AlphaIT Engineering"><meta property="og:locale" content="en"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{SHARE}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="AlphaIT Engineering"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(description)}"><meta name="twitter:image" content="{SHARE}"><meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1"><link rel="canonical" href="{canonical}"><link rel="icon" href="assets/brand/AlphaIT_Favicon.svg"><link rel="preload" href="assets/fonts/InstrumentSans-Medium.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="assets/css/experience.css"><script src="assets/js/experience.js" defer></script>{ANALYTICS}<script type="application/ld+json">{ld}</script></head><body>{header(current)}<main id="main">{body}</main>{footer()}</body></html>'''
 (OUT/file).write_text(clean_links(text),encoding='utf-8')

def product_card(p):
 return f'<a class="product-card" href="{p["slug"]}.html" style="--product:#{p["accent"]}"><div class="product-top"><img src="assets/products/{p["icon"]}" alt="" width="56" height="56" loading="lazy"><span class="card-arrow" aria-hidden="true">↗</span></div><p class="product-name">{e(p["name"])}</p><h3>{e(p["promise"])}</h3><span class="product-category">{e(p["index"])}</span></a>'

def proofwall():
 return '<div class="proof-wall">'+''.join(f'<a href="{p["slug"]}.html"><img src="assets/products/{p["icon"]}" alt="" width="42" height="42" loading="lazy"><span>{e(p["name"])}</span></a>' for p in products)+'</div>'

def steps():
 return '<div class="delivery-steps">'+''.join(f'<article><span class="step-number">0{i}</span><h3>{t}</h3><p>{d}</p></article>' for i,t,d in [(1,'Define the opportunity.','Agree what should improve or launch, who it serves and what evidence will show that it works.'),(2,'Use the strongest starting point.','Deploy an AlphaIT system where it fits, connect what already exists or engineer the missing capability.'),(3,'Put the system to work.','Confirm authority, data, integrations, responsibilities and acceptance checks. Test with the people who will use it.'),(4,'Measure and improve.','Track the agreed outcome, learn from real operation and strengthen the system as the work changes.')])+'</div>'

hero='''<section class="hero" data-hero><picture><source media="(max-width:700px)" srcset="assets/brand/hero-mobile.webp"><img class="hero-image" src="assets/brand/hero.webp" alt="" fetchpriority="high" width="1672" height="941"></picture><div class="hero-wash"></div><div class="hero-copy"><p class="eyebrow">Product Engineering. Without Limits.</p><h1><span>Improve operations.</span><span><em>Launch new services.</em></span></h1><p class="lede">AlphaIT Engineering deploys and builds the systems businesses, institutions and governments use to create revenue opportunities, improve services and strengthen critical operations.</p><div class="actions">'''+action('Show us the opportunity','contact.html')+'''<a class="text-link" href="#systems">Explore the systems <span aria-hidden="true">↓</span></a></div></div><div class="hero-bottom"><span>For businesses, institutions<br>and governments.</span><span class="hero-note">Deploy. Connect.<br>Engineer what is missing.</span></div></section>'''

outcomes='''<section class="section outcomes"><div class="section-head"><div><p class="eyebrow">What AlphaIT makes possible</p><h2>More value.<br>Stronger operations.</h2></div><p>We work where technology can open a valuable opportunity, improve an important service or remove an operating constraint.</p></div><div class="outcome-grid">'''+''.join(f'<article><span class="small-number">0{i}</span><h3>{t}</h3><p>{d}</p><span class="outcome-tag">{tag}</span></article>' for i,t,d,tag in [(1,'Create new revenue opportunities.','Launch an offering, recover qualified demand or give more people a clear route to buy, apply or participate.','Revenue & demand'),(2,'Reduce cost and delay.','Connect information and work so teams spend less time repeating, chasing and correcting it.','Cost & efficiency'),(3,'Improve services and decisions.','Put evidence, responsibility and the next action into one operating view.','Service & control'),(4,'Launch something new.','Use a built system or focused engineering to turn an opportunity into a service people can use.','New services & growth')])+'''</div><div class="outcome-method"><div><span>The AlphaIT route</span><strong>Deploy. Connect. Engineer.</strong></div><p>Start with a system already engineered. Connect it to your existing tools and data. Build only what is missing.</p><a class="text-link" href="engagements.html">See how we work ↗</a></div></section>'''

mapsection='''<section class="section route-section" id="in-action" data-route-section><div class="section-head"><div><p class="eyebrow">See AlphaIT at work</p><h2>From intent<br>to outcome.</h2></div><p>Choose the result. Watch the right AlphaIT system carry the work forward.</p></div><div class="route-tabs" role="tablist" aria-label="Outcome examples"><button role="tab" aria-selected="true" aria-controls="route-panel" id="route-tab-0" data-route="0">Create new value</button><button role="tab" aria-selected="false" aria-controls="route-panel" id="route-tab-1" tabindex="-1" data-route="1">Improve a service</button><button role="tab" aria-selected="false" aria-controls="route-panel" id="route-tab-2" tabindex="-1" data-route="2">Make a trusted decision</button></div><div class="route-stage spatial-stage" role="tabpanel" id="route-panel" aria-labelledby="route-tab-0" tabindex="0"><div class="operating-field" aria-hidden="true"><div class="field-grid"></div><div class="field-ring ring-one"></div><div class="field-ring ring-two"></div><div class="field-beam beam-one"></div><div class="field-beam beam-two"></div><div class="field-node field-opportunity"><span>Intent</span><strong data-field-label="0">Create new revenue</strong></div><div class="field-core"><div class="core-halo"></div><img data-route-icon src="assets/products/varren-mark.png" width="60" height="60" alt=""><span data-field-product>Varren</span></div><div class="field-node field-outcome"><span>Outcome</span><strong data-field-label="2">Qualified opportunities</strong></div><div class="evidence-chip">Evidence ready</div></div><div class="route-story" aria-live="polite"><div><span data-route-story-label>Varren in action</span><p data-route-summary>Varren finds the strongest commercial route, carries out approved work and improves the next move from real results.</p></div><a data-route-link class="route-story-link" href="varren.html">Explore Varren <span aria-hidden="true">↗</span></a></div></div><div class="route-caption"><span>Illustrative system journeys. Scope, integrations and measures are agreed for each organisation.</span><button type="button" class="route-pause" data-route-pause aria-pressed="false">Pause automatic preview</button></div></section>'''

home=hero+outcomes+mapsection+'''<section class="section systems" id="systems"><div class="section-head"><div><p class="eyebrow">Built by AlphaIT Engineering</p><h2>Systems we have<br>already engineered.</h2></div><div><p>License, deploy, integrate, configure or extend the system that already carries the hardest part of the work.</p><a class="text-link" href="platforms.html">Meet every system ↗</a></div></div>'''+proofwall()+'''<div class="featured-system"><div><p class="eyebrow">Built systems. Focused engineering.</p><h3>Start with a working system.<br>Build only what is missing.</h3></div><p>If an AlphaIT system already fits the core need, we deploy it and connect it to your existing tools and data. If something is still missing, we engineer that part.</p><a class="circle-link" aria-label="Explore all AlphaIT systems" href="platforms.html">↗</a></div></section><section class="section approach" id="approach"><div class="section-head"><div><p class="eyebrow">How we work</p><h2>Outcome first.<br>The right system next.</h2></div><p>We agree what should improve or launch and how the change will be measured. Then we choose the strongest route to a working result.</p></div>'''+steps()+'</section>'+close('What do you want<br>to make possible?','Show us the service, opportunity or operation. We will identify the strongest starting point and the evidence required to move forward.')

def capability_grid(items):
 return '<div class="capability-grid">'+''.join(f'<article><h3>{e(title)}</h3><p>{e(text)}</p></article>' for title,text in items)+'</div>'

# The questions are the ones buyers and assistants actually ask, and every answer is
# derived from the approved product fields above rather than written a second time.
# A hand-kept second copy drifts the first time somebody edits the product brief.
def product_faq(p):
 return [
  (f"What is {p['name']}?",p['description']),
  (f"Who is {p['name']} for?",p['buyer']),
  (f"What problem does {p['name']} solve?",p['situation']),
  (f"How does {p['name']} work?",p['system']),
  (f"What changes once {p['name']} is running?",p['visible']),
  (f"How is success measured?",p['measure']),
  (f"Can {p['name']} be deployed for a single organisation?",'Yes. AlphaIT licenses, deploys, configures and integrates the system for each organisation, and engineers the missing connection or capability where the ready system does not fully fit. Scope, integrations, data permissions, acceptance checks, support and commercial terms are agreed per deployment.'),
  (f"Which countries can {p['name']} be deployed in?",'AlphaIT Engineering works with organisations in Kenya, Nigeria, the United Arab Emirates and the wider Middle East. Deployment is subject to applicable law, the data permissions available and the authority of each participating organisation.'),
 ]

def faq_section(pairs,heading='Questions buyers ask.'):
 return f'<section class="section depth-section" id="faq"><div class="section-head"><div><p class="eyebrow">Frequently asked</p><h2>{heading}</h2></div><p>If your question is not here, ask it directly and we will answer it against what the system does today.</p></div>'+capability_grid(pairs)+'</section>'

def product_depth(p):
 name=p['name']
 if name=='Varren':
  items=[('Grow','Understand the market, sharpen the offer, identify opportunities and improve what produces measurable growth.'),('Distribute','Coordinate authorised publishing across connected channels, accounts, audiences and markets.'),('Create','Produce content, campaigns, images, video, documents, presentations and brand-governed materials.'),('Communicate','Bring authorised email, social, messaging and support work together while preserving the full history.'),('Reach','Find and qualify customers, investors, partners, talent and suppliers, then progress approved outreach.'),('Understand','Research markets, customers, competitors, operations and risk, then turn findings into executable next actions.'),('Build','Help teams plan, engineer, test, review, deploy and maintain software through governed coding agents.'),('Operate','Coordinate recurring work, connected systems, approvals, costs, handoffs and measurable results.')]
  return '''<section class="section depth-section"><div class="section-head"><div><p class="eyebrow">One governed operator</p><h2>Across the organisation.</h2></div><p>People describe the outcome. Varren brings the right capability into the work without asking them to coordinate disconnected assistants.</p></div>'''+capability_grid(items)+'''</section><section class="section operating-loop"><div><p class="eyebrow">Built to improve with control</p><h2>Evidence becomes<br>a better next move.</h2></div><div class="loop-line"><span>Intent</span><span>Plan</span><span>Work</span><span>Approval</span><span>Result</span><span>Evidence</span><span>Learn</span><span>Recommend</span><span>Next action</span></div><p>Varren can learn from verified results, actual costs, corrections, responses and approved market signals. It recommends what to improve, focus on, create, sell or pursue next. Consequential action still waits for the required human authority.</p><p class="boundary-note">Improvements are evaluated, measurable and reversible. Customer information remains isolated and governed.</p></section>'''
 if name=='Verdika':
  items=[('Experience','People contribute a structured rating, review, feedback, vote or request for change.'),('Pattern','Verdika reveals recurring strengths, problems and themes across services, locations or periods.'),('Responsibility','The relevant finding reaches the team, department or stakeholder responsible for the service.'),('Response','The organisation records its response, next action and supporting information.'),('Follow-up','Later experience shows whether people actually felt a difference after the response.')]
  return '''<section class="section depth-section"><div class="section-head"><div><p class="eyebrow">The complete record</p><h2>From experience<br>to visible improvement.</h2></div><p>Verdika keeps what people reported, what the organisation says it did and what people experienced afterwards as distinct, inspectable records.</p></div>'''+capability_grid(items)+'''</section><section class="section proof-band"><div><p class="eyebrow">Participation you can defend</p><h2>One contribution.<br>One eligible participant.</h2></div><div><p>Verdika can bind a contribution to an eligible, verified participant and preserve the basis on which that person participated. This makes duplicate, synthetic and impersonated participation materially harder.</p><p>Identity, participant opinion, documented evidence and institutional response remain separate. Verification does not turn a voluntary contribution into representative research.</p><p class="boundary-note">Verdika's first public application is live in Kenya for rating public leaders, institutions and services. It is one application of the wider platform.</p></div></section>'''
 if name=='Varren Aegis':
  items=[('Sentinel · Watch','Tests production and staging on the agreed schedule and detects what is broken or drifting.'),('Crucible · Attack','Applies deliberate adversarial pressure across access, data, scale, integrations, logic and commercial rules.'),('Witness · See','Captures what real users encounter, including errors, dead ends and failed journeys.'),('Warden · Close','Keeps every finding open until the originating check runs again and comes back clean.')]
  return '''<section class="section depth-section"><div class="section-head"><div><p class="eyebrow">Watch. Attack. Witness. Close.</p><h2>Most tools only watch.<br>Aegis does all four.</h2></div><p>Every finding becomes precise work: where it is, why it happens, what it can cost, who can fix it and the check that will prove closure.</p></div>'''+capability_grid(items)+'''</section><section class="section proof-band"><div><p class="eyebrow">The Inspector Panel</p><h2>Test the platform.<br>Test the business.</h2></div><div><p>The Adversary tests security. The Auditor tests billing and commercial health. The Engineer tests the codebase. The Operator tests business logic. The Newcomer tests first use. The Customer tests the complete journey.</p><p class="boundary-note">Aegis never changes a client system without explicit authorisation. Authorised repair is enabled per deployment, followed by the same repeat check before closure.</p></div></section>'''
 if name=='Varren Herald':
  items=[('Find the stalled step','See where a person stopped in the purchase, application, enrolment or service journey.'),('Wait for something true','Contact begins only when a real event gives the person a relevant reason to return.'),('Check every permission','Lawful basis, consent, approved wording, withdrawal and contact limits are enforced before sending.'),('Prove the return','An eligible group is left alone so the organisation can compare what happened with and without contact.')]
  return '''<section class="section depth-section"><div class="section-head"><div><p class="eyebrow">Real reasons. Approved words. Proven return.</p><h2>Re-engagement<br>without guesswork.</h2></div><p>Herald measures the organisational goal and movement past the stalled step. It records every send, every refusal and every deliberate silence.</p></div>'''+capability_grid(items)+'''</section><section class="section proof-band"><div><p class="eyebrow">Before any campaign</p><h2>Know who you may<br>reach and why.</h2></div><div><p>Herald first shows how many stalled people can lawfully be contacted and exactly why the rest cannot. Approved wording is sealed so the customer sees precisely what compliance and brand teams authorised.</p><p class="boundary-note">Herald reads through an agreed guarded path and never alters the client's customer data.</p></div></section>'''
 if name=='LisCredit Marketplace':
  items=[('Launch a marketplace','Deploy LisCredit for an operator or institution, with its own products, rules, participants and operating model.'),('Embed LisCredit','Place the qualified-demand-to-capital journey inside an existing platform through approved integrations.'),('Join as a provider','Connect products and authorised workflows so relevant qualified opportunities can progress under the provider’s own rules.')]
  return '''<section class="section depth-section"><div class="section-head"><div><p class="eyebrow">Both sides of the market</p><h2>Qualified demand.<br>Participating capital.</h2></div><p>LisCredit creates the marketplace relationship after trust and eligibility. It does not manufacture trust and it does not take over the capital provider's decision or risk.</p></div>'''+capability_grid(items)+'''</section><section class="section proof-band"><div><p class="eyebrow">Commercial routes</p><h2>Deploy. Embed.<br>Participate.</h2></div><div><p>AlphaIT can provide marketplace deployment, integration, annual platform licensing, support, usage-based infrastructure and institution-specific extensions.</p><p>Provider onboarding, distribution arrangements and transaction or success fees are used only where the applicable market, contract and regulatory position allow them.</p><p class="boundary-note">LSI establishes governed evidence. LTI governs trust and eligibility. LisCredit operates where qualified demand meets capital.</p></div></section>'''
 return ''

catalog='''<section class="page-intro"><p class="eyebrow">Systems engineered by AlphaIT</p><h1>Start with what<br>already <em>works.</em></h1><p class="lede">Each system carries a difficult part of the work already. License it, deploy it, integrate it, configure it or extend it around your organisation.</p></section><section class="section catalog-section"><div class="catalog-label"><span>AlphaIT product portfolio</span><span>12 systems and engineering routes</span></div><div class="product-grid">'''+''.join(product_card(p) for p in products)+'''</div><p class="portfolio-note">These are AlphaIT-built systems, not customer logos. Deployment scope, integrations, data permissions, timing and commercial terms are agreed for each organisation.</p></section>'''+close('Which outcome matters<br>to you now?','Tell us what you need to improve or launch. We will identify the relevant system and the smallest credible next step.')
HOME_FAQ=[
 ('What does AlphaIT Engineering do?','AlphaIT Engineering builds, deploys and licenses the systems businesses, institutions and governments run on. Where an AlphaIT system already fits the core need, we deploy it and connect it to existing tools and data. Where something is missing, we engineer that part.'),
 ('Where is AlphaIT Engineering based?','AlphaIT Engineering operates from Ajman Free Zone in the United Arab Emirates, Nairobi in Kenya and Lagos in Nigeria. The contracting entity is Alpha Innovation Technologies - F.Z.C, licence 33549, with Alpha Innovation Technologies Ltd registered in Nigeria under CAC number 7450573.'),
 ('Who founded AlphaIT Engineering?','AlphaIT Engineering was founded by Alpha Lucky Chukwunwike Okechukwu, an infrastructure and enterprise architect who also founded LisBon Platforms and LisBonFARM.'),
 ('What systems has AlphaIT built?','Verdika for experience and accountability, Varren for governed organisational execution with Aegis and Herald, the LisBon financial infrastructure of LSI, LTI, LisCredit and Trust App, LisBon Flow Infrastructure and Flow App for movement, and Pollenair for practical capability.'),
 ('Which industries does AlphaIT serve?','Financial services and lending, hospitality and distribution, transport and logistics, healthcare, property management, education and training, and public institutions.'),
 ('How does an engagement start?','Describe the service, revenue opportunity or operation you want to improve. AlphaIT identifies the strongest starting point, the evidence required and the measures that will show the change, before any build is agreed.'),
]
page('index.html',body=home+faq_section(HOME_FAQ,'What people ask<br>about AlphaIT.'),schema=[faq_schema(HOME_FAQ)])
page('platforms.html',body=catalog,current='Our systems',schema=[breadcrumbs([('Home',''),('Our systems','platforms.html')]),{'@type':'ItemList','name':'Systems engineered by AlphaIT Engineering','itemListElement':[{'@type':'ListItem','position':i,'name':p['name'],'url':SITE+p['slug']} for i,p in enumerate(products,1)]}])

for p in products:
 body=f'''<section class="product-hero" style="--product:#{p['accent']}"><a class="back-link" href="platforms.html">← All systems</a><div class="product-identity"><img src="assets/products/{p['icon']}" width="78" height="78" alt=""><p>{e(p['name'])}</p></div><div class="product-hero-grid"><div><h1>{e(p['promise'])}</h1><div class="actions">{action('Discuss '+('your build' if p['icon_key']=='alphait' else 'a deployment'),'contact.html?product='+p['slug'])}<a class="text-link" href="#system-in-action">See how it works ↓</a></div></div><div class="product-summary"><p>{e(p['description'])}</p><div class="for-label">Who it is for</div><p>{e(p['buyer'])}</p></div></div></section><section class="section product-workflow" id="system-in-action"><p class="eyebrow">The system in action</p><h2>See the work<br>change state.</h2><div class="workflow-columns">'''+''.join(f'<article><span class="step-number">0{i}</span><h3>{title}</h3><p>{e(p[key])}</p></article>' for i,title,key in [(1,'The situation','situation'),(2,'The system at work','system'),(3,'The outcome','visible')])+f'''</div><div class="measure-panel"><p class="eyebrow">Agree what success looks like</p><h3>Make the improvement visible.</h3><p>{e(p['measure'])}</p><span>Measures are agreed for each deployment. They are not guaranteed results.</span></div></section>'''+product_depth(p)+'''<section class="section product-next"><div><p class="eyebrow">From fit to deployment</p><h2>Your work.<br>Your requirements.</h2></div><div><p>We confirm the people, data, connections, authority and operating conditions required. Then we agree scope, delivery stages, acceptance checks and support.</p><p>Where the ready system does not fully fit, AlphaIT can engineer the missing connection or capability.</p>'''+('<p>Credit providers retain their decisions and capital risk. Deployment is subject to applicable law, agreed policy and the authority of each participating institution.</p>' if p['icon_key'] in ['lsi','lisbon','liscredit'] else '')+f'''</div></section>'''+close('Put '+('your opportunity' if p['icon_key']=='alphait' else e(p['name']))+'<br>to work.','Show us the use case. We will demonstrate the relevant operating route and agree the strongest next step.')
 # The FAQ goes above the closing call to action, which is the one place close() emits.
 faq=product_faq(p)
 assert body.count('<section class="closing">')==1
 body=body.replace('<section class="closing">',faq_section(faq)+'<section class="closing">',1)
 page(p['slug']+'.html',body=body,current='Our systems',schema=[software_schema(p),faq_schema(faq),breadcrumbs([('Home',''),('Our systems','platforms.html'),(p['name'],p['slug']+'.html')])])

company='''<section class="page-intro"><p class="eyebrow">AlphaIT Engineering</p><h1>Systems for stronger operations<br>and <em>new services.</em></h1><p class="lede">We are a product-engineering company serving businesses, institutions and governments.</p></section><section class="company-image"><img src="assets/brand/hero.webp" alt="AlphaIT architectural brand artwork: a clear route through connected structures" width="1672" height="941"><span>Product Engineering. Without Limits.</span></section><section class="section company-story"><div><p class="eyebrow">Our business model</p><h2>Built systems first.<br>Focused engineering where needed.</h2></div><div><p>AlphaIT has already engineered reusable infrastructure for difficult operating problems across experience, organisational execution, platform assurance, customer return, financial trust, capital access, movement and capability.</p><p>Where one of those systems fits, we license, deploy, configure and integrate it. Where part of the operation remains unsupported, we engineer the missing connection or capability rather than rebuilding everything from zero.</p><p>This gives clients a faster starting point and gives AlphaIT a repeatable platform business with implementation, licensing, support and continuous-improvement revenue.</p><a class="text-link" href="founder.html">Meet the founder and architect, Alpha Lucky Chukwunwike Okechukwu ↗</a></div></section><section class="section company-proof"><p class="eyebrow">Systems engineered by AlphaIT</p><h2>Start with what exists.<br>Extend what the work requires.</h2>'''+proofwall()+'''<a class="text-link" href="platforms.html">Explore every system ↗</a></section>'''+close('What should your<br>organisation do next?','Show us the opportunity, service or critical operation. We will identify the strongest system route and what must be true for it to work.')
company=company.replace('Systems for stronger operations<br>and <em>new services.</em>','Stronger operations.<br><em>New services.</em>')
page('company.html',body=company,current='Company',schema=[breadcrumbs([('Home',''),('Company','company.html')])])

approach='''<section class="page-intro"><p class="eyebrow">How we work</p><h1>Outcome first.<br>The <em>right system</em> next.</h1><p class="lede">Start from an AlphaIT system where it fits. Connect it to the operating reality. Engineer only the capability that remains missing.</p></section><section class="section">'''+steps()+'''</section><section class="section engagement-routes"><p class="eyebrow">Three delivery routes</p><h2>One outcome.<br>The strongest starting point.</h2><div class="workflow-columns"><article><span class="step-number">01</span><h3>Deploy a ready system.</h3><p>License and configure an AlphaIT-built product around the organisation's roles, policies and operation.</p><a class="text-link" href="platforms.html">Explore the systems ↗</a></article><article><span class="step-number">02</span><h3>Connect what exists.</h3><p>Integrate the right people, data and tools so the service or operation works as one route.</p><a class="text-link" href="contact.html?product=connect">Discuss your operation ↗</a></article><article><span class="step-number">03</span><h3>Engineer what is missing.</h3><p>Build the capability or new service that no existing product fully carries.</p><a class="text-link" href="business-systems-engineering.html">Explore a focused build ↗</a></article></div></section><section class="section company-story"><div><p class="eyebrow">Before work begins</p><h2>Clarity on the outcome.<br>Clarity on the commitment.</h2></div><div><p>We agree scope, responsibilities, delivery stages and acceptance checks. We confirm required integrations, authority, access, data permissions and operating requirements.</p><p>Licensing, configuration, custom engineering, hosting and support are set out clearly in the proposal.</p><p>We agree the measures before implementation so the organisation can see whether the intended change is happening.</p></div></section>'''+close('Choose the strongest<br>starting point.','Tell us the outcome you need. We will assess which system, connection or focused build can carry it.')
page('engagements.html',body=approach,current='How we work',schema=[breadcrumbs([('Home',''),('How we work','engagements.html')])])

contact_source=SOURCE/'AlphaIT Engineering Website - Aether Mineral 2026/contact.html'
old_contact=(contact_source if contact_source.exists() else OUT/'contact.html').read_text(encoding='utf-8')
key=re.search(r'name="access_key"\s+value="([^"]+)"',old_contact)
assert key, 'Existing contact-form key missing; do not replace with fake service'
contact='''<section class="page-intro contact-intro"><p class="eyebrow">Your next step</p><h1>What do you want<br>to <em>make possible?</em></h1><p class="lede">A revenue opportunity. A better service. A stronger operation. A new system. Tell us the outcome.</p></section><section class="section contact-layout"><div class="contact-details"><p class="eyebrow">Speak with AlphaIT</p><h2>You bring the outcome.<br>We find the route.</h2><p>You do not need a technical brief or product name. A clear description of what should improve or launch, who it serves and why it matters is enough to begin.</p><a class="contact-line" href="mailto:projects@alphaitengineering.com"><span aria-hidden="true">✉</span><span>projects@alphaitengineering.com</span></a><a class="contact-line" href="https://wa.me/254792989676" target="_blank" rel="noopener"><span aria-hidden="true">↗</span><span>Message us on WhatsApp</span></a><a class="text-link" href="AlphaIT-Company-and-Product-Profile.pdf" target="_blank" rel="noopener">Download the company profile ↗</a></div><form id="projectForm" action="https://api.web3forms.com/submit" method="POST"><input type="hidden" name="access_key" value="'''+e(key.group(1))+'''"><input type="hidden" name="subject" value="AlphaIT website project enquiry"><input type="checkbox" name="botcheck" class="botcheck" tabindex="-1" aria-hidden="true"><div class="form-pair"><label>Your name<input name="name" autocomplete="name" required maxlength="150"></label><label>Organisation<input name="company" autocomplete="organization" required maxlength="200"></label></div><label>Work email<input type="email" name="email" autocomplete="email" required maxlength="254"></label><label>Phone / WhatsApp <span>(optional)</span><input type="tel" name="phone" autocomplete="tel" maxlength="60"></label><label>What do you want to achieve?<select name="interest" id="interest"><option value="">Help me find the right starting point</option><option value="opportunity">Find or develop a new opportunity</option><option value="revenue">Create revenue or recover demand</option><option value="launch">Launch a new service</option><option value="service">Improve a service or operation</option><option value="cost">Reduce cost or delay</option><option value="problem">Solve a known problem</option><option value="missing">Find what we may be missing</option><option value="connect">Deploy or connect an AlphaIT system</option>'''+''.join(f'<option value="{p["slug"]}">{e(p["name"])}</option>' for p in products)+'''</select></label><label>What should improve or launch?<textarea name="message" rows="5" required maxlength="5000" placeholder="Tell us the outcome, who it serves and what is standing in the way."></textarea></label><p class="form-note">We use your details only to respond. Do not send passwords, financial records or other sensitive documents.</p><button type="submit" class="button primary">Send your enquiry <span aria-hidden="true">↗</span></button><p id="formStatus" role="status" aria-live="polite"></p></form></section>'''
contact=contact.replace('What do you want<br>to <em>make possible?</em>','What should happen<br><em>next?</em>')
contact=contact.replace('</option value="connect">','</option><option value="connect">')
page('contact.html',body=contact,schema=[breadcrumbs([('Home',''),('Contact','contact.html')]),{'@type':'ContactPage','url':SITE+'contact','about':{'@id':ORG_ID}}])
page('404.html',body='<section class="page-intro"><p class="eyebrow">404 / Page not found</p><h1>Let’s get you<br>back on track.</h1><div class="actions">'+action('Back to AlphaIT','index.html')+'<a class="text-link" href="platforms.html">Explore our systems ↗</a></div></section>')
# Preserve the old proof route as the product proof catalogue; the site's real work is its portfolio.
page('proof.html',body=catalog,current='Our systems')

# Founder page. Every statement here is carried by a record in Corporate Records, the
# live LisBonFARM project site or this site's own product pages. Nothing is decorative:
# an assistant asked "who is Alpha Lucky Okechukwu" should be able to quote any sentence.
FOUNDER_FAQ=[
 ('Who is Alpha Lucky Chukwunwike Okechukwu?','Alpha Lucky Chukwunwike Okechukwu is an infrastructure and enterprise architect. He is the founder of AlphaIT Engineering, which builds and licenses the operating systems businesses, institutions and governments run on; of LisBon Platforms, the group behind the LisBon financial trust and movement infrastructure; and of LisBonFARM, the agro-industrial platform developing a 1,200 tonne-per-day cassava processing facility in Edo State, Nigeria.'),
 ('What does Alpha Lucky Okechukwu build?','Infrastructure in three forms. Technology: the AlphaIT systems, including Varren for governed organisational execution, Varren Aegis for platform assurance, Verdika for experience and accountability, and LisBon Flow for movement. Capital: the LisBon trust stack and LisCredit, where qualified demand and participating capital meet. Production: AgroGlobal ICPI, the cassava processing facility LisBonFARM is developing.'),
 ('What companies does Alpha Lucky Okechukwu run?','AlphaIT Engineering, contracting through Alpha Innovation Technologies - F.Z.C in the United Arab Emirates, licence 33549, and Alpha Innovation Technologies Ltd in Nigeria, CAC 7450573. LisBon Platforms, the multi-sector infrastructure group. LisBonFARM, whose issuer is LISBONFARM LTD, registered in Nigeria under RC 8508608.'),
 ('What is Alpha Lucky Okechukwu known for professionally?','Building systems that survive being questioned. Each platform he has founded keeps the evidence, the rule that applied, the authority for the action and what changed afterwards as four separate inspectable records, so a decision can be explained, replayed and defended rather than merely asserted.'),
 ('Where does Alpha Lucky Okechukwu work?','Across Nigeria, Kenya and the United Arab Emirates. AlphaIT Engineering operates from Ajman Free Zone, Nairobi and Lagos.'),
 ('How can Alpha Lucky Okechukwu be contacted?','By email at alpha@lisbonplatforms.com.'),
]
founder_body='''<section class="page-intro"><p class="eyebrow">Founder and architect</p><h1>Alpha Lucky<br>Chukwunwike <em>Okechukwu.</em></h1><p class="lede">Infrastructure and enterprise architect. He builds the infrastructure economies run on: the systems that decide who can be trusted with capital, the systems that turn intent into authorised work, and the industrial capacity that turns a crop into a product.</p></section><section class="company-image" style="max-width:min(560px,100%);margin-inline:auto"><picture><source type="image/webp" srcset="assets/brand/founder-portrait.webp"><img src="assets/brand/founder-portrait.jpg" alt="Alpha Lucky Chukwunwike Okechukwu, founder of AlphaIT Engineering, LisBon Platforms and LisBonFARM" width="1100" height="1375" loading="lazy" style="height:auto;aspect-ratio:4/5;object-fit:cover"></picture></section><section class="section depth-section"><div class="section-head"><div><p class="eyebrow">Three platforms founded</p><h2>Technology. Capital.<br>Production.</h2></div><p>One architectural discipline across software infrastructure, financial infrastructure and industrial capacity. Each is a registered company with its own entity, its own capital perimeter and its own record.</p></div>'''+capability_grid([
 ('AlphaIT Engineering','The product engineering company behind twelve engineered systems. Varren turns organisational intent into planned, authorised, executed and verified work. Varren Aegis attacks a live platform before anyone else does and holds every finding open until the check that found it passes again. Verdika turns what people experience into something an institution has to answer for. Contracting through Alpha Innovation Technologies - F.Z.C, licence 33549, and Alpha Innovation Technologies Ltd, CAC 7450573.'),
 ('LisBon Platforms','The multi-sector infrastructure group holding the LisBon financial trust stack: LSI, which turns raw financial records into evidence a system can rely on; LTI, which governs trust, eligibility, exposure and credit obligations so a lending decision can be replayed years later; LisCredit, where qualified demand and participating capital meet; and the Flow infrastructure behind recurring physical operations.'),
 ('LisBonFARM','The agro-industrial platform and sponsor of AgroGlobal ICPI in Edo State, Nigeria: a 1,200 tonne-per-day cassava processing facility across three uniform lines, designed for roughly 90,000 tonnes of food-grade native starch a year, with a primary equity raise of up to twenty million United States dollars in progress. Nigeria grows more cassava than any country on earth and still imports its industrial starch. Issuer LISBONFARM LTD, RC 8508608.'),
])+'''</section><section class="section company-story"><div><p class="eyebrow">The method</p><h2>Built to be<br>examined.</h2></div><div><p>Most software is built to be used. He builds software to be examined. The systems are designed for the moment after a decision is made, when a regulator, a lender, a board or a member of the public asks why it was made that way and what happened next.</p><p>That requirement shapes the architecture. Every platform preserves four things as separate, inspectable records: the evidence, the rule that applied, the authority under which action was taken, and what changed afterwards. It is a harder way to build, and it is the only way the result survives scrutiny.</p><p>Three rules govern the engineering. Never weaken one part of a system to make another part pass. Never take the easier option when the harder one is correct. Never let a finding be owned by nobody. In practice those are build decisions: a duplicate participant is refused rather than quietly accepted, a check that cannot pass is fixed at its cause rather than switched off, and a system that returns nothing is proven to still serve the person entitled to see something.</p></div></section><section class="section proof-band"><div><p class="eyebrow">The record</p><h2>Dated, registered<br>and verifiable.</h2></div><div><p>Alpha Innovation Technologies - F.Z.C licensed in Ajman Free Zone, United Arab Emirates, first issued 31 January 2024, licence and registration number 33549.</p><p>Alpha Innovation Technologies Ltd incorporated in Nigeria on 17 April 2024, CAC registration number 7450573.</p><p>LISBONFARM LTD incorporated in Nigeria in May 2025, RC 8508608, as sponsor and developer of AgroGlobal ICPI, now in development with a primary equity raise of up to twenty million United States dollars in progress.</p><p>Verdika live in Kenya as the first public application of the experience and accountability platform. The LisBon trust stack, the Flow infrastructure and Pollenair engineered and in deployment across Nigeria and Kenya. Pollenair, which turns practical learning into a visible capability record, was co-founded with its lead engineer and is owned and engineered by AlphaIT.</p><p class="boundary-note">Project figures are design basis and development status, not delivered results. Detailed evidence is available to qualified parties under the applicable process.</p></div></section>'''+faq_section(FOUNDER_FAQ,'About<br>Alpha Lucky Okechukwu.')+close('Build something<br>that holds up.','Bring the operation, the institution or the opportunity. AlphaIT will architect the system it actually requires.')
page('founder.html',body=founder_body,current='Founder',schema=[
 {'@type':'Person','@id':FOUNDER_ID,'name':'Alpha Lucky Chukwunwike Okechukwu','alternateName':['Alpha Lucky Okechukwu','Alpha Okechukwu','Lucky Chukwunwike Okechukwu','Alpha Lucky'],'givenName':'Alpha','additionalName':'Lucky Chukwunwike','familyName':'Okechukwu','jobTitle':'Founder and Enterprise Architect','description':'Infrastructure and enterprise architect. Founder of AlphaIT Engineering, LisBon Platforms and LisBonFARM.','url':SITE+'founder','image':SITE+'assets/brand/founder-portrait.jpg','email':'alpha@lisbonplatforms.com','worksFor':{'@id':ORG_ID},'founder':[{'@id':ORG_ID}],'sameAs':['https://lisbonplatforms.com','https://lisbonfarm.com','https://www.instagram.com/alphalucky.co/','https://x.com/AlphaLuckyCO','https://www.facebook.com/AlphaLuckyChukwunwike','https://www.tiktok.com/@alphalucky.co','https://www.linkedin.com/in/alpha-lucky-chukwunwike-okechukwu'],'knowsAbout':['Enterprise architecture','Infrastructure architecture','Credit decisioning infrastructure','Identity verification','Platform security assurance','Agro-industrial infrastructure','Product engineering'],'workLocation':[{'@type':'Place','name':'Ajman Free Zone, United Arab Emirates'},{'@type':'Place','name':'Nairobi, Kenya'},{'@type':'Place','name':'Lagos, Nigeria'}]},
 faq_schema(FOUNDER_FAQ),
 breadcrumbs([('Home',''),('Founder','founder.html')]),
])

# Legal pages. These describe what the site actually does: a static site, a Web3Forms
# enquiry form and Google Analytics. If any of those three change, change this page in
# the same commit. A privacy notice that describes a site we no longer run is worse
# than none, and this company sells governed systems to buyers who will read it.
def legal_block(heading,paragraphs):
 return f'<section class="section company-story"><div><h2>{heading}</h2></div><div>'+''.join(f'<p>{t}</p>' for t in paragraphs)+'</div></section>'

privacy='''<section class="page-intro"><p class="eyebrow">Legal</p><h1>Privacy <em>notice.</em></h1><p class="lede">What this website collects, why, who it is shared with and what you can ask us to do about it. Last updated 1 October 2026.</p></section>'''+legal_block('Who is responsible.',[
 'This website is operated by AlphaIT Engineering. The contracting entity is Alpha Innovation Technologies - F.Z.C, a free zone company licensed by the Free Zones Authority of Ajman under licence and registration number 33549, at B.C. 1301279, Ajman Free Zone C1 Building, Ajman Free Zone, Ajman, United Arab Emirates. In Nigeria the group entity is Alpha Innovation Technologies Ltd, CAC registration number 7450573.',
 'For any question about this notice, or to make a request about your information, write to projects@alphaitengineering.com.'])+legal_block('What this website collects.',[
 '<strong>Enquiries you send us.</strong> If you use the contact form we receive the name, organisation, work email, optional phone number, the interest you select and the message you write. The form is delivered to us by Web3Forms, which processes the submission in order to send it to our inbox.',
 '<strong>Usage of the site.</strong> We use Google Analytics 4 to understand which pages are read and how people arrive. It sets cookies in your browser and records information such as pages viewed, approximate location derived from your IP address, device type and the site or search that referred you. We do not use it to identify you by name.',
 '<strong>Standard server records.</strong> Our hosting provider keeps ordinary technical logs of requests made to the site.',
 'We do not sell your information, we do not use it for advertising, and we do not combine it with information from other sources to profile you.'])+legal_block('Why we use it.',[
 'Enquiry details are used to answer you, to understand what you need and, where a relationship follows, to carry out the work. Our basis for this is your request and our legitimate interest in responding to it.',
 'Usage information is used to improve the website and to see which material is useful. Our basis for this is our legitimate interest in running the site well.'])+legal_block('Who else sees it.',[
 'Web3Forms, which delivers the contact form. Google, which provides the analytics. Our hosting provider, which serves the pages. Each of these processes information on our instructions or for the limited purpose described above. We do not share enquiry details with anyone else unless you ask us to, or unless we are required to by law.'])+legal_block('How long we keep it.',[
 'Enquiries are kept while the conversation or the relationship is live, and afterwards only for as long as we need them for the business and legal record. Analytics information is kept for the retention period configured in our Google Analytics property. Ask us and we will tell you what is currently held about you.'])+legal_block('Your rights.',[
 'Where the Kenya Data Protection Act, the Nigeria Data Protection Act, United Arab Emirates federal data protection law or another applicable law gives you rights over your information, you may ask us for a copy of what we hold, ask us to correct it, ask us to delete it, object to our use of it or ask us to restrict that use. Write to projects@alphaitengineering.com and we will respond.',
 'You can refuse analytics cookies through your browser settings, and you can use the email address or WhatsApp number on the contact page instead of the form.'])+legal_block('Information belonging to our clients.',[
 'This notice covers this website only. Where AlphaIT deploys or operates a system for a client, that client decides what is collected and why, and AlphaIT handles that information under the agreement with them. If you are a user of a system built by AlphaIT, the organisation operating it is the one to contact.'])+close('Ask us anything<br>about this.','If something here is unclear, or you want to know what we hold, write to us and we will answer plainly.')

terms='''<section class="page-intro"><p class="eyebrow">Legal</p><h1>Website <em>terms of use.</em></h1><p class="lede">The terms on which this website is made available. Last updated 1 October 2026.</p></section>'''+legal_block('What this website is.',[
 'This website is published by AlphaIT Engineering, the trading name of Alpha Innovation Technologies - F.Z.C, licence and registration number 33549, Ajman Free Zone, United Arab Emirates.',
 'It describes systems AlphaIT has engineered and the ways they can be deployed. It is published for information. It is not an offer, a quotation, a proposal or a commitment to deliver any particular capability, timescale or result.'])+legal_block('What the product statements mean.',[
 'Each product page describes what the system is built to do. Deployment scope, integrations, data permissions, authority, timing and commercial terms are agreed separately for each organisation.',
 'Where a page describes a measure, that is what a deployment can be set up to make visible. It is not a promise of a result. Measures are agreed with each client before implementation.'])+legal_block('Using the site.',[
 'You may read, quote and link to this site. You may not copy its design, text or brand assets to present them as your own, or use them in a way that suggests a relationship with AlphaIT that does not exist.',
 'The AlphaIT name, the product names and the brand assets on this site belong to AlphaIT Engineering or to the group entity that owns the relevant product.'])+legal_block('Links and availability.',[
 'This site links to other sites, including those operated by LisBon Platforms and other group companies. We are not responsible for material published on sites we do not control.',
 'We try to keep the site accurate and available, but we do not guarantee that it is free of error or that it will always be reachable.'])+legal_block('Law.',[
 'These terms, and anything arising from them, are governed by the law of the United Arab Emirates, without affecting any right you have under the law of the country you live in.'])+close('Talk to us about<br>the real thing.','The website is the summary. The agreement, the scope and the acceptance checks are set out in writing for each engagement.')

# Country pages. A single site cannot rank in three markets on one homepage, because
# Google ranks local intent by proximity and by what the page itself says about where
# the work happens. Each page below names the market, the entity standing behind the
# work there and the systems that market actually buys. Nothing claims a client, a
# delivered result or a presence that does not exist.
COUNTRIES=[
 {'file':'kenya.html','country':'Kenya','code':'KE','city':'Nairobi','region':'East Africa',
  'neighbours':'Uganda, Tanzania and Rwanda',
  'lede':'AlphaIT Engineering works with businesses, institutions and public bodies in Kenya, from Nairobi, and across East Africa.',
  'presence':'AlphaIT operates from Nairobi and serves Kenya, Uganda, Tanzania and Rwanda. Work is contracted through Alpha Innovation Technologies - F.Z.C, licence 33549, Ajman Free Zone, United Arab Emirates.',
  'focus':[('Verdika','Experience and accountability. Verdika is live in Kenya as a public application for rating leaders, institutions and services, and the same platform is deployed for organisations that need to understand customer, employee or member experience.'),
           ('Varren Aegis','Platform assurance for Kenyan fintechs, platforms and service businesses: watch a live platform, attack it deliberately, and hold every finding open until the check that found it passes again.'),
           ('LisBon Flow','Transport, logistics and field service operators who run routes, jobs and drivers across calls, messages and spreadsheets, and need one operating view instead.'),
           ('Focused AlphaIT Build','A system engineered around a Kenyan operation that no existing product carries, built to acceptance checks agreed before the work starts.')],
  'faq':[('Does AlphaIT Engineering work in Kenya?','Yes. AlphaIT operates from Nairobi and serves organisations across Kenya, and from there Uganda, Tanzania and Rwanda. Verdika, one of the systems AlphaIT engineered, is live in Kenya.'),
         ('Where is AlphaIT Engineering located in Kenya?','Nairobi. Enquiries are answered at projects@alphaitengineering.com.'),
         ('What kind of software does AlphaIT build for Kenyan businesses?','Experience and feedback platforms, platform security and assurance, credit and financial trust infrastructure, transport and logistics operations systems, practical training records, and focused custom builds where no existing system fits.'),
         ('Who contracts the work in Kenya?','Alpha Innovation Technologies - F.Z.C, a free zone company licensed in Ajman, United Arab Emirates, licence and registration number 33549.'),
         ('Can AlphaIT work with a Kenyan organisation that already has systems?','Yes. The usual route is to connect what already exists and engineer only the part that is missing, rather than replace a working system.')]},
 {'file':'nigeria.html','country':'Nigeria','code':'NG','city':'Lagos','region':'West Africa',
  'neighbours':'Ghana and the wider West African market',
  'lede':'AlphaIT Engineering works with lenders, institutions and operators in Nigeria, from Lagos, and across West Africa.',
  'presence':'AlphaIT operates from Polaris Bank Building, 30 Marina Street, Lagos Island, Lagos. The Nigerian entity is Alpha Innovation Technologies Ltd, CAC registration number 7450573, incorporated 17 April 2024.',
  'focus':[('LisBon Trust Infrastructure','Credit decisioning for Nigerian banks, lenders and fintechs: trust, eligibility, authorisation, exposure and obligations governed so every decision can be explained, replayed and defended.'),
           ('LisBon Signal Infrastructure','Bank statements and financial records validated and structured before they reach a lending decision, with the source, the confidence and the exceptions preserved.'),
           ('LisCredit Marketplace','Qualified demand and participating capital brought into one governed marketplace, deployed for an operator, embedded in an existing platform or joined as a provider.'),
           ('Focused AlphaIT Build','A system engineered around a Nigerian operation that no existing product carries, built to acceptance checks agreed before the work starts.')],
  'faq':[('Does AlphaIT Engineering work in Nigeria?','Yes. AlphaIT operates from Lagos through Alpha Innovation Technologies Ltd, CAC registration number 7450573, and serves Nigeria and the wider West African market including Ghana.'),
         ('Where is AlphaIT Engineering located in Nigeria?','Polaris Bank Building, 30 Marina Street, CMS Bus Stop, Lagos Island, Lagos. Enquiries are answered at projects@alphaitengineering.com.'),
         ('What does AlphaIT build for Nigerian lenders?','Infrastructure for credit decisioning and financial trust: LisBon Signal Infrastructure for validating financial records, LisBon Trust Infrastructure for governing the decision itself, and LisCredit for bringing qualified demand and capital providers together.'),
         ('Is the software built for Nigerian regulation?','The systems are built so that the evidence, the applicable rule, the authority for each action and what happened afterwards are preserved as separate inspectable records. Deployment is subject to applicable law, agreed policy and the authority of each institution.'),
         ('Can AlphaIT connect to systems a Nigerian institution already runs?','Yes. Where a core system is already in place, AlphaIT connects to it through approved integrations and engineers only the missing capability.')]},
 {'file':'uae.html','country':'United Arab Emirates','code':'AE','city':'Dubai','region':'the Gulf',
  'neighbours':'Saudi Arabia and Qatar',
  'lede':'AlphaIT Engineering works with organisations in Dubai, Abu Dhabi and the wider Gulf, licensed in Ajman Free Zone.',
  'presence':'The contracting entity is Alpha Innovation Technologies - F.Z.C, a free zone company licensed by the Free Zones Authority of Ajman, licence and registration number 33549, first issued 31 January 2024, at B.C. 1301279, Ajman Free Zone C1 Building. Work is delivered across the United Arab Emirates, Saudi Arabia and Qatar.',
  'focus':[('Varren Aegis','Platform assurance for Gulf platforms and digital services: deliberate adversarial pressure across access, data, scale, integrations, business logic and billing, with every finding held open until a repeat check passes.'),
           ('LisBon Trust Infrastructure','Decision infrastructure for institutions that must show why a decision was made, under what authority, and what followed from it.'),
           ('Verdika','Experience and accountability for organisations and public bodies that need to understand what people experience and show what was done about it.'),
           ('Focused AlphaIT Build','A system engineered around a Gulf operation that no existing product carries, built to acceptance checks agreed before the work starts.')],
  'faq':[('Is AlphaIT Engineering a UAE company?','Yes. Alpha Innovation Technologies - F.Z.C is a free zone company licensed by the Free Zones Authority of Ajman, licence and registration number 33549, first issued 31 January 2024. It is the contracting entity for AlphaIT Engineering.'),
         ('Does AlphaIT work with companies in Dubai?','Yes. The licensed premises are in Ajman Free Zone and work is delivered across Dubai, Abu Dhabi and the wider Gulf, including Saudi Arabia and Qatar.'),
         ('What software does AlphaIT build for organisations in the Gulf?','Platform security and assurance, decision and credit infrastructure, experience and accountability platforms, operations systems for movement and field work, and focused custom builds.'),
         ('Can AlphaIT deliver in Saudi Arabia?','Yes, as part of the Gulf coverage from the UAE entity. Delivery is subject to applicable law, the data permissions available and the authority of the organisation involved.'),
         ('How does an engagement start?','Describe the service, revenue opportunity or operation to be improved. AlphaIT identifies the strongest starting point, the evidence required and the measures that will show the change, before any build is agreed.')]},
]

def country_page(c):
 body=f'''<section class="page-intro"><p class="eyebrow">AlphaIT Engineering in {e(c['country'])}</p><h1>Systems for {e(c['country'])}.<br>Built to <em>be examined.</em></h1><p class="lede">{e(c['lede'])}</p><div class="actions">{action('Show us the opportunity','contact.html')}<a class="text-link" href="platforms.html">Explore the systems ↗</a></div></section><section class="section company-story"><div><p class="eyebrow">Presence</p><h2>Where the work<br>is done from.</h2></div><div><p>{e(c['presence'])}</p><p>AlphaIT deploys a system it has already engineered where one fits, connects it to the tools and data an organisation already runs, and engineers only the part that is still missing.</p></div></section><section class="section depth-section"><div class="section-head"><div><p class="eyebrow">What {e(c['country'])} buys</p><h2>The systems that<br>fit this market.</h2></div><p>Every deployment agrees scope, integrations, data permissions, responsibilities and acceptance checks before the work starts.</p></div>'''+capability_grid(c['focus'])+'</section>'+faq_section(c['faq'],f"Questions from<br>{e(c['country'])}.")+close(f"Put a system to work<br>in {e(c['country'])}.",'Tell us the service, opportunity or operation. We will identify the strongest starting point and what has to be true for it to work.')
 page(c['file'],body=body,schema=[
  faq_schema(c['faq']),
  breadcrumbs([('Home',''),(c['country'],c['file'])]),
  {'@type':'Service','name':f"Product engineering in {c['country']}",'provider':{'@id':ORG_ID},'areaServed':{'@type':'Country','name':c['country']},'serviceType':'Software and product engineering','description':c['lede']},
 ])

for c in COUNTRIES: country_page(c)

page('privacy.html',body=privacy,schema=[breadcrumbs([('Home',''),('Privacy notice','privacy.html')])])
page('terms.html',body=terms,schema=[breadcrumbs([('Home',''),('Website terms of use','terms.html')])])

Image.open(OUT/'assets/brand/hero.png').convert('RGB').save(OUT/'assets/brand/hero.webp',quality=86,method=6)
im=Image.open(OUT/'assets/brand/hero.png').convert('RGB'); im.thumbnail((1000,1000)); im.save(OUT/'assets/brand/hero-mobile.webp',quality=83,method=6)
# The assistant crawlers are named rather than left to the wildcard. A bare wildcard does
# allow them, but these agents are refused by default in robots files copied around the web,
# and a silent refusal is indistinguishable from not existing when somebody asks an assistant
# what AlphaIT Engineering does.
AI_AGENTS=['GPTBot','OAI-SearchBot','ChatGPT-User','ClaudeBot','Claude-SearchBot','Claude-User','Claude-Web','anthropic-ai','PerplexityBot','Perplexity-User','Google-Extended','Googlebot','Googlebot-Image','Bingbot','Applebot','Applebot-Extended','DuckDuckBot','YandexBot','CCBot','Meta-ExternalAgent','cohere-ai','Amazonbot','Bytespider','MistralAI-User','Timpibot','Diffbot','omgili']
robots='User-agent: *\nAllow: /\n\n'+''.join(f'User-agent: {a}\nAllow: /\n\n' for a in AI_AGENTS)+'Sitemap: https://alphaitengineering.com/sitemap.xml\n'
(OUT/'robots.txt').write_text(robots,encoding='utf-8')

# llms.txt states the substance in the order somebody answering a question about AlphaIT
# would want it, and claims nothing the pages do not already claim.
llms=f'''# AlphaIT Engineering

> Product engineering company that builds, deploys and licenses the systems businesses, institutions and governments run on. Operating across Kenya, Nigeria and the United Arab Emirates.

AlphaIT Engineering starts from a system it has already engineered, connects it to the tools and data an organisation already runs, and engineers only the capability that is still missing.

- Legal entity (contracting): Alpha Innovation Technologies - F.Z.C, Free Zone Company, Ajman Free Zone, United Arab Emirates. Licence and registration number 33549, first issued 31 January 2024.
- Legal entity (Nigeria): Alpha Innovation Technologies Ltd, CAC registration number 7450573, incorporated 17 April 2024.
- Founder and enterprise architect: Alpha Lucky Chukwunwike Okechukwu, who also founded LisBon Platforms and LisBonFARM.
- Locations: Ajman Free Zone, United Arab Emirates. Nairobi, Kenya. Lagos, Nigeria.
- Contact: projects@alphaitengineering.com
- Brand line: Product Engineering. Without Limits.

## Systems engineered by AlphaIT

{chr(10).join(f"- [{p['name']}]({SITE}{p['slug']}): {p['promise']} {p['index']}. For: {p['buyer']}" for p in products)}

## Pages

- [Home]({SITE}): what AlphaIT makes possible and how an engagement works.
- [Our systems]({SITE}platforms): every engineered system and who each is for.
- [How we work]({SITE}engagements): deploy a ready system, connect what exists, engineer what is missing.
- [Company]({SITE}company): business model, entities and locations.
- [Founder]({SITE}founder): Alpha Lucky Chukwunwike Okechukwu, founder and enterprise architect.
- [Kenya]({SITE}kenya): what AlphaIT does in Kenya and East Africa, from Nairobi.
- [Nigeria]({SITE}nigeria): what AlphaIT does in Nigeria and West Africa, from Lagos.
- [United Arab Emirates]({SITE}uae): what AlphaIT does in the UAE and the wider Gulf, licensed in Ajman Free Zone.
- [Contact]({SITE}contact): enquiry form, email and WhatsApp.

## Related platforms founded by Alpha Lucky Chukwunwike Okechukwu

- LisBon Platforms (https://lisbonplatforms.com): multi-sector infrastructure group. AlphaIT engineers the LisBon products; LisBon Platforms owns and operates them.
- LisBonFARM (https://lisbonfarm.com): agro-industrial infrastructure platform, sponsor of AgroGlobal ICPI in Edo State, Nigeria.
- Verdika (https://verdika.co): the live public application of the Verdika experience and accountability platform.

## What AlphaIT does not claim

- Deployment scope, integrations, data permissions, timing and commercial terms are agreed per organisation and are not published.
- Product measures are what a deployment can make visible, not guaranteed results.
- AlphaIT builds, hosts and licenses these systems. It does not operate them on its own behalf, so it publishes no usage figures of its own.
'''
(OUT/'llms.txt').write_text(llms,encoding='utf-8')

# Google Search Console ownership, property created 1 October 2026 under
# alphaitengineering@gmail.com. Both methods are published so losing one does not
# unverify the property: the meta tag above and this file. Do not remove either.
(OUT/'googleec96136a95708583.html').write_text('google-site-verification: googleec96136a95708583.html',encoding='utf-8')

# Bing Webmaster Tools ownership, site added 2 October 2026 under the same account.
# Both methods again: the meta tag above and this file. Do not remove either.
(OUT/'BingSiteAuth.xml').write_text('<?xml version="1.0"?>\n<users>\n\t<user>88FC7D77598749E72F6C4ECA833929ED</user>\n</users>\n',encoding='utf-8')
public_routes=['','platforms']+[p['slug'] for p in products]+['company','founder','engagements','contact','proof']+[route(c['file']) for c in COUNTRIES]+['privacy','terms']
sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>https://alphaitengineering.com/{route}</loc></url>\n' for route in public_routes)+'</urlset>\n'
(OUT/'sitemap.xml').write_text(sitemap,encoding='utf-8')
(ROOT/'products.json').write_text(json.dumps(products,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Generated {len(list(OUT.glob("*.html")))} pages from the approved customer profile.')
