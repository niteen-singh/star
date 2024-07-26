menu = {"burger": 100,
        "pizza": 150,
        "coffee": 50,
        "biryani": 120,
        "Gulabjamun": 620}

for item, price in menu.items():
    print(f"{item}: {price}")

orders = []

while True:
    item = input("enter item or q to quit: ")
    if item.lower() == "q":
        break
    else:
        quantity = int(input("enter quantity: "))
        orders.append((item, quantity))

print("your order")
for order in orders:
    print(f"{order[0]}: {order[1]}")