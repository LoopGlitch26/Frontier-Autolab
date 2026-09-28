# The Record: Reveal and Score, Era E4 (Jan 2008 – Dec 2013)
*Call under review: Clearline. It put Ledgerline Bid up for sale (~$40M floor, data rights retained) and built a free cross-platform SDK plus an app-to-app exchange priced per verified action, starting with Facebook apps and gating the phone on platform terms. The funded option was hosted prediction on rented compute (25% of new-bet burn), gated on measured lift by Q4 2008.*

## 1. What actually happened

**The credit crisis closed the window the board feared, and it closed hard.** Bear Stearns was rescued in March 2008. Lehman failed on September 15, 2008, and venture investment and M&A froze until mid-2009. A sale process run in H1 2008 was about the last good exit window for mid-tier ad-tech until 2010.

**The phone became the platform, and the platform owners took most of the value.** Apple's SDK shipped March 6, 2008, and the App Store opened July 10, 2008. Third-party ad and analytics libraries were allowed (AdMob, Pinch Media and Flurry were in early apps). Apple's April 2010 terms briefly barred third-party analytics, relaxed that September. Apple bought Quattro Wireless (January 2010) and launched iAd in July 2010. Google bought AdMob ($750M, announced November 2009, closed May 2010). Android shipped on the HTC Dream (October 2008) and passed iOS in shipments by 2011. The largest pools were the stores, Facebook, AWS and mobile-first networks (Instagram, WhatsApp, WeChat, Uber, Airbnb).

**Facebook apps boomed and then were absorbed by Facebook.** Zynga became the dominant app developer and bought users heavily. It went public in December 2011, then fell hard in 2012. Early app ad networks (Cubics, Social Media) faded; offer walls (Offerpal, Super Rewards) took the money until the "Scamville" scandal (November 2009). Facebook imposed ad-provider terms in 2010 and made Credits mandatory in 2011, taking 30%. It launched its own **mobile app-install ads in August 2012**. Mobile passed half its ad revenue in 2013, with install ads a major share.

**Pay-per-install became a real market in 2010–2013, and the neutral layer that lasted was attribution.** Tapjoy (the former Offerpal Media, which moved from Facebook offer walls to iOS pay-per-install), Fiksu, W3i and Chartboost (2011) grew large. Apple cracked down on incentivized installs in April 2011. Once Facebook, Twitter (which bought MoPub in 2013) and Google ran their own install auctions, advertisers needed a neutral referee. Mobile measurement firms (HasOffers/MobileAppTracking, Kochava, AppsFlyer in 2011, Adjust in 2012) became that referee, and Facebook began certifying outside measurement partners around 2013.

**The dissents did well too.** Hana's "neutral per-impression buyer across exchanges" became the demand-side platform category: Invite Media (sold to Google in 2010 for about $81M), MediaMath, and The Trade Desk (founded 2009). Elise's cloud analytics became Cloudera (2008) and Splunk (IPO 2012) on AWS. **The era's deepest curve was the one flagged and left unaddressed:** multilayer neural networks. Deep networks cut speech error rates (2010–12). AlexNet won ImageNet in 2012, Google bought DNNresearch in 2013, and Facebook opened an AI lab in December 2013.

## 2. Scorecard

| Criterion | Score | Justification |
|---|---|---|
| Frontier accuracy | **8** | It correctly named open app platforms, the phone and rented compute. It missed the deep-learning turn (listed as a weak signal, never funded), messaging, and mobile marketplaces. |
| Timing | **7** | The H1 2008 sale ran ahead of Lehman. Facebook-first was sound in 2008, but that inventory stayed cheap and scandal-prone until 2010. The paying pay-per-install market arrived about 2010, a two-year cash gap in a credit winter. |
| Layer choice | **6** | An exchange on someone else's platform is rented land. Facebook and Google shipped first-party install auctions within four years. Kill criterion #3's fallback ("cross-platform fraud and attribution tier") named the layer that actually held. |
| Reinvention courage | **9** | Sold the cash cow into a closing market, killed the search roadmap, hired client engineers, and chose to run an auction for the first time in four eras. |
| Hindsight leakage | **5** | All three memos converged on the layer the E3 reveal had just named. The memos used "cost per install", "retained install", per-user lifetime value, "Pocket Web mass market by ~2011" and a 3–5-year fragmentation timeline. The board's Vocabulary Audit caught most of this, but the choice itself looks like it followed the answer key. |

**Overall era score: 66/100**

## 3. Simulated outcome
Bid sells in Q2 2008 for about $41M, just above the floor; cash is ~$45M before the crash. Apple's March terms permit ad libraries, so criterion #1 is dead. The exchange reaches about 200 Facebook apps by September 2008 (#2 met). Through 2009, offer walls that tolerate lead-gen scams outbid it for developers; gross spend stays under $1M and #4 nearly fires. Scamville and Facebook's 2010 provider terms then reward the clean ledger. The iOS SDK, launched in 2009, becomes the main line, and gross spend passes $2M before any first-party install auction (#3 not triggered). The prediction option shows modest lift in Q4 2008 and becomes the exchange's internal pricing engine. By 2012: ~$80M gross spend, ~$18M net revenue, ~120 people. Facebook's install ads compress margins, and #3 fires in spirit: the company shifts toward cross-platform attribution and fraud scoring.

**Distribution:** about 45% modal: a mid-tier mobile performance network sold in 2012–14 for $100–250M, most of it above the preference stack. About 30%: starved by Facebook-app economics in 2009–10, a sub-$50M exit. About 25%: the attribution pivot lands early and the company becomes a category leader in neutral mobile measurement. **Verdict: a real, well-timed bet on the right platform shift. It ran an auction the platform owners would eventually take back; its better asset was the referee role.**

**Closest real-world analog:** Offerpal Media → Tapjoy (Facebook action-priced offers in 2007–08, iOS pay-per-install from 2010). The fallback's twin is AppsFlyer; AdMob is the winning case.

## 4. Lessons (appended to playbook.md)
1. **Third-party auctions on an open platform have a 3–4-year window** before the owner ships first-party. Exit or move layers inside it.
2. **If you can't own the auction, own the referee.** Cross-platform verification outlives single-platform measurement (refines [E3]).
3. **Run the sale on the credit calendar, not the product calendar.** The H1 2008 process beat Lehman (confirms [E2]).
4. **Unanimity right after a reveal is a leakage alarm; dissents are the control group.** Log them as tripwires.
5. **The reserved slot must go to a curve outside your own data.** It went to comfort twice; the neural-network revival went unfunded.
