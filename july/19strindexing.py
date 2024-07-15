# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[4:8])
print(credit_number[4:])
print(credit_number[-1])
print(credit_number[-4:])
print(credit_number[::2])
print(credit_number[::3])

print(f"XXXX XXXX XXXX {credit_number[-4::]}")

# printing credit_number is reverse order
print(credit_number[::-1])

# output

# 1
# 1234
# 1234
# -567
# -5678-9012-3456
# 6
# 3456
# 13-6891-46
# 146-136
# XXXX XXXX XXXX 3456
# 6543-2109-8765-4321