from flask import Flask, request
from helpers import id_ver, val_price, ver_add

app = Flask(__name__)

products = [
    {
        "id": 201,
        "name": "Trail puppy backpack",
        "price": 54.99,
        "category": "bags",
    },
    {
        "id": 202,
        "name": "Wireless mechanical keyboard",
        "price": 79.99,
        "category": "electronics",
    },
    {
        "id": 203,
        "name": "Ergonomic desk chair",
        "price": 149.99,
        "category": "furniture",
    },
    {
        "id": 204,
        "name": "Noise canceling headphones",
        "price": 119.50,
        "category": "electronics",
    },
    {
        "id": 205,
        "name": "Stainless steel travel mug",
        "price": 22.99,
        "category": "kitchenware",
    },
    {
        "id": 206,
        "name": "Minimalist LED desk lamp",
        "price": 29.99,
        "category": "lighting",
    },
    {
        "id": 207,
        "name": "Portable Bluetooth speaker",
        "price": 39.95,
        "category": "electronics",
    },
    {
        "id": 208,
        "name": "Large felt desk pad",
        "price": 18.50,
        "category": "accessories",
    },
    {"id": 209, "name": "Canvas messenger bag", "price": 42.00, "category": "bags"},
    {
        "id": 210,
        "name": "Adjustable laptop stand",
        "price": 25.99,
        "category": "accessories",
    },
]


@app.route("/products", methods=["GET"])
def get_products():
    return products


@app.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    for product in products:
        if product["id"] == id:
            return product
    return {"error": "product not found"}, 404


@app.route("/product", methods=["POST"])
def add_prod():
    data = request.form
    new_pro = ("id", "name", "price", "category")
    missing = [k for k in new_pro if not data.get(k)]
    if missing:
        return {"error": f"you were missing: {', '.join(missing)}"}, 400
    pid, err, stat_c = id_ver(data, products)
    if err != None:
        return f"Error: {err['error']}", stat_c
    price, err, stat = val_price(data)
    if err != None:
        return f"Error: failed to verify the price {err['error']}", stat
    newEntry = {
        "id": pid,
        "name": data["name"],
        "price": price,
        "category": data["category"],
    }
    products.append(newEntry)

    resp, err, code = ver_add(products, pid)
    if err != None:
        return f"Entry failed to be added \n{err['error']}", code

    product = get_product(pid)
    return f"{resp}\n\nEntry added successfully.\nyou added {product}.", code


if __name__ == "__main__":
    app.run(port=5001, debug=True)
