# Board Decision — Era E2 (January 1996)
*Attendees: Castell (CEO), Rao (CTO), Okafor (Chief Scientist), Weil (CSO), Hale (Red Team). Sources are limited to what was public before 1 Jan 1996.*

## 1. Transcript highlights

**Victor Hale (Red Team):** I'll start with hindsight and hype, because this room has both. Frontier's Thesis A says "usage-weighted relevance ranking licensed to indexes." No 1995 product ranks pages by anything but word matching, so it is either insight or a memory of the future. Second, every memo agrees "commerce is the frontier," and Netscape is worth $2B with almost no profit. That's a hype signal, not evidence.

**Dr. Lena Okafor (Chief Scientist):** On relevance, the 1995 evidence is thin but real. Information-retrieval research has used relevance feedback for decades, and Kofi is right that result-page clicks and server logs are unused signals. But we have no data, no Web-native team, and six funded engines in the field. It's a tripwire, not the company.

**Victor:** "Internet EDI" is a bridge between the VANs and the Internet. We just lost an era selling bridges.

**Dr. Elise Laurent (via Tomas Weil, CSO):** A bridge expires when one side loses the standards war. Here the losing side is the VAN *pricing model*, not the EDI document standards. X12 and EDIFACT survive. What we sell is the registry of trading partners, the routing, and a signed receipt.

**Victor:** GEIS, Sterling Commerce and Harbinger own the VAN customers and the EDI software. They'll add Internet transport the moment it's free, just as Novell and Microsoft added SMTP.

**Tomas Weil:** Agreed that the incumbents will add Internet transport. Our answer is that we don't compete for their existing EDI-capable trading partners. We go after the suppliers who can't afford EDI at all: the 50–300 small firms behind each big buyer, who today fax. A browser form is the whole client. Incumbents live on kilocharacter tolls, so flat pricing cannibalizes them. That protects us for a few years.

**Victor:** Product's Thesis 1, hosted mail for ISPs. Jonah already said every ISP gives mailboxes away.

**Dev Anand Rao (CTO):** Hana's instinct about infrastructure is right, but per-mailbox pricing on a commodity that ISPs bundle for free is a margin trap. It's also our comfort zone. We're killing it.

**Victor:** And Thesis 2, hosted checkout for consumer merchants?

**Dev:** CyberCash, Open Market and the Netscape and Microsoft commerce servers are funded for it, and card specs aren't done. One engineer keeps a card-capable Web form ready, nothing more.

**Victor:** Last one. Arjun wants a large raise at bubble prices. If we miss milestones, the next round is a down round in a crash.

**Mira Castell (CEO):** Then we raise enough for 30 months, not more, tranched on volume. Let me decide.

## 2. DECISION (CEO)

