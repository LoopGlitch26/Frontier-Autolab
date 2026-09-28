# Frontier Research Memo — Era E1 (January 1990)
*Department: Frontier Research. Sources limited to what was public before 1 Jan 1990.*

## Meeting transcript (condensed)

**Dr. Yuki Harada, Head of Frontier Research:** Two curves are bending that most of the market ignores. The first is TCP/IP. The NSFNET T1 backbone, more than 150,000 hosts, and the 1989 mail links from MCI Mail and CompuServe mean the "research network" is becoming the network that connects the other networks. The second is trainable pattern recognition. Bell Labs reading ZIP codes and ALVINN steering a van show that backprop networks do useful perception on ordinary hardware. The expert-system bust makes that second curve cheap to enter right now.

**Samuel Brandt, Technology Historian:** Past transitions say the standard that wins is usually the cheap, loosely specified one that already works, not the one committees and governments bless. That favors TCP/IP over GOSIP/OSI, and it is the same way the PC clones beat IBM's PS/2 plans. I disagree with Yuki on neural nets. AI has had two hype cycles already, and customers remember the Lisp machines. If we sell "AI," we get priced like Symbolics. If we sell "forms that key themselves," we get priced like a scanner vendor. That is less exciting, but it survives.

**Ines Varga, Futurist & Scenario Planner:** Here are my three scenarios for 1990–1995. (1) *Walled gardens win*: CompuServe, Prodigy and the new America Online grow, the NSF policy holds, and the Internet stays academic. (2) *Internetwork breakout*: the NSF lifts or works around its acceptable-use policy, commercial carriers peer, and offices wire their NetWare LANs to TCP/IP. (3) *Telco/ISDN path*: the Baby Bells win entry into information services and push ISDN plus Minitel-style terminals. My leading indicators are commercial mail gateways, the number of .com registrations, the price of Unix TCP/IP stacks for PCs, and any NSF policy change. I put scenario 2 at 45%, 1 at 35%, and 3 at 20%. That split is too close to bet the company on one proprietary service.

**Dr. Kofi Mensah, Research Scientist, Measurement:** My question is what nobody can measure yet. Nobody can say what is on the network, who is on it, or where a given document or person sits. There is no directory and no index, only word of mouth and FTP site lists. Paper has the same problem: fax and laser printers are booming, yet the contents of that paper cannot be searched or counted. Whoever makes networked information findable, or paper machine-readable, owns the data exhaust. I lean toward the network thesis because its data (directory and usage maps) compounds. A handwriting corpus compounds too, but more slowly.

**Harada:** Then we run both theses past the board and let Market & Capital tell us which one pays first.

**Brandt:** Agreed, as long as we are honest that thesis A is timing-dependent on Ines's scenario 2.

## DEPARTMENT RECOMMENDATION

### Thesis A — "The Internetwork Layer for the Office" (preferred)
- **Chain:** cheap 386 PCs + LANs + a TCP/IP backbone → offices adopt LANs at scale (NetWare) and email spreads → **bottleneck: the LANs are islands.** Mail formats and protocols don't interoperate, and nobody can find people, machines or documents across networks → **layer we own:** PC/LAN-to-TCP/IP gateway software plus a cross-network directory and index service → **data:** a map of addresses, hosts and published documents, with usage patterns → **next capability:** search and hypertext links across machines, a HyperCard-style experience spanning the network instead of one disk.
- **Why now:** commercial mail began exchanging with the Internet in 1989, the backbone is upgraded, OSI is stalling, and the 486 makes a PC a credible network node.
- **Wedge:** a NetWare-to-SMTP/TCP/IP mail and file gateway for mid-size firms that already have Internet-connected university or defense partners.
- **First customer:** engineering firms and defense contractors running Sun workstations alongside NetWare PCs, who need the two worlds to exchange mail and files.
- **Makes obsolete:** per-hour walled-garden services and proprietary LAN mail. Later, our own gateway becomes obsolete once TCP/IP ships inside every OS, so we must migrate from the gateway to the directory and index before that happens.

### Thesis B — "Paper-to-Data Recognition Engine"
- **Chain:** backprop networks on commodity DSP/386 → adoption through the booming fax, scanner and document-imaging markets and pen computing (GO, GRiDPad) → **bottleneck: human keypunching** of handwritten forms and faxes → **layer we own:** a licensable recognition engine/SDK for OEMs → **data:** the largest labeled handwriting and forms corpus → **next capability:** speech and general perceptual recognition as the same learning methods transfer.
- **Why now:** the Bell Labs results are public, compute is cheap enough, and AI talent is available at a discount after the expert-system collapse.
- **Wedge:** handwritten-digit and checkbox recognition for insurance claims and tax/census-style forms.
- **First customer:** insurers and form-processing bureaus, followed by pen-computer OEMs.
- **Makes obsolete:** keypunch bureaus and template-based OCR. Eventually our own engine becomes a commodity chip feature, so the corpus must be the moat.

### Playbook lessons applied
The Playbook is empty at founding. We propose these candidate heuristics for The Record to test:
1. *Bet on the open protocol that already works, not the blessed standard.*
2. *Own the layer that indexes, not only the pipe that connects.*
3. *Sell the outcome, never the buzzword.*

### What we are most uncertain about
- **Timing of Internet commercialization.** The NSF acceptable-use policy could keep thesis A in scenario 1 for five or more years, which would exhaust a $1.5M seed.
- **Whether neural recognition accuracy generalizes** beyond constrained digits to free handwriting at a price OEMs will pay.
- **Distribution power.** Novell or Microsoft could bundle TCP/IP and a directory and crush a gateway startup. That is why the durable asset has to be the index and data, not the connector.
