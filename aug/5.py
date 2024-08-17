class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance methods - Best for operations on instances of the class (objects)
    def get_info(self):
        return f"{self.name} : {self.position}"

    # Static methods - Best for utility functions that do not need access to class data
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

print(Employee.is_valid_position("doodwala"))
emp1 = Employee("Nitin", "student")
print(emp1.get_info())