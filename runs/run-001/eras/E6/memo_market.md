# Market & Capital Memo: Era E6 (January 2020)
*Carmen Ortiz (Head of GTM), Arjun Mehta (CFO), Dr. Elise Laurent (Chief Economist). Sources limited to what was public before 1 Jan 2020.*

## Meeting transcript

**Carmen Ortiz, Head of Go-To-Market:** Two budgets are growing faster than anything we sell into. The first is trust and safety. NetzDG, the Christchurch Call and the UK Online Harms white paper turn moderation into a legal obligation, and mid-size platforms can't hire reviewers at Facebook's scale. The second is enterprises testing BERT-style models without labels for their own domain. That buyer has no vendor yet.

**Arjun Mehta, CFO & Capital Strategist:** We hold ~$100M, a clean cap table, near-zero burn and $150–400M of acquisition interest. That makes us rich for a trust vendor and poor for a frontier lab. OpenAI needed Microsoft's $1B, and compute on the largest runs doubles every ~3.4 months, so we should not train the largest models. Record equity prices alongside post-WeWork caution are a late-cycle signal. [E4] says to prepare a sale option on the moderation book in 2020 and fund any new bet from cash.

**Dr. Elise Laurent, Chief Economist:** [E5] says value on a public curve pools at the scarce inputs. Transformer weights are going free: BERT, GPT-2, T5 and Hugging Face's library. What stays scarce is compute (we can't compete) and labeled domain outcomes (we have those). Our per-decision price has capped us twice. A fine or a chargeback is a loss worth pricing against. A moderator's wage is not.

**Carmen:** I disagree on guarantees. Underwriting needs a balance sheet and loss history, and nobody has priced harmful-content liability yet. Buyers will want an audit trail they can show a regulator before they want insurance.

**Arjun:** That argues for a referee before an underwriter. [E5] warns against putting the referee on a revenue clock, and I won't do that twice.

**Elise:** Agreed, with one warning. Jigsaw's Perspective toxicity API has been free since 2017. [E3] and [E5] say a general text classifier gets bundled. What survives is the outcome loop: which decisions a regulator, a court or a chargeback proved correct.

## DEPARTMENT RECOMMENDATION

### Thesis A: The compliance referee for platform harm (lead)
**Capability** transformer language models plus our vision stack give multilingual, multimodal judgment that can be fine-tuned cheaply → **adoption** regulation forces mid-size platforms (marketplaces, dating, gaming, forums) to act on and report harmful content and fake accounts → **bottleneck** they cannot show a regulator that their decisions are consistent, timely and auditable → **layer we own** a neutral decision record and certified review service: model and human decisions, signed on our action ledger, with audit reports in the formats regulators ask for → **data** appeal outcomes, regulator findings and reversed decisions (outcomes, not only labels) → **next capability** priced liability: we warrant a platform's compliance and underwrite fines and chargebacks once loss history exists.
- **Why now:** NetzDG is in force, Online Harms is heading toward law, and CCPA/GDPR add audit duties.
- **Wedge:** "Clearsight Record": signed decision logs plus a monthly transparency report, bundled with our existing judgment models.
- **First customer:** 5 EU-exposed marketplace and dating clients from our ~150-app base.
- **Makes obsolete:** the per-image moderation price and our own flat per-decision API, which moves to per-platform compliance pricing.

### Thesis B: Domain outcomes for pretrained language models (reserved slot, [E4])
**Capability** pretrained transformers transfer to new tasks with small labeled sets → **adoption** enterprises fine-tune for support, claims, contracts and risk → **bottleneck** domain labels and evaluation, not model weights → **layer** a managed label-and-evaluation service that measures whether a fine-tuned model is right, safe and unbiased in a specific domain → **data** cross-customer evaluation benchmarks, with contractual rights negotiated up front (our per-client keys limited us last era) → **next capability** misuse and synthetic-text detection as generation spreads (GPT-2's staged release and Allen AI's Grover already frame the threat).
- **Why now:** BERT runs in Google Search, and open weights mean every enterprise can have a model it cannot check.
- **Wedge:** evaluation suites for text classifiers in trust, fraud and insurance claims.
- **First customer:** two insurers or banks already buying our account-risk scores.
- **Makes obsolete:** our hand-labeled moderator queue as a cost center, which becomes a product.
- **Budget:** 15% of new-bet burn, gated on capability evidence rather than incumbent willingness to pay ([E2]).

### Playbook lessons applied
- [E5] price against the loss (compliance outcomes, then underwriting). [E5] scarce inputs: own outcomes, not models. [E4]/[E5] own the referee, with no revenue clock. [E4] credit calendar: prepare the sale in 2020. [E2] gate Thesis B on capability evidence.
- **Argued against:** [E4] "reserved slot outside your own data." Thesis B still leans on our data. The Board may prefer an outside curve instead, such as synthetic-media provenance.
- **Convergence Audit:** Thesis A echoes the E5 reveal's line on guarantees. Pre-era sources the reveal did not cite: NetzDG, the Online Harms white paper, Perspective API (2017) and Signifyd's guaranteed-fraud model.

### Most uncertain
1. Whether the model owners start selling large language models as a product themselves (the capped-profit structure and the Microsoft investment hint at this). If they do, the evaluation layer may be absorbed, as [E3] warns.
2. Whether harm regulation passes, and when. A delay leaves Thesis A as a compliance product with no mandate behind it.
3. Whether the market peak lasts long enough to sell on our terms.
