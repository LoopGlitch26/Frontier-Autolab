# Market & Capital Memo: Era E4 (January 2008)
*Attendees: Carmen Ortiz (Head of GTM), Arjun Mehta (CFO & Capital Strategist), Dr. Elise Laurent (Chief Economist). Sources are limited to what was public before 1 Jan 2008.*

## Transcript

**Carmen Ortiz, Head of Go-To-Market:** Our agencies pay us because the engines grade their own homework, but Google now owns the free analytics, DoubleClick and the bid API. Each quarter we're a line item on their platform. Where I see unmet demand is Facebook Platform developers. Some of those apps have millions of users and earn almost nothing, because nobody runs a performance auction for that inventory. The iPhone SDK arrives next month, and the same gap will open there. Those developers are the first people who would pay us, and they'd pay in revenue share, not licenses.

**Dr. Elise Laurent, Chief Economist:** Carmen, the [E3] lesson is that the auction owner takes the value, and on Facebook the auction owner will be Facebook. Once Beacon calms down, it will build its own ad system. I care more about a cost curve. S3 and EC2 turned servers into a metered utility, and Hadoop turned log processing into commodity software. With credit tightening, CFOs will cut capital spending before operating spending, so renting compute is the recession-proof purchase. Margins will pool at the layer that turns rented compute into answers for businesses that can't hire a Yahoo-sized grid team. We already run that for ourselves: a multi-year event log of queries, clicks and conversions.

**Arjun Mehta, CFO & Capital Strategist:** You're both skipping the fact that the financing window is closing. Bear's funds, Northern Rock, a Fed cutting 100 basis points: 2008 will not be kind to Series E rounds. We have ~$12M, burn near breakeven, and a residual preference overhang. The DoubleClick, aQuantive and Right Media deals set peak prices for ad-tech assets. My proposal is that we sell Ledgerline Bid, or put it up for auction, in H1 2008 while agency holding companies still have cash. Then we'd fund whatever comes next from those proceeds, not from a down round. [E2] says a bubble is a financing event, and this is the tail of one.

**Carmen:** Sell the business that pays our salaries before the replacement has a customer?

**Arjun:** Run a process, not a fire sale. If bids come in below ~$40M we keep Bid as a cash engine and cap the new bet at ~$4M/yr. Above that, we sell. Either way the decision is made by a number, not by nostalgia.

**Elise:** One more point for Carmen. Social-app inventory is enormous but low-intent. [E2] says money pools where intent is priced. A poke is not a query. CPMs on that inventory are cents.

**Carmen:** That's why it has to be performance-priced. Installs, sign-ups and virtual-goods purchases are intent. Our conversion ledger is the one asset that prices them.

## DEPARTMENT RECOMMENDATION

### Thesis A: Run the performance auction for app inventory (Carmen lead; Arjun supports)
- **Capability → adoption → bottleneck → layer → data → next:** Open app platforms (Facebook Platform, iPhone SDK in Feb 2008, Android announced) → tens of thousands of small developers reach millions of users → they can't monetize or acquire users efficiently, and there's no neutral auction for cost-per-install or cost-per-action → **we run the auction**, not a tool for bidders: an ad exchange with a signed conversion ledger → install × action × revenue data by app → next: user-acquisition pricing and lifetime-value prediction per user segment.
- **Why now:** platforms are open, but their owners have not shipped an ad system for third-party apps. Recession pushes advertisers toward pay-for-results.
- **Wedge:** a cost-per-install exchange for Facebook apps (apps advertising apps), with click-fraud scoring built in.
- **First customer:** the top 50 Facebook app developers, who are both buyers and sellers.
- **Obsoletes:** our own search bid tool (engine APIs already make it a commodity), and banner networks on social inventory.

### Thesis B: The analytics utility on rented compute (Elise lead)
- **Capability → adoption → bottleneck → layer → data → next:** metered compute and storage (EC2/S3) + open MapReduce (Hadoop) → web and commerce firms generate logs faster than warehouses can absorb them → they lack cluster engineers, and on-premises warehouses are expensive capex in a credit crunch → **a hosted, metered log-processing and analytics service** running on rented infrastructure → cross-customer benchmarks, voluntarily contributed → next: hosted predictive models such as churn, fraud and conversion propensity.
- **Why now:** rented compute is cheap, capex budgets are about to be cut, and Hadoop skills are scarce outside Yahoo.
- **Wedge:** "send us your click and order logs, get answers in hours," billed per job. It starts with our own agency and retailer customers.
- **First customer:** mid-size e-commerce and ad-tech firms that already send us logs.
- **Obsoletes:** our on-premises reporting stack, and the licensed data-warehouse appliance for mid-market buyers.

### Playbook lessons applied
- **[E3] Auction owner absorbs measurement:** this drives A. We become the auction owner instead of renting from one. Elise argues it *against* A, since the platform owner will run the auction eventually.
- **[E3] Date the option against the incumbent's ship date:** Facebook and Apple could ship ad systems in 12–24 months. A must launch in 2008 or not at all, so there is no long evidence gate.
- **[E3] Reserve a slot for what the Playbook can't see:** that's B. Cloud was the weak signal we ignored in E3.
- **[E3] Suspect comfort, don't reject it:** B uses our existing log infrastructure. We judge it on pull, not identity.
- **[E2] Bubble is a financing event:** drives Arjun's sale process for Bid.
- **Argued against: [E2] Money pools where intent is priced**, in its strict form. Elise holds to it; Carmen argues that actions inside apps are a new form of priced intent.

### Capital plan (Arjun)
Run a sale process for Ledgerline Bid in H1 2008 with a ~$40M floor. Cap the new bet at ≤20 people and ~$4M/yr. We don't raise in 2008 unless proceeds fall short. Pre-committed kill criterion for A: if Facebook or Apple launches a first-party ad auction for apps before we reach $2M in annual gross spend, we fold the ledger into B and exit A.

### Department split
Carmen favors A and Elise favors B. Arjun favors A as the thesis and B as the funded option (25%, not 15%, per the [E1]/[E3] underweighting pattern). Consolidated vote: **A as the lead, B as a funded option, and the Bid sale process begins now.**

### What we're most uncertain about
1. Whether platform owners will *allow* a third-party auction on their inventory, or tax or ban it. This is the E3 rented-land risk again.
2. How deep the credit crisis gets. Ad budgets and acquisition cash could both freeze in 2008.
3. Whether social or app actions monetize like search intent at all. This is unmeasured.
