from flask import Flask, request

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
        return(f"You searched for {request.args["item"]}")
    else:
        return("Please gib an item")


if __name__ == "__main__":
    app.run(debug=True)
