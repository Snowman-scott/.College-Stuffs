# T Level Digital — Full Study Guide: CA1–CA8

---

## CONTENT AREA 1: Problem Solving

---

### 1.1 — Computational Thinking

The four core techniques for breaking down problems:

| Technique | What it means |
|-----------|--------------|
| **Decomposition** | Break a big problem into smaller, more manageable sub-tasks — each can be tackled separately |
| **Abstraction** | Hide unnecessary detail — only expose what's relevant to the current level (e.g. a user doesn't need to know how HTTP works to use a browser) |
| **Pattern Recognition** | Spot common structures or solutions across different problems — reuse what already works |
| **Algorithmic Thinking** | Define a clear, step-by-step set of instructions that solves the problem |

#### Top-Down vs Bottom-Up Design
- **Top-down** — start with the big picture, break it into subtasks, then break each subtask further (decomposition driven)
- **Bottom-up** — different people or teams build individual components independently, then combine them into a working whole

#### Modularisation
Breaking code into **functions/modules**. Each module does one job. Benefits: easier to test, reuse, debug, and maintain. Teams can work on separate modules simultaneously.

---

### 1.2 — Program Structures

| Structure | What it does | Example |
|-----------|-------------|---------|
| **Sequence** | Instructions execute in the order they're written | Line 1, then line 2, then line 3 |
| **Selection** | Code branches based on a condition | `if`, `elif`, `else` |
| **Iteration** | Code repeats | `for` loop, `while` loop |
| **Recursion** | A function that calls itself until a base condition is met — acts like a loop but self-referential |

#### For vs While Loops
| | **For loop** | **While loop** |
|--|--|--|
| Best when | You know exactly how many iterations are needed | You repeat until a condition changes (unknown count) |
| Risk | Overruns if length check is wrong | Infinite loop if condition never becomes false |

---

### 1.3 — Variables, Constants & Scope

- **Variable** — a named store of data that can change during program execution
- **Constant** — a named store of data that is set once and never changes (e.g. `PI = 3.14159`)

| | **Local Variable** | **Global Variable** |
|--|--|--|
| Where declared | Inside a function/block | Outside all functions (program level) |
| Where accessible | Only within that function | Anywhere in the program |
| Memory | Freed when function ends | Persists for the entire program runtime |
| Risk | None — changes stay contained | Any function can change it unexpectedly → harder to debug |

> **Rule:** Use local variables by default. Only use globals when data genuinely needs to be shared across the whole program (e.g. app settings, read-only constants).

---

### 1.4 — Pseudocode

A structured, plain-English way of writing an algorithm — not tied to any real language. Exam uses specific keywords:

```
SET variable TO value
INPUT variable
OUTPUT "text"
IF condition THEN
    ...
ELSE IF condition THEN
    ...
ELSE
    ...
END IF
FOR x FROM 0 TO 9
    ...
END FOR
WHILE condition
    ...
END WHILE
DEFINE functionName parameter
    ...
    RETURN value
END DEFINE
CALL functionName
```

---

### 1.5 — Data Validation

Validation = checking input meets expected rules **before** processing it.

| Check | What it does | Example |
|-------|-------------|---------|
| **Presence check** | Ensures a field isn't left empty | Username must not be blank |
| **Length check** | Verifies input is the right length | Password must be 8–20 characters |
| **Type check** | Ensures input is the correct data type | Age must be an integer, not a string |
| **Format check** | Checks input matches a required pattern | Date must be DD/MM/YYYY |
| **Range check** | Confirms input falls within acceptable limits | Age must be between 0 and 120 |
| **Constraint check** | Verifies additional rules/restrictions | Password must contain a special character |
| **Check digit** | Mathematical check — validates numbers like barcodes and ISBN codes | Last digit of a barcode validates the others |

---

### 1.6 — Testing Types

| Test Type | What it tests |
|-----------|--------------|
| **Unit test** | A single function or module in isolation |
| **Integration test** | Multiple functions/modules working together |
| **System test** | The entire system end-to-end |
| **Boundary test** | Values at the exact edges of acceptable ranges (and just outside) |
| **Erroneous test** | Invalid inputs the code should reject gracefully |
| **Regression test** | Confirms that new features or bug fixes haven't broken anything that already worked |
| **Acceptance/Usability test** | Tests with real end-users to confirm the system meets requirements in practice |
| **Performance/Load/Stress test** | Tests how the system behaves under high load or limited resources |
| **Concept test** | Testing feasibility before building the full product (avoid wasted effort) |

#### Test Data Types (Boundary Testing)
- **Normal** — valid data well within the expected range
- **Extreme/Boundary** — valid data at the very edge of the range (should still work)
- **Erroneous** — data outside/above the range (should be rejected with an error)

---

### 1.7 — Code Quality

| Quality | What it means |
|---------|--------------|
| **Reliable** | Produces correct, logical output consistently |
| **Robust** | Doesn't crash when given unexpected or invalid input |
| **Maintainable** | Code is clean, readable, well-commented, and easy for others to understand and modify |

#### Naming Conventions
- **Snake_case** — `my_variable`, `calculate_area` (common in Python)
- **camelCase** — `myVariable`, `calculateArea` (common in JavaScript/Java)
- **PascalCase** — `MyClass`, `CalculateArea` (common for class names)

---

### 1.8 — Libraries

Pre-written collections of code that provide ready-to-use functions.

- **Open source** — free to use, inspect, and modify (e.g. NumPy, requests)
- **Proprietary/Patented** — requires a licence or payment to use

> **Risks:** libraries can have poor documentation, outdated code, security vulnerabilities, or malicious code (e.g. crypto-miners) — always vet what you import.

---

### 1.9 — Sorting & Searching Algorithms

