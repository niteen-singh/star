# simple program to create a calculator using if and else statement

operator = input("Enter an operator( + - * / ): ")

one = int(input("Enter a number: "))
two = int(input("Enter a number: "))

if operator == "+":
    print(one + two)
elif operator == "-":
    print(one - two)
elif operator == "*":
    print(one * two)
elif operator == "/":
    print(one / two)
else:
    print(f"this {operator} is not a valid operator")

# output
# Enter an operator( + - * / ): +
# Enter a number: 2
# Enter a number: 4
# 6

# Enter an operator( + - * / ): -
# Enter a number: 2
# Enter a number: 6
# -4

# Enter an operator( + - * / ): *
# Enter a number: 3
# Enter a number: 4
# 12

# Enter an operator( + - * / ): /
# Enter a number: 9
# Enter a number: 3
# 3.0