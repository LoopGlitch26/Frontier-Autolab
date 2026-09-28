# E2 Memo: Product & Engineering (January 1996)

## Transcript

**Priya Nair, VP Engineering:** Here is where we actually stand. We have $2M in cash, a gateway whose revenue is falling, and a team that knows SMTP, MIME and address rewriting better than almost anyone. The gateway dies inside 24 months whatever we do, and E1 told us to date that death on day one. I can ship one new server product in 9–12 months with 12 engineers if we stop gateway custom work now.

**Jonah Reyes, Head of Product:** I see pull in two places. The first is the new ISPs and small businesses getting a .com. Every one of them has to run mail servers, and they're bad at it, so they call our support line even though they aren't customers. The second is merchants who put up a catalog site and then fax orders to themselves; nobody sells the part between "Buy" and the processor.

**Hana Kowalski, Principal Infrastructure Engineer:** I want to push back on Jonah's second one. A merchant server that connects Web forms to card processors is a bridge. We lost E1 by selling a bridge. The unavoidable layer is the server side of the open protocols: mail stores and directories on commodity Unix and NT, run for millions of new users. I'd build hosted mail and directory as infrastructure for ISPs.

**Leo Mbeki, Head of Developer Ecosystem:** Hana, a bridge only expires when one side disappears. The card networks aren't going to vanish the way X.400 did. Visa and MasterCard are writing the online payment spec right now, which tells you the Web side is going to *adopt* their rails. Every storefront developer is rewriting the same order-and-payment code in CGI. Give them a free commerce API and they bring us the merchants.

**Priya:** Leo, CyberCash, Open Market and First Virtual are already funded for exactly that, and the capital climate favors them. Mail is a place where we have a real edge.

**Jonah:** An edge in something becoming free. Every ISP gives away a mailbox, so they'll outsource it but haggle hard on price.

## DEPARTMENT RECOMMENDATION

### Thesis 1 (Priya, Hana): "Mail and identity infrastructure for the newly connected"
- **Capability:** SMTP/POP/MIME are universal, cheap Unix and NT servers exist, LDAP is a lightweight directory, and browsers can render a mailbox.
- **Adoption:** home users are joining ISPs; small businesses are registering .com domains.
- **Bottleneck:** running reliable, spam- and abuse-resistant mail and directory at scale. Mail admin skills are scarce.
- **Layer we own:** outsourced mailbox, directory and account infrastructure, white-labeled for ISPs and businesses, with mail readable from any browser.
- **Data:** the address graph, which people and organizations exchange mail, delivery and abuse patterns, and account identity.
- **Next capability:** a Web identity and address-book service, meaning one login and one contact list across sites.
- **Why now:** ISP counts and .com registrations are exploding; new ISPs don't want to be mail operators.
- **Wedge:** a hosted POP/SMTP and LDAP service for regional ISPs, billed per mailbox.
- **First customer:** a regional ISP with 5–20k subscribers whose mail server keeps falling over.
- **Makes obsolete:** our own gateway (we sunset it and sell the customer base), in-house LAN mail servers, and closed online-service mail.

### Thesis 2 (Jonah, Leo): "The transaction layer between the Web and the money"
- **Capability:** SSL, the forthcoming card-payment spec, Java and CGI, and cheap Web servers.
- **Adoption:** thousands of merchants are putting catalogs online,, and early stores show that consumers will order.
- **Bottleneck:** secure order capture, authorization, fraud and fulfillment handoff. Every merchant rebuilds it badly.
- **Layer we own:** a hosted order-and-payment service with a free developer API (a "Buy" button any site can embed).
- **Data:** cross-merchant transaction streams, including which cards, addresses and patterns end in chargebacks.
- **Next capability:** learned fraud scoring and a buyer reputation network. Statistical learning finally gets the labeled data it lacked in E1.
- **Why now:** the payment spec is being written and merchants are fax-ordering today.
- **Wedge:** hosted checkout for small catalog merchants, charged per transaction.
- **First customer:** a mail-order catalog business moving to the Web.
- **Makes obsolete:** our gateway and document-exchange roadmap. Small-firm EDI too.

### Playbook lessons applied
- **[E1] Bridges expire:** this is why the gateway is sunset in both theses. Hana argues Thesis 2 is a bridge. Leo counters that the lesson applies only when one side of the bridge is losing a standards war, and card rails aren't.
- **[E1] Value pools where the open protocol becomes usable:** both theses sit at the server-side usability layer, not translation to legacy systems.
- **[E1] Pipe, then traffic, then index:** 1996 is the traffic phase, so we deliberately don't compete with Yahoo or AltaVista on the index. Mail volume and transactions are traffic.
- **[E1] Your "next capability" line is often the frontier:** we flag Web identity (T1) and learned fraud scoring (T2) for funded tripwires.
- **[E1] Right science, right decade:** fraud learning stays a cheap option, not strategy.

### Most uncertain about
1. **Whether mailboxes become free commodities** (T1). If ISPs and portals give mail away, per-mailbox pricing collapses.
2. **Whether banks or processors bundle checkout** (T2).
3. **Hindsight check:** the room slightly prefers Thesis 2 because "commerce" sounds like the frontier. We ask the Red Team to test it on 1995 evidence alone.
4. **Capital:** can $2M plus a gateway sale fund either thesis?
