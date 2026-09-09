# CA7 & CA8 — Condensed Study Guide

---

## CONTENT AREA 7: Hardware, Software & Networks

---

### 7.1 — Hardware & Physical Devices

#### Computer Types
| Type | Key Trait |
|------|-----------|
| Desktop | Best performance/price ratio, upgradeable, desktop-class chip |
| Laptop | Portable, limited cooling/upgradeability, mobile chip = less powerful |
| Workstation | High-end desktop for intensive tasks (3D modelling, video editing) |
| Embedded System | Purpose-built for a single task (e.g. car ECU, thermostat) |
| Server | Runs services for clients on a network |

#### Core PC Components
| Component | Role |
|-----------|------|
| **CPU** | The "brain" — decodes and executes all instructions |
| **RAM** | Volatile high-speed workspace for active processes; lost on power loss |
| **Storage (HDD/SSD)** | Non-volatile — persists data between boots. SSD massively faster than HDD |
| **GPU** | Second processor for graphical calculations; offloads rendering from CPU |
| **Motherboard** | Connects everything; allows expansion cards (GPU, NIC) |
| **PSU** | Provides power to all components |
| **I/O** | Interfaces (USB, HDMI) for peripherals like monitors, keyboard, mouse |

> **Key distinction:** RAM is ~100,000× faster than SSDs but loses data without power. Storage is slow but persistent.

#### Input / Output / Sensors
- **Input:** Keyboard, mouse, touchscreen, microphone, scanner, motion/temperature sensors
- **Output:** Monitor, speakers, printer
- **Sensors:** Motion (detect presence), smoke/temperature (fire detection)

---

### 7.2 — Software & Utilities

