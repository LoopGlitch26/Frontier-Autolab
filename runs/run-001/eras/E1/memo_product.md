# E1 Memo: Product & Engineering (January 1990)

## Transcript

**Priya Nair, VP Engineering:** With $1.5M and under 20 people, chips, workstations and pen hardware are out. We ship software on floppies within 12 months, on hardware customers already own. I can staff a protocol stack or a recognition engine, not both.

**Jonah Reyes, Head of Product:** The real pull I see is the office that has a NetWare LAN full of PCs, two Sun workstations in engineering, and a fax machine that never stops. They ask why the PCs can't talk to the Suns and why someone still retypes faxed orders into dBASE. The wedge should be what that IT manager already swears about.

**Hana Kowalski, Principal Infrastructure Engineer:** The layer that's becoming unavoidable is TCP/IP, not OSI. Every Sun ships with it, NSFNET is growing fast, and MCI Mail and CompuServe now exchange mail with the Internet. Once commercial traffic is allowed, every LAN needs a gateway. I'd own the PC and Mac side of that connection.

**Leo Mbeki, Head of Developer Ecosystem:** Agreed on TCP/IP, but I'd warn against selling a closed stack at the price of a box. The protocols are public RFCs, universities pass around free implementations, and GNU shows where builders are heading. We win distribution by giving builders a programming interface they can build on, and we charge the enterprise for support, management and the mail gateway. On recognition, the Bell Labs ZIP-code result is real, but no neural-net developer ecosystem exists yet.

**Priya:** Leo, "give it away" is hard to finance on seed money with prime near 11%. I'd charge per site from day one.

**Jonah:** And Hana, you're betting on a policy change you don't control. The fax retyping pain exists today, and people will pay for it this quarter.

**Hana:** The fax is a transitional medium. If networked mail wins, forms arrive digital and your recognition business shrinks. That's exactly why I'd own the network layer.

## DEPARTMENT RECOMMENDATION

### Thesis A (primary): "The PC-to-Internet connectivity layer"
- **Capability:** cheap 386 PCs on office LANs, plus TCP/IP as a proven, open protocol suite running on the NSFNET T1 backbone.
- **Adoption:** mixed offices (NetWare PCs, Macs, Unix workstations) and universities that need shared files, mail and remote login across systems.
- **Bottleneck:** interoperability. DOS has no native TCP/IP, memory is tight under 640K, mail systems are proprietary silos, and support expertise is scarce.
- **Layer we own:** the TCP/IP stack and developer programming interface for DOS/Windows/Mac, plus an SMTP mail gateway between LAN mail and the Internet.
- **Data:** installed-base telemetry on network configurations, driver and card compatibility, and support tickets.
- **Next capability:** directory, routing and access services, meaning we become the on-ramp when commercial Internet access opens up.
- **Why now:** Internet mail interconnection happened in 1989, the ARPANET is being retired in favor of NSFNET, and no PC vendor owns the network under client-server.
- **Wedge:** a DOS TCP/IP kit with a mail gateway for NetWare shops, sold per site.
- **First customer:** university computing centers and engineering firms that run Sun alongside PCs.
- **Makes obsolete:** proprietary LAN mail islands, hourly-billed closed online services as the only way to reach people, and the OSI/GOSIP bet. We have no current business, but this would make obsolete our own Thesis B if it succeeds, because digital forms replace faxed ones.

### Thesis B (alternate): "Recognition engine for paper-to-database"
- **Capability:** backpropagation neural nets, which Bell Labs has shown can read handwritten digits, combined with faster 386/486 PCs.
- **Adoption:** the fax and laser-printer boom means offices are flooded with paper forms.
- **Bottleneck:** people retyping forms into databases.
- **Layer we own:** a recognition engine SDK that form-processing and database vendors embed.
- **Data:** a labeled corpus of real-world handwriting and fax images from customers.
- **Next capability:** full handwriting and document understanding, and input for pen computers if pen computing arrives.
- **Why now:** recognition accuracy has jumped in research, while commercial AI is out of favor, so talent and ideas are cheap.
- **Wedge:** numeric and checkbox field recognition for faxed order forms and claims forms.
- **First customer:** insurers and mail-order businesses doing high-volume data entry.
- **Makes obsolete:** data-entry bureaus and the keyboard as the only way data gets in.

### Playbook lessons applied
The Playbook is empty at founding, so there are no tags to cite. Instead we propose working principles for The Record to test:
- **Own the open standard's missing layer, not the standard itself.** TCP/IP is free, and the value lies in making it usable.
- **Bet on the medium that replaces the pain, not the pain.** This is Hana's argument against fax-centric products.

We argue against the "AI comeback" framing as the lead bet. The curve is bending in research, but the adoption infrastructure (data, compute, buyers) isn't there yet.

### What we are most uncertain about
1. **Timing of commercial Internet access.** If the NSF acceptable-use policy holds for five or more years, Thesis A stays a niche university product.
2. **Whether Microsoft or Novell bundles TCP/IP** into the operating system or NetWare, which would commoditize our stack.
3. **Business model.** Priya wants to sell licenses and Leo wants a free core with paid services. We have not resolved this.
4. **Neural-net robustness** on noisy fax images outside the lab (Thesis B).
