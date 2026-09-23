from flask import Flask, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Welcome"

@app.route("/greet/<username>")
def greet(username):
    return f"Welcome {username}!"

@app.route("/double/<int:number>")
def double(number):
    return str(number * 2)

#/search?item=shoe&category=clothing
@app.route("/search")
def search():
    if "item" in request.args.keys() and "category" in request.args.keys():
        item = request.args["item"]
        category = request.args["category"]
    #ampersand
        return f"Searching for '{item}' in '{category}'"
    else:
        return "Please provide an item and a category"

if __name__ == "__main__":
    app.run(debug=True)
