# Email slicer

email = input('Enter your email: ')

if len(email) < 30:
    user_name = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    print(f"your username is {user_name} and domain is {domain}")

else:
    print("your email is too long it should be less than 20 characters")

# output
# Enter your email: nitinsingh@gmail.com
# your username is nitinsingh and domain is gmail.com