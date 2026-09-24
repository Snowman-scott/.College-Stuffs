# Industry OH YEAH

## PasteBin Website

### Front-End
The Front needs to have a box to paste text and info into, As well as a preview tab for the chosen file types syntax.
A create button to allow the user to make the link that goes to that information. 
Then the settings along the top of the screen that allows users to add a password to the bin, or make it burn on read what type of file it is (md, source code, plain txt) and a dark mode toggle and a toggle for the amount of time until the bin burns itself.

### Back-End
The code needs to take the information from the front and store it in an encrypted manor both at rest and in transit. It also needs to burn the info after the specified amount of time or when a user opens and reads it (if set to burn after read). It also needs to handle files given to it, and the format of the inputted text too. User accounts and routes for admins only. Hashed passwords!

### Front-End Table

| Componant | Description | Technology / Approach |
|-----------|-------------|-----------------------|
| Editor/Preivew Box | The Box that shows where people should type or preiview their work makes it obvious what the user is supposed to do | Radix UI/ Shadcn UI `Tabs` Primitive, CSS for design |
| Input box | The area that allows users to enter text based items that they want to share or move to another computer | Codemirror 6 for auto indenting code or a standard `<textarea>` styled with monaspace fonts |
| Multi-type preview tab | Allows users to preview their Md elements, code or plain text docs | would use react-markdown, shiki for code and native html `<pre><code>` block with `white-space: pre-wrap` styling.|
| Create button | Allows the user to make the bin sharable | Plain HTML button with some CSS |
| Top settings bar | a place for all the settings to be held | CSS and HTML header |
| File Type selector | Allows users to toggle the paste to be in markdown, source code, plaintext | Dropdown selection HTML or React stuffs |
| Password | Allows user to add a password to the pastebin | can be serverside or client side hashing |
| Burn on read | Burns the file after someone has read it | Delete SQL or redis sent to the db |
| Expiration selection | Allows the bin to be burnt after a specified time | Db cron, redis TTL, cf worker event
| Theme toggle | Light or dark mode bwo | CSS and Javascript Theme toggle |

### Back-End Table
| Componant | Description | Technology / Approach |
|-----------|-------------|-----------------------|
| API Gateway / Server | Handles requests from the front and keeps data secure in transit | Go Fiber/Gin or flask with TLS 1.3 / HTTPS |
| Encryption Engine | Encrypts paste contents before saving so data is locked at rest | AES-256-GCM authenticated encryption via Web Crypto API or language crypto |
| Database Storage | Stores paste metadata, paste contents, and user info | PostgreSQL, SQLite, or Redis key-value store |
| File Handler | Handles attached files sent with the paste and checks inputted text formats | Multipart form parser (multer / Go mime) and Zod or Go struct validation |
| File Storage | Keeps uploaded files in object storage instead of clogging the main database | S3-compatible storage (Cloudflare R2, MinIO) with pre-signed URLs |
| User Accounts & Auth | Lets users create accounts with hashed passwords to manage their pastes | Argon2id or bcrypt password hashing with HTTP-only cookies or JWTs |
| Admin Routes & RBAC | Blocks normal users from seeing admin panel tools and routes | Middleware route guards checking admin user roles + rate limiting |

## What Might Businesses have to worry about?
- SQL injection (attack)
- DDoS (Denial of service attack)
- Being sued 
- Bankruptcy  
- not doing H&S or risk assessments
- lawsuit 
- GDPR 
- Child labor
- Insider threats 
- Cyber security 
- No stock / Supply chain risk 
- Distribution attack 
- Phishing attacks  
- Credit risk 
- Stocks and shares 
- Stakeholders

| Risk | Impact | Mitigation Strategy |
|------|--------|---------------------|
| SQL injection | Someone can minipulate a DB to get access to things they should not have like making themsevs an admin | Prepared statements, parameterized queries, and input validation |
| DDoS attack | Servers get flooded with fake traffic making the website or app go down for actual users | Cloudflare / CDN filtering, rate limiting, and traffic monitoring |
| Being sued / Lawsuits | Huge legal fees, losing money to court settlements, and massive damage to company reputation | Solid contracts, clear terms of service, legal compliance, and liability insurance |
| Bankruptcy | Business completely runs out of cash and has to shut down or liquidate assets | Good financial planning, keeping cash reserves, budgeting, and watching cash flow |
| Missing H&S / Risk assessments | Staff or customers get hurt on site, leading to heavy fines, legal action, or forced closure | Regular health and safety audits, staff safety training, and clear risk assessment docs |
| GDPR non-compliance | Getting hit with massive fines (up to 4% global turnover) for leaking or mismanaging user data | Strict data privacy policies, encrypting user data, and getting explicit consent |
| Child labor in supply chain | Huge ethical breach, total brand destruction, legal sanctions, and boycotted products | Strict supplier audits, ethical sourcing policies, and vetting third-party factories |
| Insider threats | Rogue or disgruntled employees stealing source code, leaking customer data, or wiping servers | Principle of least privilege (RBAC), access logging, and revoking access immediately on offboarding |
| General Cyber security | Ransomware locking down systems, data leaks, and complete loss of customer trust | Firewalls, MFA everywhere, keeping software updated/patched, and regular pen testing |
| No stock / Supply chain risk | Can't ship products to customers, losing sales to competitors, and factory downtime | Having backup suppliers, keeping buffer stock, and tracking logistics carefully |
| Distribution attack | Compromised third-party software packages or updates infecting internal build servers | Dependency scanning, lockfiles, and vetting third-party software vendors |
| Phishing attacks | Staff getting tricked into giving away login details or transferring money to scammers | Email spam filters, hardware keys / MFA, and running staff phishing tests |
| Credit risk | Clients or customers defaulting on invoices so the business never gets paid for work done | Credit checks before signing deals, taking upfront deposits, and strict payment terms |
| Stocks & shares volatility | Share price crashing, losing market value, and panic among company shareholders | Diversifying revenue, clear financial reporting, and focusing on long-term stability |
| Stakeholder issues | Conflicts over business direction, management deadlocks, or investors pulling funding | Regular reporting, clear board governance, and open communication with investors |
