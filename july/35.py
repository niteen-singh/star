import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for i in plain_text:
    index = chars.index(i)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

# DECRYPTION
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for i in cipher_text:
    index = key.index(i)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")