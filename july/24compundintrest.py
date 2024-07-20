# compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("Principle can't be less than zero")

while True:
    rate = float(input("Enter the interest rate in (%): "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate can't be less than zero")

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be less than zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: Rs{total:.2f}")

# output
# Enter the principle amount: 12000
# Enter the interest rate in (%): 12
# Enter the time in years: 2
# Balance after 2 year/s: Rs15052.80