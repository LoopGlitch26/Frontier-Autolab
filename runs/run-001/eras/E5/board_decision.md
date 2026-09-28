# Board Decision: Era E5 (January 2014)
*Attendees: Castell (CEO), Rao (CTO), Okafor (Chief Scientist), Weil (CSO), Hale (Red Team). Sources are limited to what was public before 1 Jan 2014.*

## 1. Transcript highlights

**Victor Hale (Red Team):** [E4] says unanimity right after a reveal is a leakage alarm, and we have it again. All three departments put "deep networks on GPUs" as lead or reserved slot, and all three put "neutral trust referee" as the other thesis. The E4 reveal named neural networks as the curve we left unfunded, and it named the referee as the layer that held. Briefing or answer key?

**Victor, on Frontier's Thesis A (perception for camera phones):** Separate the evidence from the hype. Evidence: ImageNet 2012–13, speech results at three labs, the Hinton and LeCun hires. Hype: "a billion cameras nobody can read" is a market-size slide, not a buyer. Brandt says value goes to corpus and distribution owners, and Google, Facebook and Microsoft own both. Google has sold a Prediction API since 2010 and can add labeling any time. Vocabulary Audit: "models small enough to run on the phone" has no 2013 evidence. Strike it.

**Dr. Lena Okafor (Chief Scientist):** Struck. The rest stands without any reveal: third briefing in a row listing GPU networks, a tiny team among the 2013 ImageNet leaders, public code (cuda-convnet, Theano, Torch), gains replicated across labs. The talent shortage is what a small company can arbitrage for ~24 months.

**Victor, on Market's Thesis A (trust network for marketplaces):** Comfort in a new costume: our fraud models resold to a new buyer ([E2]), no new curve. [E3] with a new owner: Stripe and Square can bundle risk scoring free. The EU draft targets cross-app device graphs. "Underwriting" is a balance-sheet business we've never run.

**Tomas Weil (CSO):** Fair on payments. But fake accounts, promo abuse and collusion don't pass through the processor, and no processor sees across Uber, Lyft and delivery apps.

**Victor, on Product's Thesis A (hosted recognition API):** Moderation is real, but outsourced review costs cents an image. We'd undercut a cheap queue in an 18-month window before a giant ships free, with researchers we can't afford.

**Dev Anand Rao (CTO):** We need 3–4 applied people who fine-tune ImageNet-class networks on messy commercial data, not architecture inventors; the labs aren't bidding for them yet. Giants will ship general labels ("dog"). They won't ship "this listing photo is stolen" or "this profile violates a dating app's policy." Domain judgment is where corrections compound.

**Victor:** So the two theses are really one: learned models judging content and accounts for trust teams.

**Mira Castell (CEO):** Yes. The curve is documented; the buyer is the trust-and-safety budget, which exists, sits outside marketing, and no ad auction absorbs. I'm deciding.

## 2. DECISION (CEO)

**Company name:** **Clearsight**. The performance exchange keeps the Clearline name for the sale.
**Identity:** *Trained judgment for every app: learned models that read photos, profiles and actions for the trust teams the platform giants don't serve.*

**Reinvention thesis:**
- **Capability:** GPU-trained deep networks beat hand-built features in vision and speech (2010–13).
- **Adoption:** photo, dating, classifieds and on-demand marketplace apps take in millions of images and unknown accounts every day.
- **Bottleneck:** human review queues and hand-built rules. Talent and GPUs sit with 3–4 giants who don't sell domain judgment.
- **Layer we own:** a hosted *judgment API*: image moderation, listing and profile verification, and account-risk scoring on one learned stack. It is priced per decision and delivered through our existing SDK.
- **Data:** customer corrections and outcomes (moderator overrides, bans, chargebacks), voluntary, held per client under separate keys.
- **Next capability:** multimodal judgment (image + text + behavior). Then speech and video review. Then priced risk (guarantees) once loss data is deep enough.

**KILL:** the performance exchange as identity and business (sold in H1 2014 on the credit calendar, [E4]); the hand-engineered fraud feature roadmap; any cross-app device graph that isn't privacy-first by design; the licensed legacy search dataset (let it lapse).

