def val_price(data):
    try:
        float(data["price"])
    except ValueError as e:
        return {
            "error": f"price could not be accepted. Not a valid entry (Type needs to be a float)\nError: {e}"
        }, 400
    else:
        return data["price"], 200


def id_ver(data, products):
    if data["id"] in products:
        return {
            "error": "Id was already in products list. Please use a different ID"
        }, 400
    else:
        return data["id"], 200

def ver_add(products, id):
    for product in products:
        if product["id"] == id:
            return {"error":"success"}, 201
    return {"error":"product not added"}, 400
