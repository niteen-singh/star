# while loop = perform some code WHILE some condition remains

name = input("enter your name: ")
while name == "":
    print("you did not enter a name!!!")
    name = input("enter your name: ")
print(f"your name is {name}")

age = int(input("enter your age: "))
while age < 0:
    print("age cannot be negative")
    age = input("enter your age: ")
print(f"your age is {age}")

food = input("enter your favorite food (q to quit): ")
while not food == "q":
    print(f"{food}")
    food = input("enter your favorite food (q to quit): ")
print("Thank you!")

num = int(input("enter a phone number: "))
while len(str(num)) > 10:
    print("enter a ten digit phone number!!!!")
    num = int(input("enter a phone number: "))
print(f"Your number is {num}")