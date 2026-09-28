# E4 Memo: Product & Engineering (January 2008)

## Transcript

**Priya Nair, VP Engineering:** Here's the inventory. We have 75 people, $12M in cash, and a bid-management business at breakeven that is 60% agencies. With credit seizing and no 2008 round, the next thesis is 15–20 engineers paid for by Bid's cash. What transfers: our optimization and fraud models and a signed event pipeline. We've never shipped client software or touched a phone.

**Jonah Reyes, GM:** [E3] told us to reserve a slot for what the Playbook can't see, and the briefing is full of it. Apple opens a native iPhone SDK next month, Android has an alliance but no devices, and Facebook's Platform turned thousands of small developers into publishers within a year. In every case those developers ship something and then can't answer three questions: who installed it, who kept using it, and how to earn money from it. It's our old click-to-sale problem, asked by a new population with no incumbent tool.

**Hana Kowalski, Principal Infrastructure Engineer:** I think rented compute is the durable layer, not phones. Display is consolidating around exchanges: Right Media, DoubleClick's exchange, and Microsoft's ad network. As each impression goes to auction, buyers will need to price it individually using their conversion history. We have that history, and nobody else owns it.

**Leo Mbeki, Head of Developer Ecosystem:** Hana, the exchange owners run those auctions, and [E3] says the auction owner absorbs the tooling. Your thesis survives only for buyers spending across several exchanges. But developers are the distribution for Jonah's thesis. A free SDK that drops into iPhone, Android, BlackBerry and Facebook apps. Handset fragmentation is our bridge. I'll date its death now: it ends when one platform holds most usage and bundles free analytics.

**Priya:** Jonah, what if Apple's SDK terms prohibit third-party analytics or ad libraries, or background networking?

**Jonah:** Then we learn it in February, before spending anything. The gate is SDK terms and developer uptake, not revenue.

## DEPARTMENT RECOMMENDATION

### Thesis A (Jonah, Leo; lead): "The developer's ledger for mobile and social apps"
- **Capability:** native SDKs on full-browser smartphones (iPhone, with Android coming), Facebook Platform, and cheap rented backends (S3/EC2).
- **Adoption:** thousands of small developers are becoming app publishers on platforms that open this year, and carriers no longer control what gets installed.
- **Bottleneck:** developers have no visibility into installs, retention or in-app behavior, and no way to monetize across fragmented platforms.
- **Layer we own:** a free cross-platform SDK plus a hosted service for install and usage analytics and fraud-filtered attribution. A monetization network comes next.
- **Data:** a cross-app, cross-platform graph of device-level usage and engagement, contributed voluntarily by developers. No single platform owner sees it.
- **Next capability:** performance-priced app promotion (pay per retained install), in-app ad placement ranked by our conversion models, and later location- and context-aware targeting.
- **Why now / wedge / first customer:** the SDK opens in February, so first-wave apps set the standards. The wedge is a free analytics SDK with paid multi-platform tiers. First customers: Facebook-app and early iPhone studios, plus agency clients building branded apps.
- **Obsoletes:** carrier-portal ("on-deck") distribution and WAP measurement; for us, desktop search bid tooling becomes a cash cow.

### Thesis B (Hana, Priya): "Neutral per-impression buyer across display exchanges"
- **Capability:** exchange-based display inventory, elastic compute (EC2/Hadoop), and our conversion and fraud models.
- **Adoption:** agencies are moving display budgets to exchanges after the 2007 consolidation.
- **Bottleneck:** buyers can't price individual impressions across several exchanges using their own conversion data.
- **Layer we own:** a buying and optimization engine for agencies that bids per impression across all exchanges.
- **Data:** cross-exchange impression × conversion outcomes joined to our search graph.
- **Next capability:** audience valuation shared across search, display and mobile.
- **Why now / wedge / first customer:** the consolidation created exchanges but no neutral buyer. The wedge is cross-exchange optimization for our existing agency accounts, and the first customer is our top five agencies.
- **Obsoletes:** manual insertion-order media buying, and our search-only Bid product.

### Playbook lessons applied
- **[E3] Reserve a slot for what the Playbook can't see.** This is why Thesis A leads, even though it's outside our comfort zone.
- **[E3] Auction owner absorbs measurement.** A is exposed to Apple/Google bundling; B is built only for the multi-exchange tier.
- **[E3] Date the option against the incumbent's ship date.** A's gate is the SDK terms in February 2008 plus 500 integrated apps by Q4. If a platform owner announces free analytics first, we pivot A to cross-platform monetization.
- **[E3 note] Suspect comfort, don't reject it.** B is comfort with genuine market pull, and it funds A.
- **[E2] Voluntary data beats mandated data.** Both theses collect data that users contribute voluntarily.
- **[E1] Bridges expire.** A's death is the end of handset fragmentation, expected in 3–5 years.

**Build:** A gets 10 engineers, including 3 new mobile/client hires. The hire is the thesis, per [E2]. B gets 6 on EC2. Bid runs for cash (~20 people).

### Most uncertain
1. Whether Apple's SDK terms allow third-party analytics or ad libraries, and how Apple will handle distribution.
2. Whether app developers will pay anything, or whether A monetizes only through the network, which would put us in the auction-owner seat we've never held.
3. Whether the credit crunch cuts agency display budgets before B earns revenue.
