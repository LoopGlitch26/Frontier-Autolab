# Independent Red Team critique — E1

## Frontier: LAN diagnostics/configuration tool

**Kill case:** A NetWare administrator or support manager must own the purchase and show that recurring configuration and support work costs enough to justify a separate tool. “Technician-confirmed fixes” is a proposed data source, not evidence that technicians will record cases consistently or that recorded fixes will transfer across mixed configurations. Authorized collection, accurate diagnosis, and safe fixes are a substantial support and liability burden for a 16-person team. One mixed system is a pilot boundary, not proof the tool generalizes to other LANs.

**Kill if:** Interviews fail to identify a budget owner and repeated costly incidents; a small case sample cannot be captured and resolved reliably; or each customer needs bespoke diagnosis or support.

**Cheap proof:** Shadow one support team through a limited set of recurring incidents. Manually record configurations and resolutions, then test whether technicians can use the record to resolve a repeat case faster. Do not build automated collection until that value is shown.

## Product: departmental request/issue log

**Kill case:** Replacing paper intake and follow-up sounds concrete, but the buyer, budget, and current pain are still hypotheses. A log only helps if staff enter requests, keep status current, and trust its reports; optional LAN sharing adds concurrency and support demands. Limiting the first release to one supported PC environment helps buildability, but does not establish repeatable deployment across departments.

**Kill if:** No department manager will sponsor a pilot; staff do not reliably use the log; overdue/recurrent reports do not change follow-up; or tested LAN sharing requires substantial customer-specific support.

**Cheap proof:** Have one department run a short pilot using the simplest supported setup, with manual import or setup. Compare request capture and follow-up against its paper process; test LAN sharing separately before making it a commitment.

## Market: paid LAN workflow application

**Kill case:** “Mid-size distribution/manufacturing” is too broad to establish a real buyer or a repeatable sale. Existing budgets are a sales hypothesis, not proof of demand for this product. Integrations across a customer's existing systems could dominate a focused software budget and support capacity. Structured data may permit reporting, but that is not evidence customers will pay or that deployments will be alike enough to scale.

**Kill if:** No named buyer will commit to a paid pilot for one specific workflow; required integrations vary materially between prospects; or the workflow cannot show measurable value without custom implementation.

**Cheap proof:** Choose one workflow at one prospect, document its current process and baseline, and sell a bounded pilot with explicit integration limits. Deliver the first reporting value manually if needed; use the pilot to test payment, implementation effort, and repeatability before building broader integrations.

These are critique hypotheses, not observed market evidence. No post-1990 outcomes are used in the kill cases.
