"""Articles published at /insights.

Every claim here is either reasoning the reader can check for themselves, a fact from
the public record, or a statement about what an AlphaIT system does that the product
pages already make. No client is named, no delivered result is claimed and no statistic
is quoted that is not sourced in the text. A buyer who checks one of these sentences and
finds it hollow will not read the second article.

Each entry: slug, title (search phrase first), description, published, updated, lede,
and body as HTML using the site's existing section classes.
"""

ARTICLES = [
 {
  'slug': 'explain-a-credit-decision',
  'title': 'What a Lender Must Be Able to Show About a Credit Decision',
  'description': 'A credit decision is questioned months after it is made, by someone who was not there. What a lender has to be able to produce, and what that requires of the system that made the decision.',
  'published': '2026-10-03',
  'updated': '2026-10-03',
  'eyebrow': 'Credit and financial trust',
  'heading': 'What a lender must be able<br>to <em>show</em> about a decision.',
  'lede': 'Nobody questions a credit decision on the day it is made. They question it months later, when the loan has gone bad, the borrower has complained or a regulator has asked. By then the person who made it has moved on and the screen they saw no longer exists.',
  'body': '''<section class="section company-story"><div><h2>The question is never "was it right".</h2></div><div>
<p>It is "show me". Show me what you knew. Show me the rule you applied. Show me who was allowed to approve it. Show me what happened after.</p>
<p>Those are four different questions and most lending systems answer only the first, badly. They hold the application and the outcome. The reasoning in between lives in a score that cannot be reconstructed, a policy document that has been edited since, and the memory of an analyst who has left.</p>
</div></section><section class="section depth-section"><div class="section-head"><div><p class="eyebrow">Four records, not one</p><h2>What has to survive<br>the decision.</h2></div><p>If any one of these is missing, the answer to "show me" becomes "trust me", and trust is not an answer a regulator accepts.</p></div><div class="capability-grid">
<article><h3>The evidence</h3><p>Not the document that was uploaded, but what the system concluded from it and how confident it was. A bank statement is not evidence. The identified income, the verified source, the gaps and the integrity checks that ran on it are evidence. Keep the conclusion and the basis for it, because the document alone will not tell you later what the system actually read.</p></article>
<article><h3>The rule that applied</h3><p>Policy changes. The version that applied on the day is the only version that matters when the decision is examined, and it must be retrievable without reconstructing it from memory or from a document that has since been revised. A system that applies "the current policy" cannot explain a decision made under an older one.</p></article>
<article><h3>The authority</h3><p>Who or what was permitted to take this action, under which delegation, at that moment. An approval by a person who did not hold the authority is not an approval, and discovering that two years later is considerably worse than refusing it at the time.</p></article>
<article><h3>What followed</h3><p>Exposure, obligations, repayments, restructures, defaults. A decision is not a point in time; it is the start of a state that changes. Judging the decision without its consequences tells you nothing about whether the decision was sound.</p></article>
</div></section><section class="section company-story"><div><h2>Why scores are not explanations.</h2></div><div>
<p>A score compresses many inputs into one number. That is its purpose and also its limit. It cannot tell you which input moved it, whether that input was reliable, or what the answer would have been had one field been different.</p>
<p>A score is useful for ranking and useless for defending. When the question is "why was this applicant refused", a number between 0 and 100 is not a reason. It is the output of a reason that was not kept.</p>
<p>This matters more, not less, as models get better. A more accurate model that cannot be explained is a larger liability than a cruder one that can, because more decisions rest on it.</p>
</div></section><section class="section proof-band"><div><p class="eyebrow">The practical test</p><h2>Replay it.</h2></div><div>
<p>Here is the test worth running against any lending system, today, on a decision from last year.</p>
<p>Take a decision that is now disputed. Feed the same evidence back into the system and ask it to produce the same outcome, under the policy that applied at the time, with the authority that was held at the time. If the result differs, or if the question cannot be asked at all, the system cannot defend its own decisions. Everything after that is a question of how long before someone notices.</p>
<p class="boundary-note">Most systems fail this test not because anyone designed them badly, but because nobody required them to pass it.</p>
</div></section><section class="section company-story"><div><h2>What this costs to fix.</h2></div><div>
<p>Less than it looks, if it is treated as an infrastructure problem rather than a reporting problem. The common mistake is to bolt an audit log onto a system that was not built to produce one, which yields a record of what the software did without a record of why.</p>
<p>The alternative is to put the four records at the centre of the decision path, so the explanation is a by-product of making the decision rather than a reconstruction after it. That is what LisBon Trust Infrastructure is: deterministic infrastructure for governing trust, eligibility, authorisation, exposure and credit obligations, which preserves the evidence, the rule, the state and the history behind each consequential decision. LisBon Signal Infrastructure sits in front of it and turns raw financial records into evidence with a source and a confidence attached.</p>
<p>Neither removes the lender\'s judgement or the lender\'s risk. They make the judgement legible.</p>
</div></section>''',
  'faq': [
   ('What should a lender keep about a credit decision?','Four things, kept separately: the evidence and what the system concluded from it, the version of the policy that applied at the time, the authority under which the action was taken, and what happened afterwards to exposure and obligations.'),
   ('Is a credit score enough to explain a decision?','No. A score compresses many inputs into one number, which is useful for ranking and useless for defending. It cannot tell you which input moved it or what the answer would have been had one field been different.'),
   ('How can a lender test whether its system can explain a decision?','Take a disputed decision from last year, feed the same evidence back in, and ask the system to reproduce the outcome under the policy and the authority that applied at the time. If the result differs, or the question cannot be asked, the system cannot defend its decisions.'),
   ('What does AlphaIT provide for this?','LisBon Signal Infrastructure validates and structures financial records before they reach a decision. LisBon Trust Infrastructure governs trust, eligibility, authorisation, exposure and obligations, and keeps the decision replayable. Neither removes the lender\'s judgement or risk.'),
  ],
 },
 {
  'slug': 'test-your-platform-first',
  'title': 'Test Your Platform Before a Regulator or a Customer Does',
  'description': 'A platform can look healthy while a security boundary, a payment, a journey or a pricing rule is already failing. What to test, in what order, and why a dashboard that is green proves very little.',
  'published': '2026-10-03',
  'updated': '2026-10-03',
  'eyebrow': 'Platform assurance',
  'heading': 'Attack your platform<br>before <em>anyone else</em> does.',
  'lede': 'Uptime monitoring answers one question: is the server responding. It is the easiest question to answer and the least useful one, because almost everything that damages a business happens while the server responds perfectly.',
  'body': '''<section class="section company-story"><div><h2>Green dashboards and broken businesses.</h2></div><div>
<p>A payment that silently fails for one card type. A permission check that passes for a user who should not have it. A journey that dies on the third step for anyone on a slow connection. A pricing rule that has been charging the wrong amount since a release in March.</p>
<p>Every one of those is invisible to uptime monitoring, and every one of them is more expensive than an outage. An outage is noticed in minutes by everyone. These are noticed in months by one person, usually a customer, often publicly.</p>
</div></section><section class="section depth-section"><div class="section-head"><div><p class="eyebrow">Four jobs, not one</p><h2>Watch. Attack.<br>Witness. Close.</h2></div><p>Most tools do the first. The gap between the first and the other three is where the damage accumulates.</p></div><div class="capability-grid">
<article><h3>Watch</h3><p>Run the real journeys on a schedule, in production and in staging, as a user would. Not a ping. A sign-in, a search, an application, a payment. Detect what is broken or drifting before a customer meets it.</p></article>
<article><h3>Attack</h3><p>Apply deliberate adversarial pressure across access, data, scale, integrations, business logic and commercial rules. The question is not whether the system works when used correctly. It is what happens when it is used incorrectly, maliciously, or at ten times the expected rate.</p></article>
<article><h3>Witness</h3><p>Capture what real users actually encounter, including the errors, dead ends and failed journeys that never reach a support ticket because the person simply left.</p></article>
<article><h3>Close</h3><p>Hold every finding open until the check that found it runs again and comes back clean. A finding marked resolved without a passing repeat check is a finding that has been filed, not fixed.</p></article>
</div></section><section class="section company-story"><div><h2>The test nobody runs.</h2></div><div>
<p>Here is a check worth running this week, on a live system, with a real account.</p>
<p>Take a user who should be able to see exactly one organisation\'s data. Have them request another organisation\'s record directly, by changing an identifier in a request. If they get the data, you have a boundary failure that no dashboard will ever show you.</p>
<p>Then run the inverse, which is the one teams forget. After you fix it, confirm that the legitimate user can still see their own data. A fix that returns nothing to everybody looks identical to a fix that works, right up until the first support call.</p>
</div></section><section class="section proof-band"><div><p class="eyebrow">Commercial, not only technical</p><h2>Billing is part<br>of the attack surface.</h2></div><div>
<p>Security testing that stops at authentication misses where the money leaks. A discount rule that applies twice. A subscription that is cancelled in the interface but not in the billing system. A currency conversion that rounds in the customer\'s favour on every transaction.</p>
<p>These are not security defects in the textbook sense and they are often larger. They are also the easiest to find deliberately and the hardest to find by accident, because the system behaves exactly as written.</p>
<p class="boundary-note">Varren Aegis examines security, performance, integrations, user experience, business logic, billing and releases, and never changes a client system without explicit authorisation.</p>
</div></section><section class="section company-story"><div><h2>Why the order matters.</h2></div><div>
<p>Teams usually start with a penetration test because it is the thing a board asks for. A penetration test is a snapshot: it tells you what was true on one day, against one scope, by one tester.</p>
<p>The better order is continuous watching first, so you learn what normal looks like, then deliberate attack against the parts that matter commercially, then witnessing what real users hit. The snapshot is worth more once you can tell the difference between a new finding and a condition that has been there for a year.</p>
</div></section>''',
  'faq': [
   ('What does uptime monitoring miss?','Almost everything that damages a business: silently failing payments, permission checks that pass for the wrong user, journeys that die partway, and pricing rules charging the wrong amount. All of those happen while the server responds normally.'),
   ('How do you test a permission boundary?','Have a user who should see exactly one organisation\'s data request another organisation\'s record directly, by changing an identifier. Then, after fixing any failure, confirm the legitimate user can still see their own data. A fix that returns nothing to everybody looks identical to one that works.'),
   ('Is billing part of security testing?','It should be. A discount applied twice, a cancellation that does not reach the billing system, or a conversion that rounds the wrong way are not textbook security defects, but they are often larger losses and easier to find deliberately.'),
   ('What is Varren Aegis?','A platform assurance system that watches, attacks and witnesses a digital platform, then holds every finding open until the check that found it passes again. It covers security, performance, integrations, user experience, business logic, billing and releases, and never changes a client system without explicit authorisation.'),
  ],
 },
 {
  'slug': 'feedback-that-holds-up',
  'title': 'Customer Feedback That Holds Up When It Is Challenged',
  'description': 'Most feedback data cannot survive a serious question about who provided it. What verified participation changes, what it does not, and the difference between feedback and research.',
  'published': '2026-10-03',
  'updated': '2026-10-03',
  'eyebrow': 'Experience and accountability',
  'heading': 'Feedback that holds up<br>when it is <em>challenged.</em>',
  'lede': 'An organisation acts on feedback, publishes a number, and is then asked a simple question: who said this? For most feedback systems, the honest answer is that nobody knows.',
  'body': '''<section class="section company-story"><div><h2>The question that ends most dashboards.</h2></div><div>
<p>Ratings are easy to collect and easy to manufacture. The same person can respond ten times. A competitor can respond at all. An automated script can respond faster than a human can read the question.</p>
<p>None of this matters while the number is flattering and nobody is looking. It matters enormously the first time the number is used to justify a decision, a budget, a dismissal or a public claim, and someone with an interest in the opposite result starts asking how it was gathered.</p>
</div></section><section class="section depth-section"><div class="section-head"><div><p class="eyebrow">Three separate things</p><h2>Keep them apart.</h2></div><p>Most systems merge these, and the merge is what makes the result impossible to defend later.</p></div><div class="capability-grid">
<article><h3>Who participated</h3><p>Whether the contribution came from an eligible, verified person, and on what basis they were eligible. This is an identity question and it has an identity answer.</p></article>
<article><h3>What they said</h3><p>The opinion itself, which is subjective, voluntary and does not become more true because the person is verified. Verification makes the response attributable, not correct.</p></article>
<article><h3>What the organisation did</h3><p>The response, the action taken and the evidence for it. This is the organisation\'s claim about itself and belongs in a separate record from the public\'s claim about the organisation.</p></article>
</div></section><section class="section company-story"><div><h2>What verification actually buys.</h2></div><div>
<p>Binding a contribution to an eligible, verified participant, and preserving the basis on which that person was eligible, makes duplicate, synthetic and impersonated participation materially harder. That is a real gain and it is worth paying for when the output will be used for anything consequential.</p>
<p>It is also commonly oversold. Here is what it does not do.</p>
<p>It does not make the sample representative. A verified self-selected group is still self-selected. The people who respond are the people who felt strongly enough to respond, and verification changes nothing about that bias.</p>
<p>It does not make an opinion accurate. A verified person can be mistaken, unfair or lying about their experience.</p>
<p>It does not turn feedback into research. Research requires a designed sample and a method. Verified feedback is a stronger form of feedback, which is a different thing and should be described as a different thing.</p>
</div></section><section class="section proof-band"><div><p class="eyebrow">The hard part</p><h2>Refusing the<br>duplicate.</h2></div><div>
<p>The engineering problem is not detecting duplicates. It is deciding what to do when you detect one, in the moment, while the person is on the screen.</p>
<p>The easy path is to accept the contribution and flag it for review, which keeps the participation numbers healthy and quietly ruins the data. The correct path is to refuse it, tell the person why, and give them a route to appeal, which costs you a response and keeps the result defensible.</p>
<p>A refusal a person cannot see or contest is not governance, it is a filter. The refusal has to be visible, reviewable by a human and reversible if it was wrong. That is the part that takes the work, and it is the part a serious buyer should ask about.</p>
<p class="boundary-note">Verdika can bind a contribution to an eligible, verified participant and preserve the basis for that participation. Identity, participant opinion, documented evidence and institutional response remain separate records.</p>
</div></section><section class="section company-story"><div><h2>What to ask a vendor.</h2></div><div>
<p>Four questions worth asking anyone selling a feedback or review platform.</p>
<p>Can the same person contribute twice, and what happens when they try? Can the person see and contest a refusal? Are the organisation\'s response and the public\'s contribution stored as separate records, or does one overwrite the other? And when a recurring problem is identified, does the system name the team responsible for it, or does it stop at a chart?</p>
<p>The last one matters more than it sounds. A finding owned by nobody never gets fixed, and a system that produces unowned findings produces activity rather than improvement.</p>
</div></section>''',
  'faq': [
   ('Why is most customer feedback data hard to defend?','Because the same person can respond repeatedly, competitors can respond, and scripts can respond faster than a human can read. None of that matters until the number is used to justify a decision and someone starts asking how it was gathered.'),
   ('What does verified participation actually prove?','That a contribution came from an eligible, verified person, and on what basis they were eligible. It makes duplicate, synthetic and impersonated participation materially harder. It does not make the sample representative, make the opinion accurate, or turn feedback into research.'),
   ('What should happen when a duplicate contribution is detected?','It should be refused while the person is still there, with the reason shown and a route to appeal. Accepting it and flagging it for review keeps participation numbers healthy and quietly ruins the data.'),
   ('What should a buyer ask a feedback platform vendor?','Can the same person contribute twice and what happens when they try; can a person see and contest a refusal; are the organisation\'s response and the public\'s contribution stored separately; and when a recurring problem is found, does the system name the team responsible for it.'),
  ],
 },
 {
  'slug': 'buy-or-build-a-system',
  'title': 'Buy or Build: How to Decide Before You Spend',
  'description': 'The question is rarely buy or build. It is which part to buy, which part to connect and which part genuinely has to be engineered, and the answer changes the cost by an order of magnitude.',
  'published': '2026-10-03',
  'updated': '2026-10-03',
  'eyebrow': 'How engagements start',
  'heading': 'Buy or build:<br>decide <em>before</em> you spend.',
  'lede': 'Most organisations ask the wrong question. They ask whether to buy a system or build one, as though the operation were a single thing. It is not, and treating it as one is what produces both the failed implementation and the three-year internal project.',
  'body': '''<section class="section company-story"><div><h2>Two expensive failures.</h2></div><div>
<p>The first is buying a platform that fits most of the operation and forcing the rest of the operation to change shape around it. The software works. The business quietly degrades to match it, and nobody attributes the degradation to the purchase.</p>
<p>The second is building everything, because the fit was imperfect, and discovering that ninety percent of what was built already existed and the remaining ten percent is the only part that mattered.</p>
<p>Both come from the same error: deciding at the level of the whole system rather than at the level of each capability.</p>
</div></section><section class="section depth-section"><div class="section-head"><div><p class="eyebrow">Three routes, one operation</p><h2>Deploy. Connect.<br>Engineer.</h2></div><p>Almost every real operation needs all three. The skill is knowing which is which before the money is committed.</p></div><div class="capability-grid">
<article><h3>Deploy what exists</h3><p>Where a capability is genuinely common, buy it. Feedback collection, credit decision governance, route coordination, platform assurance. These are solved problems and rebuilding them is a way of spending a year to arrive where you could have started.</p></article>
<article><h3>Connect what you run</h3><p>The systems already in place usually hold the data and the authority. Connecting them is cheaper than replacing them and far cheaper than migrating off them, and it keeps the institutional knowledge that lives in how they are used.</p></article>
<article><h3>Engineer what is missing</h3><p>There is always a part that is specific to this organisation, this regulation, this market. That part is where custom engineering earns its cost, and it is usually much smaller than the original scope suggested.</p></article>
</div></section><section class="section company-story"><div><h2>How to tell which is which.</h2></div><div>
<p>A capability should be bought when another organisation in another country would recognise it immediately. Authentication. Payments. Document validation. Scheduling. If it is common, someone has already paid for the mistakes.</p>
<p>A capability should be engineered when describing it requires naming your market, your regulator or your particular operation. If the explanation starts with "in Nigeria, lenders have to..." or "our dispatchers do this differently because...", that is the part to build.</p>
<p>Everything in between should be connected rather than replaced, and the test is simple: does the existing system hold data or authority that would have to be recreated? If yes, connect to it. Migration is a project with no visible benefit to anyone outside the technology team.</p>
</div></section><section class="section proof-band"><div><p class="eyebrow">Before anything is agreed</p><h2>Decide how you will<br>know it worked.</h2></div><div>
<p>The single most useful thing to do before committing money is to write down what should change and how the change will be visible. Not a business case. A measure.</p>
<p>Time from application to decision. Number of records requiring manual investigation. Proportion of journeys completed. Recurring issues closed with a passing repeat check. Whatever it is, it must be something the organisation can observe without asking the vendor.</p>
<p>If no such measure can be written, the project does not have an agreed purpose yet, and no amount of software will supply one.</p>
<p class="boundary-note">Measures are agreed for each deployment. They describe what the system can make visible, not a guaranteed result.</p>
</div></section><section class="section company-story"><div><h2>What this looks like in practice.</h2></div><div>
<p>A lender needs credit decisions that can be explained two years later. The decision governance is bought, because the four records a decision must preserve are the same in every market. The core banking system is connected, because it holds the accounts and nobody benefits from replacing it. The product rules specific to that lender, in that regulatory environment, are engineered.</p>
<p>The result costs a fraction of the full build and fits the operation in the places where fit actually matters. It also arrives this year rather than the year after next, which is usually the difference that decides whether it is used at all.</p>
</div></section>''',
  'faq': [
   ('Should we buy software or build it?','Rarely one or the other. Decide at the level of each capability: buy what is genuinely common, connect the systems that already hold your data and authority, and engineer only the part that is specific to your market, your regulator or your operation.'),
   ('How do you know which capability to build?','If describing it requires naming your market, your regulator or your particular operation, build it. If another organisation in another country would recognise it immediately, buy it.'),
   ('When should an existing system be connected rather than replaced?','Whenever it holds data or authority that would otherwise have to be recreated. Migration is a project with no visible benefit to anyone outside the technology team.'),
   ('What should be agreed before money is committed?','A measure. Something the organisation can observe without asking the vendor, such as time to decision, records requiring manual investigation, or journeys completed. If no such measure can be written, the project does not yet have an agreed purpose.'),
  ],
 },
]
