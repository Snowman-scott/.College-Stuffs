from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    return "Hello world"


@app.route("/post", methods=["POST"])
def post():
    return "This is a post route"


if __name__ == "__main__":
    app.run(debug=True)