#### Searching
| Algorithm | How it works | When to use | Time complexity |
|-----------|-------------|-------------|-----------------|
| **Linear search** | Check each item one by one from start to end | Unsorted data | O(n) |
| **Binary search** | Repeatedly halve the search space; requires sorted data | Large sorted datasets | O(log n) |

#### Sorting
| Algorithm | How it works | Time complexity | Notes |
|-----------|-------------|-----------------|-------|
| **Bubble sort** | Repeatedly swap adjacent elements until sorted | O(n²) | Simple but very slow on large datasets |
| **Insertion sort** | Build a sorted list by inserting each element in the right position | O(n²) | Better than bubble for nearly-sorted data |
| **Merge sort** | Divide into halves recursively, then merge sorted halves | O(n log n) | Efficient for large datasets |

> **Exam answer:** For a large unsorted dataset — sort with **merge sort** (O(n log n)), then search with **binary search** (O(log n)). Never linear search a large dataset when a sort + binary is possible.

---

## CONTENT AREA 2: Introduction to Programming

---

### 2.1 — Data Types

| Data Type | What it stores | Example |
|-----------|---------------|---------|
| **Integer** | Whole numbers, no decimal | `42`, `-7`, `0` |
| **Real / Float** | Numbers with decimal places | `3.14`, `68.5`, `-0.001` |
| **Boolean** | True or False only | `True`, `False` |
| **String** | Text — a sequence of characters | `"Hello"`, `"42"`, `""` |
| **Character** | A single character | `'A'`, `'9'`, `'!'` |
| **Date** | A date value | `15/03/2026` |
| **BLOB** | Binary Large Object — stores binary data like images, videos, audio files | A JPEG image in a database |

