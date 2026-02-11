# Shopping checkout debugging exercise

# SKU means stock keeping unit, it's essentially an ID for the item

def get_cart_from_user():
    """
    Prompts the user to enter cart items.
    Each item has: sku, price, quantity
    """
    cart = []

    print("Enter your shopping cart items.")
    print("Type 'done' when finished.\n")

    while True:
        sku = input("SKU (or 'done'): ")
        if sku.lower() == "done":
            break

        price = float(input("Unit price: "))
        qty = int(input("Quantity: "))

        cart.append({
            "sku": sku,
            "price": price,
            "qty": qty
        })

    return cart


def checkout_total(cart, inventory, coupon_percent, tax_rate, free_shipping_threshold, shipping_fee):

    # --- Subtotal ---
    subtotal = 0.0

    for item in cart:
        sku = item["sku"]
        price = item["price"]
        qty = item["qty"]
        available = inventory.get(sku, 0)

        if available <= qty:
            continue

        subtotal += price * qty

    # --- Coupon ---
    discount = 0.0
    if coupon_percent is not None:
        discount = subtotal * coupon_percent

    discounted_subtotal = subtotal - discount

    # --- Shipping ---
    if discounted_subtotal <= free_shipping_threshold:
        shipping = 0.0
    else:
        shipping = shipping_fee

    # --- Tax ---
    tax = subtotal * tax_rate

    # --- Total ---
    total = discounted_subtotal + shipping + tax

    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "discounted_subtotal": round(discounted_subtotal, 2),
        "shipping": round(shipping, 2),
        "tax": round(tax, 2),
        "total": round(total, 2)
    }


# ---------------- MAIN PROGRAM ----------------

inventory = {
    "A1": 5,
    "B2": 10,
    "C3": 2
}

print("Available inventory:", inventory)
print()

cart = get_cart_from_user()

coupon_percent = float(input("\nEnter coupon percent (e.g. 10 for 10% off, 0 for none): "))
tax_rate = 0.20
free_shipping_threshold = 30.0
shipping_fee = 5.00

result = checkout_total(
    cart,
    inventory,
    coupon_percent,
    tax_rate,
    free_shipping_threshold,
    shipping_fee
)

print("\n--- Checkout Summary ---")
for k, v in result.items():
    print(f"{k}: {v}")
