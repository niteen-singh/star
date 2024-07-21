# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# ---------------- EXAMPLE 1 ----------------

for x in range(1, 11):
    print(x)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# ---------------- EXAMPLE 2 ----------------

for x in reversed(range(1, 11)):
    print(x)

print("Happy New Year!")

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Happy New Year!

# ---------------- EXAMPLE 3 ----------------

for x in range(1, 11, 2):
    print(x)

# 1
# 3
# 5
# 7
# 9

# ---------------- EXAMPLE 4 ----------------

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# 1
# 2
# 3
# 4
# -
# 5
# 6
# 7
# 8
# -
# 9
# 0
# 1
# 2
# -
# 3
# 4
# 5
# 6

# ---------------- CONTINUE ----------------

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 14
# 15
# 16
# 17
# 18
# 19
# 20

# ---------------- BREAK ----------------

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12