#### Common Utility Software
- **File management** — organise/store files
- **Compression** — reduce file size for storage/transfer
- **Defragmentation** — reorganises HDD data so read heads access files faster (SSDs don't need this — no moving parts)
- **Package managers** — automate mass software install, keep dependencies correct, auto-update with security patches
- **Protection software** — antivirus, firewalls, intrusion detection

#### Code Development Tools (IDEs)
- **Syntax highlighting** — colour-codes code, makes errors visually obvious in real time
- **IntelliSense / autocomplete** — suggests completions as you type, catches errors before running
- **Debugger / Breakpoints** — pause execution at a chosen line, inspect variable values, step through code line by line
- **Screen design tools (SDTs)** — drag-and-drop UI building; generates the underlying UI code for you — speeds up prototyping

#### Compiler vs Interpreter
| | **Compiler** | **Interpreter** |
|--|--|--|
| How | Translates entire program to machine code **before** running | Translates and runs **line by line** at runtime |
| Speed | Faster at runtime (already translated) | Slower (translating as it runs) |
| Errors | All flagged before execution — won't run until fixed | Stops at the first error it hits |
| Use case | Performance-critical apps (games, OS) | Scripts, data processing, interpreted languages |
| Cross-platform | Must recompile per OS/architecture | Runs anywhere an interpreter exists |

---

### 7.3 — Networks

#### Network Types
| Type | Scope |
|------|-------|
| **PAN** | Personal devices, very short range (Bluetooth headphones, phone hotspot) |
| **LAN** | Local — home, classroom, office |
| **WAN** | Wide — the internet is a WAN connecting many LANs together |
| **VPN** | Not a physical network — encrypts traffic and masks IP via a private tunnel over an existing network |

#### Network Topologies
| Topology | Pros | Cons |
|----------|------|------|
| **Bus** | Cheap, simple, easy to extend | One cable break = whole network down past that point |
| **Star** | One cable down ≠ whole network down; switch manages bandwidth efficiently | Central switch failure = whole network down |
| **Ring** | Predictable, consistent performance | One break can affect the whole ring |
| **Mesh** | Extremely fault-tolerant, multiple paths between nodes | Very expensive, impractical at scale (exponentially more cables) |
| **Extended Star** | Scalable across buildings, reliable, lower latency | Costly (many switches), complex maintenance |
| **Wireless** | Flexible, mobile, easy to scale (just add APs) | Higher latency, lower security, interference from microwaves/walls/water |

#### Wired vs Wireless
| | **Wired (Ethernet)** | **Wireless (Wi-Fi)** |
|--|--|--|
| Speed | Faster, more stable | Fast but variable |
| Security | More secure (physical access needed) | Less secure if misconfigured |
| Latency | Lower | Higher |
| Flexibility | Limited to cable location | Mobile anywhere in range |
| Cost | More cables/switches | Fewer cables, buy APs |

#### Ethernet Cable Standards
| Cable | Speed | Notes |
|-------|-------|-------|
| Cat5 | 100 Mb/s | Largely obsolete |
| Cat5e | 1 Gb/s | Common in older installs |
| Cat6 | 1 Gb/s | Better interference rejection than Cat5e |
| Cat7 | 10 Gb/s | Shielded, used in data centres |
| Cat8 | 40–100+ Gb/s | High-end data centre use |

- **STP** = Shielded Twisted Pair — foil wrap around each pair blocks interference
- **UTP** = Unshielded Twisted Pair — no foil, cheaper, more common in homes/offices

#### Key Protocols
| Protocol | Port | Purpose |
|----------|------|---------|
| **HTTP** | 80 | Web browsing — unencrypted |
| **HTTPS** | 443 | Web browsing — encrypted + authenticated via TLS |
| **DNS** | 53 | Translates domain names → IP addresses |
| **TCP** | — | Reliable delivery — checks all packets arrive (web, files) |
| **UDP** | — | Fast, no delivery guarantee — used where speed > reliability (gaming, streaming, VoIP) |
| **SMTP** | 25 / 587 | Send email |
| **POP3** | 110 | Download email and remove from server |
| **IMAP** | 143 | Sync email — keeps messages on server |
| **FTP** | 21 | File transfer |
| **TLS** | — | Encryption layer used by HTTPS, email etc. (replaced SSL) |

> **TCP vs UDP in one line:** TCP is a recorded delivery parcel — every packet confirmed. UDP is a flyer through a letterbox — fast but no confirmation.

#### Bandwidth, Throughput & Latency
- **Bandwidth** — maximum theoretical capacity of a connection (e.g. 1 Gb/s)
- **Throughput** — the actual data transfer rate achieved in practice (always ≤ bandwidth)
- **Latency** — time for a single packet to travel from source to destination
  - Affected by: cable length, network congestion, quality of hardware

#### Compression
| Type | How | Trade-off | Examples |
|------|-----|-----------|---------|
| **Lossy** | Permanently discards some data | Massive size reduction, some quality loss | JPEG (images), MP3 (audio), H.264 (video) |
| **Lossless** | Stores patterns so original can be fully reconstructed | Smaller reduction, but no quality loss | PNG (images), FLAC (audio), ZIP (files) |

> Use lossy for streaming/sharing where file size matters. Use lossless where you need to preserve the exact original (e.g. medical imaging, archiving).

- **Codec** — compresses/decompresses video/audio (H.264, H.265, AV1)
- **Container** — wraps codec data + audio + metadata into one file (MP4, MKV, MP3)

#### OSI Model (7 Layers) — Know These!
| Layer | Name | Key Function | Example Protocols/Devices |
|-------|------|-------------|--------------------------|
| 7 | **Application** | User-facing apps | HTTP, DNS, FTP, SMTP |
| 6 | **Presentation** | Encryption/decryption (TLS), compression, data format translation | TLS, JPEG, ASCII |
| 5 | **Session** | Opens, manages, and closes sessions between devices; authentication | NetBIOS, RPC |
| 4 | **Transport** | Segments data, end-to-end delivery, error checking | TCP, UDP |
| 3 | **Network** | IP addressing, routing, fragmentation | IP, routers |
| 2 | **Data Link** | MAC addressing, error detection (CRC/checksums), flow control | Ethernet, switches |
| 1 | **Physical** | Raw bits over cables/Wi-Fi | Copper, fibre, hubs, cables |

**Mnemonic (top → bottom):** **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing  
**Mnemonic (bottom → top):** **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

#### OSI → TCP/IP Mapping
```
OSI 7 + 6 + 5  =  TCP/IP Application layer
OSI 4          =  TCP/IP Transport layer
OSI 3          =  TCP/IP Network layer
OSI 2 + 1      =  TCP/IP Network Access (Physical) layer
```

#### Data Encapsulation (sending data down the stack)
1. Layers 7–5 add application data
2. Layer 4 adds TCP/UDP headers (source/destination port)
3. Layer 3 wraps into packets, adds IP headers (source/destination IP)
4. Layer 2 wraps into frames, adds MAC addresses
5. Layer 1 transmits raw binary over the medium

> On the **receiving end**, decapsulation happens in reverse — each layer strips its own header and passes the data upward.

#### MAC vs IP Address
- **IP address** — logical, software-assigned address; gets packets to the right **network**
- **MAC address** — physical address burned into the NIC at manufacture; gets packets to the right **device on a LAN**
  - Format: `C8:7F:54:5D:58:C4` (6 hex pairs, 48 bits)

#### Routers, Switches & the Internet Backbone
- **Router** — routes packets **between networks** using IP addresses + routing tables (longest prefix match wins)
- **Switch** — switches packets **within a LAN** using MAC addresses; smarter than a hub
- **Internet backbone** — Tier 1 ISPs connected by ultra high-speed fibre globally. Tier 2 buys capacity from Tier 1. Tier 3 serves consumers.
- If backbone fails → higher latency (packets reroute around damage) or services become unreachable entirely

---

### 7.4 — Virtualisation & Hypervisors

#### What is a VM?
A software-based emulation of a physical computer — runs its own OS and apps on shared hardware. The physical host thinks it has multiple independent machines.

#### Hypervisor Types
| | **Type 1 (Bare Metal)** | **Type 2 (Hosted)** |
|--|--|--|
| Runs on | Directly on hardware | On top of an existing OS |
| Performance | Better — no OS overhead | Reduced — goes through host OS |
| Security | Higher — smaller attack surface | Lower |
| Setup | Complex, needs IT expertise | Easy, consumer-friendly GUI |
| Examples | Proxmox, KVM, VMware ESXi | VirtualBox, VMware Workstation |

#### Why Virtualise?
- Consolidate many physical servers onto fewer machines — lower hardware and power costs
- Easy snapshot/backup/restore of entire VMs
- Simpler monitoring and centralised management
- **Risk:** if one physical host goes down, all VMs on it go down → mitigated with clustering/live migration

---

### 7.5 — Client-Server Architecture

#### Client-Server vs Peer-to-Peer
| | **Client-Server** | **Peer-to-Peer (P2P)** |
|--|--|--|
| Control | Centralised — server manages everything | Distributed across all nodes |
| Cost | High — needs dedicated server hardware | Cheaper — just PCs |
| Security | Better — centralised control | Weaker — no central enforcement |
| Scalability | Scales well | Limited |
| Failure risk | Server down = everyone affected | No single point of failure |

#### Thin vs Thick Clients
| | **Thin Client** | **Thick Client** |
|--|--|--|
| Processing | Done on the server | Done on the device itself |
| Hardware needed | Low-spec terminal | High-spec machine |
| Examples | Web apps, Google Docs, cloud email | Photoshop, video games, video editing |

#### Architecture Tiers
- **2-tier** — client talks directly to server (e.g. a desktop app talking to a database)
- **3-tier** — client → application server → database server (separates logic from data)
- **N-tier** — further split for scalability (load balancers, caching layers, microservices)

---

### 7.6 — Resilient Systems

#### What Makes a System Resilient?
A resilient environment maintains operations and recovers quickly from failures, with minimal disruption to users. The goal is to eliminate **single points of failure (SPOF)** — any component whose failure alone takes everything down.

#### Standby Types
| Type | How | Failover time | Cost | Use case |
|------|-----|--------------|------|----------|
| **Hot standby** | Backup runs live simultaneously, shares load | Instant (seconds) | Highest | Mission-critical, zero downtime tolerated |
| **Warm standby** | Backup is running but not serving traffic until needed | Fast (seconds–minutes) | Medium | Important systems with brief interruption tolerated |
| **Cold standby** | Backup is offline until failure | Slow (minutes–hours) | Lowest | Non-critical systems |

#### Redundancy Types
- **Hardware redundancy** — multiple servers, dual power supplies, RAID arrays for drives
- **Network redundancy** — dual ISP connections, redundant switches/routers, multiple network paths
- **Data redundancy** — database replication across servers, data centre mirroring

> **Key principle:** Redundancy eliminates SPOFs. If one component's failure can bring down everything, that's a SPOF that needs to be addressed.

#### Load Balancing
Distributes incoming traffic across multiple servers so no single server gets overwhelmed.

**Benefits:** even traffic distribution, faster response times, if one server fails others continue serving requests

**Common algorithms:**
- **Round robin** — requests sent to each server in rotation; simple, works well when servers are similar
- **Least connections** — new request goes to whichever server has fewest active connections; better for varying workloads
- **IP hash** — same client always hits the same server; useful for session-based apps

#### Backup Types
| Type | What it backs up | Speed to back up | Speed to restore | Storage use |
|------|-----------------|-----------------|-----------------|-------------|
| **Full** | Everything, every time | Slowest | Fastest (one restore point) | Most |
| **Incremental** | Only changes since the last backup of any kind | Fastest | Slowest (need all incrementals + full) | Least |
| **Differential** | All changes since the last full backup | Medium | Medium (just full + latest differential) | Medium |

> **Typical strategy:** weekly full backup + daily incremental or differential.

#### 3-2-1 Backup Rule
- **3** copies of data
- **2** different storage media/types (e.g. local SSD + cloud)
- **1** copy stored offsite (different building, cloud, off-premises)

> Protects against ransomware (offline copy can't be encrypted), hardware failure, and physical disasters.

#### Geographic Distribution & CDNs
- **Geographic distribution** — systems deployed across multiple physical locations; a regional disaster (fire, flood, power cut) doesn't take everything down
- **CDN (Content Delivery Network)** — static content cached at edge locations globally; reduces load on the origin server and improves speed for distant users

#### Other Resilience Strategies
- **RAID arrays** — multiple drives so one failing doesn't lose data. **Not a backup replacement** — RAID won't save you from ransomware, accidental deletion, or fire
- **Redundant power supplies / dual NICs** — eliminates single hardware points of failure
- **Regular backup testing** — a backup that doesn't restore is worthless; test them regularly
- **Disaster recovery plan** — documented, rehearsed process for restoring services; everyone should know their role before an incident happens

#### Benefits of Resilience (for exam questions)
| Benefit | What it means |
|---------|--------------|
| **Business continuity** | Critical functions keep running during disruptions |
| **Reduced downtime costs** | Downtime costs enterprises thousands per minute — less downtime = less loss |
| **Customer satisfaction** | Reliable, always-on services build trust and loyalty |
| **Competitive advantage** | Outperform competitors who suffer frequent outages |
| **Regulatory compliance** | Meet GDPR, ISO 27001, PCI DSS requirements for availability and data protection |
| **Brand/reputation protection** | Prevents incidents that cause public trust to collapse |

---

### 7.7 — Cloud Computing

#### Service Models

The key concept: the higher the service model, the less you manage yourself.

| Model | Full Name | What you get | You manage | Provider manages |
|-------|-----------|-------------|------------|-----------------|
| **IaaS** | Infrastructure as a Service | Raw compute, storage, networking | OS, runtime, apps, data | Physical hardware, virtualisation, networking infrastructure |
| **PaaS** | Platform as a Service | An environment to build and deploy apps | Your application code and data | OS, runtime, middleware, hardware |
| **SaaS** | Software as a Service | A ready-to-use application | Nothing (just your data/settings) | Everything — software, updates, infrastructure |

> **Examples:** IaaS = AWS EC2 (a raw virtual machine). PaaS = Heroku, Google App Engine (deploy your code, everything else handled). SaaS = Gmail, Office 365, Dropbox.

> **Analogy:** IaaS is renting an empty warehouse (you fit it out). PaaS is renting a fitted workshop (tools provided, bring your project). SaaS is hiring a full service (turn up and use it).

#### Deployment Models
| Model | Description |
|-------|-------------|
| **Public** | Shared infrastructure (AWS, Azure, GCP) — pay-as-you-go, elastic scalability |
| **Private** | Dedicated hardware for one organisation — more control and security, higher cost |
| **Hybrid** | Mix of public + private — sensitive/regulated data stays private, scalable workloads use public |

#### Cloud Pros & Cons
**Pros:** Scale up/down on demand (elasticity), no upfront hardware cost, deploy globally fast, automatic updates, pay only for what you use

**Cons:** Internet dependency (no connection = no access), data sovereignty concerns (where is your data stored legally?), migration complexity, ongoing subscription costs add up

> **Key exam point:** A hybrid model is usually the right recommendation when a company has sensitive data — keeps regulated data private while using public cloud for scalable/non-sensitive workloads.

---
---

## CONTENT AREA 8: Data Security & Protecting Systems

---

### 8.1 — The CIA Triad

The three core principles of information security:

| Principle | Meaning | How to achieve it | Example failure |
|-----------|---------|-------------------|-----------------|
| **Confidentiality** | Data accessible only to authorised people | Encryption, access controls, data classification (public/internal/confidential/secret), physical security | Unencrypted database exposed in a breach |
| **Integrity** | Data is accurate, consistent, and trustworthy | Checksums/hashes, version control, audit trails, 3-2-1 backups, data validation | Attacker silently alters a transaction amount |
| **Availability** | Data accessible when needed by authorised users | Hardware maintenance, redundant systems, load balancing, failover, disaster recovery plan | DDoS attack takes a service offline |

---

### 8.2 — Threats & Vulnerabilities

#### IT Threat Types
| Threat | Description |
|--------|-------------|
| **Malware** | Umbrella term — includes viruses, worms, botnets, ransomware |
| **Ransomware** | Encrypts your data, demands payment for the decryption key |
| **Social engineering** | Manipulating humans psychologically rather than hacking systems technically |
| **Phishing** | Mass fake emails/messages designed to steal credentials or install malware |
| **Spear phishing** | Targeted phishing — attacker researches the victim for a personalised, convincing attack |
| **Pretexting** | Attacker fabricates a believable scenario (e.g. "I'm from IT") to extract information |
| **Baiting** | Leaving infected USB drives in public places hoping victims plug them in |
| **Tailgating** | Physically following someone through a secure door using their access — no card/fob needed |
| **Insider threats** | Employees or contractors stealing, leaking, or damaging data — intentionally or through negligence |
| **Supply chain attacks** | Malicious code inserted into a trusted vendor's software used by many organisations (e.g. SolarWinds) |
| **DDoS** | Flood a server with traffic from many sources to overwhelm and take it offline |
| **Zero-day exploits** | Attack using a vulnerability unknown to the vendor — no patch exists yet |

#### Human Factors
- **Human error** — unpatched systems, sending files to the wrong person (e.g. Equifax breach — 140 million records exposed due to an unpatched vulnerability)
- **Password mismanagement** — weak or reused passwords make credential stuffing easy; one breached site = all reused accounts at risk
- **Lack of training** — IBM study: 75% of untrained staff clicked a phishing link
- **Physical security failures** — lost fobs not deactivated, tailgating unchallenged

---

### 8.3 — Threat Mitigation

#### Firewalls
| | **Traditional Firewall** | **Next-Gen Firewall (NGFW)** |
|--|--|--|
| Inspects | Packet headers only (IP address + port number) | Full packet contents — Deep Packet Inspection |
| Can block | IP addresses, ports | Malware, specific applications, phishing URLs |
| Intelligence | Static rules | DPI, application awareness, IPS, live threat feeds |

**NGFW key features:**
- **Deep Packet Inspection (DPI)** — reads inside packets (not just headers) to detect malware and phishing
- **Application Awareness** — can block specific applications (Facebook, YouTube) regardless of port
- **Intrusion Prevention System (IPS)** — detects and actively blocks attacks in real time
- **Threat Intelligence feeds** — uses live data to identify and block known malicious traffic sources

#### Other Mitigation Techniques
| Technique | What it does |
|-----------|-------------|
| **Patch management** | Keeps OS/software updated — closes known vulnerabilities including zero-days once patched |
| **Security awareness training** | Trains staff to recognise phishing and social engineering; needs regular refreshing |
| **Network segmentation** | Splits network into isolated zones — breach of one zone can't automatically spread laterally |
| **Offline backups** | Backups disconnected from the network can't be encrypted by ransomware |
| **MFA (Multi-Factor Authentication)** | Requires a second proof beyond password — stolen passwords alone aren't enough |
| **Access controls** | Limit what each user can see and do; **principle of least privilege** — users get only what they need |
| **Audit trails / logs** | Record who changed what and when — essential for forensics and accountability |
| **Disciplinary policies** | Deterrent — clear consequences for policy violations |

#### Physical Security Controls
- **Access levels** — tiered access to rooms and systems by role (not everyone reaches the server room)
- **Security officers** — guard entry points, verify identity
- **CCTV** — monitor and deter; provides evidence post-incident
- **Fob/card systems** — log every entry and exit by named individual

---

### 8.4 — Access Controls & Authentication

#### File Permissions vs Access Levels
- **File permissions** — what a user can do *with a specific file* (read, write, execute)
- **Access levels** — what a user can do *on the system overall* (admin rights vs standard user)

#### Password Security
- Longer passwords = exponentially longer cracking time
- **Passphrases** (a short random sentence) are both strong and memorable — e.g. `correct-horse-battery-staple`
- Never reuse passwords across sites — one breach = all reused accounts compromised
- MFA adds a critical second layer even if the password is already stolen

#### IAAA Security Model
1. **Identification** — who are you? (username)
2. **Authentication** — prove it (password, MFA token, biometric)
3. **Authorisation** — what are you allowed to do? (permissions, role)
4. **Accountability** — log what you did (audit trail, timestamps)

---

### 8.5 — Data Protection & Backups

#### Implications of Poor Backup/Recovery
- Ransomware attack with no offline backup = permanent data loss
- GDPR fines for losing or exposing customer data
- Loss of business continuity — operations halt
- Reputational damage — customers and partners lose trust

#### Key Backup Practices
- Follow **3-2-1** (3 copies, 2 different media types, 1 offsite)
- **Test and validate backups** regularly — a backup that fails to restore is worthless
- **Offline backups** — immune to ransomware (unreachable from the network)
- **RAID** — hardware drive redundancy. Important: RAID is *not* a backup — it protects against drive failure, not accidental deletion, ransomware, or fire

---

### 8.6 — Real-World Case Study: Stuxnet

**What:** A highly sophisticated computer worm discovered in 2010 — widely considered the world's first cyber weapon.

**Target:** Iran's uranium enrichment facility at Natanz — specifically Siemens PLCs (Programmable Logic Controllers) controlling the centrifuges.

**How it worked:**
- Used **4 zero-day exploits** simultaneously — unprecedented at the time
- Spread via USB drives, network shares, and infected air-gapped systems
- Subtly altered centrifuge spin speeds to cause physical destruction while appearing normal
- Fed **false data** to monitoring systems so operators saw "all normal" as machines failed

**Attribution:** Widely attributed to a US–Israel joint operation ("Operation Olympic Games").

**Impact:** ~1,000 centrifuges destroyed; significantly set back Iran's nuclear programme.

**Why it matters for your exam:**
- First malware designed to cause **physical, real-world destruction**
- First confirmed **nation-state cyberwarfare** operation
- Proved cyber attacks can substitute for or complement conventional military action
- Raised critical awareness of **industrial/critical infrastructure vulnerabilities**
- Established cyberspace as a recognised domain of warfare

---

## Quick-Reference Summary

### OSI Layers Mnemonic
**Top → bottom (7→1):** **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing  
**Bottom → top (1→7):** **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

### Key Exam Scenarios — What to Recommend
| Scenario | Recommendation |
|----------|---------------|
| Company with sensitive data moving to cloud | **Hybrid** deployment |
| Hospital network needing max reliability | **Mesh** topology (or extended star) |
| Performance-critical software (game, OS) | **Compiler** |
| Script or data processing app | **Interpreter** |
| Company with 30 servers wanting to consolidate | **Type 1 Hypervisor** (Proxmox/KVM/ESXi) |
| Single point of failure data centre | **Geographic distribution + cloud backups** |
| Stopping ransomware data loss | **Offline 3-2-1 backups + patch management** |
| Stopping phishing attacks | **Staff training + MFA + email filtering (NGFW)** |
| Small office, no IT team, needs apps | **SaaS** — minimal management required |
| Dev team wants to deploy apps without managing servers | **PaaS** |
| Company needs full control over virtual machines | **IaaS** |

---

*Compiled from CA7 & CA8 notes — covers 7.1–7.7 Hardware/Networks/Cloud and 8.1–8.6 Security/CIA Triad/Threats/Mitigation/Stuxnet*
