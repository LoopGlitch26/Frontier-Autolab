# The Record: Reveal and Score, Era E5 (Jan 2014 – Dec 2019)
*Call under review: Clearsight. It sold the performance exchange on the credit calendar and built a hosted "judgment API" (image moderation plus fake-profile and account-risk scoring on one GPU-trained stack, priced per decision) for trust teams at photo, dating, classifieds and marketplace apps. It kept attribution for 12 months as Clearline Verify, with sale unless the unit passed $5M ARR. It reserved 10% of new-bet burn for messaging platforms as distribution.*

## 1. What actually happened

**Deep learning was the defining curve; value pooled at scarce inputs and platforms.** ResNet beat the human ImageNet benchmark (2015). TensorFlow (Nov 2015) and PyTorch (2016–17) commoditized the craft. The frontier moved to scale and labs: DeepMind (Google, ~$500M, Jan 2014), AlphaGo (2016), OpenAI (Dec 2015), the Transformer (2017), BERT (2018), GPT-2 (2019). Nvidia's data-center revenue rose from ~$0.3B (FY2015) to ~$2.9B (FY2019); Google built TPUs (2016); labeling became a layer (Scale AI, 2016).

**General perception APIs were commoditized inside two years, as kill criterion #3 predicted.** Microsoft Project Oxford (Apr 2015); Google Cloud Vision beta (Dec 2015) with SafeSearch adult/violence detection; Amazon Rekognition (Nov 2016, moderation Apr 2017). Vision startups mostly became acqui-hires (Madbits, Magic Pony, Jetpac, MetaMind, Dextro). Clarifai (ImageNet 2013 winner, moderation API) raised well but never broke out.

**Trust-and-safety budgets exploded, mostly as human labor.** After the 2016 election, YouTube's 2017 ad boycott, NetzDG (2017), Cambridge Analytica and GDPR (2018), Facebook reached ~30,000 safety staff, about half contracted reviewers (Accenture, Cognizant, Genpact). Platforms built classifiers in-house; mid-market moderation vendors (Two Hat, Besedo) stayed modest.

**Fraud and risk was the stronger half.** Sift Science, Forter and Riskified grew large; Forter and Riskified won with **chargeback guarantees**, the "priced risk" step the board left for last. Stripe bundled ML fraud scoring as **Radar (Oct 2016)**, firing Weil's payments tripwire. Marketplace account abuse stayed open to vendors; TransUnion bought iovation (2018).

**The referee on a sale clock became a franchise.** As mobile ad fraud surged, attribution became mandatory infrastructure; AppsFlyer, Adjust and Branch (bought TUNE's attribution, 2018) grew toward $1B scale. Certification was a moat, not a utility. Jonah's dissent was right.

**The reserved slot was a Western bust.** Facebook bought WhatsApp ($19B, Feb 2014); Messenger bots (Apr 2016) faded within a year; the real messaging platform, WeChat Mini Programs (Jan 2017), was closed. The era's consumer shift was the AI-ranked feed (ByteDance's Douyin/TikTok).

**Exit climate:** the 2014 mobile-ad window was real (Yahoo–Flurry and BrightRoll, Opera–AdColony ~$350M, AOL–Millennial 2015); Fiksu later collapsed (2017).

## 2. Scorecard

| Criterion | Score | Justification |
|---|---|---|
| Frontier accuracy | **9** | It named the era's defining curve at the start, with correct evidence and talent-scarcity logic. It missed that the frontier would move to compute scale and research labs. |
| Timing | **8** | Starting in 2014 was early enough to lead the mid-market for ~18 months, and the exchange sale caught the 2014 mobile-ad M&A window. |
| Layer choice | **5** | General moderation-as-API was commoditized by 2015–17 and priced against cheap human queues. The fallback (domain trust judgments, account risk, priced risk) was sound but sat in phases 2–3. Value pooled in chips, cloud, labeling and in-house platform models. |
| Reinvention courage | **8** | It sold the cash business, hired a capability it lacked, and bought GPUs. It hedged by folding the new curve into its familiar fraud buyer, and it put its best existing asset on a sale clock. |
| Hindsight leakage | **6** | The evidence cited was public (ImageNet 2012–13, cuda-convnet/Theano/Torch, the DNNresearch and LeCun moves, Google Prediction API 2010). The phone-model line was struck. But the pivot tracks the E4 reveal almost word for word, and "Stripe/Square bundling" and "loss guarantees" come close to later history (Radar, Riskified). The Convergence Audit is a good control. |

**Overall era score: 68/100**

## 3. Simulated outcome
Exchange sells mid-2014 for ~$115M; preferences clear. #2 met narrowly (one hire via acqui-hire). Moderate beats human queues for nudity/spam at 4 customers (#1 passes), at cents per image. At ~$2.5M ARR, Cloud Vision SafeSearch (Dec 2015) fires #3; retreat to profile/listing fraud and marketplace account risk. Radar removes the payments tier. Verify sells Q2 2015 (~$3.5M ARR, ~$25M), a clear miss. Messaging slot closed 2017. **By Dec 2019: ~$22M ARR, ~75 people, a respected mid-tier fraud and trust vendor.**

**Distribution:** about 45%, acquired in 2018–21 by an identity or fraud consolidator for $150–400M. About 25%, stalled after the hyperscaler APIs and acqui-hired for under $60M in 2016–17. About 20%, a pivot to chargeback guarantees makes it a Forter/Riskified-class unicorn. About 10%, a breakout in labeling or trust-and-safety infrastructure.

**Closest real-world analog:** Clarifai (ImageNet-2013 team, moderation API, hit by hyperscaler APIs) for the perception wedge, drifting toward Sift Science for the account-risk half.

## 4. Lessons (appended to playbook.md)
1. **A public, benchmarked curve pools value at its scarce inputs** (chips, compute, labeled data, researchers) and with whoever owns distribution. A general API on top gets commoditized by hyperscalers within about 2 years. Own an input, or own an outcome loop no giant sees.
2. **Price against the loss, not the labor.** A wedge priced below a cents-per-item human queue caps itself. The winners priced against chargebacks and took the risk (guarantees).
3. **Don't put the referee on a revenue clock during a platform shift that raises the need for it.** Certification became a moat. This revises the [E2 note] claim that certification makes a referee a utility.
4. **On a talent-scarce curve, the modal small-company outcome is an acqui-hire.** Plan it as a valid exit, or build a proprietary data or outcome moat from day one.
5. **Judge a new distribution platform by user behavior, not by developer hype.** Bots on Western messengers failed, and the real messaging platform was closed.
