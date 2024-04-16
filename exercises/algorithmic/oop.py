"""
OOP Exercise 1: Create a Classes class without any variables and methods
"""


class Classes:
    pass


"""
OOP Exercise 2: Create a Class with instance attributes

Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""


class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100


"""
OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

Give the capacity argument of Bus.seating_capacity() a default value of 50.

The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
"""


class Bus(Vehicle):
    def display_attributes(self):
        return f"Color: {self.color} Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self):
        amount = super().fare()
        extra_amount = amount + (amount / 10)
        return f"Total Bus fare is: {extra_amount}"


"""
OOP Exercise 4: Define a property that must have the same value for every class instance (object)

Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
"""


class Car(Vehicle):
    def display_attributes(self):
        return f"Color: {self.color} Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"


"""
OOP Exercise 5: Check type of an object
"""


def type_object(cl):
    return type(cl)


"""
OOP Exercise 6: Determine if School_bus is also an instance of the Vehicle class
"""


def is_instance(child_class, parent_class):
    return isinstance(child_class, parent_class)
