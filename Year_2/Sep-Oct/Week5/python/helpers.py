def val_price(data):
    try:
        price = float(data["price"])
    except ValueError as e:
        return (
            None,
            {
                "error": f"price could not be accepted. Not a valid entry (Type needs to be a float)\nError: {e}"
            },
            400,
        )
    else:
        if price > 0:
            return price, None, 200
    return None, {"error": "Price needs to be a positive number"}, 400


def id_ver(data, products):
    try:
        pid = int(data["id"])
    except ValueError as e:
        return (
            None,
            {
                "error": f"Item ID was not of type int. please use an integer for the product id\nError: {e}"
            },
            400,
        )
    else:
        if pid > 0:
            for product in products:
                if product["id"] == pid:
                    return (
                        None,
                        {
                            "error": "Id was already in products list. Please use a different ID"
                        },
                        400,
                    )
            return pid, None, 200
    return None, {"error": "products id needs to be a positive number"}, 400


def ver_add(products, pid):
    for product in products:
        if product["id"] == pid:
            return "I left it, But full rn :P (yw)", None, 201
    return None, {"error": "I ate your yummy product entry!"}, 400
