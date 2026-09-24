# Industry OH YEAH

## PasteBin Website

### Front-End
The Front needs to have a box to paste text and info into, As well as a preview tab for the chosen file types syntax.
A create button to allow the user to make the link that goes to that information. 
Then the settings along the top of the screen that allows users to add a password to the bin, or make it burn on read what type of file it is (md, source code, plain txt) and a dark mode toggle and a toggle for the amount of time until the bin burns itself.

### Back-End
The code needs to take the information from the front and store it in an encrypted manor both at rest and in transit. It also needs to burn the info after the specified amount of time or when a user opens and reads it (if set to burn after read). It also needs to handle files given to it, and the format of the inputted text too. User accounts and routes for admins only. Hashed passwords!

### Front end Table

| Componant | Description | Technology / Approach |
|-----------|-------------|-----------------------|
| Editor/Preivew Box | The Box that shows where people should type or preiview their work makes it obvious what the user is supposed to do | Radix UI/ Shadcn UI `Tabs` Primitive, CSS for design |
| Input box | The area that allows users to enter text based items that they want to share or move to another computer | Codemirror 6 for auto indenting code or a standard `<textarea>` styled with monaspace fonts |
| Multi-type preview tab | Allows users to preview their Md elements, code or plain text docs | would use react-markdown, shiki for code and native html `<pre><code>` block with `white-space: pre-wrap` styling.|
