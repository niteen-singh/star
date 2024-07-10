x = 3.14
y = 4
z = 2

# this round func is used to round up the float number
one = round(x)

# absolute value is a distance away from 0 as a whole number
two = abs(y)

# power (two to the power of z)
three = pow(two,z)

# maximum and minimum of these three variables
four = max(x,y,z)
five = min(x,y,z)

print(one,two,three,four,five)

# output
# 3, 4, 16, 4, 2

import math

x = 5
y = 7.5

print(round(math.pi, 2))
print(round(math.e, 2))

one = round(math.sqrt(x), 2)

# ceil always round a floating point number up and floor does opposite
two = math.ceil(y)
three = math.floor(y)

print(one, two, three)

# output
# 3.14
# 2.72
# 2.24, 8, 7




