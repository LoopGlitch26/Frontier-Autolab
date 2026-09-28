# Board Decision: Era E4 (January 2008)
*Attendees: Castell (CEO), Rao (CTO), Okafor (Chief Scientist), Weil (CSO), Hale (Red Team). Sources are limited to what was public before 1 Jan 2008.*

## 1. Transcript highlights

**Victor Hale (Red Team):** I'll start with the convergence. All three departments independently chose "run a performance auction for app inventory." In E3 that kind of unanimity meant the Playbook was herding us. This time it's worse. The E3 reveal literally named mobile, social and cloud as the pools we missed. So is this 2008 reasoning or the answer key from last round? Let me test it with the evidence a January 2008 board actually has.

**Victor, the base rate:** "Next year is the year of mobile advertising" has been said every year since WAP in 1999. Carrier decks, 2G data pricing and blind CPM killed each wave. The iPhone is one handset on one carrier on EDGE. Mobile ad networks already exist (AdMob, Millennial Media, JumpTap, AOL's Third Screen Media). We would not be first.

**Victor, the phrases that smell of the future:** (1) "Cost per install." There's no observable install funnel on phones. Apple has *not* said how software will be distributed or whether an ad library may phone home. (2) "Developers pick monetization partners in year one": asserted, not evidenced. (3) Frontier gives Pocket Web 40% with a mass market "by ~2011", which is suspiciously specific. (4) Leo "dates the bridge's death" as the end of handset fragmentation in 3–5 years, which quietly assumes that consolidation happens. (5) "Retained install" and per-user lifetime value are the vocabulary of a market that doesn't exist yet.

**Dr. Lena Okafor (Chief Scientist):** Partly fair. But separate the curve from the vocabulary. The curve is documented: a full browser on a phone, a promised native SDK, an open Android stack, and flat-rate data plans. The Facebook Platform is also real. It created developers with millions of users and almost no revenue. That population exists *today*, with no assumption about Apple.

**Tomas Weil (CSO):** That's my answer to Victor. The honest 2008 thesis isn't "mobile." It's "open application platforms create a new publisher class with no performance auction." Facebook is the evidence, and the phone is the extension. If Apple closes its SDK, the thesis still holds on Facebook, Android and the mobile Web.

**Victor, on Market's Facebook wedge:** Then Elise's objection applies. A poke is not a query. Facebook-app inventory sells for cents, app-ad networks (Social Media, Cubics, RockYou) are already there, and Facebook can change Platform rules overnight. Rented land again.

**Dev Anand Rao (CTO):** Those networks lack our signed ledger and six years of fraud models; incentivized app traffic is the next click fraud. Our gap: we've never shipped client code. The hires are the thesis ([E2]).

**Victor, on the B-theses:** All three B's converge on conversion models on rented compute for our agencies. Comfort. And if we sell Bid, B's customers leave with it.

**Arjun (via Tomas):** Sell the business, keep licensed rights to the anonymized dataset as a sale condition.

**Mira Castell (CEO):** Victor is right that the *vocabulary* leaked; the evidence didn't. We strip the leaky claims. Facebook apps first; the phone is gated on Apple's terms, known in weeks. We price whatever action advertisers can verify. I'm deciding.

## 2. DECISION (CEO)

**Company name:** **Clearline**. Ledgerline Bid keeps its name for the sale process.
**Identity:** *The neutral clearing house that prices verified actions inside third-party apps, and pays the developers who produce them.*

**Reinvention thesis:**
- **Capability:** open application platforms (Facebook Platform, May 2007; native iPhone SDK promised for Feb 2008; Android announced) plus metered compute (EC2/S3, Hadoop).
- **Adoption:** thousands of small developers reach large audiences outside carrier decks.
- **Bottleneck:** there's no trusted way to price and pay for verified user actions across these platforms. Inventory sells at blind CPM, and incentivized traffic is unaudited.
- **Layer we own:** the auction itself, a cross-platform exchange priced per verified action (sign-up, engagement, purchase), cleared against our signed ledger with fraud scoring. It's not a tool for bidders.
- **Data:** a platform × placement × action × revenue graph that developers contribute voluntarily in exchange for payouts.
- **Next capability:** action-value prediction per placement, then context-aware (including location) matching as phones expose it.

**KILL:** search bid management as our identity and growth line (the sale process runs); the E3 pay-per-action roadmap for *search* (the engines own that auction); new desktop-analytics features; the small-merchant tier (already dead).

**KEEP:** signed event-log infrastructure (the clearing ledger); fraud models; the optimization team; licensed rights to the cross-engine dataset; agency relationships; the frozen fax corpus.

**Funded option (25% of new-bet burn, per [E1]/[E3] underweighting):** *Hosted prediction on rented compute*: conversion-propensity and per-impression valuation models on EC2/Hadoop, with held-out evaluation. The gate is *measured lift versus the buyer's own models* by Q4 2008, never whether an exchange owner will pay ([E2]). No 15-month gate ([E3]).

**Wedge product:** *Clearline SDK + Exchange*. A free drop-in event-counting library for Facebook apps, then the mobile Web and native phone SDKs where terms allow. It has an app-to-app promotion exchange priced per verified action, with fraud filtering. Developers get a revenue share.

**First customer:** 20 design-partner Facebook developers who are both advertisers and publishers, signed by April 2008. Then 5 agency clients running branded apps as the first outside advertisers.

**3-year plan:**
- **2008:** hire 3 client/mobile engineers. Exchange live on Facebook by Q2. Read the Apple and Android terms, and ship to each platform only if third-party networking and ad libraries are permitted. Run the Bid sale process in H1.
- **2009:** 1,000 integrated apps. $5M annualized gross spend. Open to outside advertisers. Decide on the option.
- **2010:** $20M gross spend. Cross-platform action-value models become the pricing engine. Raise only on traction.

**Capital need:** ~$12M cash; the new bet is capped at ≤20 people and ~$5M/yr. Bid sale with a ~$40M floor. Below the floor, Bid is kept as a cash engine and the bet is capped at $4M/yr. No 2008 raise; the credit market is treated as closed.

**Kill criteria** (pre-committed, no waivers):
1. If Facebook bans or taxes third-party action-priced ad units *and* Apple bars third-party ad/analytics libraries by June 2008, exit the exchange within 90 days and fold the ledger into the option.
2. Fewer than 150 integrated apps by Sep 2008.
3. If a platform owner launches a first-party app-ad auction before we reach $2M annualized gross spend, retreat to a cross-platform fraud and attribution tier only.
4. If fraud-adjusted actions show no better advertiser ROI than CPM buys across two quarters, the thesis is falsified.
5. Runway must never fall below 18 months. If it's breached, cut the bet to 10 people.

**Org changes:** Jonah Reyes becomes GM, Clearline Exchange. Priya Nair becomes VP Engineering with 3 client/mobile hires. Leo Mbeki becomes Head of Developer Platform (SDK, design partners, platform terms). Dr. Kofi Mensah becomes Head of Action Verification & Fraud. Hana Kowalski leads the prediction option with Dr. Elise Laurent as economic owner. Carmen Ortiz leads developer and advertiser GTM. Arjun Mehta owns the Bid sale and the data-licence carve-out. Victor Hale gets a standing **Vocabulary Audit** duty: any memo term with no pre-era usage must be flagged.

**Dissent log:**
- **Victor Hale:** the convergence is reveal-herding. Mobile ads have a decade of failures, and incumbents (AdMob, Millennial) are already there. He would lead with the prediction option. He won the vocabulary purge and Facebook-first sequencing.
- **Dr. Elise Laurent (via Tomas):** social inventory is low-intent, and Facebook will own its auction. Cloud prediction should lead.
- **Hana Kowalski (via Dev):** the neutral cross-exchange display buyer is the real durable layer. Dev says 25% underfunds it.
- **Carmen Ortiz:** concurs, but wants Facebook-only focus with no phone spend until Apple's distribution terms are proven.
