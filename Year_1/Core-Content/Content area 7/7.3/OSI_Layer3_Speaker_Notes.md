# OSI Model – Layer 3: Speaker Notes
*T-Level Digital Infrastructure | Network Layer*

---

## Slide 1 – Title Slide

Good morning/afternoon everyone. Today we're looking at Layer 3 of the OSI model — the **Network Layer**. This is one of the most important layers to understand because it's what actually gets data from one network to another. Everything from loading a website to sending an email depends on Layer 3 working correctly.

Worth flagging early on: Layer 3 doesn't exist in isolation. It maps directly onto the **Internet Layer** of the TCP/IP model, which is the model engineers actually use day to day. We'll cover that on the next slide.

---

## Slide 2 – OSI vs TCP/IP Model

One thing that confuses people is that there are *two* networking models — OSI and TCP/IP — and they don't have the same number of layers.

The **OSI model** has 7 layers and is mainly used as a teaching tool. It gives you a nice, clean way to think about how networking works.

The **TCP/IP model** has 4 layers and is the one actually implemented in real networks — it's what the internet runs on.

Layer 3 in OSI is the **Network Layer**. In TCP/IP, the equivalent is called the **Internet Layer**. They do the same job: logical addressing and routing packets across networks.

Any time you hear someone talk about "Layer 3 switches" or "Layer 3 routing" in a professional context, they mean this layer.

---

## Slide 3 – What is the Network Layer?

So what exactly does Layer 3 do? Four core jobs:

**Logical Addressing** — Every device that wants to communicate across networks needs a unique address. That's an IP address. Unlike a MAC address (which is hardcoded into your network card), an IP address is *logical* — it can be assigned and changed.

**Routing** — When you send data, it doesn't go directly to the destination. It hops through a series of routers. Layer 3 is responsible for figuring out which route to take.

**Packet Forwarding** — Once a route is chosen, each router forwards the packet to the next hop until it arrives.

**Fragmentation** — Different networks can carry different sized packets. If a packet is too big, Layer 3 breaks it up into smaller pieces (fragments) and the destination reassembles them.

Think of it like posting a parcel internationally — it might go through several sorting offices (routers), and if it's too big for a particular transport, it might get broken into smaller boxes.

---

## Slide 4 – Routing

Routing is how networks know *where* to send data. Routers maintain **routing tables** — essentially maps that say "to reach network X, send the packet out of this interface towards router Y."

There are two ways those tables get built:

**Static routing** — an admin types in the routes manually. Simple, no overhead, but doesn't adapt if something breaks. Fine for a small office with one internet connection.

**Dynamic routing** — routers talk to each other using routing protocols and automatically share information about the network. If a link goes down, they reroute automatically.

The three main dynamic routing protocols to know for T-level:

- **RIP** (Routing Information Protocol) — the oldest and simplest. Counts hops to choose a route. Maximum of 15 hops, so not suitable for large networks.
- **OSPF** (Open Shortest Path First) — used in most enterprise networks. Routers share a full map of the network and calculate the mathematically shortest path using Dijkstra's algorithm.
- **BGP** (Border Gateway Protocol) — this is what routes traffic across the entire internet. Internet Service Providers use BGP to tell each other which networks they can reach.

---

## Slide 5 – Logical Addressing

Every device on a network needs an IP address. There are two versions in use today:

**IPv4** — 32-bit address, written as four numbers separated by dots (e.g. 192.168.1.1). Only allows about 4.3 billion unique addresses. We've essentially run out globally, which is why IPv6 was developed.

**IPv6** — 128-bit address, written in hexadecimal (e.g. 2001:0db8::1). Allows 340 undecillion addresses — effectively unlimited. Also has a fixed-size header, which makes routing faster.

A few important related concepts:

**Subnetting** — dividing a network into smaller segments. For example, `/24` (or subnet mask 255.255.255.0) gives you 254 usable host addresses. This is heavily used in network design for security and efficiency.

**NAT** (Network Address Translation) — because IPv4 addresses ran out, most home and office networks use private IP ranges internally (e.g. 192.168.x.x) and NAT translates these to a single public IP when connecting to the internet. You don't need NAT with IPv6.

