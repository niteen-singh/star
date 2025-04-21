arr = []
n = int(input("enter size of array: "))
for i in range(n):
    arr.append(int(input("enter element: ")))
print(arr)

search = int(input("enter element to search: "))
k = 0
for i in arr:
    if i == search:
        break
    k += 1
print(f"element {search} is found at index {k} ")

i = 0
j = n - 1
while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i += 1
    j -= 1
print(arr)
