# Board Decision: Era E3 (January 2002)
*Attendees: Castell (CEO), Rao (CTO), Okafor (Chief Scientist), Weil (CSO), Hale (Red Team). Sources are limited to what was public before 1 Jan 2002.*

## 1. Transcript highlights

**Victor Hale (Red Team):** All three memos agree because the Playbook told them to. "Money pools where intent is priced" is the last war, and overfitting to 1996–2001 would look exactly like this.

**Victor, on Frontier's "Intent Everywhere":** Matching paid listings to the content of any page smells like memory of the future. In 2002 contextual advertising is a banner-era idea with a bad record, and the portals have their search inventory to fill. Overture already syndicates to partners, and firms like Applied Semantics sell concept matching. We'd be a late entrant with no publisher network.

**Dr. Lena Okafor:** The capability is real. Text classifiers are good enough to tell what a page is about. Whether a page read converts like a typed query is unmeasured, and I'd put it under 50%. That's why Kofi's half matters more than Yuki's. Measurement is useful from the first customer on.

**Victor, on Market's "priced intent for business sourcing":** Two problems. First, the hub-and-spoke lesson cuts against you: your "trust signal" is receipted history from 20 buyer hubs, and those buyers own it. Second, Alibaba and Global Sources already run the export side, and procurement is still done through relationships and trade shows. By your own memo, where buyers search is the biggest unknown.

**Tomas Weil:** Sourcing intent is real, but it means building a two-sided marketplace in a recession with $15M. Merchants already pay for clicks.

**Victor, on Product's "seller's side of intent":** It's a feature on someone else's platform. Overture and Google can ship conversion tracking in a quarter. The engines can throttle our access whenever they like.

**Dev Anand Rao (CTO):** Each engine can report on its own channel, but only a neutral party sees all of them plus the order. The signed log and multi-tenant event system we already run for EDI. What we lack is a ranking and bidding team. We hire two or three people this quarter, which is cheap in a bust.

**Victor:** And Hana's hosted-applications thesis?

**Dev:** Salesforce.com and NetLedger lead it.

**Victor, on Arjun's trade finance:** Third era asking. The data is mandated invoices, which means the buyer's graph.

**Mira Castell (CEO):** Then here's what the room agrees on. The neutral measurement ledger shows up in two memos, Frontier's wedge and Product's thesis. It uses signed receipts while pointing at a market we've never served. Matching is the upside option, gated on evidence. Sourcing waits. I'm deciding.

## 2. DECISION (CEO)

**Company name:** **Ledgerline**. The Manifest name stays with the Web-EDI utility, which becomes a division and a saleable asset.
**Identity:** *The neutral, receipted ledger that proves which paid click became a sale, across every channel.*

**Reinvention thesis:**
- **Capability:** pay-per-click auctions (Overture, AdWords) and marketplace listings (eBay) price intent at scale. Commodity Linux clusters make logging every click and order cheap, and statistical classifiers work.
- **Adoption:** advertisers are moving budgets from banners to pay-per-click, and hundreds of thousands of merchants now buy clicks.
- **Bottleneck:** nobody measures across channels whether a click was real and whether it led to a sale. The engines grade their own results.
- **Layer we own:** a neutral measurement and optimization layer. It includes an order-page tag, a signed click-to-order log, cross-channel conversion reporting and then bid management.
- **Data:** a query × channel × click × order × revenue graph that merchants contribute *voluntarily*. No single engine sees it.
- **Next capability:** automated bidding on conversion value, learned click-quality scoring, contextual placement priced on proven conversions, and eventually pay-per-action.

**KILL:**
- Web-EDI as the growth thesis. We stop investing in features for it. Manifest Exchange runs for cash, with a sale process opening in 2003.
- The supplier-scoring and trade-finance roadmap, including Market Thesis B.
- Hosted business applications (Product B).
- Sourcing marketplace (Market A); kept only as an indicator Carmen tracks.
- Flat-fee thinking. Ledgerline prices by tracked spend.