**KEEP:** the signed action ledger; fraud models and labelled fraud outcomes (the first training set); the SDK footprint (a sale condition, same as the 2008 data carve-out); the client/mobile team; developer relationships; the frozen handwriting/fax corpus, which is finally a candidate training set.

**Attribution referee (Jonah's asset):** kept for 12 months as *Clearline Verify*, a cash-positive unit of ≤10 people. Sell it by Q2 2015 unless it passes $5M ARR, because Elise's certification argument ([E2 note]) says it becomes a flat-priced utility.

**Reserved slot (10% of new-bet burn, [E3]/[E4]):** messaging platforms as the next distribution layer (WeChat official accounts and payments, WhatsApp, Line). Deliverable: a working bot/commerce integration on one messaging platform by Q4 2014. The gate is capability evidence, not incumbent willingness to pay ([E2]).

**Wedge product:** *Clearsight Moderate*: image moderation plus fake-profile detection, charged per image below the customer's human-queue cost, with a correction console that feeds fine-tuning.

**First customer:** 10 photo, dating and classifieds apps from our SDK base, signed by June 2014. Then 3 on-demand marketplaces for account-risk scoring.

**3-year plan:**
- **2014:** Exchange sale (floor $90M). Hire 3–4 applied deep-learning + 2 GPU engineers; own a small GPU cluster. Moderate live in 9 months ([E3]).
- **2015:** 50 paying apps, $4M ARR. Add account-risk scoring on the same stack. Decide on Verify.
- **2016:** $15M ARR. Multimodal judgment. Raise only on traction.

**Capital need:** ~$38M plus sale proceeds; bet capped at ≤20 people, ~$7M/yr incl. GPUs; no 2014 raise. Proceeds partly clear the preference stack. Below the floor: keep the exchange for cash, cap the bet at $5M/yr.

**Kill criteria** (pre-committed, no waivers):
1. If models don't beat each customer's human moderators on held-out accuracy at lower cost for at least 3 customers by Q4 2014, fold perception back into a fraud-scoring feature.
2. Fewer than 3 applied deep-learning hires by June 2014: license models or acqui-hire, or exit the thesis.
3. If Google, Microsoft, Amazon or Facebook release a free general image-labeling API before we reach $3M ARR, retreat to domain-specific trust judgments only. No general tagging.
4. Fewer than 25 paying customers by Q2 2015.
5. If EU regulation bars cross-client risk signals, move to per-client models only, and the shared-graph ambition is killed.
6. Runway must never fall below 18 months.

**Org changes:**
- Hana Kowalski becomes GM, Clearsight (judgment API).
- New external hire: Head of Applied Deep Learning, reporting to Hana.
- Priya Nair stays VP Engineering, now owning the GPU cluster.
- Dr. Kofi Mensah becomes Head of Trust Science (labels, evaluation, privacy-by-design).
- Jonah Reyes becomes GM, Clearline Verify, with the sale decision in 2015.
- Leo Mbeki becomes Head of Developer Platform and leads the messaging reserved slot.
- Carmen Ortiz takes GTM to trust-and-safety and risk buyers.
- Arjun Mehta owns the exchange sale and carve-outs.
- Dr. Elise Laurent owns per-decision pricing against human-queue cost.
- Victor Hale keeps the Vocabulary Audit and adds a **Convergence Audit**: any thesis that matches the previous reveal must cite at least two pre-era sources the reveal didn't mention.

**Dissent log:**
- **Victor Hale:** the convergence is still reveal-herding, and moderation is a cheap budget. He would fund perception at 30% as an option and lead with nothing new. He won the phone-model strike, kill criterion #3 and the Convergence Audit.
- **Jonah Reyes:** the referee should lead, and Verify shouldn't be put on a sale clock. Logged as a tripwire ([E4]).
- **Carmen Ortiz:** sell the exchange only after 10 contracts are signed. Overruled by the credit calendar.
- **Tomas Weil:** concurs, but wants Stripe/Square bundling tracked as an explicit [E3] tripwire.
