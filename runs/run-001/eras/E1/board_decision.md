# Board Decision — Era E1 (January 1990)
*Attendees: Mira Castell (CEO), Dev Anand Rao (CTO), Dr. Lena Okafor (Chief Scientist), Tomas Weil (CSO), Victor Hale (Red Team Lead). Inputs: E1 world briefing and the three department memos. Sources limited to what was public before 1 Jan 1990.*

## 1. Transcript highlights

**Victor Hale (Red Team):** I'll start with hindsight. All three departments independently put TCP/IP over OSI and "the Internet" at the center of everything. That consensus is suspicious. As of today, the US government mandates GOSIP, the NSF bans commercial traffic, and the research network has maybe 150,000 hosts, most of them in universities. Ines herself gives the "walled gardens win" scenario 35%. If you're this sure the research network becomes the business network, show me evidence from 1989, not a feeling.

**Dr. Lena Okafor (Chief Scientist):** The evidence exists. Every Sun ships with TCP/IP. The ARPANET is being retired in favor of NSFNET rather than OSI. MCI Mail and CompuServe chose to gateway into SMTP in 1989. But you're right that we don't know *when* commercial traffic is permitted, and I won't claim otherwise.

**Tomas Weil (CSO):** Which is why the thesis has to pay whichever protocol wins. Market & Capital framed it correctly: sell translation between islands. If OSI wins the government segment, an X.400/SMTP/LAN-mail gateway still sells. The bet is on fragmentation lasting five years, not on TCP/IP winning.

**Victor:** Then attack number two. "Own the directory and index" appears in every memo like a magic word. Who pays for a directory in 1990? Nobody has paid for one yet. X.500 was published in 1988 and nobody runs it commercially. That's the hype in this room: we've dressed up a gateway box as a data empire.

**Dev Anand Rao (CTO):** Fair. The gateway is the product and the directory is a by-product we collect for free. Every gateway we install has to rewrite addresses, and that address map is the directory. We don't sell it until customers ask to look someone up across systems.

**Victor:** Product & Engineering. You want a DOS TCP/IP stack *and* a mail gateway *and* a free developer API, with a VP Engineering who says she can staff one of those. FTP Software already sells a DOS TCP/IP stack. Novell or Microsoft can bundle one whenever they want. You'd be competing with incumbents on their own turf using $1.5M.

**Dev:** Agreed, so we drop the stack as a product. We license or partner for the PC stack layer and build only the mail and address gateway, which nobody owns because it lives between vendors. Leo gets his free programming interface, but it's the gateway's addressing API, not a whole stack.

**Victor:** Thesis B. The pro-B voices say it's "not AI, it's keystroke reduction." That's a rebrand, not a correction. Bell Labs read constrained ZIP digits in a lab. Faxed claims forms at 200 dpi are a different animal. The expert-systems crowd also had a lab demo.

**Lena:** This is where I disagree with the room. I think B is the more important curve scientifically. Backprop plus labeled data is a general method, and whoever collects the labeled corpus first learns something that transfers. But I accept it is not a company in 1990: no buyer standard, accuracy unknown on real input, and Hana makes a fair point that digital forms shrink the fax market.

**Victor:** Last one, capital. Every memo says "services fund the product." That's how you become an integration consultancy forever, which is Elise's own warning.

**Mira Castell (CEO):** Right, so services get a cap. Let me decide.

## 2. DECISION (CEO)

**Company name:** **Switchyard Systems**
**Identity:** *We connect the islands: the addressing and exchange layer between incompatible networks.*

**Reinvention thesis:**
- **Capability:** cheap 386/486 PCs on office LANs, plus working open mail protocols (SMTP on TCP/IP) and emerging standards (X.400/X.500).
- **Adoption:** email spreading inside companies, on NetWare LAN mail, mainframe mail, commercial carriers and the research network.
- **Bottleneck:** mail and addresses can't cross between these islands, and nobody can find a person or host across systems.
- **Layer we own:** the multi-protocol mail and address gateway (LAN mail ↔ SMTP ↔ MCI Mail/CompuServe ↔ X.400), sold per site, with an open addressing API for builders.
- **Data:** the cross-organization address map and anonymized routing and volume patterns that every installation produces.
- **Next capability:** a cross-network directory and lookup service, then inter-company document exchange (orders, invoices, forms) over the same routes.

**KILL:** Nothing exists from a prior era. We explicitly reject: (a) building our own DOS TCP/IP stack; (b) any hardware; (c) a consumer online service; (d) Thesis B as a company line.
**KEEP (assets to build and compound):** the 16-person team; the address map from each gateway; protocol-translation expertise; a relationship base in engineering firms and universities. Thesis B survives as a **two-person research option** capped at 10% of burn. It collects a labeled fax and handwriting corpus through two pilot sites and does not ship a product.

**Wedge product:** *Switchyard Gateway 1.0*, software that runs on a dedicated commodity 386 PC. It connects a NetWare LAN mail system to SMTP and one commercial carrier, with address rewriting and a shared address book. Target ship date is Q4 1990.

**First customer:** a mid-size engineering or defense-contracting firm running NetWare PCs alongside Sun workstations, with university partners already reachable over the research network.

**3-year plan:**
- **1990:** ship Gateway 1.0 to 5 paying sites and 2 design partners. Publish the addressing API free.
- **1991:** add X.400 and a second carrier, reach 40 sites, and launch the cross-site shared directory as a paid option. Raise a Series A if the numbers hold.
- **1992:** directory lookup across customers (opt-in) and a first document-exchange pilot. If commercial traffic opens on the research backbone, reposition as the on-ramp for businesses joining it.

**Capital need:** $1.5M seed covers about 18 months at a lean burn. Target a **$3–4M Series A in late 1991**, contingent on 25+ paying sites and more than $1M in annualized revenue. Services capped at 30% of revenue.

**Kill criteria:**
1. Fewer than 5 paying sites by March 1991 means we pivot or merge.
2. Novell or Microsoft bundles a multi-carrier SMTP gateway at zero marginal cost before we have a directory product, which means we retreat to the directory and exchange layer or exit.
3. Services exceed 50% of revenue for two straight quarters, which means we've become a consultancy and must restructure.
4. No movement on leading indicators (commercial mail gateways, .com registrations, NSF policy) by end-1992, which means we cap growth and reassess the on-ramp plan.
5. The research option: if two pilots show field accuracy under 95% on numeric fields by end-1991, we freeze it.

**Org changes:**
- Dr. Kofi Mensah becomes **Head of Directory & Recognition Research**, owning the address-map data asset and the Thesis B option.
- Hana Kowalski and Leo Mbeki's scopes merge into a **Gateway & Protocols** team under Priya Nair. Leo keeps the API/builder program.
- Carmen Ortiz adds **Services Governor** duty to enforce the 30% cap.

**Dissent log:**
- **Victor Hale:** The directory story is still unproven hype. We are a gateway company until customers pay for lookup.
- **Dr. Lena Okafor:** She believes recognition via trainable nets is the deeper long-term curve and that a two-person option underfunds it. She asks for a review at E1 midpoint.
- **Arjun Mehta (via Tomas):** He preferred B for its measurable ROI and warns that gateway sales cycles into IT departments will be long.
- **Leo Mbeki (noted by Dev):** He wanted a fully free core product. The compromise frees only the API.
- **Tomas Weil:** He concurs but flags that the real prize depends on NSF policy, which we can't influence. We are selling fragmentation, and fragmentation may end.
