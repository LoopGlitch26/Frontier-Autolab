# Board Decision — Era E6 (January 2020)
*Present: Mira Castell (CEO), Dev Anand Rao (CTO), Dr. Lena Okafor (Chief Scientist), Tomas Weil (CSO), Victor Hale (Red Team). Pre-2020 sources only.*
*Run note: the board step for E6 was run by the lab orchestrator directly because agent launches were unavailable. It follows the same instructions.*

## 1. Transcript highlights

**Victor Hale (Red Team):** First the Convergence Audit. All three departments list the same "B": an adaptation/evaluation layer for pretrained language models. That is exactly the kind of agreement [E4] tells us to distrust. I checked the sources. The memos cite GPT-2's staged release, Grover, Megatron, DistilBERT, Hugging Face Transformers, Deep TabNine and "The Bitter Lesson". All of these were public in 2019, and none are in the E5 reveal. The convergence looks earned, but I'm marking it anyway.

**Victor on Product A (scam-loss underwriter):** You want to write guarantees with no actuarial team, no reinsurer and per-client keys that stop you pooling losses. Signifyd had years of chargeback history before it guaranteed anything. This is [E5] "price against the loss" taken as a slogan. It is not a plan.

**Jonah (invited):** The loss is the only price that hasn't capped us.

**Victor on Market A (compliance referee):** NetzDG is German. Online Harms is a white paper, not a law. You would be selling compliance with a mandate that doesn't exist in most of your customer base. That is [E1] again: selling to a budget that isn't there yet.

**Victor on Frontier A (drafting copilot):** It's the most interesting option, and also the one most exposed to Ines's "scale continues" scenario. If a lab ships a model 10× Megatron that does tasks from a prompt, per-client fine-tuning becomes a feature.

**Dr. Lena Okafor (Chief Scientist):** Every scenario has the same shape. Weights are getting cheaper, and whether a model is right for a particular company is getting harder to know. GLUE saturated in about a year, and nobody can score whether generated text is correct or safe. We have what that question needs: seven years of human corrections tied to real outcomes. We don't need to predict which model wins. We need to measure all of them.

**Dev Anand Rao (CTO):** I agree, and it's buildable. We rent GPUs and don't refresh the V100 cluster. We build a model-neutral harness: customer data, customer policy, any model (BERT, T5, GPT-2, a cloud API), and scoring against outcomes, not labels. Drafting runs on the harness as the first application.

**Tomas Weil (CSO):** That fixes [E5]'s mistake. Last time we sold the output of a public curve and the hyperscalers gave it away. This time we sell the grade. Model owners can't credibly grade themselves, just as ad platforms couldn't ([E4]: own the referee).

**Victor:** [E3] says the owner of the model can bundle evaluation.

**Tomas:** It bundles evaluation *of its own model*. A referee across several models survives, as [E4] revised.

**Mira Castell (CEO):** Decision. We take the evaluation layer as the core, drafting as the first product on top of it, and compliance logging as a feature. Guarantees wait until we have two years of outcome data we're allowed to pool.

## 2. DECISION

**Company name:** Clearproof (renamed from Clearsight; the moderation book keeps the Clearsight name).
**Identity:** "The outcome-graded proving ground for pretrained language models: we tell you which model to trust in your workflow, and we prove it on your real outcomes."

**Reinvention thesis:**
pretrained transformers and open weights make capable language models cheap (capability) → every trust, support and risk team tries them on its own text (adoption) → nobody can measure whether a given model is right, safe and consistent *on their policy and their outcomes*; benchmarks saturate and vendor claims can't be checked (bottleneck) → **we own the model-neutral evaluation and adaptation layer, scored against real outcomes** (layer) → cross-customer, opt-in evaluation results showing which models work for which tasks, plus accept/edit/reject logs from drafting (data) → certified model deployment, then priced assurance for model decisions (next capability).

**KILL:**
- The per-decision classifier API as our identity (it moves to maintenance).
- Buying hardware: no V100 refresh, all compute rented.
- Scam-loss guarantees for now (revisit at the end of 2022).
- The sale option on the moderation book is **not** pursued on a revenue clock ([E5]). It runs as a cash business.

**KEEP:**
- The correction and outcome corpus (7 years, ~150 apps). From 2020, new contracts carry opt-in pooling rights.
- The signed action ledger, which becomes the audit trail for every evaluated decision (compliance logging comes free with it).
- The applied deep-learning team and trust-and-safety relationships.

**Wedge product:** *Clearproof Draft*. Suggested enforcement notices, appeal replies and support drafts for 5 existing clients, running on the evaluation harness. Every draft is graded against reviewer edits and appeal outcomes. It's priced per resolved case, with a monthly scorecard comparing models.

**First customer:** 5 dating and marketplace clients with large appeal backlogs.

**3-year plan:**
- 2020: harness plus Draft.
- 2021: self-serve evaluation for any team fine-tuning language models; an open-source evaluation SDK.
- 2022: published cross-model task benchmarks and certified deployment.

**Capital:** ~$100M cash. New-bet burn ~$15M/yr. No raise.

**Reserved slot (5%):** protein structure (AlphaFold/CASP13) as a watch option, since it's a curve outside our data ([E4]).

**Kill criteria:**
1. By Q4 2020, the harness must beat the clients' in-house model choice on outcome accuracy for at least 3 of 5 clients.
2. **Tripwire:** if a public model ≥10× Megatron does tasks from prompts alone, stop per-client fine-tuning within 60 days. Move to evaluating prompted models and to workflow.
3. If a model owner launches cross-model evaluation for third-party models, sell the harness or open-source it.
4. At least 30 paying evaluation customers by the end of 2021.

**Org changes:**
- Dr. Kofi Mensah → Head of Evaluation Science.
- Hana Kowalski → GM, Clearproof.
- Leo Mbeki → Head of Open Source & Developers.
- Priya Nair → VP Engineering (rented compute).
- Jonah Reyes → GM, Clearsight (moderation cash business) and owner of the guarantee research track.
- Victor Hale keeps the Convergence Audit.

**Dissent log:**
- **Jonah:** guarantees are the only pricing that doesn't cap us, and we're deferring the one thing the Playbook said works.
- **Carmen:** the compliance mandate will arrive, and we should be the default audit log when it does.
- **Samuel:** the labs may make evaluation part of their API. The model-owner risk is under-weighted.
