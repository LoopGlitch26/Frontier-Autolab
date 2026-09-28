# E6 Memo: Product & Engineering (January 2020)

## Transcript

**Priya Nair, VP Engineering:** We have ~75 people, ~$100M in cash, twelve applied deep-learning engineers, an aging V100 cluster, and years of corrections and abuse outcomes from ~150 apps under per-client keys. We can fine-tune BERT-class models in weeks. We cannot train something like Megatron, and with frontier compute doubling every ~3.4 months, we never will. I'd rent the next cluster, not buy it. Whatever we ship in 12 months will sit on top of someone else's pretrained model.

**Hana Kowalski, GM, Clearsight:** That's [E5]: our general API lasted about 18 months. Language is now the same public, benchmarked curve (BERT, GPT-2, T5). A "text moderation API" gets absorbed by the cloud language APIs. The unavoidable layer is the outcome loop: adapt a pretrained model to one company's policy, measure it against that company's real losses, and stand behind the result. Our corrections and loss data are the part nobody else has.

**Jonah Reyes, Head of Product:** And [E5] says to price against the loss, not the labor. Marketplaces already buy guarantees: Airbnb's Host Guarantee, eBay's Money Back Guarantee, Signifyd's chargeback guarantee. Nobody guarantees the losses that happen in *messages*: romance scams on dating apps, off-platform payment scams on classifieds, account takeovers on gig apps. Those losses live in text, and our corpus is text plus outcomes. So the wedge is "we cover the scam loss if our model misses it." It is not "cheaper than your reviewers."

**Leo Mbeki, Head of Developer Ecosystem:** You're both staying in the comfortable trust budget, which [E2] warns about. The deepest curve here is text *generation*. GPT-2 writes fluent paragraphs zero-shot. Hugging Face's open Transformers library and distillation work (DistilBERT, October 2019) mean a small team can now serve these models cheaply. [E4] says the reserved slot must go to a curve outside our own data. Builders want to *use* language models (drafting, summarizing, triaging tickets) and have no fine-tuning, evaluation or serving pipeline. Whoever gives them one gets distribution first.

**Hana:** The model owners will productize it. OpenAI took $1B from Microsoft.

**Leo:** They'll ship *their* model. A neutral layer that evaluates *any* model on a customer's own data is the referee position, one level up.

**Priya:** Both fit under 20 people. The guarantee needs actuarial talent and a reinsurance partner; we've never run a balance sheet. The pipeline needs serving engineers and an open-source posture we've never had. Staff A fully; give B a real team, not a tripwire.

## DEPARTMENT RECOMMENDATION

### Thesis A (lead: Jonah, Hana, Priya): "The scam-loss underwriter for conversational marketplaces"
- **Capability:** pretrained Transformers (BERT, RoBERTa, T5) fine-tune to domain text with small labeled sets.
- **Adoption:** dating, classifieds, gig and peer-to-peer commerce move trust-critical activity into in-app chat.
- **Bottleneck:** scams hide in conversations; marketplaces absorb unpriced losses.
- **Layer we own:** policy-tuned language models plus a loss guarantee, priced per protected transaction or conversation.
- **Data:** conversation → intervention → realized-loss outcomes per client; the guarantee contract grants outcome-data rights.
- **Next capability:** priced risk across conversation, identity and behavior; real-time in-chat intervention.
- **Why now:** pretrained models make text judgment cheap; NetzDG and Online Harms push liability onto platforms. **Wedge:** guaranteed scam protection for in-app chat. **First customer:** 5 dating and classifieds clients from our existing ~150. **Makes obsolete:** keyword filters, human chat review, and our own per-image and per-decision moderation pricing.

### Thesis B (Leo, with Priya's staffing): "The adaptation and evaluation layer for pretrained language models"
- **Capability:** open pretrained models plus distillation make task-specific language models cheap to fine-tune and serve.
- **Adoption:** developers want classification, extraction and drafting on their own text, with no machine-learning team.
- **Bottleneck:** fine-tuning, evaluation against the customer's own outcomes, and cost-efficient serving.
- **Layer we own:** a model-neutral hosted adapt/evaluate/serve pipeline with an open-source SDK on the Hugging Face and PyTorch ecosystem.
- **Data:** customer evaluation sets and corrections; an opt-in cross-customer benchmark of which models work for which tasks.
- **Next capability:** assistive generation in workflows, such as drafting replies for support and moderation queues.
- **Why now:** GPT-2's full release and open libraries collapsed the research barrier in 2019. **Wedge:** reply drafting and ticket triage for trust and support teams. **First customer:** 3 existing clients' support teams, then self-serve developers. **Makes obsolete:** our own bespoke per-category classifiers and rules-based support tooling.

### Playbook lessons applied
- **[E5] Price against the loss:** this is the core of Thesis A.
- **[E5] Public curve pools at inputs:** rent compute; own the outcome loop, not a general text API.
- **[E4] Reserved slot outside our own data:** this justifies Thesis B.
- **[E5] Don't put the referee on a revenue clock:** no sale clock on either thesis.
- **Convergence Audit:** Thesis A matches the E5 reveal ("guarantees"). The two pre-era sources it cites that the reveal did not name are Airbnb's Host Guarantee and Signifyd's merchant guarantee.
- **Argued against [E5] acqui-hire:** with $100M and a correction corpus, the acqui-hire default doesn't apply.

### What we are most uncertain about
1. Whether generation becomes the product, not just an assist. If so, B is the era's thesis and A is comfort (Leo's view).
2. Whether GDPR and per-client keys allow enough pooled outcome data to price risk.
3. How fast model owners offer fine-tuning themselves ([E3] ship-date risk for B).
4. Whether we can carry a guarantee book without reinsurance.
