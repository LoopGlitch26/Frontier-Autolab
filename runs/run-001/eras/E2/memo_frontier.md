# Frontier Research Memo — Era E2 (January 1996)
*Department: Frontier Research. Sources limited to what was public before 1 Jan 1996.*

## Meeting transcript (condensed)

**Dr. Yuki Harada, Head of Frontier Research:** The pipe war is over. Windows 95 ships TCP/IP, NSFNET is retired, and SMTP/MIME won, so our gateway is a bridge whose standards war just ended. The curve that is bending now is the Web's traffic. Sites double every few months, AltaVista indexes all of it, and SSL makes transactions possible. The question now is what gets built on top.

**Samuel Brandt, Technology Historian:** Every medium has repeated the same order: first the pipe, then the audience, then whoever measures and sells the audience. The Web has millions of readers and no trusted audience count, so advertisers are paying on faith. I also want to warn the room about Netscape. Microsoft's December 7 strategy says the OS vendor absorbs the client. Don't fight at the browser.

**Ines Varga, Futurist & Scenario Planner:** Here are my three scenarios for 1996–2001. (1) *Open Web boom* (50%): the Web becomes the mass medium, advertising and commerce move online, and indexes and portals become the new networks. (2) *Microsoft absorbs it* (30%): IE and MSN inside Windows capture the client and the default home page, and independents survive only in server-side and business niches. (3) *Walled gardens re-close* (20%): AOL-style services and interactive TV set-tops keep consumers inside curated environments. Leading indicators: monthly Web ad spend, SSL merchant servers, AOL's share of Web hours, and the Visa/MasterCard card specification. Business transactions over the Internet happen in all three.

**Dr. Kofi Mensah, Research Scientist, Measurement:** I'll say what we can't measure yet. First, *which pages matter*. Indexes rank thousands of hits by word counts. The relevance signals sit in server logs and result-page clicks, and nobody collects them across sites. Second, *who saw what*. Hit counts are inflated by proxies and caches, and there is no audited unique-visitor number. Third, *whether a business message arrived and was accepted*. Our 60 sites already email orders and invoices as unsigned, untracked attachments. Measured delivery between companies is a product.

**Harada:** Kofi, the relevance problem is the bigger prize. The measurement problem is where we can win.

**Brandt:** The network is large enough now for an index to pay, but that space is crowded, with six engines in two years.

## DEPARTMENT RECOMMENDATION

### Thesis A — "The Web's Measurement and Relevance Layer" (preferred by Harada, Mensah)
- **Chain:** commercial Web + browsers on every Windows 95 PC → **adoption:** mass readership, and advertisers and merchants moving budgets online → **bottleneck:** nobody can measure audience or relevance, so ads are unpriceable and search results are noisy → **layer we own:** a neutral, audited audience and ad-delivery measurement service (log analysis plus a tagged-panel method), sold to publishers and advertisers → **data:** cross-site, anonymized behavior (which pages people choose, stay on and return to) → **next capability:** usage-weighted relevance ranking licensed to indexes, then ad targeting.
- **Why now:** the first Internet IPOs have made Web ad inventory worth auditing.
- **Wedge:** log-auditing software plus a certified monthly report for the top 200 commercial sites.
- **First customer:** large publishers and search/directory companies selling banner ads, which need third-party numbers to close agency deals.
- **Obsoletes:** self-reported hit counts. It also retires our gateway and directory ambitions.

### Thesis B — "Internet Business Exchange" (preferred by Brandt, Varga)
- **Chain:** SMTP/MIME universal + SSL → **adoption:** companies already emailing orders, and small suppliers who could never afford EDI → **bottleneck:** there is no trusted, receipted, cheap exchange of business documents over the public Internet, while value-added networks charge per kilocharacter → **layer we own:** secure, receipted document exchange (EDI and forms over SMTP/HTTP) with signing and delivery tracking → **data:** the inter-company trading graph (who orders what from whom, and when) → **next capability:** a marketplace and supplier-finance layer.
- **Why now:** VANs are expensive, the Internet is free at the margin, and our 60 enterprise customers and SMTP/MIME team get us to a shipping product in 9 months.
- **Wedge:** "Internet EDI" for the supply chains of our existing customers, with a Web form front end so small suppliers need only a browser.
- **First customer:** a current engineering/manufacturing customer and its long tail of 50–300 suppliers.
- **Obsoletes:** VAN EDI and fax ordering, and our own gateway (redeployed as its transport).

### Playbook lessons applied
- **[E1] Bridges expire:** we date Switchyard Gateway's death to 1996–97 (Exchange and Notes SMTP, TCP/IP in Windows 95). We recommend harvesting it for cash and selling it if a buyer appears.
- **[E1] Pipe, then traffic, then index:** the traffic now exists, which is the case for A.
- **[E1] Value pools where the open protocol becomes usable:** Brandt argues this points to the browser and client, which Microsoft will contest, so we avoid that layer.
- **[E1] Next-capability tripwire:** we fund A's relevance-ranking research as a tripwire even if the board picks B.
- **[E1] Right science, right decade:** the handwriting corpus stays frozen.

### Most uncertain about
1. Whether ranking by usage and relevance beats portals and human directories, or whether audience owners (AOL, Yahoo, MSN) just build their own measurement.
2. Whether security, export controls and trust concerns stall Internet commerce past 1998.
3. Whether our enterprise reputation prevents us from hiring a Web-native team, which is a direct threat to Thesis A.
