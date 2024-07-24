# shopping cart

item = []
prices = []
total = 0

while True:
    items = input("enter item name (q to quit): ")
    if items == 'q':
        break
    else:
        item.append(items)
        price = float(input("enter price: "))
        prices.append(price)

print("----- YOUR CART -----")

for items in item:
    print(items)

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")