> **Key distinctions:** Use `Real` not `Integer` for product prices (they have decimals: £24.99). Use `Integer` for stock quantities (you can't have 1.5 items). Use `Boolean` for yes/no flags like "Is Premium Member?". Use `BLOB` for images, scans, and media stored in a database.

---

### 2.2 — File Saving & Secondary Storage

Computers save data to files on **secondary storage** (HDD/SSD) because:
- RAM is **volatile** — data is lost when power is removed
- Secondary storage is **non-volatile** — persists after shutdown

#### Why save to files?
Configuration, game saves, user accounts, website caches, preferences — anything that needs to survive a reboot.

#### Common File Extensions
- **General data:** `.json`, `.xml`, `.csv`, `.dat`, `.bin`
- **Config:** `.cfg`, `.ini`, `.env`
- **Game saves:** `.sav`, `.ess`, `.gvas`, `.mcr`

---

### 2.3 — Object-Oriented Programming (OOP) Concepts

| Concept | What it means |
|---------|--------------|
| **Class** | A blueprint/template defining attributes and methods |
| **Object** | An instance of a class (a specific thing made from the blueprint) |
| **Encapsulation** | Bundling data and methods together; hiding internal details |
| **Inheritance** | A child class inherits attributes and methods from a parent class |
| **Polymorphism** | Same method name behaves differently depending on the object it's called on |

---

## CONTENT AREA 3: Emerging Issues

---

### 3.1 — Acceptable Use Policies (AUPs)

An **AUP** is a set of rules governing acceptable use of an organisation's systems, networks, and digital resources.

**Purpose:**
- Protect infrastructure from misuse and damage
- Reduce the risk of security breaches and unauthorised access
- Set clear expectations for users

**Key ethical principles covered by an AUP:**
- **Privacy** — don't access others' files or data without permission
- **Security** — use encryption and strong authentication for sensitive data
- **Accuracy & Honesty** — no fake accounts, misinformation, or data manipulation

#### Internet Filtering
| | Pros | Cons |
|--|------|------|
| Filtering | Stops inappropriate/illegal content, keeps students focused, protects the organisation from liability | Can block legitimate educational sites (over-aggressive blacklisting), can disrupt learning |

---

### 3.2 — Ethics in Computing

| Ethical Area | Description |
|-------------|-------------|
| **Digital divide** | Unequal access to technology and the internet — e.g. remote regions of Africa with no internet infrastructure |
| **Online privacy** | People's right to control their personal data online; tension with surveillance |
| **Internet censorship** | Governments blocking content — e.g. China, North Korea. Prevents citizens accessing information about their country or the world |
| **Encryption backdoors** | Governments wanting access to encrypted messages — trade-off between catching criminals/terrorists and mass surveillance of ordinary citizens |
| **Netiquette** | Good internet etiquette — respectful, honest online behaviour |
| **Online harassment** | Trolling, cyberbullying, hate speech (e.g. Gamergate 2014 — targeted harassment of women in gaming, including death threats and forced displacement) |

---

### 3.3 — Globalisation of IT

**Globalisation** = the world becoming more economically and digitally interconnected.

**Impact of IT globalisation:**
- Increased international trade and multinational corporations
- Cheaper product manufacturing overseas (outsourcing)
- Global data storage — easier access but greater breach risk in less secure jurisdictions
- **Positive:** more countries connected → more communication, collaboration, economic growth
- **Negative:** outsourcing = fewer local IT jobs, digital divide, data crossing borders into weaker regulatory environments

---

### 3.4 — Professional Development in IT

**Why it matters:**
- IT evolves rapidly — professionals must keep skills current
- Out-of-date staff → compatibility issues, slower systems, increased security vulnerabilities

| Standard Type | Examples |
|--------------|---------|
| **Technical standards** | Python, Java, TCP/IP protocols, HTML/CSS, SQL |
| **Professional standards** | BCS Code of Conduct, IEEE Code of Ethics, professional body membership |

**Professional development routes:** formal certifications (CompTIA, Cisco, Microsoft), CPD (Continuing Professional Development), conferences, self-study.

---

## CONTENT AREA 4: Legislation & Regulatory Requirements

---

### 4.1 — Key Laws & Regulations

| Legislation | What it covers | Key points |
|-------------|---------------|------------|
| **GDPR** (General Data Protection Regulation) | How organisations collect, store, and process personal data of EU/UK citizens | Must have legal basis; consent required; right to erasure; breach must be reported within 72 hrs; fines up to €20M or 4% global turnover |
| **CCPA** (California Consumer Privacy Act) | US equivalent of GDPR for California residents | Right to know, right to delete, right to opt out of data sale |
| **Computer Misuse Act 1990** | Criminalises unauthorised access to computer systems | 3 offences: unauthorised access, unauthorised access with intent, unauthorised modification of data |
| **Consumer Contracts Regulations 2013** | Protects online shoppers | 14-day cooling-off period for online purchases — right to cancel without reason |
| **Consumer Rights Act 2015** | Rights for goods and digital content | Goods must be satisfactory quality, fit for purpose, as described — applies to digital content |
| **PCI DSS** | Industry standard for handling payment card data | Any business processing card payments must maintain secure systems |
| **Data Localisation Laws** | National laws requiring data to be stored/processed within a country's borders | Ensure data stays subject to national law; complicate global cloud storage strategies |

---

### 4.2 — Data Localisation

Laws requiring personal data to be **stored, processed, and/or kept physically within a country's borders**.

**Challenge for organisations:** If a company uses AWS (US-based), data may physically sit in another country's jurisdiction. Some governments require data about citizens to stay domestic.

---

## CONTENT AREA 5: Business Context

---

### 5.1 — Industry Sectors

| Sector | Type | What they do | UK Example |
|--------|------|-------------|-----------|
| **Primary** | Extract raw materials | Farming, mining, fishing | British Sugar |
| **Secondary** | Manufacture goods | Car manufacturing, construction | Jaguar Land Rover |
| **Tertiary** | Provide services | Retail, banking, healthcare | Tesco |
| **Public** | Government-funded services | Healthcare, education | NHS |

#### IT's Impact by Sector
- **Primary (British Sugar):** IBM AI partnership, digital twin factory, private 4G network for real-time monitoring, automated storage/retrieval → 20% faster data analysis, 25% faster decisions
- **Secondary (JLR):** NVIDIA DRIVE platform, ADAS (radar + camera processing every 20ms), in-house OS development, DGX for AI model training
- **Tertiary (Tesco):** "Scan as You Shop" — 359 stores, 10M+ transactions/month, self-service checkouts, Clubcard loyalty data for targeted marketing
- **Public (NHS):** 90% of trusts using Electronic Patient Records (EPRs), telemedicine growth, NHS App, virtual wards — EPRs linked to 3.5% reduction in sepsis mortality

---

### 5.2 — IT in Business Functions

| Function | What IT does |
|----------|-------------|
| **Human Resources** | HRIS (Workday, SAP SuccessFactors) — employee records, payroll; ATS for recruitment; LMS for training |
| **R&D** | CAD software (SolidWorks, AutoCAD), HPC clusters for simulation, Git for version control, Jira for project management |
| **Logistics** | WMS (Warehouse Management), TMS (Transport Management), ERP (SAP), GPS/barcode scanners for real-time tracking |
| **Marketing** | CRM (Salesforce), email automation (HubSpot), social media management (Hootsuite), Google Analytics |
| **Finance** | Accounting software (QuickBooks, Xero), ERP finance modules, BI tools (Power BI), Hardware Security Modules for transaction security |
| **Management** | ERP dashboards, project management (Asana, Trello), video conferencing (Teams/Zoom) for real-time decision-making |

---

### 5.3 — E-Commerce

**E-commerce** = buying and selling goods or services over the internet.

#### Business Models
| Model | Description | Example |
|-------|-------------|---------|
| **B2C** | Business sells to individual consumers | Amazon, ASOS |
| **B2B** | Business sells to other businesses | Alibaba, wholesale suppliers |
| **C2C** | Consumer sells to consumer via a platform | eBay, Depop, Facebook Marketplace |
| **C2B** | Individual provides services to a business | Fiverr freelancers, stock photography sites |

#### Advantages/Disadvantages
**For customers:**
- ✅ Cheaper prices via comparison, available 24/7, access to niche products, no travel needed, consumer reviews, wider range
- ❌ Can't try products first, fraud/phishing risk, delivery delays, misleading listings, no face-to-face advice

**For businesses:**
- ✅ Global reach, lower overheads (no physical store costs), 24/7 sales, data analytics, easy scaling
- ❌ High competition, complex logistics/returns, website maintenance costs, cybersecurity risks, customer trust harder to build

#### Brick and Click
A business with **both** a physical store and an online presence.
- **Examples:** Argos, John Lewis, Currys, Tesco
- **Advantages:** click-and-collect, wider reach, flexible returns, physical trust + digital reach
- **Disadvantages:** higher costs (physical + digital), complex inventory sync across channels

---

### 5.4 — Key IT Systems in E-Commerce
- **Online storefront** — Shopify, WooCommerce, custom-built — must be responsive and fast
- **Payment processing** — Stripe, PayPal, WorldPay — must use SSL/TLS and comply with PCI DSS
- **DBMS** — stores products, orders, customers (MySQL, PostgreSQL)
- **CRM** — tracks customer interactions, history, preferences (Salesforce, HubSpot)
- **Inventory Management** — real-time stock tracking, auto-reorder triggers
- **Analytics** — Google Analytics tracks traffic, conversions, demographics
- **Security** — SSL certs, 2FA, GDPR compliance tools, firewalls

---

### 5.5 — Streaming Services Impact

#### TV/Film Streaming
- 20M+ UK households subscribed to at least one service
- Traditional broadcast TV viewing down 30%+ since 2010
- Mass-audience programmes halved between 2014 and 2022
- Binge-watching normalised; scheduled TV largely abandoned by under-25s

**Key services (UK, 2026):**
| Service | Cheapest Plan | 4K | Live Sport | Unique Strength |
|---------|--------------|-----|-----------|-----------------|
| Netflix | £5.99/mo (ads) | Premium (£18.99) | No | Broad originals |
| Disney+ | £5.99/mo (ads) | Premium (£14.99) | No | Disney/Marvel/Star Wars |
| Amazon Prime Video | £5.99/mo (ads) | Included | Yes (Champions League) | Bundled with Prime delivery |

#### Music Streaming (Spotify)
- 100M+ tracks, 6M podcasts
- Pays artists ~£0.003 per stream — only 0.4% of artists earn a living from streaming alone
- **Positive impact:** reduced piracy, global reach, new artist discovery, industry revenue recovery (£1B+ UK annually)
- **Negative impact:** devalues individual songs, favours major artists, algorithm homogenisation, "playlist gatekeeping"

---

### 5.6 — IT Impact on Key Sectors

| Sector | Key IT impact |
|--------|--------------|
| **Financial services** | Mobile banking, contactless payments, digital-only banks (Monzo, Revolut), AI fraud detection, algorithmic trading, Open Banking APIs |
| **Education** | VLEs (Google Classroom, Moodle), MOOCs (Coursera), gamification (Kahoot), AI tutoring, remote/hybrid learning (Zoom/Teams) |
| **News & Information** | 24/7 online news, citizen journalism via smartphones, social media news (filter bubbles), decline of print media |
| **Productivity software** | Cloud suites (Google Workspace, Microsoft 365), project management (Jira, Asana), SaaS subscription model, AI coding assistants |
| **Booking systems** | Online travel (Skyscanner, Booking.com), digital boarding passes, restaurant booking (OpenTable), GP appointments (NHS App), real-time availability |

---

### 5.7 — System Changeover Methods

When an organisation switches from an old system to a new one:

| Method | How | Pros | Cons |
|--------|-----|------|------|
| **Direct** | Old system off, new system on instantly | Fast, cheap, no duplication | High risk — no fallback if new system fails |
| **Parallel running** | Both systems run simultaneously | Safe — can compare and fall back | Expensive, double the workload |
| **Pilot** | New system rolled out to one small group first | Low risk, early feedback | Doesn't test full load; selected group may not be representative |
| **Phased** | New system rolled out in stages by function or department | Gradual, manageable | Takes time; parts of org on different systems |

> **Exam tip:** Direct changeover is best when switching from paper-based to digital (low risk — can literally just go back to paper). Parallel is best for high-stakes systems like payroll.

---

### 5.8 — Transactional Data, Targeted Marketing & Collaborative Working

#### Transactional Data
Every recorded transaction (purchase, booking, return). Used for: stock management, fraud detection, trend analysis, customer profiling, regulatory compliance.

#### Targeted Marketing
Using customer data to send relevant ads/offers rather than blanket messaging.
- **Segmentation** — group customers by demographics, behaviour, interests
- **Retargeting** — ads follow users who viewed but didn't buy
- **Loyalty programmes** — Tesco Clubcard analyses what you buy → personalised vouchers
- **A/B testing** — compare two versions of an ad/page to pick the better one
- **Ethical concern:** GDPR requires consent; customers may feel surveilled

#### Collaborative Working Tools
| Tool type | Examples | What it enables |
|-----------|---------|----------------|
| Cloud documents | Google Docs, Microsoft 365 | Real-time co-editing with version history |
| Video conferencing | Zoom, Teams, Meet | Face-to-face from anywhere |
| Messaging | Slack, Teams, Discord | Persistent channels, faster than email |
| Project management | Trello, Asana, Jira | Task tracking, deadlines, accountability |
| Version control | Git, GitHub | Track code changes, team development |

---

## CONTENT AREA 6: Data

---

### 6.1 — Data Types

*(See CA2 table — same types apply: Integer, Real, Boolean, String, Character, Date, BLOB)*

> **Choosing the right type matters:** Using `Integer` for body temperature instead of `Real` loses the decimal → could represent 38°C as 38 instead of 38.5, clinically dangerous. Using `String` for a Boolean `is_admitted` wastes memory and allows invalid values.

---

### 6.2 — Structured vs Unstructured Data

| | **Structured** | **Unstructured** |
|--|--|--|
| Format | Predefined schema — rows and columns | No fixed format |
| Storage | Relational databases (MySQL, PostgreSQL) | Files, documents, media (cloud storage) |
| Search/Query | Easy — SQL queries | Hard without AI/NLP |
| Examples | Customer ID, stock quantity, price, date | Doctor's notes, emails, social media posts, X-rays, audio, video |

#### Quantitative vs Qualitative
- **Quantitative = Structured** — numerical, measurable (age, salary, blood pressure) — can run maths and stats on it
- **Qualitative = Unstructured** — descriptive, opinion-based (review comments, interview transcripts) — needs interpretation

---

### 6.3 — How Organisations Use Data

#### System Performance Analysis
E.g. a streaming service with 7–10 PM buffering spikes:
- **Analyse:** CPU usage, memory utilisation, concurrent users, bandwidth
- **Act:** Auto-scaling (add servers at peak times), load balancing across multiple servers

#### Pattern Analysis
E.g. 60% of nappy buyers also buy baby food:
- **Cross-sell:** Offer baby food coupon when nappies are scanned
- **Targeted email:** Send nappy discount to baby food buyers who don't yet buy nappies there

#### User Monitoring & Security Analysis
E.g. account logged in from London at 9am, New York at 9:30am:
- **Impossible travel** → credentials compromised → lock account immediately, force password reset, enforce MFA

#### Employee Monitoring
- **Tools:** Keyloggers, screen capture, CCTV, badge tracking, productivity reports
- **Reason:** Verify work completion, protect trade secrets, ensure compliance
- **Ethical concern:** Privacy vs security; GDPR still applies to employee data

---

### 6.4 — IAAA Security Model

1. **Identification** — state who you are (username)
2. **Authentication** — prove it (password, MFA token, biometric)
3. **Authorisation** — system checks what you're allowed to access (role-based access control / RBAC)
4. **Accountability** — every action is logged (audit trail with timestamp, user, device, IP, success/failure)

#### MFA (Multi-Factor Authentication) Options
| Option | Security | How |
|--------|---------|-----|
| **SMS code** (Option A) | Good | Code sent to registered phone — attacker needs your number |
| **Authenticator app + PIN** (Option C) | Better | Physical token + user PIN — two factors |
| **Authenticator app + fingerprint** (Option B) | Best | Password + app + biometric — attacker needs all three |

#### RBAC (Role-Based Access Control)
Users are assigned a **role** (receptionist, doctor, admin) that grants access only to what that role needs. A receptionist can book appointments but cannot view surgical records.

#### Audit Logs
Should capture: **who** performed the action, **what** action was performed, **when** (timestamp), **where** (device/IP), and **whether it succeeded or failed**.

---

### 6.5 — Workplace Monitoring

**Definition:** Using digital tools to observe employee activity at work.

| Tool | What it monitors |
|------|----------------|
| Keyloggers | Every keystroke typed |
| Screen capture | What's on-screen at intervals |
| CCTV | Physical location and behaviour |
| Badge tracking | Entry/exit times and locations |
| Network monitoring | Websites visited, data transferred |

**Employer reasons:** productivity assurance, IP/data protection, GDPR compliance
**Ethical issues:** invasion of privacy, reduced morale, power imbalance

---

## CONTENT AREA 7: Digital Environments

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
- **Defragmentation** — reorganises HDD data so read heads access files faster (SSDs don't need this)
- **Package managers** — automate mass software install, keep dependencies correct, auto-update with security patches
- **Protection software** — antivirus, firewalls, intrusion detection

#### Code Development Tools (IDEs)
- **Syntax highlighting** — colour-codes code, makes errors visually obvious
- **IntelliSense / autocomplete** — suggests completions as you type, catches errors before running
- **Debugger / Breakpoints** — pause execution at a chosen line, inspect variable values
- **Screen design tools (SDTs)** — drag-and-drop UI; generates underlying UI code — speeds up prototyping

#### Compiler vs Interpreter
| | **Compiler** | **Interpreter** |
|--|--|--|
| How | Translates entire program to machine code **before** running | Translates and runs **line by line** at runtime |
| Speed | Faster at runtime | Slower (translating as it runs) |
| Errors | All flagged before execution | Stops at the first error it hits |
| Use case | Performance-critical apps (games, OS) | Scripts, data processing, interpreted languages |
| Cross-platform | Must recompile per OS/architecture | Runs anywhere an interpreter exists |

---

### 7.3 — Networks

#### Network Types
| Type | Scope |
|------|-------|
| **PAN** | Personal devices, very short range (Bluetooth, phone hotspot) |
| **LAN** | Local — home, classroom, office |
| **WAN** | Wide — the internet is a WAN connecting many LANs together |
| **VPN** | Encrypts traffic and masks IP via a private tunnel over an existing network |

#### Network Topologies
| Topology | Pros | Cons |
|----------|------|------|
| **Bus** | Cheap, simple, easy to extend | One cable break = whole network down past that point |
| **Star** | One cable down ≠ whole network down; switch manages bandwidth | Central switch failure = whole network down |
| **Ring** | Predictable performance | One break can affect the whole ring |
| **Mesh** | Extremely fault-tolerant, multiple paths | Expensive, impractical at scale (exponentially more cables) |
| **Extended Star** | Scalable across buildings, reliable | Costly, complex maintenance |
| **Wireless** | Flexible, mobile | Higher latency, lower security, interference from microwaves/walls |

#### Wired vs Wireless
| | **Wired (Ethernet)** | **Wireless (Wi-Fi)** |
|--|--|--|
| Speed | Faster, more stable | Fast but variable |
| Security | More secure (physical access needed) | Less secure if misconfigured |
| Latency | Lower | Higher |
| Flexibility | Fixed location | Mobile anywhere in range |

#### Ethernet Cable Standards
| Cable | Speed | Notes |
|-------|-------|-------|
| Cat5 | 100 Mb/s | Largely obsolete |
| Cat5e | 1 Gb/s | Common in older installs |
| Cat6 | 1 Gb/s | Better interference rejection |
| Cat7 | 10 Gb/s | Shielded, data centres |
| Cat8 | 40–100+ Gb/s | High-end data centre use |

- **STP** = Shielded Twisted Pair — foil around pairs blocks interference
- **UTP** = Unshielded Twisted Pair — cheaper, more common

#### Key Protocols
| Protocol | Port | Purpose |
|----------|------|---------|
| **HTTP** | 80 | Web browsing — unencrypted |
| **HTTPS** | 443 | Web browsing — encrypted + authenticated via TLS |
| **DNS** | 53 | Translates domain names → IP addresses |
| **TCP** | — | Reliable delivery — checks all packets arrive |
| **UDP** | — | Fast, no delivery guarantee (gaming, streaming, VoIP) |
| **SMTP** | 25 / 587 | Send email |
| **POP3** | 110 | Download email, remove from server |
| **IMAP** | 143 | Sync email, keeps messages on server |
| **FTP** | 21 | File transfer |
| **TLS** | — | Encryption layer used by HTTPS, email etc. (replaced SSL) |

> **TCP vs UDP:** TCP is recorded delivery — every packet confirmed. UDP is a flyer through a letterbox — fast, no confirmation.

#### Bandwidth, Throughput & Latency
- **Bandwidth** — maximum theoretical capacity (e.g. 1 Gb/s)
- **Throughput** — actual data rate achieved in practice (always ≤ bandwidth)
- **Latency** — time for a single packet to travel source → destination. Affected by cable length, congestion, hardware quality.

#### Compression
| Type | How | Trade-off | Examples |
|------|-----|-----------|---------|
| **Lossy** | Permanently discards some data | Massive size reduction, some quality loss | JPEG, MP3, H.264 |
| **Lossless** | Stores patterns so original can be reconstructed | Smaller reduction, no quality loss | PNG, FLAC, ZIP |

- **Codec** — compresses/decompresses video/audio (H.264, H.265, AV1)
- **Container** — wraps codec data + audio + metadata into one file (MP4, MKV, MP3)

#### OSI Model
| Layer | Name | Key Function | Example Protocols/Devices |
|-------|------|-------------|--------------------------|
| 7 | **Application** | User-facing apps | HTTP, DNS, FTP, SMTP |
| 6 | **Presentation** | Encryption/decryption (TLS), compression, format translation | TLS, JPEG, ASCII |
| 5 | **Session** | Opens, manages, closes sessions; authentication | NetBIOS, RPC |
| 4 | **Transport** | Segments data, end-to-end delivery, error checking | TCP, UDP |
| 3 | **Network** | IP addressing, routing, fragmentation | IP, routers |
| 2 | **Data Link** | MAC addressing, error detection (CRC), flow control | Ethernet, switches |
| 1 | **Physical** | Raw bits over cables/Wi-Fi | Copper, fibre, hubs |

**Mnemonic (7→1):** **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing  
**Mnemonic (1→7):** **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

#### OSI → TCP/IP Mapping
```
OSI 7 + 6 + 5  =  TCP/IP Application layer
OSI 4          =  TCP/IP Transport layer
OSI 3          =  TCP/IP Internet (Network) layer
OSI 2 + 1      =  TCP/IP Network Access (Physical) layer
```

#### Data Encapsulation (sending data)
1. Layers 7–5: application data
2. Layer 4: adds TCP/UDP headers (ports)
3. Layer 3: wraps in packets, adds IP headers (source/destination IP)
4. Layer 2: wraps in frames, adds MAC addresses
5. Layer 1: transmits raw binary

Receiving end: **decapsulation** in reverse — each layer strips its header upward.

#### Layer 3 Deep Dive: Network Layer
- **Logical addressing** — IP addresses (IPv4: 32-bit, `192.168.1.1`; IPv6: 128-bit, hexadecimal — solves IPv4 exhaustion)
- **Routing** — routers use routing tables to determine the best path. Static routing (manually set) vs Dynamic routing (auto-updates using protocols like OSPF, BGP, RIP)
- **Fragmentation** — breaks packets too large for a network link's MTU (Maximum Transmission Unit); destination reassembles
- **QoS (Quality of Service)** — prioritises time-sensitive traffic (VoIP, video calls) over bulk transfers to reduce latency and jitter
- **NAT (Network Address Translation)** — translates private internal IPs (e.g. 192.168.x.x) to a single public IP — allows many devices to share one public address

#### MAC vs IP Address
- **IP address** — logical, software-assigned; gets packets to the right **network**
- **MAC address** — physical, burned into the NIC; gets packets to the right **device on a LAN**. Format: `C8:7F:54:5D:58:C4` (6 hex pairs, 48 bits)

---

### 7.4 — Virtualisation & Hypervisors

#### What is a VM?
A software-based emulation of a physical computer — runs its own OS on shared host hardware.

#### Hypervisor Types
| | **Type 1 (Bare Metal)** | **Type 2 (Hosted)** |
|--|--|--|
| Runs on | Directly on hardware | On top of an existing OS |
| Performance | Better — no OS overhead | Reduced — goes through host OS |
| Security | Higher | Lower |
| Setup | Complex, needs IT expertise | Easy, consumer-friendly GUI |
| Examples | Proxmox, KVM, VMware ESXi | VirtualBox, VMware Workstation |

#### Why Virtualise?
- Consolidate many physical servers onto fewer machines — lower hardware and power costs
- Easy snapshot/backup/restore of entire VMs
- Simpler monitoring and centralised management
- **Risk:** if one physical host goes down, all its VMs go down → mitigate with clustering/live migration

---

### 7.5 — Client-Server Architecture

#### Client-Server vs Peer-to-Peer
| | **Client-Server** | **Peer-to-Peer (P2P)** |
|--|--|--|
| Control | Centralised | Distributed across all nodes |
| Security | Better | Weaker — no central enforcement |
| Scalability | Scales well | Limited |
| Failure risk | Server down = everyone affected | No single point of failure |

#### Thin vs Thick Clients
| | **Thin Client** | **Thick Client** |
|--|--|--|
| Processing | Done on the server | Done on the device |
| Hardware needed | Low-spec terminal | High-spec machine |
| Examples | Web apps, Google Docs | Photoshop, video games |

#### Architecture Tiers
- **2-tier** — client talks directly to server
- **3-tier** — client → application server → database server
- **N-tier** — further split for scalability (load balancers, caches, microservices)

---

### 7.6 — Resilient Systems

#### What Makes a System Resilient?
Maintain operations and recover quickly from failures, with minimal disruption. Goal: eliminate **single points of failure (SPOF)**.

#### Standby Types
| Type | How | Failover time | Cost | Use case |
|------|-----|--------------|------|----------|
| **Hot standby** | Backup runs live simultaneously | Instant (seconds) | Highest | Mission-critical, zero downtime |
| **Warm standby** | Backup running but not serving traffic | Fast (seconds–minutes) | Medium | Brief interruption tolerable |
| **Cold standby** | Backup offline until failure | Slow (minutes–hours) | Lowest | Non-critical systems |

#### Redundancy Types
- **Hardware** — multiple servers, dual power supplies, RAID arrays
- **Network** — dual ISP connections, redundant switches/routers
- **Data** — database replication, data centre mirroring

#### Load Balancing
Distributes incoming traffic so no single server is overwhelmed.
- **Round robin** — requests rotate through servers; simple
- **Least connections** — new request goes to least-busy server
- **IP hash** — same client always hits the same server (session-based apps)

#### Backup Types
| Type | What it backs up | Backup speed | Restore speed | Storage |
|------|-----------------|-------------|--------------|---------|
| **Full** | Everything | Slowest | Fastest | Most |
| **Incremental** | Changes since last backup of any kind | Fastest | Slowest (need all incrementals) | Least |
| **Differential** | All changes since last full backup | Medium | Medium | Medium |

#### 3-2-1 Backup Rule
- **3** copies of data
- **2** different storage types (e.g. SSD + cloud)
- **1** copy offsite

#### Geographic Distribution & CDNs
- **Geographic distribution** — multiple physical locations; regional disaster doesn't take everything down
- **CDN** — static content cached globally; reduces origin server load, improves speed for distant users

#### Other Strategies
- **RAID** — drive redundancy. **Not a backup** — won't protect against ransomware/fire/deletion
- **Test backups** — untested backups are worthless
- **Disaster recovery plan** — documented, rehearsed procedure for restoring services

#### Benefits of Resilience
| Benefit | What it means |
|---------|--------------|
| **Business continuity** | Critical functions keep running during disruptions |
| **Reduced downtime costs** | Downtime costs enterprises thousands per minute |
| **Customer satisfaction** | Reliable, always-on services build trust |
| **Competitive advantage** | Outperform competitors who suffer frequent outages |
| **Regulatory compliance** | Meet GDPR, ISO 27001, PCI DSS requirements |
| **Brand protection** | Prevents reputation-damaging public incidents |

---

### 7.7 — Cloud Computing

#### Service Models
| Model | What you get | You manage | Provider manages | Example |
|-------|-------------|------------|-----------------|---------|
| **IaaS** | Raw compute, storage, networking | OS, runtime, apps, data | Physical hardware, virtualisation | AWS EC2 |
| **PaaS** | App deployment environment | Your app code and data | OS, runtime, middleware, hardware | Heroku, Google App Engine |
| **SaaS** | Ready-to-use application | Nothing (just your data/settings) | Everything | Gmail, Office 365, Dropbox |

> **Analogy:** IaaS = renting an empty warehouse. PaaS = renting a fitted workshop. SaaS = hiring a full service.

#### Deployment Models
| Model | Description |
|-------|-------------|
| **Public** | Shared infrastructure (AWS, Azure, GCP) — pay-as-you-go, elastic |
| **Private** | Dedicated hardware for one org — more control, higher cost |
| **Hybrid** | Mix of both — sensitive data stays private, scalable workloads use public |

#### Cloud Pros & Cons
- ✅ Scale on demand, no upfront hardware cost, deploy globally fast, pay per use
- ❌ Internet dependency, data sovereignty concerns, migration complexity, ongoing costs

> **Key exam point:** Hybrid is usually the right recommendation when a company has sensitive/regulated data.

---

## CONTENT AREA 8: Data Security & Protecting Systems

---

### 8.1 — The CIA Triad

| Principle | Meaning | How to achieve it | Example failure |
|-----------|---------|-------------------|-----------------| 
| **Confidentiality** | Data accessible only to authorised people | Encryption, access controls, data classification, physical security | Unencrypted database exposed in a breach |
| **Integrity** | Data is accurate, consistent, and trustworthy | Checksums/hashes, version control, audit trails, 3-2-1 backups, data validation | Attacker silently alters a transaction amount |
| **Availability** | Data accessible when needed by authorised users | Hardware maintenance, redundant systems, load balancing, failover, disaster recovery | DDoS attack takes a service offline |

---

### 8.2 — Threats & Vulnerabilities

#### IT Threat Types
| Threat | Description |
|--------|-------------|
| **Malware** | Umbrella term — viruses, worms, botnets, ransomware |
| **Ransomware** | Encrypts your data, demands payment for the key |
| **Social engineering** | Manipulating humans psychologically rather than hacking systems |
| **Phishing** | Mass fake emails/messages designed to steal credentials or install malware |
| **Spear phishing** | Targeted phishing — attacker researches the victim for a personalised attack |
| **Pretexting** | Fabricates a believable scenario (e.g. "I'm from IT") to extract info |
| **Baiting** | Leaving infected USB drives hoping victims plug them in |
| **Tailgating** | Physically following someone through a secure door |
| **Insider threats** | Employees/contractors leaking or damaging data — intentionally or negligently |
| **Supply chain attacks** | Malicious code inserted into trusted vendor's software (e.g. SolarWinds) |
| **DDoS** | Flood a server with traffic from many sources to overwhelm it |
| **Zero-day exploits** | Attack using an unknown vulnerability — no patch exists yet |

#### Human Factors
- **Human error** — unpatched systems, sending to wrong recipient (Equifax: 140M records exposed via unpatched vulnerability)
- **Password mismanagement** — weak/reused passwords → one breach = all reused accounts compromised
- **Lack of training** — IBM study: 75% of untrained staff clicked a phishing link
- **Physical security failures** — lost fobs not deactivated, tailgating unchallenged

---

### 8.3 — Threat Mitigation

#### Firewalls
| | **Traditional Firewall** | **Next-Gen Firewall (NGFW)** |
|--|--|--|
| Inspects | Packet headers only (IP + port) | Full packet contents — Deep Packet Inspection |
| Can block | IP addresses, ports | Malware, specific apps, phishing URLs |
| Intelligence | Static rules | DPI, application awareness, IPS, live threat feeds |

**NGFW key features:**
- **Deep Packet Inspection (DPI)** — reads inside packets to detect malware/phishing
- **Application Awareness** — block specific apps (Facebook, YouTube) regardless of port
- **IPS** — detects and actively blocks attacks in real time
- **Threat Intelligence feeds** — live data to identify and block known malicious sources

#### Other Mitigation Techniques
| Technique | What it does |
|-----------|-------------|
| **Patch management** | Keeps OS/software updated — closes known vulnerabilities |
| **Security awareness training** | Trains staff to recognise phishing and social engineering |
| **Network segmentation** | Splits network into zones — breach of one zone can't spread laterally |
| **Offline backups** | Disconnected from network — immune to ransomware encryption |
| **MFA** | Requires second proof beyond password — stolen password alone isn't enough |
| **Access controls / RBAC** | Limit what each user can see/do — principle of least privilege |
| **Audit trails / logs** | Record who changed what and when — forensics and accountability |
| **Disciplinary policies** | Deterrent — clear consequences for policy violations |

#### Physical Security Controls
- **Access levels** — tiered access to rooms by role
- **Security officers** — guard entry points
- **CCTV** — monitor, deter, and provide evidence
- **Fob/card systems** — log every entry/exit by named individual

---

### 8.4 — Access Controls & Authentication

#### File Permissions vs Access Levels
- **File permissions** — what a user can do *with a specific file* (read, write, execute)
- **Access levels** — what a user can do *on the system overall* (admin vs standard user)

#### IAAA Security Model
1. **Identification** — who are you? (username)
2. **Authentication** — prove it (password, MFA token, biometric)
3. **Authorisation** — what are you allowed to do? (role-based permissions)
4. **Accountability** — log what you did (audit trail, timestamps, IP, device)

#### Password Security
- Longer passwords = exponentially longer to crack
- **Passphrases** are both strong and memorable
- Never reuse passwords — one breach = all reused accounts compromised
- MFA adds critical second layer even if password is stolen

---

### 8.5 — Data Protection & Backups

#### Implications of Poor Backup/Recovery
- Ransomware with no offline backup = permanent data loss
- GDPR fines for losing or exposing customer data (up to 4% global turnover)
- Business continuity lost — operations halt entirely
- Reputational damage — customer and partner trust destroyed

#### Key Backup Practices
- **3-2-1** rule (see 7.6)
- **Test and validate** regularly — a backup that fails to restore is worthless
- **Offline backups** — immune to ransomware
- **RAID is not a backup** — protects against drive failure only, not ransomware/fire/deletion

---

### 8.6 — Real-World Case Study: Stuxnet

**What:** Sophisticated computer worm discovered 2010 — first cyber weapon designed to cause physical damage.

**Target:** Iran's uranium enrichment facility at Natanz — Siemens PLCs controlling centrifuges.

**How it worked:**
- Used **4 zero-day exploits** simultaneously
- Spread via USB drives, network shares, and air-gapped systems
- Altered centrifuge spin speeds to cause physical destruction
- Fed **false data** to monitoring systems — operators saw "all normal" while machines failed

**Attribution:** Widely attributed to a US–Israel joint operation ("Operation Olympic Games").

**Impact:** ~1,000 centrifuges destroyed; Iran's nuclear programme significantly set back.

**Why it matters:**
- First malware designed to cause **physical, real-world destruction**
- First confirmed **nation-state cyberwarfare** operation
- Proved cyber attacks can substitute for conventional military action
- Exposed vulnerability of **industrial/critical infrastructure** to software attacks
- Established cyberspace as a recognised domain of warfare

---

## Quick-Reference Summary

### OSI Mnemonic
**7→1:** **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing  
**1→7:** **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

### Key Exam Scenarios
| Scenario | Best answer |
|----------|------------|
| Company with sensitive data moving to cloud | **Hybrid** deployment |
| Hospital network needing max reliability | **Mesh** topology (or extended star) |
| Performance-critical software (game, OS) | **Compiler** |
| Script or data processing app | **Interpreter** |
| Company with 30 servers wanting to consolidate | **Type 1 Hypervisor** (Proxmox/KVM/ESXi) |
| Single point of failure data centre | **Geographic distribution + cloud backups** |
| Stopping ransomware data loss | **Offline 3-2-1 backups + patch management** |
| Stopping phishing attacks | **Staff training + MFA + NGFW email filtering** |
| Small office, no IT team, needs apps | **SaaS** — minimal management required |
| Dev team wants to deploy without managing servers | **PaaS** |
| Company needs full VM control | **IaaS** |
| High-stakes system switch (e.g. payroll) | **Parallel running** |
| Low-risk switch from paper system | **Direct changeover** |
| Large unsorted dataset — find an item | **Merge sort + binary search** |
| Impossible login location — what's happened? | **Credential compromise** → lock account, reset password, enforce MFA |

---

*Full guide covering CA1–CA8 — compiled from notes, lesson materials, and specification content.*
