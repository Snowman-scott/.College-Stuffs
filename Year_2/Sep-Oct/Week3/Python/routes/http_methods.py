from flask import Flask, jsonify, request

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
    try:
        data = request.form


        user = data["username"]
        em = data["email"]
        age = data["age"]
        phone = data["phoneNumber"]
    except KeyError as e:
        return(f"You were missing a feild\nMake sure you have a username, email, age, and phone number \n\nError was: {e}")
    else:
        return(f"Hello {user} your email is {em} you are {age} old and your digits are {phone} :3")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
