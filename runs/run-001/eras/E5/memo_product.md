# E5 Memo: Product & Engineering (January 2014)

## Transcript

**Priya Nair, VP Engineering:** Here's the inventory. We have 120 people and $38M. The exchange is at breakeven, but Facebook's install ads are squeezing its margins. We have an SDK in a few thousand apps, a signed action ledger, fraud models, and a client team that can ship on both iOS and Android. What we don't have: anyone who has trained a deep network, and no GPUs. A new bet can take 15–20 people and about $6M a year without touching the 18-month floor.

**Hana Kowalski, Principal Infrastructure Engineer:** I'll say the uncomfortable thing first. The last reveal named neural networks as the curve we left unfunded, so a pivot to them now looks like we're following the answer key. But the evidence is in this briefing and doesn't depend on any reveal. Convnets on GPUs cut ImageNet error sharply in 2012. Speech error rates fell at three companies at once. The 2013 ImageNet leaders included a tiny academic team. Code for this is public (cuda-convnet, Theano, Torch). What's scarce is people who can train these models and GPU capacity on demand. Only Google, Microsoft and Facebook have both. Every other app developer has a billion phone cameras sending photos and no way to understand what's in them.

**Jonah Reyes, GM, Clearline Exchange:** A capability isn't a product, Hana. Who pays, and for what? And when a curve is this public, [E3] tells us to date the option against the incumbent's ship date. Google can put image labeling behind an API whenever it chooses. My wedge is closer to our assets. On-demand marketplaces, payment startups and messaging apps all have the fraud problem we solved for installs: fake accounts, stolen cards, promo abuse, collusion between drivers and riders. [E4] says that if you can't own the auction, own the referee. The referee is worth more when every marketplace, and not just every ad network, needs one.

**Leo Mbeki, Head of Developer Ecosystem:** Both of these reach customers through developers, and that's our real distribution. Developers already put our SDK in their apps. One more call that returns "what is in this photo" or "how risky is this signup" is an easy sale. I'd push against Jonah on one point, though. Fraud scoring for marketplaces is a crowded, adjacent layer, which is exactly what [E2] warns about. It also doesn't use any curve outside our own data, and [E4] says the reserved slot must. I'm backing Hana's thesis to lead. I'd also keep a small tripwire on messaging apps as the next platform. WeChat already runs payments and official accounts inside a chat app.

**Priya:** On buildability: we can't hire ten deep-learning researchers, because the big labs are buying them. We can hire three or four strong applied people plus GPU engineers and ship models trained on ImageNet-class data, then fine-tuned per customer. Rented GPUs are immature, so we'd own a small cluster. The exchange should be sold while the IPO window is open and before tapering ([E4] credit calendar).

**Jonah:** I'll concede the sale. I dissent on selling the attribution ledger with it. It's the referee asset, and it pays.

## DEPARTMENT RECOMMENDATION

### Thesis A (lead; Hana, Priya, Leo): "Perception as a service for every app"
- **Capability:** GPU-trained deep networks now beat hand-built features in vision and speech.
- **Adoption:** billions of phone photos and a growing volume of voice and video in apps. Developers want search, tagging, moderation and product matching.
- **Bottleneck:** training talent and GPU operations are held by 3–4 giants, and nobody sells trained models to everyone else.
- **Layer we own:** a hosted recognition API (tag, match, moderate) with customer fine-tuning, delivered through our existing SDK.
- **Data:** customer-labeled corrections and domain datasets (retail catalogs, UGC moderation). Each customer's labels improve the shared base models.
- **Next capability:** video and speech understanding, then smaller on-device models as phone chips improve.
- **Why now:** the error-rate break is 2012–13, and outside developers still can't buy it. **Wedge:** moderation and auto-tagging for photo-heavy apps in our SDK base. **First customer:** 10 UGC and photo apps already integrated with us, plus 3 retail apps with catalogs. **Makes obsolete:** hand-labeling services, first-generation keypoint image-matching vendors, and our own install exchange.

### Thesis B (Jonah): "The neutral trust referee for phone-native marketplaces"
- **Capability:** mobile identity signals plus our fraud models and signed ledger.
- **Adoption:** marketplaces, payments and install buying all run through phones.
- **Bottleneck:** there's no shared, cross-company view of fake accounts and abuse.
- **Layer we own:** a cross-platform risk score and attribution referee that marketplaces and platforms accept.
- **Data:** device × account × action × outcome graph shared across participants.
- **Next capability:** learned risk models, trained on the Thesis A stack.
- **Why now:** marketplaces and payment startups are scaling faster than their fraud teams. **Wedge:** promo-abuse and fake-account scoring. **First customer:** 5 ride, delivery and payment startups. **Makes obsolete:** the exchange; in-house rules engines.

### Playbook applied
- [E4] Reserved slot goes to a curve outside our data: this is Thesis A.
- [E2] Hiring the team you lack *is* the thesis.
- [E4] Run the sale on the credit calendar: sell the exchange in H1 2014.
- [E4] Own the referee: Thesis B, and the argument for keeping the ledger.
- [E3] Date the option against the incumbent's ship date: ship the API within 9 months, because a giant can release a free one at any time.
- **Argued against:** [E4] "unanimity is a leakage alarm." We aren't unanimous. Jonah dissents, and Hana named the leakage risk on the record.

### Most uncertain
Whether Google or Microsoft commoditizes perception APIs before we build a data moat ([E3] auction-owner risk, applied to models). Whether customer labels compound or stay siloed. Whether we can hire deep-learning talent against the big labs' offers. What privacy regulation after Snowden does to device-level signals, which affects Thesis B.
