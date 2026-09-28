# E3 Memo: Product & Engineering (January 2002)

## Transcript

**Priya Nair, VP Engineering:** Here's the inventory. We have about 65 people, $15M in cash, and a Web-EDI utility near breakeven. A 2002 raise would be a crushing down round, so the next thesis has to be built by fewer than 20 people and paid for by the utility's cash flow. The upside is that 2002 is the cheapest year in a decade to build. Linux boxes are cheap, the telecom overbuild made bandwidth nearly free, and dot-com engineers are available.

**Jonah Reyes, Head of Product:** E2 taught us that money pools around declared, priced intent, not mandated traffic. Our 5,000 suppliers log in because big-box buyers make them, and none of them has ever asked us for anything. Meanwhile, small sellers list on eBay and buy Overture and AdWords clicks with no idea which click became an order. The pull is on the seller's side of search.

**Hana Kowalski, Head of Exchange Reliability & Security:** I'll argue the other side. What we're good at is running multi-tenant, signed, audited hosted software for thousands of small firms. Salesforce.com and NetLedger show that businesses will rent applications over a browser, and in a recession CFOs want a monthly fee instead of a license. Hosted business applications are the unavoidable layer.

**Leo Mbeki, Head of Partner Network:** Hana, that's the E2 comfort warning word for word. I'll grant half of it: SOAP and WSDL are the integration theme, and whoever ships a clean API gets the builders. Either thesis should expose an open API from day one so developers bring us the merchants.

**Priya:** Jonah, Overture and Google sell the clicks. What stops them from building your tool into their own consoles?

**Jonah:** Each of them sees only its own channel. Only a neutral tool sees Overture, Google and eBay together, plus the order. We should date the bundling risk now: if any of them ships cross-channel conversion reporting, the tool's standalone value ends.

**Hana:** Then my thesis is the fallback. Hosted applications don't die when one engine adds a feature.

## DEPARTMENT RECOMMENDATION

### Thesis A (Jonah, Leo; lead): "The seller's side of intent"
- **Capability:** intent is now priced at scale through Overture's pay-per-click auction, AdWords and eBay listings. PayPal handles small-merchant payments, and Linux clusters make logging clicks cheap.
- **Adoption:** hundreds of thousands of small sellers buy clicks and listings with no measurement.
- **Bottleneck:** sellers can't manage feeds and bids across channels or tie a click to a sale, so they overpay or quit.
- **Layer we own:** a hosted performance hub for sellers that sends catalog feeds to each channel, manages bids, and tracks conversions from click to order to payment.
- **Data:** cross-channel conversion data from query to sale, given to us voluntarily by sellers. No engine has it.
- **Next capability:** automated bidding, then a shopping index ranked by real conversion, then merchant credit based on observed sales flows (trade finance, this time on voluntary data).
- **Why now / wedge / first customer:** ad budgets are shrinking, so measurable performance wins. The wedge is conversion tracking plus bid management at $50–300/month, with a free tier. The first customers are merchants spending more than $1K/month on paid listings. We also pilot with about 200 of our own suppliers who want direct buyers.
- **Obsoletes:** agency-run search buying, and our own mandated Web-EDI, which we run as a cash cow.

### Thesis B (Hana, Priya): "Hosted business applications as a utility"
- **Capability:** browser applications, commodity servers, XML web services and E-SIGN-valid signatures.
- **Adoption:** the recession pushes firms from licenses to monthly fees, despite 2001's ASP failures.
- **Bottleneck:** trust in multi-tenant uptime, security and audit after Code Red, Nimda and Enron.
- **Layer we own:** an audited multi-tenant platform with an API. Our exchange becomes its first application, followed by order-to-invoice and billing.
- **Data:** cross-tenant operating data (orders, invoices, payment timing).
- **Next capability:** third parties build and sell their own applications on our infrastructure.
- **Why now / wedge / first customer:** capital scarcity rewards monthly-fee models, and ERP vendors are license-bound. The wedge is hosted order-to-invoice as an upsell to our 5,000 suppliers.
- **Obsoletes:** desktop EDI software, and our flat-fee exchange as a standalone product.

### Playbook lessons applied
- **[E2] Money pools where intent is priced.** This is why Thesis A leads.
- **[E2] Hub-and-spoke yields no neutral data moat.** Thesis B's data stays inside buyer-mandated hubs; Thesis A's doesn't.
- **[E2] Suspect comfort.** Thesis B is our adjacent-skill layer, so it ranks second as the fallback.
- **[E1] Pipe, then traffic, then index.** The index now exists; the next layer measures its value for the people who pay it.
- **[E1] Bridges expire.** Thesis A's death condition, dated on day one, is an engine or marketplace bundling cross-channel conversion reporting.
- **[E2] Gate tripwires on capability.** If the pilot shows better merchant return, we fund Thesis A fully without waiting for any engine to partner.

**Build:** 12–15 engineers, beta in 9 months, funded from cash. We hire two search and ranking engineers, the team we lack.

### Most uncertain
1. How fast the engines and eBay bundle their own measurement or restrict third-party bid management.
2. Whether small sellers will pay for measurement.
3. Whether our utility reputation and preference overhang let us hire search talent.
