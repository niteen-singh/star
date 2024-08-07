class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

class Dog(Animal):
    def speak(self):
        print("WooF!!")

class Cat(Animal):
    def speak(self):
        print("MeoW!!")

class Mouse(Animal):
    def speak(self):
        print("SqueeK!!")

dog = Dog("chimera")
dog.eat()
dog.sleep()
dog.speak()
print(dog.name)

print()

cat = Cat("luffy")
cat.eat()
cat.sleep()
cat.speak()
print(cat.name)

print()

mouse = Mouse("ham")
mouse.eat()
mouse.sleep()
mouse.speak()
print(mouse.name)