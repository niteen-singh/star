# type casting = The process of converting a value of one data type to another
# (string, integer, float, boolean)
# Explicit vs Implicit

name = "Bro"
age = 21
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student)) 

# explicit casting

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

name = bool(name)
print(name)

# implicit casting

x = 2
y = 2.0
x = x / y
print(x)

# fnish
