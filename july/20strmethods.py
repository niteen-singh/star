user_name = input("Enter your name: ")

if len(user_name) > 12:
    print("Sorry, you can't have more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Sorry, you can't have space")
elif not user_name.isalpha():
    print("Sorry, you can only have alphabetic characters")

print(f"Hello {user_name}!")

# Enter your name: Valentine
# Hello Valentine!