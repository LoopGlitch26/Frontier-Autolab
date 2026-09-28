# The Record: Reveal and Score, Era E3 (Jan 2002 – Dec 2007)
*Call under review: Ledgerline. It harvested Web-EDI for sale and built a neutral, receipted cross-channel conversion ledger for pay-per-click advertisers (Track, then Bid, then automated bidding and pay-per-action). A contextual-matching option was funded at 15% of Ledgerline burn and gated on measured conversion lift by Q2 2003.*

## 1. What actually happened

**The auction owner took nearly all the value.** Google moved AdWords to cost-per-click auctions ranked on bid × click-through rate in February 2002. Revenue rose from about $440M (2002) to $16.6B (2007); IPO August 2004. Overture consolidated search (AltaVista, AllTheWeb), then sold itself to Yahoo in July 2003 for about $1.63B. Microsoft launched adCenter in 2006. The [E2] lesson that money pools where intent is priced held completely. But the money pooled with whoever *ran* the auction, not with the tools that served bidders.

**Contextual matching arrived early, and it came from the engine.** Google launched content-targeted ads in March 2003 and bought Applied Semantics in April (about $102M). AdSense opened to small publishers that June, and Overture followed with its own content match. Frontier's Thesis A was the right idea, but the company that already had the advertisers shipped it within 15 months.

**Measurement was bundled, and engines opened access rather than closing it.** Google bought Urchin in April 2005 and made Google Analytics free in November 2005. That erased the small-merchant market for paid analytics. Engines published bid APIs (the AdWords API, 2005) instead of banning third-party tools. Neutral tools survived only at the enterprise and agency tier. Omniture went public in 2006, WebSideStory in 2004, and Coremetrics stayed private. Efficient Frontier (founded 2002), and later Marin and Kenshoo (2006), sold bid optimization to large advertisers and agencies. DoubleClick bought Performics in 2004 for about $58M. Click fraud was real: Google's Lane's Gifts settlement (2006, $90M) confirmed Kofi's click-quality concern.

**The ad-tech consolidation of 2007:** Google agreed to buy DoubleClick for $3.1B, Microsoft bought aQuantive for $6B, and Yahoo bought Right Media for $680M.

**The theses the org rejected did well.** Hosted spam and threat filtering (Frontier Thesis B): Symantec bought Brightmail (2004, about $370M), Cisco bought IronPort (2007, about $830M) and Google bought Postini (2007, $625M). Hosted applications (Hana): Salesforce went public in June 2004, and NetSuite (formerly NetLedger) in December 2007. B2B sourcing (Laurent/Ortiz): Alibaba.com's November 2007 Hong Kong IPO raised about $1.7B. The winners were exporters, not a US vertical.

**The era's defining layers were ones no memo named:** user-generated and social media (Facebook 2004, MySpace sold for $580M in 2005, YouTube sold to Google for $1.65B in 2006), rented infrastructure (MapReduce paper 2004, S3 and EC2 2006) and the smartphone (iPhone, June 2007). The briefing listed Wikipedia and Blogger; the org ignored them.

## 2. Scorecard

| Criterion | Score | Justification |
|---|---|---|
| Frontier accuracy | **6** | It correctly identified the money (search pay-per-click), the unmeasured-conversion pain and click fraud. It missed social and user-generated content, cloud and mobile, and it misread engine behavior (they opened APIs and made measurement free rather than banning third parties). |
| Timing | **8** | 2002 was close to the ideal entry for search-marketing tools. Talent was cheap, and advertiser spend on search grew several times over by 2007. |
| Layer choice | **4** | A tool on rented land that paid platform rent. The $50–300/month small-merchant tier was the part a free product would kill, and in November 2005 one did. Durable value existed only at the enterprise and agency tier. |
| Reinvention courage | **7** | It killed EDI growth, trade finance and flat fees, and hired a ranking team. The contextual option got only 15%, and a lift gate that ran to Q2 2003 guaranteed it would be preempted. |
| Hindsight leakage | **7** | Mostly defensible. Points off for "pay-per-action" named as the endpoint, a suspiciously exact bridge-death condition, and Frontier's contextual thesis arriving about 14 months ahead of AdSense (though it was knowable from Applied Semantics). |

**Overall era score: 58/100**

## 3. Simulated outcome
Track hits beta in Q3 2002, and kill criterion #1 is met, with about 350 paying merchants by September 2003. The contextual option shows promising lift, but AdSense and Overture content match launch before the Q2 2003 gate. It is killed under criterion #5 because there is no publisher network. Manifest Exchange sells in 2004 to an EDI consolidator for about $9M, below target. Ledgerline Bid (2003–04) finds its market in agencies and mid-size retailers. Free Google Analytics (November 2005) sends small-merchant Track churn above 5%. That trips criterion #3 in 2006, so Track is folded into Bid and the free tier is dropped. Criterion #2 half-fires: one engine made analytics free, and a second (Microsoft's adCenter Analytics) is in beta. The board rules that it is not triggered. A $12M 2005 Series D restructures preferences. By end-2007 there is about $11M ARR, about 60% from agencies, with about 75 people and about $12M cash.

That path is modal, at about 50%. In about 30% of cases, the company sells in 2005–07 for $40–120M to an agency holding company or an ad-tech consolidator, and preferences absorb most of the proceeds. In about 20%, the small-merchant focus persists and GA forces a sub-$30M sale. **Verdict: a credible, mid-tier search-bid-management vendor. Useful, acquirable, not era-defining.**

**Closest real-world analog:** Efficient Frontier (2002, bid optimization for large advertisers, sold to Adobe in 2011). Urchin (acquired by Google in 2005 and made free) is the cautionary twin.

## 4. Lessons (appended to playbook.md)
1. **The auction owner absorbs the measurement.** A platform bundles a tool for free once measurement increases spend on that platform. It opens APIs rather than banning tools, so it can commoditize them. Neutral tools survive only where the buyer spends across several platforms at scale (enterprise and agencies). Price and build for that tier from day one.
2. **Date your option against the incumbent's ship date, not your own calendar.** If the demand-side owner can ship the idea, a 15-month lift gate is a kill order. Fund it to launch before them, or drop it.
3. **"Suspect comfort" is not "reject comfort."** Hosted filtering and hosted apps were both adjacent to the org's skills and both produced large exits. Judge comfort options on market pull, not on identity.
4. **Reserve a slot for the thesis the Playbook can't see.** Every memo optimized on the last era's lesson (priced intent). The era's new pools were social/UGC, cloud and mobile, and they were visible in the briefing's weak signals.
