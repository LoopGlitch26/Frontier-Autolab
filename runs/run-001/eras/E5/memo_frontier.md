# Frontier Research Memo: Era E5 (January 2014)
*Public sources before 1 Jan 2014 only. Written without coordinating with other departments.*

## Meeting transcript

**Dr. Yuki Harada (Head of Frontier Research):** This is the third briefing in a row that lists GPU-trained neural networks. Speech error rates fell at three separate labs, and convolutional networks won ImageNet in 2012 and again in 2013. Google, Facebook and DeepMind are hiring the researchers. It's no longer a weak signal. It's a documented curve with a talent shortage attached, and the shortage is where a small company can get in.

**Samuel Brandt (Technology Historian):** Careful. We were just told we missed this curve, and [E4] calls fast consensus after a reveal a leakage alarm. The history has to stand on its own, and it partly does. When statistical speech recognition replaced rule-based systems in the late 1980s, the value went to whoever owned the corpus and distribution, not the algorithm. Yuki's curve is real, but selling the algorithm ends up as a component business.

**Ines Varga (Futurist & Scenario Planner):** I have three scenarios. *Concentration:* the largest platforms hire nearly all the researchers and give recognition away to attract developers. *Diffusion:* open papers and cheap GPUs make it a standard skill within three to four years, and value goes to whoever holds domain data. *Stall:* the gains stay in speech and images, and the field cools as it did around 1995. My indicators: open-source GPU training libraries appearing, the big labs continuing to publish, and benchmark error still falling in 2014. And not one curve only: messaging apps are becoming platforms, and Bitcoin is a public signed ledger, which is our core skill.

**Dr. Kofi Mensah (Research Scientist, Measurement):** What can't anyone measure yet? First, the content of a photo or voice clip. A billion camera phones a year produce images no ranking system, fraud filter or advertiser can read. Second, trust between strangers. Ride and room marketplaces and card payments need verification of people and actions that isn't tied to one platform, and our fraud models and ledger are the nearest thing we have. After Snowden and the EU draft regulation, any referee must be privacy-preserving by design, not retrofitted.

**Samuel:** Kofi's second gap is familiar ground for us, which makes me suspicious of it. It is the adjacent layer again ([E2]).

**Kofi:** Adjacency isn't disqualifying ([E3] revised). What counts is whether the market is pulling for it.

## DEPARTMENT RECOMMENDATION

### Thesis A (lead): Learned perception for the camera-phone era
- **Capability:** GPU-trained deep networks reach usable accuracy on images and speech → **Adoption:** a billion phones a year generate photos and voice that apps can't interpret → **Bottleneck:** scarce researchers, GPU training know-how and *labelled* domain data → **Layer we own:** a hosted recognition service plus a labelling-and-correction pipeline for app developers (tagging, moderation, product and document recognition) → **Data:** developer-contributed corrections: labelled images and utterances in narrow commercial domains → **Next capability:** recognition that uses context (location, time, the user's actions), then models small enough to run on the phone itself.
- **Why now:** the benchmark gap is public, GPUs rent hourly on AWS, and few people outside the big labs can train these models.
- **Wedge:** image moderation and tagging for our SDK apps, which already trust our code; moderation is measurable and already paid for.
- **First customer:** a user-generated-photo app or marketplace in our SDK base that pays today for manual moderation.
- **Makes obsolete:** hand-engineered vision, manual review queues, and our own hand-built fraud features.
- **Hire:** 3–4 neural-network researchers. [E2] says hiring the team *is* the thesis.

### Thesis B (reserved-slot alternate): The neutral trust referee for person-to-person markets
- **Capability:** phone identity signals plus learned fraud scoring → **Adoption:** marketplaces for rides, rooms, delivery and payments → **Bottleneck:** no shared, privacy-compliant way to verify a stranger or a transaction across platforms → **Layer:** a cross-marketplace risk-scoring and verification service → **Data:** a consented graph of outcomes (fraud, chargebacks, disputes) → **Next capability:** portable reputation that users carry between platforms.
- **Why now:** marketplace fraud is growing faster than in-house teams.
- **Wedge / first customer:** chargeback scoring for mid-size marketplaces on Stripe or Square.
- **Makes obsolete:** our ad-network exchange as the company's identity. Install-ad arbitrage is going back to the platform owners.

### Playbook lessons applied
- **[E4] Reserved slot outside our own data:** Thesis A uses curves and data we don't have yet. We are not giving the slot to our install ledger a third time.
- **[E1] Right science and the right decade are separate bets:** the gate is falling benchmark error *on our customers' data* by Q4 2014, not a pitch deck.
- **[E3] Date the option against the incumbent's ship date:** Google and Facebook may offer recognition free. So we launch in narrow commercial domains within 9 months and don't wait on a long gate.
- **[E4] Own the referee:** applied in Thesis B, but we argue against it as a reflex; it is the last reveal's obvious lesson.
- **[E4] Unanimity is a leakage alarm:** if every department lands on neural networks plus attribution, weight the dissents heavily.

### What we are most uncertain about
Whether the gains generalize beyond speech and ImageNet or stall. Whether the big labs' hiring leaves any researchers for a 120-person company. Whether perception becomes a free platform feature before domain data becomes a moat (Samuel's risk). Watchlist, unfunded: messaging platforms, public ledgers, gene editing.
