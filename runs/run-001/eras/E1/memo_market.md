# Market & Capital — Department Memo, Era E1 (January 1990)

*Attendees: Carmen Ortiz (Head of GTM), Arjun Mehta (CFO & Capital Strategist), Dr. Elise Laurent (Chief Economist). Sources: E1 world briefing only; no knowledge after Jan 1, 1990.*

## Meeting transcript

**Carmen Ortiz, Head of Go-To-Market:** The people who pay today are corporate IT managers and department heads with budgets, not consumers. Homes are still a hobbyist market billed by the hour. What I hear from buyers is that they have NetWare LANs on one floor, a mainframe in the basement, MCI Mail or CompuServe for outside contacts, and none of it talks to anything else. If we sell "connect what you already bought," the budget already exists and nobody has to be persuaded that computers matter.

**Arjun Mehta, CFO & Capital Strategist:** We have $1.5M and a closed IPO window. Venture money is scarce after the '87 crash, and prime is at 10–11%, so the cost of capital punishes long burns. That rules out hardware, semiconductors, and anything that needs a consumer network before it earns revenue. I want software with a first paying customer inside 9 months, services revenue that funds the product, and a design where each deployment makes the next one cheaper. I'd rather be a dull profitable company in 1991 than an exciting dead one.

**Dr. Elise Laurent, Chief Economist:** The cost curves are clear. Compute and storage per dollar keep falling (386 to 486, 1Mb to 4Mb DRAM, cheaper disks), while communication and integration labor are expensive and fragmented. Margin migrates toward whatever stays scarce. Right now that's interoperability between incompatible systems, plus turning paper into data, because the machines are cheap and clerks are not. I disagree with Arjun on one point. Being "dull and profitable" in consulting-style integration becomes a trap if we never capture a standard. Services margins won't compound. We need a layer where every new connection raises the value of the network.

**Carmen:** That's fine as long as the wedge sells before the standards war ends. TCP/IP versus OSI is unresolved, and government buyers are told to buy GOSIP. We can't bet the company on one of them.

**Elise:** Then we sell the thing that stays valuable whichever side wins: translation between them.

**Arjun:** And the second thesis? Neural nets are fashionable in labs, but the last AI boom burned investors badly. I'd need a customer whose cost savings we can measure in dollars.

**Carmen:** Forms-heavy industries have exactly that. Banks, insurers, and payment processors pay armies of data-entry clerks. Bell Labs reading handwritten ZIP codes tells me the capability is close. We should sell it as keystroke reduction, not as "AI."

## DEPARTMENT RECOMMENDATION

### Thesis A: The Messaging Interconnect (preferred)
- **Capability → adoption → bottleneck → layer → data → next capability:** Cheap networked PCs and LAN email → rapid adoption of email inside companies → islands that can't reach each other (LAN mail, mainframe, commercial carriers, the research Internet) → **we own the gateway/directory layer that routes messages and addresses across systems** → we accumulate the cross-organization address directory and traffic patterns → next capability: a commercial inter-company messaging and document-exchange network (orders, invoices, EDI-style forms).
- **Why now:** commercial carriers began exchanging mail with the Internet in 1989, LANs are spreading fast, and the protocol war means no single vendor can promise universal reach.
- **Wedge:** a gateway product (software plus a small server box built on commodity PCs) connecting a NetWare LAN mail system to MCI Mail/CompuServe and to SMTP/Internet addresses. It is buildable by fewer than 20 people.
- **First customer:** a mid-size multinational or a university-linked engineering firm that already sees the pain every day.
- **What it makes obsolete:** fax-and-courier document exchange, proprietary single-vendor mail silos, and hand-maintained address lists. We have no prior business to cannibalize, but we note that if the network ever becomes universal and open, the gateway itself becomes obsolete, and we should plan to move up to directory and exchange services before then.

### Thesis B: Paper-to-Data Recognition
- **Chain:** Trainable pattern recognition (backprop nets, HMMs) → adoption in high-volume forms processing → bottleneck is accuracy on messy real-world input and integration into existing workflows → **we own the recognition-plus-verification engine sitting in front of the database** → we collect labeled images of handwriting and forms, a proprietary corpus that grows with every customer → next capability: automated document understanding and later speech input.
- **Why now:** neural nets are showing practical results (ZIP codes, vehicle steering), 386/486 PCs can run small networks, and labor costs make keystroke savings easy to measure.
- **Wedge:** hand-printed numeric field recognition (amounts, account and ZIP fields) with human verification of low-confidence fields.
- **First customer:** a regional bank's item-processing center or an insurer's claims-entry department.
- **What it makes obsolete:** offshore and back-office keying bureaus, and rule-based OCR that fails on handwriting.

### Playbook lessons
The Playbook is empty at founding, so there's nothing to cite. We propose seed principles for The Record to test:
1. Sell to budgets that already exist.
2. Own the layer that gains value with every connection.
3. Put a number on the savings before calling it AI.

### What we are most uncertain about
- **(A)** Whether the fragmentation lasts long enough to build a business. A single winning protocol or a dominant vendor bundling gateways could compress our margin. We also can't predict when commercial traffic will be allowed on the research network.
- **(B)** Whether recognition accuracy reaches the threshold at which customers trust it, or stalls the way expert systems did.
- **Capital:** whether a follow-on round is available at all in 1991–92 if the recession people fear arrives.

*Department vote: A as the lead thesis 2–1 (Laurent and Ortiz for; Mehta preferred B for its measurable ROI). All three recommend keeping B as a small research option funded by A's revenue.*
