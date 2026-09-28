# Frontier Research Memo — Era E3 (January 2002)
*Department: Frontier Research. Sources limited to what was public before 1 Jan 2002.*

## Meeting transcript (condensed)

**Dr. Yuki Harada, Head of Frontier Research:** The bending curve is statistical learning on text and behavior: SVMs and boosting beat hand-written rules, Viola–Jones runs learned detectors in real time, and LDA models the topics of any page. At the same time, Google and Overture have shown that a typed query is priced intent, bought by the click in an auction. Combine them: priced intent read from *any* page, not just a search box.

**Samuel Brandt, Technology Historian:** Busts are when franchises get founded: talent is cheap and the tourists are gone. My warning is the playbook's. Twice we named the frontier and built the layer next to our skills. "Web services for EDI" is a bridge ebXML and AS2 will make free.

**Ines Varga, Futurist & Scenario Planner:** My three scenarios for 2002–2007. (1) *Performance economy* (45%): ad money that fled banners returns as pay-per-click, and query owners become the new media companies. (2) *Trust crisis* (30%): after 9/11, worms, Enron and spam, budgets go to security, identity and filtering. (3) *Long winter* (25%): only cost-cutting enterprises buy; offshore services win. Indicators: Overture syndication revenue, spam share of email, broadband households.

**Dr. Kofi Mensah, Research Scientist, Measurement:** What nobody measures yet: first, *whether a paid click was real and led to a sale*. No one audits click quality or conversion across networks. Second, *whether a message is wanted*. Spam and worm traffic are growing, and filters rely on hand-written rules. Our 1997 click-ranking result plus our receipt system is the start of a conversion ledger.

**Harada:** Kofi, the bigger prize is matching ads to pages, and a ledger alone won't get us there.

**Mensah:** Matching without measurement is banners again. Whoever proves the conversion sets the price.

**Brandt:** Neither needs our EDI platform. Good sign.

## DEPARTMENT RECOMMENDATION

### Thesis A (preferred): Intent Everywhere — contextual pay-per-click matching plus a click-quality and conversion ledger
- **Capability:** statistical text classification and topic models read what any page is about. Pay-per-click auctions put a price on intent.
- **Adoption:** budgets are shifting from banners to pay-per-click; content publishers earn almost nothing.
- **Bottleneck:** paid listings reach only search-results pages. Across the rest of the Web, nobody matches ads to page content, and advertisers can't verify that clicks are genuine or lead to a sale.
- **Layer we own:** a relevance-and-measurement layer. We match an advertiser's existing keyword listings to page content, and we audit every click with a signed, receipted conversion record.
- **Data:** a page-topic × ad × click × conversion graph that advertisers and publishers join *voluntarily*.
- **Next capability:** learned click-fraud detection, then pricing by conversion (pay-per-action) across Web, email and eventually mobile.
- **Why now:** pay-per-click is proven, publishers are desperate, and bust-era engineers are cheap.
- **Wedge:** a click-audit and conversion-tracking service for pay-per-click advertisers (a tag on the order-confirmation page plus a signed log), with contextual matching for mid-size publishers as the second product.
- **First customer:** mid-size online retailers already spending on Overture and AdWords, including several of our own buyer hubs.
- **Makes obsolete:** banner networks, panel measurement for direct response, and our Web-EDI business (harvest or sell).

### Thesis B: Learned Trust Filter — hosted statistical filtering of mail and transactions
- **Capability:** Bayesian and SVM classifiers applied to message traffic; signed receipts.
- **Adoption:** email is universal, and worms and spam are pushing IT and security budgets up after 9/11.
- **Bottleneck:** rule-based filters break every week, and no one pools signals across organizations.
- **Layer we own:** a hosted gateway that scores every inbound message and document for spam, virus and fraud risk.
- **Data:** a cross-organization abuse corpus, which gets better with every customer.
- **Next capability:** reputation scores for senders and counterparties (we have the address and registry heritage for this), and then fraud scoring on payments.
- **Why now / wedge / first customer:** spam is rising fast; hosted per-mailbox filtering, first sold to our 20 buyer hubs.
- **Makes obsolete:** rule-based filtering appliances and our own untrusted-email onboarding path.
- **Caveat:** closer to our mail heritage, so likely the comfort option.

### Playbook lessons applied
- **[E2] Suspect comfort:** we rank A over B precisely because it requires a team we lack. We need to hire 3–4 statistical learning and ads engineers, and hiring them *is* the thesis.
- **[E2] Voluntary intent:** A's data comes from voluntary participants. The EDI graph came from mandates and never became a moat.
- **[E2] Gate tripwires on capability:** if A becomes an option, promote it on measured lift, never on whether portals will pay.
- **[E1] Pipe, then traffic, then index:** the Web now has traffic *and* an index. The next layer is whoever measures and prices intent across the Web.
- **[E2] Bubble is a financing event:** we argue this lesson applies in reverse now. The bust is a hiring event.

### What we are most uncertain about
- Whether search incumbents extend paid listings onto content pages first; if so, A's durable asset is the neutral audit ledger, not the matching.
- Whether contextual ads convert near search levels; page intent is weaker than a typed query.
- Whether a cash-constrained company with a preference overhang can fund A while it harvests Web-EDI.
