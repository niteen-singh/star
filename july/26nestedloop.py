# nested loop = A loop within another loop (outer, inner)

row1 = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")
for row in range(row1):
    for col in range(cols):
        print(symbol, end=" ")
    print()

# Enter number of rows: 3
# Enter number of columns: 3
# Enter symbol: *
# * * *
# * * *
# * * *
print("\n")

rows = int(input("Enter number of rows: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("!", end=" ")
    print()

# Enter number of rows: 5
# !
# ! !
# ! ! !
# ! ! ! !
# ! ! ! ! !

print("\n")

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("!", end=" ")
    print()

# ! ! ! ! !
# ! ! ! !
# ! ! !
# ! !
# !