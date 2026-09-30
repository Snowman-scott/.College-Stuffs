# Validation
## Types

1. Presence checks are a type of check making sure data has been inputted into a field, Like a Username in a username box. You would use it to make sure the required information gets used in a form. It stops important information from being left blank by the user.
2. Length checks check how long an entry is. The length of a password. You may use it for a char limit or making sure a password is long enough to be "secure". It stops too much or too little information being used.
3. Range checks are making sure data is within a set min and max range. like ensuring customer ages are between 18 - 100. You may use it when validating a date range, or a users age. It stops data being used when it will be incorrect or breaks a platform rule like age.
4. Type checks ensure the data is a specific type, like an address being a string and an age being an integer. you may use it to validate a pice of information that needs to be an int or a float. It stops incorrect data being used like a string in an age box.
5. Format checks ensure data is entered in the correct format. A date being YYYY/MM/DD. This is useful for dates or data that needs to follow a strict convention like time. It stops users from using different methods that the backend may not understand.
6. pattern matching validation uses regular expressions to check an input value matches a specific format before submission. Like a password having special chars and numbers. This is good for making sure secure passwords are made and makes finding data very easy.
7. character checks ensure that input data contains only the expected characters for the specific field. Like an age only having numbers and no special chars. Important for data integrity and stopping the backend throwing errors when processing data.
8. Uniqueness ensures that each value in a dataset is distinct and not duplicated. May be used for databases. Helps maintain data integrity!
9. Comparison checks verify changes between version. good for seeing why a pass changed making sure a hash has changed!
10. whitelist validation is ensuring that only data or inputs that are explicitly allowed (or "whitelisted") are accepted by a system. useful for making sure only allowed data is let into the db
11. Blacklists are the same as whitelists but they block data that is in the blacklist. this stops any bad data from going into the db.


## Can validation make a website secure?

**Short answer:** it helps, but on its own, no. It's one layer of defence.

1. **Client-side validation**
   - Runs in the browser before data is sent (`required`, `pattern`, JavaScript).
   - Gives instant feedback and saves server round trips.
   - It's about user experience, not security.

2. **Server-side validation**
   - Runs on the server after data arrives, before it's used or stored.
   - Checks type, length, format and allowed values, and rejects bad input.
   - This is the one you can trust, because the user can't tamper with server code.

3. **Why use both**
   - Client-side gives speed and a friendly experience.
   - Server-side is the real security gate.

4. **If only client-side is used**
   - The server accepts whatever arrives, assuming the browser checked it.
   - It can't know that. Anyone who sends data another way skips your rules.
   - Bad or malicious data ends up in your database or app logic.

5. **How an attacker bypasses client-side validation**
   - Edit or delete HTML attributes (`maxlength`, `required`, `pattern`) in dev tools.
   - Disable JavaScript.
   - Send requests directly with `curl`, Postman or a script.
   - Intercept and change requests with a proxy like Burp Suite or OWASP ZAP.

6. **Why server-side is still necessary**
   - Client code runs on the attacker's machine, so they control it.
   - All client input (fields, headers, cookies, hidden fields) can be forged.
   - Only server-side checks are outside their control.

7. **Validation vs sanitisation**
   - Validation checks if input is acceptable, then accepts or rejects it. Example: age must be 0-120, so reject "abc".
   - Sanitisation cleans or modifies input to make it safe. Example: escaping `<` to `&lt;`.
   - Best used together: validate first, then sanitise or encode depending on where the data is used (HTML, SQL, etc.).

8. **Why validation alone doesn't stop every attack**
   - Valid-looking input can still be malicious, e.g. a comment box that has to accept text which might contain script or SQL.
   - Injection attacks are best stopped at the point of use: parameterised queries for SQL, output encoding for HTML.
   - It doesn't cover other threats: weak authentication, poor access control, CSRF, misconfigured servers, unpatched software.
   - Logic flaws: a perfectly valid request (like changing an order ID in the URL) may still be something the user shouldn't be allowed to do.
