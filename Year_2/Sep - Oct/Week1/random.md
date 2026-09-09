# Damn
1. When you click order on amazon, the backend database gets queried, it checks if the item is in stock. If the item is in stock It will take you to the page where put in you confirm payment. After payment is accepted, It will reduce the total inventory count and add it to a database for your personal account.

2. When you Click a login button with your login info filled out a database gets queried checks if your username matches an entry in their logins database, If your username matches it will then pull the password hash, and hash the password you just typed in, If the hashes match then you move on to 2fa or other verification. If it does not match it rejects you and shows that user/pass was wrong. If your username is not seen it may show you a button telling you to make an account.

3. Skipped

4. a. Deny access, b. State username is wrong and suggest account creation and deny access to the account, c. Deny access and tell user a pass is required, d. the backend should remember the clients username and password and let them in


# Backend responsibilities

## Request handling.
Handles incoming HTTP(S) from clients and routes them to the correct place based on the URL path, HTTP method (GET/POST/PUT/DELETE) and headers </3

## Business logic processing.
The actual rules and processes that make the app do what it is meant to do like calculating shopping cart totals etc..

## DBMS.
The Back talks ot the Database to create, read, update, and delete (CRUD) data. This includes writing and executing queries, managing db connections effciently. ensuring data integrity, and structuring data sensibly.

## Authentication and authorisation.
the back verifies who a user is and what they are allowed to do. This is so no random user can sign into any account and so a normal user does not have access to admin tooling.

## Security enforcment.
The back activley defends agains attacks, sanitising/validating all inputs to prevent SQL injections and XSS, enforcing HTTPS, rate-limiting requests to prevent abuse / DDoS, Setting proper CORS policys, and keeping sensitive data encrypted at both ends

## Response formatting and delivery.
Once the  backend has processed the data it needs to package the result into a proper response. usually JSON for APIs, or rendered HTML for traditional server-side apps, along with the correct HTTP status code and headers, before sending it back to the client

# Just Web stuff 

## APIs
Allow you to interface with a server in code
Application Programming interface.

It lets you make a request to it so you can get a response with the data you requested 


## HTTP
A protocol that browsers and servers use to communicate
It is a request-response protocol: Client sends a request, Server processes the request and sends back the response.
Stateless - By default the server wont remember anything about previous requests, This is why things like cookies and sessions exist

## HTTP vs HTTPS
### HTTP:
Data is sent as plain text, Anyone could intercept the traffic and read exactly what you were doing on the site, 
Because it is plain text it is really easy to steal passwords, bank info etc...

### HTTPS
Same protocol but wrapped in TLS/SSL encryption. 
This encrypts the data in transit so an attacker cannot see what the data is. 
It also verifies it goes to the right server using an SSL cert so no bad actor can pretend to be the server and get the info.
It also ensures data has not been tampered with in transit. 
HTTPS runs over port 443 by default 


## HTTP Requ and it's contents 
The Request is what the client sends to the server.
### Request line:
This includes the Method (GET, POST, PUT, DELETE, etc..), the target URL/path ,and the HTTP version
### Headers:
Headers are metadata about the request, eg- the host (domain), User-Agent, Content-type (format of any data being sent), Auth tokens and cookies
### Body:
Optional but mainly on PUT, POST PATCH and it is the actual data being sent.

## HTTP Resp and it's contents
The Response sent from the server to the client

### Status Line:
the HTTP version and a status code with a short reason phrase (HTTP/1.1 200 OK, HTTP/1.1 404 Not Found)
Status codes:
1xx = informational, 2xx = success, 3xx = redirection, 4xx = client error (bad request, unauthorized), 5xx = server error

### Headers: 
Metadata about the response like Content-Type (what format the body is in), Content-Length, Set-Cookie, caching instructions

### Body/payload:
Optional - the actual content returned - HTML for a webpage, JSON for an API resp, an image file, etc...
the term Body is used more when referencing web pages/web apps and payload is used more when talking about APIs
