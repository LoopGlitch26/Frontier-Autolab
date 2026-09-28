# Frontier Research Memo: Era E6 (January 2020)
*Public sources before 1 Jan 2020 only. Written without coordinating with other departments.*

## Meeting transcript

**Dr. Yuki Harada (Head of Frontier Research):** In 2014 the curve was perception. Now it's pretraining. BERT, GPT-2, Megatron (8.3B) and T5 all show the same thing: one large model trained on raw text, then lightly fine-tuned, beats years of task-specific engineering. GPT-2 also *writes*. Deep TabNine (July 2019) put a GPT-2-style model into code editors. Generation is starting to ship, and our whole stack is classifiers.

**Samuel Brandt (Technology Historian):** [E4] says unanimity right after a reveal is a leakage alarm, so I'll say the uncomfortable part. [E5] says this kind of curve pools value at compute and at labs, and OpenAI's 2018 analysis puts the doubling at 3.4 months. With ~$100M we're a customer of that curve, not a participant. The precedent I'd use is the relational database in the early 1980s: the engine concentrated in a few vendors, and the durable small winners owned an application's workflow and its data.

**Ines Varga (Futurist & Scenario Planner):** Three scenarios. *Scale continues:* few-shot generalists arrive in 2–4 years, and fine-tuning shops get squeezed the way vision APIs were. *Diffusion:* the Hugging Face Transformers library and distillation (DistilBERT, ALBERT) make pretrained models a commodity skill, and value goes to whoever holds outcome data. *Stall:* GPT-2 stays a toy, compute costs cap progress, and the field retreats to BERT-class classifiers. Indicators to watch: whether any lab trains a model 10x larger than Megatron in 2020, SuperGLUE progress, and whether generated text shows up in abuse queues. My outside-our-data slot is AlphaFold: CASP13 is a benchmark win in biology, and it's early.

**Dr. Kofi Mensah (Head of Trust Science):** Here's what nobody can measure yet: whether a piece of text, a face or a voice was made by a person. Grover (May 2019) showed a generator is also the best detector of its own output. GLTR offers statistical tells, and Facebook's Deepfake Detection Challenge (September 2019) admits the problem is open. The second unmeasured thing is generative model quality itself: GLUE saturated within about a year, and nobody has a reliable score for "is this output correct or safe." Our ~150 clients' correction logs are exactly the labels that problem needs.

**Samuel:** That's the adjacent layer again ([E2]). Detection is a classifier arms race that the generator's owner wins.

**Kofi:** Unless we price it as a referee, which [E4]/[E5] say holds. And provenance doesn't go stale the way a classifier does.

**Yuki:** I'd rather we generate than referee. Detection is defensive. The bigger jump is drafting: support replies, moderation rationales, code.

## DEPARTMENT RECOMMENDATION

**Thesis A: Generative drafting on our outcome loop (Yuki; Samuel dissents on timing)**
- *Chain:* pretrained transformers fine-tune on small labeled sets and write fluent text → trust, support and ops teams adopt suggested drafts and decisions → bottleneck is controllability and knowing which drafts are safe to send → **layer we own:** a fine-tuned drafting-and-decision copilot inside the reviewer console, tuned per client → **data:** accept/edit/reject logs, which are an outcome loop no hyperscaler sees ([E5]) → **next capability:** agents that act on queues with a human spot-check.
- *Why now:* open weights (GPT-2 full release in November 2019, T5), Transformers library, and V100/T4 serving are cheap enough for a team of 15.
- *Wedge:* auto-drafted enforcement notices and appeal replies for dating and marketplace clients, priced per resolved case against the reviewer headcount it removes. We price it against the loss ([E5]), not per token.
- *First customer:* 5 current account-risk clients with large appeal backlogs.
- *Makes obsolete:* outsourced review queues, and our own per-decision classifier API.

**Thesis B: Authenticity referee for synthetic media and text (Kofi)**
- *Chain:* generators produce convincing text, faces and voice → fake profiles and review spam scale at near-zero cost → bottleneck is proving what's human → **layer we own:** a neutral cross-platform provenance and synthetic-content referee → **data:** labeled synthetic-abuse corpus plus client outcomes → **next capability:** certified provenance (signed capture, building on our signed action ledger).
- *Why now:* GPT-2 is public, deepfakes are a live policy issue, CCPA started 1 January, and the UK Online Harms paper raises the cost of failure.
- *Wedge:* a synthetic-profile and bot-text detector in the existing SDK, sold to dating and classifieds apps.
- *Makes obsolete:* our face and photo-verification rules. **Risk:** the generator owner bundles it ([E3]).

**Playbook applied:** [E5] scarce inputs: we don't try to out-train labs, we own the outcome loop. [E5] price against loss. [E4] reserved slot outside our data: AlphaFold/protein structure as a 5% watch option. [E5] acqui-hire is the modal outcome, so we plan data rights early. **Argued against:** [E2] "suspect comfort" applies to Thesis B, and we accept that knowingly because the referee held twice.

**Convergence Audit:** Thesis A echoes the E5 reveal's "scale and labs." Pre-era sources the reveal didn't cite: Sutton's "The Bitter Lesson" (March 2019), Deep TabNine (July 2019), Megatron-LM (August 2019), Grover (May 2019).

**Most uncertain:** whether scale keeps paying off. If Ines's first scenario holds, a general model from a lab outperforms our per-client fine-tunes within about 3 years, and Thesis A lasts only as long as its data loop. We can't measure that from here. Tripwire: if a publicly announced model is ≥10x Megatron and does tasks from prompts alone, move off fine-tuning and onto workflow plus evaluation.