**Company name:** **Manifest Networks** (the Switchyard name goes with the gateway line we're selling).
**Identity:** *The trusted, receipted exchange for business documents over the open Internet.*

**Reinvention thesis:**
- **Capability:** SMTP/MIME, HTTP and SSL are universal; Windows 95 puts a browser on every new PC; EDI-over-MIME is being standardized.
- **Adoption:** firms are connecting with new "Internet" budgets; big buyers mandate electronic orders.
- **Bottleneck:** VAN per-kilocharacter tolls and EDI software cost lock out small and mid-size suppliers. Orders and invoices sent by email are unsigned, unreceipted and unauditable.
- **Layer we own:** a hosted trading-partner exchange that provides a registry of who trades with whom and how, routing, signed delivery receipts and an audit trail. EDI over MIME for large buyers, Web forms for small suppliers. We price the registry and the receipt, never the translation.
- **Data:** the inter-company trading graph (who orders what from whom, when, and how reliably they deliver and pay).
- **Next capability:** supplier performance and credit scoring, trade finance on receipted invoices, then cross-company catalog procurement.

**KILL:**
- The Switchyard Gateway product line. We sell it and its maintenance base to one of the messaging or ISP buyers now showing interest,. Target close Q2 1996.
- The cross-network directory ambition, as a standalone product.
- Custom integration services beyond a 25% revenue cap.
- Hosted mail (Thesis 1) and consumer checkout (Thesis 2) as company lines.

**KEEP:**
- The SMTP/MIME and routing engineering team.
- Our ~60 enterprise customers, as anchor buyers bringing their supplier tails.
- The address map, recast as the seed of the partner registry.
- Services discipline (Carmen as governor).
- The Thesis B handwriting/fax corpus stays frozen and costs nothing.

**Funded tripwire (≤10% of burn):** Kofi Mensah and one engineer run a **Web measurement and relevance research option**. They test whether opt-in log and click data improve ranking or audience audits. We promote it at end-1997 if an index or publisher will pay.

**Wedge product:** *Manifest Exchange 1.0*, a hosted service for exchanging purchase orders, invoices and ship notices between one large buyer and its suppliers. It has signed receipts and an audit trail, and costs a flat monthly fee per supplier. Target ship Q4 1996.

**First customer:** an existing manufacturing account that is a tier-2 supplier under an automotive or big-box retail EDI mandate, together with its own 50–300 suppliers.

**3-year plan:**
- **1996:** close the gateway sale and raise the new round. Ship Exchange 1.0 with 2 anchor buyers and 300 connected suppliers.
- **1997:** reach 15 anchor buyers and 3,000 suppliers. Add a second vertical (distribution/wholesale). Open the partner registry so any company can look up a trading partner's capabilities. Launch a supplier-rating pilot with one anchor.
- **1998:** reach 10,000+ suppliers. Pilot invoice financing on receipted invoices with a bank partner. If consumer card specs have settled and merchants are pulling, promote the checkout option.

**Capital need:** ~$2M cash, plus $6–10M expected from the gateway sale, plus a **$10M Series B** in 1996 on the new story. That gives ~30 months of runway at ~18–20 people in the core product team.

**Kill criteria:**
1. Fewer than 2 anchor buyers live and 200 active suppliers by March 1997 means we pivot.
2. A VAN incumbent or Microsoft/Netscape/IBM bundles Internet EDI with *flat* pricing *and* a supplier Web form before we have 5,000 suppliers. Then we retreat to the registry/rating layer or sell.
3. Services exceed 35% of revenue for two quarters.
4. Transactions per supplier stay flat for 12 months (mandate-only suppliers make the graph worthless).
5. Bridge-death date: we assume Internet-native EDI transport becomes a free commodity by ~2000. Before then, the registry and scoring layer must produce at least 30% of revenue.

**Org changes:**
- **Arjun Mehta** owns the gateway divestiture and the tranche covenants.
- **Priya Nair** leads a new **Exchange Engineering** team. **Hana Kowalski** becomes **Head of Exchange Reliability & Security** (signing, receipts, uptime).
- **Leo Mbeki** is renamed **Head of Partner Network**. He owns supplier onboarding and a free registry lookup API for EDI software vendors.
- **Dr. Kofi Mensah** becomes **Head of Measurement & Relevance Research**, running the tripwire. The directory remit is retired.
- **Carmen Ortiz** keeps her Services Governor duty, with the cap now set at 25%.

**Dissent log:**
- **Victor Hale:** Internet EDI is still a bridge with a nicer registry on top. The incumbents will match flat pricing faster than we think.
- **Dr. Yuki Harada and Dr. Kofi Mensah (via Lena):** The Web's traffic is the frontier and we're underweighting it again. They want the tripwire at 20%.
- **Hana Kowalski (via Dev):** Hosted mail and identity are the unavoidable layer; we're abandoning our strongest skill.
- **Jonah Reyes and Leo Mbeki (via Dev):** Consumer commerce arrives sooner than Carmen expects; checkout deserves more than one engineer.
- **Tomas Weil:** He concurs but warns that the scenario he calls *Microsoft absorbs it* (30%) would also reach business servers. The moat must be the trading graph.
