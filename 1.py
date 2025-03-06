size = input("choose your pizza size (s/m/l):")
pepperoni = input("do yo need pepperoni or not (yes/no):")
extra_cheese = input("do you need extra cheese or not(yes/no):")
price = ""
if size=="s":
    price = 150
    if pepperoni == "yes":
        price += 20

        if extra_cheese == "yes":
            price += 10
        else:
            price = 150

elif size == "m":
    price = 200
    if pepperoni == "yes":
        price += 30
        if extra_cheese == "yes":
            price += 10
        else:
            price = 200

elif size == "l":
    price = 250
    if pepperoni == "yes":
        price += 30
        if extra_cheese == "yes":
            price += 10
        else:
            price = 250

print("Total bill is :RS.",price)