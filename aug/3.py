class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, year, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    def display_car(self):
        return f" {self.make} {self.model} of {self.year} {self.engine.horse_power}(hp) {self.wheels[0].size}in "

car = Car("ford", "mustang", 1990, 1200, 18)
print(car.display_car())