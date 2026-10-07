from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Trail & Timber"


@app.route("/product")
def product():
    product_info = {
        "name": "Pine Ridge Trail Stove",
        "category": "Camping Cookware",
        "price": 45.99,
        "stock": 4,
        "description": "Ultra-lightweight titanium camp stove built for fast-and-light backcountry cooking.",
    }

    return render_template("product.html", product=product_info)


if __name__ == "__main__":
    app.run(debug=True)
