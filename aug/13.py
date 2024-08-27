fruits = ["banana", "orange", "apple", "coconut"]

fruits.sort()
fruits.sort(reverse=True)

print(fruits)

fruits = ("banana", "orange", "apple", "coconut")

fruits = tuple(sorted(fruits))
fruits = tuple(sorted(fruits, reverse=True))

print(fruits)

fruits = {
   "banana": 105,
   "apple": 72,
   "orange": 73,
   "coconut": 354
}

fruits = dict(sorted(fruits.items()))
fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))