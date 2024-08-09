# insertion sort
size = int(input("enter size of array: "))
arr = []
for i in range(size):
    arr.append(int(input(f"enter {i} element of array: ")))
print(arr)

insert = []
for i in range(1, size):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("sorted", arr)