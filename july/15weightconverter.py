# converting the weight from kg to pound or pounds to kgs

unit = input("Enter your unit (K or L): ")
weight = int(input("Enter your weight : "))

if unit == "K":
    weight *= 2.205
    unit = "lbs"
elif unit == "L":
    weight /= 2.205
    unit = "kgs"
else:
    print("Please enter a valid unit (K or L)")

print(f"your weight in {unit} is {round(weight, 2)}")

# output
# Enter your unit (K or L): K
# Enter your weight : 100
# your weight in lbs is 220.5

# Enter your unit (K or L): L
# Enter your weight : 220
# your weight in kgs is 99.77