#Dictionary task
"""
dictionary = {"Key":"Value", "dog":"Harley"}
# The Key is how the value is indexed and located
print(dictionary["dog"])
#Outputs Harley 
"""

checkout = False

shopinvo = {"Custard Creams":0.56, "Lemonade":1.50, "Bread":0.40, "Milk":1, "Pringles":1.99, "An smart plug":4.99, "mealdeal":3, 
            "An batteries":2.99, "Gum":0.99, "Keyboard":2}

print(shopinvo)

items = []

total = 0
while checkout != True:
    wtw = input("What do you want to buy? ")
    items.append(wtw)
    Dwtco = input("Do you want to check out? ").lower()
    if Dwtco == "yes":
        for item in items:
            total = total + shopinvo[item]
            print("£", total)
        print("Total cost is £",total)
        
        checkout = True
    else:
        print("")

