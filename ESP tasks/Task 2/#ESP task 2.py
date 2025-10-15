#ESP task 2

# minecraft_trading_billing_STUDENT.py
# Village Trading & Billing – Minecraft theme

stands = [["STAND 1 - ", 0],["STAND 2 - ", 0],["STAND 3 - ", 0],["STAND 4 - ", 0],["STAND 5 - ", 0],
          ["STAND 6 - ", 0],["STAND 7 - ", 0],["STAND 8 - ", 0],["STAND 9 - ", 0],["STAND 10 - ", 0]]

menu = {
    "Bread": 2.00,
    "Arrow": 0.50,
    "Iron Pickaxe": 12.00,
    "Shield": 8.00,
    "Golden Apple": 20.00,
    "Torch": 0.25
}

def get_clerk_name():
    flag = True
    while flag:
        clerk = input("Enter your player name: ")
        if clerk.isalpha() == False:
            print("Name not recognised.")
            flag = True
        else:
            clerk = f"Clerk: {clerk.capitalize()}"
            flag = False
    return clerk

def get_stand_number():
    flag = True
    while flag:
        stand_num = input("Enter stand number (1-10): ")
        try:
            int(stand_num)
        except:
            print("You did not enter a number.")
            flag = True
        else:
            stand_num = int(stand_num)
            if stand_num < 1 or stand_num > 9:
                print("Stand must be between 1 and 10.")
                flag = True
            else:
                flag = False
    return stand_num

def get_item():
    flag = True
    while flag:
        item = input("Enter item (x to finish): ")
        if item.isalpha() == False and item not in ("x","X"):
            print("Invalid item name.")
            flag = True
        elif item in ("x","X"):
            flag = False
        elif item.title() not in menu:
            print("That item is not in the shop.")
            flag = True
        else:
            item = item.title()
            flag = False
    return item

def get_qty():
    flag = True
    while flag:
        q = input("Enter quantity: ")
        try:
            int(q)
        except:
            print("Quantity must be a whole number.")
            flag = True
        else:
            q = int(q)
            if q < 1:
                print("Quantity must be positive.")
                flag = True
            else:
                flag = False
    return q

def get_discount_choice():
    print("\n### Choose Discount ###")
    print("1. Happy Hour (15%)")
    print("2. Staff (Villager) (25%)")
    print("3. No discount")
    flag = True
    while flag:
        ch = input("Select 1/2/3: ")
        try:
            ch = int(ch)
        except:
            print("Not a valid option.")
            flag = True
        else:
            if ch < 1 or ch > 3:
                print("Option must be 1, 2 or 3.")
                flag = True
            else:
                if ch == 1:
                    discount = 15
                elif ch == 2:
                    discount = 25
                else:
                    discount = 0
                flag = False
    return discount

running = True
while running:
    print("\n###############################################")
    print("#### Village Trading & Billing (Minecraft) ####")
    print("###############################################\n")
    print("1. Enter trade order")
    print("2. Output bill")
    print("3. Exit\n")

    choice = input("Enter option: ")

    if choice == "1":
        clerk = get_clerk_name()
        stand = get_stand_number()

        stands[stand].append(clerk)

        item_loop = True
        subtotal = 0.0

        stands[stand-1].remove(0)

        while item_loop:
            it = get_item()
            if it in ("x","X"):
                stands[stand-1].append(subtotal)
                item_loop = False
            else:
                qty = get_qty()
                price = menu[it]
                cost = price * qty
                stands[stand-1].append(it)
                stands[stand-1].append(qty)
                stands[stand-1].append(cost)
                subtotal = subtotal + (cost * qty)

    elif choice == "2":
        stand = get_clerk_name()
        disc = get_discount_choice()
        print(str(stands[stand - 1][0]))
        print(str(stands[stand - 1][1]))
        print("Summary before discounts:")
        print(str(stands[stand - 1][2:-1]))
        print(f"Discount selected = {disc}")
        sb = float(stands[stand - 1][-1])
        print(f"Subtotal = {sb} emeralds")
        final_total = sb - (sb * disc)
        print(f"Final total = {final_total} emeralds")

    elif choice == "3":
        exit()
    else:
        pass
