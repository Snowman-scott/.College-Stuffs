# Homework
## Section A

### What is Jinja?
Jinja is a templating engine. It allows developers to combine static text files (like html, YAML or plain text) with Dynamic data using simple placeholders and logic blocks.

### What is the difference between these?
- {{ }} This is Used for taking a variable from the backend and using it in the front
- {% %} This is a control statement like for loops and if statements 
- {# #} This is a comment, Like in python

### How are variables passed from Flask to Jinja?
In flask variables are passed to Jinja templates by passing keyword augments directly into the `render_templates()` function. 
Flask then instates the jinja environment takes every keyword augment given to it and injects it into the template's rendering context.
Inside the template those variables become accessible as local identifiers using standard Jinja syntax.

## Section B

### Album.html
1. Error: `</h2>` instead of the actual `</h1>` ending header that should have been used
2. Error: No endif statement in the code. Added the {% endif %}
3. Error: Invalid if statement Jinja syntax `=` instead of `==` Added the second `=` to the statement
4. Error: album.date uses the wrong dictionary key, date does not exist. Changed it to year the actual key defined in the dict
5. Error: {{title}} tries to render a title directly. Changed it to `album.title` so it actually renders the title

### app.py
1. Error: Invalid render_template arguments `album` should be `album = album` So I implemented this fix. It errors because album is not passed as the argument, it just raises a TypeError

### Improvements
I removed the Genera if statement as it seemed pretty useless to me
Then added the needed code
