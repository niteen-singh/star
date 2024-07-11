# if = Do some code IF condition is True
# else = Do something else if above condition/s are False

# simple age signup program

age = int(input("Enter your age: "))

if age >= 75:
   print("You are too old to sign up")
elif 74 >= age >= 18:
   print("You are now signed up")
elif age < 0:
   print("You haven't been born yet")
else:
   print("You must be 18+ sign up")

# output
# Enter your age: 72
# You are now signed up

# if else program to take input from user as yes or no

response = input("Do you want food (Y/N)?: ")

if response == "Y":
   print("Have some food")
else:
   print("No food for you!")

# output
# Do you want food (Y/N)?: n
# No food for you!

# if else using f string.

name = input("Enter your name: ")

if name == "":
   print("You did not enter your name!")
else:
   print(f"Hello {name}")

# output
# Enter your name: nitin
# Hello nitin

# if else program in boolean

online = False

if online :
   print("You are online")
else:
   print("You are offline")

# output
# You are offline