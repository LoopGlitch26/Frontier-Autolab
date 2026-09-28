# Market & Capital Memo: Era E5 (January 2014)
*Carmen Ortiz (Head of GTM), Arjun Mehta (CFO & Capital Strategist), Dr. Elise Laurent (Chief Economist). Sources limited to facts public before 1 Jan 2014.*

## Meeting transcript

**Carmen Ortiz (Head of GTM):** Who pays us today is app advertisers buying installs, and that budget is moving to Facebook, Twitter/MoPub and Google, who all run their own auctions now. The budget that is growing *and* unowned is somewhere else: the new phone marketplaces (Uber, Lyft, Airbnb, delivery apps) and card-on-phone merchants on Square and Stripe. They onboard millions of strangers, pay out promo credits, and eat chargebacks. Their fraud losses hit the P&L, not a marketing line, so no ad auction can bundle the fix. Sell our fraud models to risk teams, not media buyers.

**Dr. Elise Laurent (Chief Economist):** Careful. Install attribution is the obvious refuge, but several vendors do it and platforms now certify partners. Certification makes the referee a flat-priced utility ([E2 note]). Where do margins go in 2014? Toward whoever owns scarce inputs. For now that means GPU compute plus labeled data plus the few people who can train deep networks. The DNNresearch purchase and the LeCun hire are talent price signals.

**Carmen:** Who signs the PO for deep learning?

**Elise:** Anyone paying humans to look at pictures. Photo and dating apps run human moderation queues. Price per image, below the queue's cost: an existing budget ([E1]) that doesn't anchor us to old architecture.

**Arjun Mehta (CFO):** Capital first. We have ~$38M, ~120 people, and credible $100–250M acquisition interest. Tapering starts this month, 2013 was the best tech IPO year since 2000, and there's now a word for $1B startups. That's a financing peak ([E2]). I propose selling the performance exchange this year. It's in year six of a 3–4-year window for third-party auctions ([E4]), and consolidators are paying now. We keep the ledger, fraud models and SDK footprint as sale conditions, as with the search dataset in 2008 ([E4] credit calendar).

**Carmen:** Selling the exchange also sells the advertiser relationships that fund attribution. I'd sell it, but only after we have ten risk-team contracts signed.

**Arjun:** The window sets the deadline, not the contracts. Launch in H1.

**Elise:** And a cross-app device graph is exactly what the post-Snowden EU regulation targets. Build it privacy-first (hashed identifiers, per-client keys) or it gets killed.

## DEPARTMENT RECOMMENDATION

### Thesis A: the neutral trust network for phone marketplaces and commerce
- **Capability → adoption → bottleneck → layer → data → next capability:** cheap smartphones, card APIs (Stripe, Square) and advertising identifiers → marketplaces and apps sign up millions of anonymous users and pay them credits → trust between strangers breaks down (fake accounts, stolen cards, promo abuse, fake installs), and each app fights it alone → **we own the cross-app risk score**, a neutral consortium no single platform or marketplace can operate for its rivals → a device × account × event × outcome (chargeback, refund, ban) graph, contributed voluntarily in exchange for better scores → real-time risk pricing, then loss guarantees and underwriting for marketplaces.
- **Why now:** marketplace volume is funded and growing, and fraud losses scale with it. No platform owner runs a cross-marketplace risk auction to absorb us into ([E3]).
- **Wedge:** a risk-scoring API reusing our SDK signals and signed ledger, priced per decision.
- **First customer:** 5 mid-size on-demand and marketplace apps already in our SDK base, sold to their risk and payments leads.
- **Makes obsolete:** per-app rules engines and manual review teams, plus our own install exchange and, in time, attribution as a standalone product.

### Thesis B (reserved slot, curve outside our data, [E4]): learned perception as a metered service
- **Chain:** deep networks on GPUs cut speech and image error rates → app makers want to understand uploaded photos, voice and text → human review is slow and costly → **we own a per-call perception API** on rented GPUs, starting with moderation → labeled judgments from customer feedback loops → general visual and speech understanding for apps (tagging, search, handwriting from the frozen corpus).
- **Why now:** ImageNet 2012, speech results and GPU rental on cloud platforms.
- **Wedge:** image moderation for photo, dating and social apps, priced below the human-queue cost.
- **First customer:** 3 photo and dating apps from our developer base.
- **Makes obsolete:** outsourced moderation queues, and our own hand-built fraud features, which learned features will replace.

### Capital recommendation
Sell the performance exchange in 2014 while multiples are high, keeping the ledger, fraud models, SDK and data rights. Fund A at ≤20 people and B at 25–30% of new-bet burn, gated on measured accuracy against human moderators by Q4 2014. The gate is never whether an incumbent will pay ([E2]).

### Playbook applied or argued
[E4] own the referee, but we argue against attribution as the thesis (crowded, becoming a certified utility). Also applied: [E2], [E4] credit calendar and reserved slot, [E3], [E1].

### Most uncertain about
1. Whether marketplace fraud budgets are big enough, or whether payment processors bundle risk scoring for free (the [E3] pattern again, with Stripe or Square as the auction owner).
2. Whether Google and Facebook release perception capabilities free to developers, collapsing B's price.
3. Whether the EU regulation outlaws cross-app device graphs.
4. Hindsight risk: Thesis B tracks the curve the E4 reveal named. We ask the Red Team to test whether the moderation wedge stands on January 2014 evidence alone.
