# JSON research

## Fundamentals

1. JavaScript Object Notation
2. Used for transferring data between a server and a web application, making it easier for different systems to communicate
3. it is commonly used for API's because it is light weight, human-readable, natively supported by javascript and most modern programming langs and is easy to parse
4. No, Json is a dictionary or storage language, not a fully fledged programming language like Go, C or Rust
5. JSON was directly derived form the syntax used to write object literals in javaScript
6. JSON is useful as it is widely accepted across all languages making it easy to parse and use.

## JSON Structure

7. A JSON object is an unordered collection of Key-value pairs enclosed in curly braces `{ }`. It is the primary structure used in JSON to represent formatted data.
8. A key is the identifier used to pull data out of the dict. it is what you use when calling the data in the code
9. A value is what the key gives, when you call the key the value is returned.
10. A key-value pair is when you have a key `Key` and `value data`. You call the value data using the key
11. A JSON array is an ordered list of values enclosed in `[ ]`, Unlike a JSON object (which stores key-value pairs), an array stores a simple sequence of items accessed by their numerical index starting at 0.
12. Objects use `{}` and are unordered key-vale pairs. Arrays use `[]` and are ordered lists of values

## Python Dict vs JSON

A Python dict is a live in-memory data structure specific to Python, while JSON is a language-agnostic text format used to transmit data over a network.

```py
# Python dict (in-memory object, uses True/None and single/double quotes)
py_dict = {'user': 'Rose', 'active': True, 'score': None}

# JSON string (text format for data transfer, uses double quotes and true/null)
json_str = '{"user": "Rose", "active": true, "score": null}'
```

Syntax rules differ significantly: Python allows single quotes, trailing commas, comments, and diverse key types, whereas JSON strictly mandates double quotes, string keys, no trailing commas, and lowercase booleans/null.

```py
# Python dict (flexible syntax: single quotes, trailing comma, set/tuple, comment)
py_dict = {
    'id': 101,
    'admin': True,
    'extra': None,
    'tags': {'dev', 'foss'},  # Sets & trailing commas allowed
}

# JSON string (strict syntax: double quotes only, no trailing comma, array, no comments)
json_str = '{"id": 101, "admin": true, "extra": null, "tags": ["dev", "foss"]}'

```
