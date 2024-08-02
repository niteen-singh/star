def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="sharma", first="pujan")

# ----- EXAMPLE -----
for number in range(1, 11):
    print(number, end=" ")
print()
print("1", "2", "3", "4", "5", sep="-")

# ----- EXERCISE -----
def get_phone(country, number):
    return f"{country}-{number}"

phone_num = get_phone(country=91, number=8087265433)
print(phone_num)