# The Record — Reveal & Score, Era E1 (Jan 1990 – Dec 1995)
*Company call under review: Switchyard Systems — multi-protocol mail and address gateway, then cross-network directory, then inter-company document exchange. Thesis B (neural recognition) kept as a two-person option.*

## 1. What actually happened

**The open network won, faster and more completely than the board's 45% scenario.** Commercial ISPs appeared almost at once: UUNET and PSINet were selling commercial IP service by 1990–91, and the Commercial Internet Exchange (CIX) was formed in 1991 to route around the NSF acceptable-use policy. The 1992 Scientific and Advanced-Technology Act let NSFNET carry commercial traffic, and NSFNET itself was decommissioned on 30 April 1995 in favor of commercial backbones and exchange points. OSI/GOSIP faded, and OSI-heavy vendors such as Retix faded with it.

**The capability jump was the Web, not mail.** Tim Berners-Lee's WWW ran at CERN in late 1990 and was released publicly in 1991. NCSA Mosaic (1993) made it graphical and usable on PCs and Macs. Netscape was founded in April 1994, shipped Navigator that December, and its August 1995 IPO valued a 16-month-old company at roughly $2B+ on its first day. Yahoo (1994/95), Lycos, Excite, Infoseek and DEC's AltaVista (December 1995) turned "findability" into the index layer.

**Where value pooled in 1990–95:**
- **The desktop OS.** Windows 3.0 (1990), 3.1 (1992) and Windows 95 (August 1995) made Microsoft dominant. Windows 95 shipped TCP/IP built in, which ended the market for third-party PC stacks.
- **The router.** Cisco, which IPO'd in February 1990, became the defining infrastructure winner of the era.
- **Access.** UUNET, PSINet and Netcom (IPOs in 1994–95), plus AOL's growth to several million subscribers.
- **Late in the era, the browser and the index** (Netscape, Yahoo).

**The mail-gateway layer was real but transitional.** SMTP plus MIME (1992) became the lingua franca. Lotus bought cc:Mail (1991) and the mail-switch vendor SoftSwitch (1994), and was itself acquired by IBM in 1995. Novell shipped SMTP connectivity for MHS and bundled a directory, NDS, in NetWare 4 (1993). Microsoft built gateways into Microsoft Mail and announced Exchange. X.400 and X.500 never became commercial mass markets. The directory idea survived as LDAP (1993), and it was a feature of other people's products, not a standalone business. Kill criterion #2 (a vendor bundles SMTP gateways) was effectively triggered by 1993–95.

**Thesis B:** Lena's view of the science was right, but the payoff was decades away. Pen computing flopped: GO Corp folded in 1994 and the Apple Newton's (1993) handwriting recognition was widely mocked. LeCun's convolutional networks did reach production check reading through AT&T/NCR in the mid-to-late 1990s, but as a niche inside a large incumbent. A two-person option was about the right size.

**Capital:** the 1990–91 recession made 1991 a trough year for venture capital. A late-1991 Series A would have been hard, and on poor terms. The climate reversed sharply in 1994–95.

## 2. Scorecard

| Criterion | Score | Justification |
|---|---|---|
| Frontier accuracy | **7** | Correctly called TCP/IP over OSI, the collapse of the walled gardens and the recognition curve. The Frontier memo's "hypertext spanning the network / own the index" idea was the real jump, and the board dropped it. |
| Timing | **5** | The gateway window (1990–94) was real but short. The directory and document-exchange steps were premature by 3–5+ years, and the Series A was scheduled into the VC trough. |
| Layer choice | **4** | Chose translation between islands, a layer that melts when one protocol wins. Value pooled in the OS, routers, access providers and then the browser/index. The "on-ramp" pivot clause was the right hedge but was deferred to 1992. |
| Reinvention courage | **6** | Sensible founding discipline: rejected its own stack product and capped services. However, it bet on fragmentation lasting, which is the conservative reading of its own evidence, and it underweighted the scenario it thought most likely. |
| Hindsight leakage | **7** | Most of the reasoning is defensible from 1989 sources. Points off for a suspiciously unanimous TCP/IP consensus and for the precise "gateway dies when TCP/IP ships inside every OS" prediction. The Red Team did flag the first. |

**Overall era score: 55/100**

## 3. Simulated outcome
A real Switchyard would plausibly ship in 1990–91 and reach 40–80 paying sites and $3–6M in revenue by 1993. It would raise a smaller, dilutive A round in 1992, not late 1991. From 1993 its gateway margins would be compressed by Novell, Lotus and Microsoft bundling SMTP, and the directory product would not find buyers. If it executed the 1992 on-ramp pivot aggressively, it could become a regional business ISP, which is capital-intensive but acquirable. The modal outcome is **acquisition in 1994–96 for roughly $15–40M** by a messaging or networking vendor or an ISP consolidator. That is a respectable exit but not an era-defining company. There is a ~25% chance it stays a sub-scale integrator selling "connect the islands" after the islands have merged.

**Closest real-world analog:** **SoftSwitch Inc.**, an enterprise mail-switching and gateway vendor acquired by Lotus in 1994, with Retix as the cautionary OSI-side twin. The road the org considered and did not take, the on-ramp, corresponds to **UUNET/PSINet**.

## 4. Lessons (appended to playbook.md)
1. **Bridges expire when the standards war ends.** A translation layer between incompatible systems lasts only as long as the fragmentation. Date its death on day one and have the next layer funded before then.
2. **When an open "good-enough" protocol is winning, value pools where it becomes usable and ubiquitous.** That means the client, the access point, the router and the index, not the connection back to legacy islands.
3. **Your own memos' "next capability" line is often the real frontier.** When the org names the bigger jump (here, networked hypertext and the index) and then drops it for the safer wedge, keep a funded tripwire on it.
4. **Order of value: pipe, then traffic, then index.** Directories and indexes pay only once an open network is big. Before that they are features that incumbents bundle.
5. **Right science and the right decade are separate bets.** Keep a deep-curve option cheap, judge it on field accuracy, and don't let it set company strategy until the data and compute arrive.
