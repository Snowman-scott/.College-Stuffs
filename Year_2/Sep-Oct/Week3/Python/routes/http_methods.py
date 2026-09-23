from flask import Flask, jsonify, request

from helper import emailValidator, phoneValidator

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    return "Hello world"


@app.route("/post", methods=["POST"])
def post():
    return "This is a post route"


@app.route("/search")
def search():
    if "item" in request.args.keys():
        return f"You searched for {request.args['item']}"
    else:
        return "Please gib an item"


@app.route("/register", methods=["POST"])
def register():
    data = request.form
    required = ("username", "email", "age", "phoneNumber")
    missing = [k for k in required if not data.get(k)]
    if missing:
        return f"You were missing: {', '.join(missing)}"
    user = data["username"]
    age = data["age"]
    em, err = emailValidator(data)
    if err != None:
        return f"Email verification failed\n ERROR: {err}"
    phone, err =phoneValidator(data)
    if err != None:
        return f"Phone verification failed\n ERROR: {err}"
    return f"Hello {user} your email is {em} you are {age} old and your digits are {phone} :3"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
