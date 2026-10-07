from flask import Flask, request

app = Flask(__name__)

products = [
    {
        "id": 201,
        "name": "Trail puppy backpack",
        "price": 54.99,
        "catagory": "bags",
    },
    {
        "id": 202,
        "name": "Wireless mechanical keyboard",
        "price": 79.99,
        "catagory": "electronics",
    },
    {
        "id": 203,
        "name": "Ergonomic desk chair",
        "price": 149.99,
        "catagory": "furniture",
    },
    {
        "id": 204,
        "name": "Noise canceling headphones",
        "price": 119.50,
        "catagory": "electronics",
    },
    {
        "id": 205,
        "name": "Stainless steel travel mug",
        "price": 22.99,
        "catagory": "kitchenware",
    },
    {
        "id": 206,
        "name": "Minimalist LED desk lamp",
        "price": 29.99,
        "catagory": "lighting",
    },
    {
        "id": 207,
        "name": "Portable Bluetooth speaker",
        "price": 39.95,
        "catagory": "electronics",
    },
    {
        "id": 208,
        "name": "Large felt desk pad",
        "price": 18.50,
        "catagory": "accessories",
    },
    {"id": 209, "name": "Canvas messenger bag", "price": 42.00, "catagory": "bags"},
    {
        "id": 210,
        "name": "Adjustable laptop stand",
        "price": 25.99,
        "catagory": "accessories",
    },
]


@app.route("/products", methods=["GET"])
def get_products():
    return products


if __name__ == "__main__":
    app.run(port=5001, debug=True)
