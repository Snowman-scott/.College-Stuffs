# HTTP Headers
- GET: Just retrives data, no body, No server side changes
- POST: Create a new resource / submit data. Used when submitting a form or logging in, account creation etc..
- PUT: Replace a resource entirely, Idempotent. Used when updating a full user profile where you send send the complete profile back.
- PATCH: partially update a resource. Use when changing just one field 
- DELETE: Remove something, Used when deleting a user or a post
- HEAD: Same as GET but only returns headers, No body. used when checking if something exists, or how large it is / date last modified.
- OPTIONS: asks the server what methods/actions are allowed on a resource. Browsers send it automatically before a "real" request (CORS preflight check) to check perms.

# LONG QUESTIONS :/
1. Retrieves data, no body, No server side change
2. Creates a new resource or new data. Server side change
3. Get data is Usually in the URL as a query string [search?q=creep](https://lrclib.net/api/search?q=creep) or [search?track_name=creep&artist_name=radiohead](https://lrclib.net/api/search?track_name=creep&artist_name=radiohead)
4. Post data is placed in the body not the URL.
5. It is not forbidden, But not standard practice to have a GET request with a body.
6. Yes, POST requests can contain sensitive data. it's why it is preferred for passwords.
7. No POST is not automatically secure. Without HTTPS POST data is still sent in plaintext.
8. No POST does not encrypt data automatically. Encryption comes from HTTPS/TLS, Not the method.
9. Get requests can be bookmarked since all the data is in the URL.
10. POST requests cannot be bookmarked as the data is not in the URL.
11. GET requests can be cached, browsers and proxies commonly cache GET Requests.
12. Idempotent means making the same request multiple times yeilds the same results as making the request once or has the same results every time.
13. GET is Idempotent as it is just reading data so repeating it should not change it.
14. POST is not Idempotent as repeating a POST can make Duplicate entries of the data.
15. It tells you what's safe to retry, prefetch and cache or let Browsers repeat automatically.
16. GET requests can technically change data in a DB, Nothing stops the dev writing a GET that runs an UPDATE
17. It would be bad design because it breaks the idempotent/safe assumption. Browsers, proxies, crawlers and Caches all assume GET is harmless. So they may resend, prefetch, or cache it triggering unintended changes.
18. other then GET and POST you have: PUT, PATCH, DELETE, HEAD, OPTIONS
19. PUT: Replacing an entire resource. PATCH: Updating part of a source, DELETE removing the source entirely 
20. The HTTP method is the verb (GET,POST,etc). It says the type of action being requested. The flask route is the URL path. it says which resource/endpoint the request is for. FLASK lets you bind specific methods to each route, e.g:
```py
@app.route('/users/<id>', methods=['GET', 'DELETE'])
def user(id):
    if request.method == 'GET':
        #return user data
    elif request.method == 'DELETE':
        # delete user 
```

## Examples
**1.** Retrieves data, no body, No server side change

Example:
```
GET /articles/42 HTTP/1.1
Host: example.com
```
No body, nothing on the server changes — it just hands back article 42.

**2.** Creates a new resource or new data. Server side change

Example:
```
POST /articles HTTP/1.1
Host: example.com
Content-Type: application/json

{"title": "New Post", "body": "..."}
```
This creates a new article row in the DB — a real server-side change.

**3.** Get data is Usually in the URL as a query string [search?q=creep](https://lrclib.net/api/search?q=creep) or [search?track_name=creep&artist_name=radiohead](https://lrclib.net/api/search?track_name=creep&artist_name=radiohead)

Example: `GET /search?q=creep` — the whole request is the URL, nothing else needed.

**4.** Post data is placed in the body not the URL.

Example: `POST /login` with body `{"username": "rose", "password": "hunter2"}` — the credentials never appear in the URL.

**5.** It is not forbidden, But not standard practice to have a GET request with a body.

Example: some tools (like Elasticsearch's `_search` endpoint) accept a GET with a JSON body for complex query definitions — it works, but many HTTP libraries and proxies will silently strip or mangle it.

**6.** Yes, POST requests can contain sensitive data. it's why it is preferred for passwords.

Example: a login form POSTing `{"password": "..."}` in the body rather than as `?password=...` in a URL, where it'd end up in browser history and server access logs.

**7.** No POST is not automatically secure. Without HTTPS POST data is still sent in plaintext.

Example: `POST http://example.com/login` (note `http`, not `https`) — anyone sniffing the network traffic can read the body in plaintext, password included.

**8.** No POST does not encrypt data automatically. Encryption comes from HTTPS/TLS, Not the method.

Example: `GET https://example.com/data` is encrypted (HTTPS), but `POST http://example.com/data` is not (plain HTTP) — the method didn't decide that, the protocol did.

**9.** Get requests can be bookmarked since all the data is in the URL.

Example: `https://example.com/search?q=creep` — bookmark it, and reopening it replays the exact same search.

**10.** POST requests cannot be bookmarked as the data is not in the URL.

Example: bookmarking a page after submitting a login POST just saves the URL (e.g. `/login`), not the username/password that were in the body — replaying it gets you an empty form, not a resubmission.

**11.** GET requests can be cached, browsers and proxies commonly cache GET Requests.

Example: a browser or CDN caching `GET /style.css` so the second visit loads it instantly from cache instead of hitting the server again.

**12.** Idempotent means making the same request multiple times has the same effect as making it once.

Example: setting a light switch to "on" five times in a row leaves it in exactly the same state as setting it once.

**13.** GET is Idempotent as it is just reading data so repeating it should not change it.

Example: calling `GET /articles/42` a hundred times still just returns article 42 — nothing on the server is altered by asking.

**14.** POST is not Idempotent as repeating a POST can make Duplicate entries of the data.

Example: double-clicking a "Submit Order" button that fires `POST /orders` twice can create two separate orders instead of one.

**15.** It tells you what's safe to retry, prefetch and cache or let Browsers repeat automatically.

Example: a browser will silently retry a failed GET on a flaky connection, but it won't silently retry a failed POST — because retrying a GET is harmless, retrying a POST might double-submit.

**16.** GET requests can technically change data in a DB, Nothing stops the dev writing a GET that runs an UPDATE

Example: `@app.route('/delete-user/<id>', methods=['GET'])` that runs a DELETE on the DB — technically works, nothing stops you writing it.

**17.** It would be bad design because it breaks the idempotent/safe assumption. Browsers, proxies, crawlers and Caches all assume GET is harmless. So they may resend, prefetch, or cache it triggering unintended changes.

Example: a web crawler (like Googlebot) follows every link it finds — if `GET /delete-user/42` is a real link on your site, the crawler visiting it could delete user 42 without any human intending it.

**18.** other then GET and POST you have: PUT, PATCH, DELETE, HEAD, OPTIONS

Example:
```
PUT /users/42
PATCH /users/42
DELETE /users/42
HEAD /users/42
OPTIONS /users/42
```

**19.** PUT: Replacing an entire resource. PATCH: Updating part of a source, DELETE removing the source entirely

Example:
```
PUT /users/42       {"name": "Rose", "email": "rose@example.com"}   # replaces the whole user record
PATCH /users/42     {"email": "new@example.com"}                    # only updates the email field
DELETE /users/42                                                    # removes the user entirely
```

**20.** *(unchanged — already has your example block)*

Look at the original answers i did this one there :3