This is worth spending extra time on as subnetting frequently comes up in T-level and professional exams.

---

## Slide 6 – Quality of Service (QoS)

QoS is how networks prioritise certain types of traffic over others.

Think about what happens on a busy network — video calls, file downloads, and software updates all competing for bandwidth. Without QoS, a large file download could disrupt a VoIP call by hogging the connection.

The three problems QoS helps manage:

- **Packet loss** — packets that don't arrive. Particularly bad for VoIP where there's no time to retransmit.
- **Latency** — delay between sending and receiving. Under 150ms is acceptable for voice calls; above that and it becomes noticeable.
- **Jitter** — variation in delay. Even if average latency is fine, if some packets arrive 10ms late and others 200ms late, the audio becomes choppy.

QoS works by tagging packets with a priority level (using the DSCP field in the IP header) and giving high-priority traffic preferential treatment through router queues.

VoIP and video conferencing get the highest priority. File transfers and backups get the lowest — it doesn't matter if a backup takes 5 minutes longer.

---

## Slide 7 – Key Layer 3 Protocols

Let's run through the main protocols that operate at Layer 3. These are all worth knowing for your T-level assessments.

**IP (Internet Protocol)** — the foundation of everything. Provides addressing and routing. Importantly, IP is *connectionless* and *unreliable* — it doesn't guarantee delivery or order. That's deliberately left to Layer 4 (TCP). IP focuses purely on getting packets to the right destination.

**ICMP (Internet Control Message Protocol)** — used for diagnostics. When you run `ping`, you're sending ICMP Echo Request messages. When you run `traceroute`, routers along the path send ICMP Time Exceeded messages back. Routers also use ICMP to report errors like "destination unreachable."

**ARP (Address Resolution Protocol)** — when your computer knows the IP address of another device on the same network but needs its MAC address to actually send a frame, it broadcasts an ARP request: "who has IP 192.168.1.5?" The device responds with its MAC. Technically sits between layers 2 and 3.

**OSPF** — covered in routing slide, but key point: it's *open standard* (unlike Cisco's EIGRP), so it works across different manufacturers' equipment.

**BGP** — again covered earlier, but worth noting it's what makes the internet work. Any organisation with multiple ISPs uses BGP.

**NAT** — also sits between layers 3 and 4. Translates private addresses to public. A home router doing NAT is acting as a Layer 3 device.

---

## Slide 8 – Fragmentation & Reassembly

Each network technology has a **Maximum Transmission Unit (MTU)** — the largest packet it can carry. Ethernet's MTU is 1500 bytes. If a packet is larger than this, it must be fragmented.

How it works:
1. A router receives a packet too large for the next network link
2. It splits the packet into fragments, each with a *Fragment Offset* field (so the receiver knows the order) and a *More Fragments* flag (set to 1 on all but the last fragment)
3. All fragments travel independently to the destination (possibly via different routes)
4. The **destination** reassembles them — intermediate routers don't reassemble

Important IPv6 point: **IPv6 doesn't allow routers to fragment**. Instead, the sending host must use **Path MTU Discovery** — it finds out the smallest MTU along the entire route before sending, and sizes its packets accordingly. This is more efficient.

Real-world tip: Fragmentation is generally considered bad practice today because it adds overhead and increases the chance of packet loss (if one fragment is lost, the whole original packet must be retransmitted). Modern networks try to avoid it using Path MTU Discovery.

---

## Slide 9 – Summary

Quick recap before we move on:

Layer 3 is the Network Layer. Its four main jobs are **logical addressing**, **routing**, **packet forwarding**, and **fragmentation**.

It maps to the **Internet Layer** in TCP/IP — these two concepts describe the same real-world functionality.

IP addresses come in two flavours: **IPv4** (32-bit, nearly exhausted) and **IPv6** (128-bit, solves the exhaustion problem).

Routing can be **static** or **dynamic**, with OSPF and BGP being the most important dynamic protocols to know.

QoS protects time-sensitive traffic from latency and jitter on congested networks.

Any questions before we move on to Layer 4?

---

*End of Layer 3 notes*
