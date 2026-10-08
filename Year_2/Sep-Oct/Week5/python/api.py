from flask import Flask, request

from helpers import val_price, id_ver, ver_add

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

@app.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    for product in products:
        if product["id"] == id:
            return product
        else:
            ...
    return {"error" :"product not found"}, 404

@app.route("/product", methods=["POST"])
def add_prod():
    data = request.form
    new_pro = {"id","name","price","catagory"}
    missing = [k for k in new_pro if not data.get(k)]
    if missing:
        return{"error": f"you were missing: {', '.join(missing)}"}, 400
    id, stat_c = id_ver(data, products)
    if stat_c == 200:
        price, stat = val_price(data)
        if stat == 200:
            newEntry = {"id": id, "name": data["name"], "price": price, "catagory": data["catagory"],}
            products.append(newEntry)
        elif stat == 400:
            return f"Error: failed to verify the price {price}"
    elif stat_c == 400:
        return f"Error: {id}"

    resp, code = ver_add(products, id)
    if code == 201:
        product = get_product(id)
        return f"Entry added successfully.\nyou added {product}."
    elif code == 400:
        return f"Entry failed to be added \n{resp}"
    return "All is quiet on the western front"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