**KEEP:**
- Signing, receipt and audit infrastructure, which becomes the tamper-evident log.
- Multi-tenant operations know-how.
- Recurring cash from ~5,000 suppliers; the EDI/XML team moves to feed formats and the API.
- About 200 suppliers who want direct buyers, as pilot merchants.
- Kofi's 1997 click-ranking result and dataset.
- Frozen handwriting/fax corpus (no cost).

**Funded option (15% of Ledgerline burn):** Yuki Harada and one hire run a **contextual-matching research option** that places Ledgerline merchants' listings on partner content pages. Per [E2], it is promoted on *measured conversion lift* compared with search clicks, never on whether a portal or engine will pay. If conversion reaches ≥50% of the search baseline by Q2 2003, it gets a full team and we sell to publishers directly.

**Wedge product:** *Ledgerline Track*, a hosted service at $50–300/month by tracked spend with a free tier. Order-page tag, cross-channel reports (Overture, Google, eBay), signed conversion log, open API. Beta Q3 2002.

**First customer:** mid-size online retailers spending $1K+/month on paid listings, with 3 design partners by Q2 2002.

**3-year plan:**
- **2002:** hire 2–3 ranking/bidding engineers. Get Track into beta with 50 merchants and to GA by Q4. Cut Manifest to ~40 people at breakeven.
- **2003:** 1,000 paying merchants. Launch bid management (Ledgerline Bid). Make the contextual option's promote-or-kill call. Sell Manifest Exchange or spin it out, with a target of $10–15M.
- **2004:** $6M+ ARR. Automated bidding on conversion value. Agency API program. Evaluate pay-per-action brokering.

**Capital need:** No priced round in 2002. We start with ~$15M cash. Ledgerline stays under 20 people at ~$4–5M/yr, and Manifest runs at breakeven. That gives ~36 months of runway, plus proceeds from the Manifest sale. We raise only after ≥$2M ARR, restructuring preferences then.

**Kill criteria** (pre-committed; the board may not waive them):
1. Fewer than 150 paying merchants by Sep 2003 → cut to bid-tooling only or sell to an agency.
2. **Bridge-death date:** if two major engines ship free *cross-channel* conversion reporting, or ban third-party bid access, before we reach $3M ARR → sell to an agency holding company or an engine.
3. Monthly merchant churn above 5% for two consecutive quarters.
4. Manifest drops below breakeven for two quarters → accelerate the sale, whatever the price.
5. The contextual option fails the lift gate by Q2 2003 → kill it with no extension.

**Org changes:**
- **Jonah Reyes** becomes GM of Ledgerline. **Priya Nair** becomes VP Engineering, Ledgerline, and hires the ranking/bidding lead. The hire *is* the thesis.
- **Dr. Kofi Mensah** becomes **Head of Measurement & Click Quality** (the old tripwire is now the core product).
- **Dr. Yuki Harada** also leads the contextual-matching option.
- **Hana Kowalski** becomes **GM, Manifest Exchange**, running it for cash and preparing it for sale.
- **Leo Mbeki** becomes **Head of Developer & Agency Program**.
- **Carmen Ortiz** takes GTM to merchants and keeps Services Governor duty (≤20%).
- **Arjun Mehta** owns the Manifest sale and the preference restructuring.

**Dissent log:**
- **Victor Hale:** He sees this as a feature on rented land, and thinks the Playbook herded us to it. He won criterion #2 and the no-waiver rule.
- **Dr. Elise Laurent and Carmen Ortiz (via Tomas):** B2B sourcing intent is the larger unpriced pool, and China's WTO entry makes it urgent. Consumer clicks are the crowded half.
- **Arjun Mehta (via Tomas):** Killing trade finance permanently throws away the one asset buyers can't copy, which is receipted invoices.
- **Hana Kowalski (via Dev):** Hosted applications are the durable layer. Measurement tools depend on a platform we don't control.
- **Dr. Yuki Harada (via Lena):** Contextual matching is the bigger prize and deserves 30%, not 15%. That's the same underweighting mistake as E1 and E2.
