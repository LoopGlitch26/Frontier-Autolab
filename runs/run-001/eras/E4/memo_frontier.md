# Frontier Research Memo: Era E4 (January 2008)
*Department: Frontier Research. Sources are limited to what was public before 1 Jan 2008.*

## Meeting transcript (condensed)

**Dr. Yuki Harada, Head of Frontier Research:** Two curves are bending. The phone is becoming a real computer: the iPhone has a full browser, a native SDK is promised for February, and Android is an open stack. And compute is now rentable: EC2, S3 and Hadoop let ten people run learning jobs only Google could run in 2004. Neither curve runs through our desktop click data.

**Samuel Brandt, Technology Historian:** The iPhone looks like 1984: a new interface, a closed maker, no third-party software yet. Value went to whoever owned developer distribution. And we have been the tool on rented land three eras running. If we go mobile as "conversion tracking," the platform owner bundles it free, as Google did with Analytics. We have to run the auction.

**Ines Varga, Futurist & Scenario Planner:** Three scenarios for 2008–2013. (1) *Pocket Web* (40%): SDKs open, smartphones go mass-market by ~2011, and an ad-and-commerce economy grows around phone software. (2) *Credit winter* (35%): recession; venture dries up, budgets shift to measurable performance, rented compute beats capex. (3) *Walled gardens* (25%): carriers keep mobile distribution; action stays in desktop social networks. Indicators: iPhone SDK terms, first Android device, Facebook Platform usage, EC2 leaving beta, credit spreads. Scenarios 1 and 2 can co-occur.

**Dr. Kofi Mensah, Head of Measurement & Click Quality:** Two things can't be measured yet. First, what happens after a tap on a phone: no cookies, carriers strip identifiers, nobody ties a mobile ad to an install or purchase. Whoever proves the conversion sets the price. Second, which prediction model is actually better. The Netflix Prize shows that a held-out test set gets thousands of teams improving one number; retailers lack that discipline.

**Harada:** Kofi, measurement is your comfort zone again.

**Mensah:** This time it's the price key inside an auction *we* run, not a report sold to bidders.

**Brandt:** Good. That's the first time in four eras we've proposed owning the auction.

## DEPARTMENT RECOMMENDATION

### Thesis A (preferred): Pocket Intent, a performance ad exchange for phone software and the mobile Web
- **Capability:** smartphones with full browsers and third-party SDKs (iPhone SDK in Feb 2008, Android), plus data plans getting cheaper.
- **Adoption:** developers will ship thousands of small apps needing users and revenue; advertisers follow, but want proof.
- **Bottleneck:** no cross-platform attribution of installs or purchases to mobile ads, so inventory sells at blind CPM.
- **Layer we own:** a cross-platform SDK plus an auction priced on *measured actions* (cost per install or purchase). We run the auction.
- **Data:** a device-context × placement × action × revenue graph that developers contribute voluntarily in exchange for monetization.
- **Next capability:** location- and context-aware matching, then payments and commerce inside apps.
- **Why now:** SDKs arrive this quarter; developers pick monetization partners in year one.
- **Wedge:** a free install/event-counting SDK plus a house network swapping installs between developers.
- **First customer:** independent iPhone and Symbian game and utility developers, with 10 design partners at SDK launch.
- **Makes obsolete:** carrier-deck merchandising, blind mobile CPM networks, and **our own desktop bid business** (becomes cash cow and advertiser source).

### Thesis B (reserved slot per [E3]): Prediction Utility, conversion and recommendation models trained on rented compute
- **Capability:** EC2, S3 and Hadoop make large-scale training cheap and elastic. Statistical learning (boosting, collaborative filtering) is proven.
- **Adoption:** retailers and agencies drown in logs they can't model.
- **Bottleneck:** mid-size firms can't staff ML teams or run held-out evaluation.
- **Layer we own:** a hosted prediction API with continuous evaluation against held-out data (a "private Netflix Prize" for each customer).
- **Data:** cross-customer model-performance benchmarks and pooled conversion features.
- **Next capability:** automated decisioning (price, bid and recommendation) across channels.
- **Why now:** capex-free compute arrives just as a recession forces spend onto performance.
- **Wedge:** a conversion-propensity score for our existing agency clients, run on EC2.
- **First customer:** our top 20 agency accounts.
- **Makes obsolete:** our rule-based bid rules, and in-house analytics teams at mid-size retailers.

### Playbook lessons applied
- **[E3] Auction owner absorbs the measurement:** this is why Thesis A runs its own exchange instead of selling mobile analytics to bidders.
- **[E3] Date the option against the incumbent's ship date:** Google owns Android and DoubleClick and can ship mobile ads in 12–24 months. Launch with the SDK; no lift gate.
- **[E1] Pipe, then traffic, then index:** mobile is at "traffic"; launch early enough to be the index when it arrives.
- **[E2] Suspect comfort (revised in E3):** Thesis B is comfort; kept for market pull and because it funds the core.
- **[E3] Reserve a slot the Playbook can't see:** Thesis B (rented compute). Weak signals still unaddressed: Facebook Platform social apps, sequencing costs, the multilayer-network revival.

### What we are most uncertain about
1. **Distribution terms.** Apple may bar third-party ad SDKs or control distribution; one February policy could kill Thesis A. Kill trigger: if so, pivot to Android and mobile Web within 60 days.
2. **Timing of the mass market.** The iPhone sold in the low millions on 2G. If the Pocket Web slips to 2012, our ~$12M runs out first.
3. **Credit.** A deep recession could close fundraising; Thesis B is the hedge.
