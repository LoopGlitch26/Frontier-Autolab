# Product & Engineering Memo: Era E8 (Jan 2032, forecast)
*Assumes the E7 base case: Proofworks has ~$90–130M revenue, mostly AI Act continual certification plus trace evidence. Foundry has shrunk to a regulated-domain niche, and the open trace schema was absorbed into the OTel agent-trace standard. Tags: FACT(2026) / EXTRAPOLATION / SPECULATION, H/M/L.*

## Transcript

**Priya Nair, VP Engineering (GM, Foundry):** I'll start with the uncomfortable part. Lab RL signal now comes mostly from production usage and synthetic environments (EXTRAPOLATION, M-H); Foundry is a regulated-domain boutique. What we can ship in 12 months must reuse the pipeline we already run: re-testing deployed agents after every monthly model release. No second greenfield stack.

**Jonah Reyes, Head of Product:** Fourth era I'm saying it: the money is in the loss, not the test. Certification priced like SOC 2 is a mid-sized, audit-firm-heavy market (EXTRAPOLATION, M). Agent cover got folded into cyber (EXTRAPOLATION, M), which means cyber carriers are now holding correlated agent risk they cannot measure. That gap is our wedge. E7's Assure failed as standalone cover; pitch it as aggregation data for existing lines.

**Hana Kowalski, Head of Evidence Infrastructure:** Tamper-evident logging is now table stakes, and the OTel standard means nobody gets paid for the recorder (EXTRAPOLATION, M). What's unavoidable is one layer up: a live inventory of *which model version, with which tools and permissions, runs where*. A monthly release cadence (FACT(2026), H) combined with open-weight models dominating cost-sensitive deployment (EXTRAPOLATION, M) gives us a dependency graph nobody maps, which is the SBOM problem for agents.

**Leo Mbeki, Head of Developer Ecosystem:** I agree on the graph, and I'm worried about who owns it. Hyperscalers and model owners see their own deployments ([E3], [E6]). Open-weight deployers see nobody's. Our schema is inside OTel: publish the inventory-event spec openly, keep the aggregation index. I oppose Priya's operator idea: once we run agents for money, certified vendors stop sending traces.

**Priya:** Leo, the labs have the rights to production traces because they *run* the agents (E7 kill case). If we want rights-bearing data, we have to do the work too ([E6] "outcome pricing wins when you do the work").

**Jonah:** Then spin it out. The referee can't play.

## DEPARTMENT RECOMMENDATION

### Thesis A (preferred): Agent exposure registry and correlated-loss model, "the cat model for agents"
- **Chain:** multi-week autonomous agents on monthly model releases (EXTRAPOLATION, M) → thousands of firms running the same few model versions and tool stacks under cyber/E&O cover (EXTRAPOLATION, M) → **bottleneck:** carriers and reinsurers can't measure aggregation, so they set blunt sublimits (SPECULATION, M) → **layer we own:** a cross-deployment exposure registry (model version × tool × permission × deployer) plus a regression-propagation model → **data:** inventory events, our certification results after each model release, and incident traces → **next capability:** carrier-accepted "circuit breakers" (auto-rollback or parametric triggers on book-wide regression; SPECULATION, L-M).
- **Why now:** insurers already require logs, and a standard exists (EXTRAPOLATION, M). The first correlated event, if it happened, created the reinsurance question.
- **Wedge:** a quarterly *Model Regression Exposure Report* for a cyber carrier's book, priced per insured deployment.
- **First customer:** one Lloyd's cyber syndicate or a reinsurer's cyber desk, plus our top 20 certification clients as data contributors (opt-in).
- **Makes obsolete:** per-deployment certification as a product. It becomes a data feed, which cannibalises roughly 60% of our current revenue (EXTRAPOLATION, M).

### Thesis B (contested): Licensed operator of outcome-priced agents in one high-risk domain (spun out)
- **Chain:** outcome-priced agents are the default (EXTRAPOLATION, M) → high-risk domains need conformity files and someone to carry liability, which labs avoid (EXTRAPOLATION, M) → **bottleneck:** a certified operator that accepts the loss → **layer:** we run the work (e.g. claims adjudication for mid-size insurers) and hold the conformity file and E&O → **data:** rights-bearing trajectories × outcomes × audit findings → **next:** license that regulated-domain RL data to labs, which is the one niche that survives.
- **Why now:** the high-risk duties have applied since 2028 (FACT(2026) dates; EXTRAPOLATION on enforcement).
- **Wedge:** per-claim pricing, with a guaranteed audit-clean rate.
- **First customer:** a mid-size EU insurer we already certify, so a conflict of interest forces a legal spin-out.
- **Makes obsolete:** Foundry, and our neutrality.

### Playbook lessons applied
- [E6] "A referee is a franchise only under third-party mandate." Carrier logging requirements and sublimits are the mandate, and Thesis A sells to the party that imposes them.
- [E5] "Price against the loss": Thesis A prices per insured deployment.
- [E7-forecast] "Sell rights, not labor": contributed inventories are licensed rights that no lab holds across competitors.
- [E7-forecast] "Point the tripwire at the likeliest substitute": for Thesis A the substitute is the incumbent cyber-cat modelers (Verisk, Moody's RMS, CyberCube, all FACT(2026) as companies) adding an agent module. **Tripwire:** if any of them ships agent aggregation modeling before we have two carrier contracts, license our registry to them and exit.
- **Argued against:** [E2] "suspect comfort" catches Thesis A, since it is Jonah's Assure again. We claim the [E3 note] pull test now passes because carriers already hold the risk; Victor should attack that.

### Most uncertain
1. Whether a correlated agent-loss event actually happened (SPECULATION, M). Without one, sublimits stay blunt and nobody pays for aggregation.
2. Whether deployers will contribute inventory data when doing so can raise their premiums, which is the [E2] hub-and-spoke risk.
3. Whether model owners publish their own regression feeds and kill the independent signal.
4. Whether Thesis B's spin-out is real separation or a brand-damaging hedge.
