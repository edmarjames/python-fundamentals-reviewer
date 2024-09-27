# Exercise 1: Polymorphic Employee System
# Create a base class `Employee` with a `work()` method that prints "Working...". Then, create three derived classes: `Manager`, `Designer`, and `Developer`. Each class should override the `work()` method to print job-specific tasks.
    # **Input**: Create instances of `Manager`, `Designer`, and `Developer` and call their `work()` method.
    # **Expected Output**:
    # Managing team
    # Designing interfaces
    # Writing code

# solution
class Employee:
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        return "Managing team"

class Designer(Employee):
    def work(self):
        return "Designing interfaces"

class Developer(Employee):
    def work(self):
        return "Writing code"

emp1 = Manager()
emp2 = Designer()
emp3 = Developer()
employees = [emp1, emp2, emp3]
for emp in employees:
    print(emp.work())


print("\r")
# Exercise 2: Polymorphism with Animal Sounds
# Create a base class `Animal` with a method `make_sound()` that returns "Some sound". Then create child classes `Dog`, `Cat`, and `Cow` that override the `make_sound()` method with their specific sounds: "Bark", "Meow", and "Moo" respectively.
    # **Input**: Create a list of animal objects and loop through them, calling `make_sound()` on each.
    # **Expected Output**:
    # Bark
    # Meow
    # Moo

# solution
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

animal1 = Dog()
animal2 = Cat()
animal3 = Cow()
animals = [animal1, animal2, animal3]
for animal in animals:
    print(animal.make_sound())


print("\r")
# Exercise 3: Vehicle Polymorphism
# Create a base class `Vehicle` with a method `start_engine()` that prints "Engine started". Create child classes `Car`, `Truck`, and `Motorcycle`, each overriding `start_engine()` to print a different engine sound.
    # **Input**: Create a list of vehicles (`Car`, `Truck`, `Motorcycle`) and call the `start_engine()` method for each.
    # **Expected Output**:
    # Car engine roars
    # Truck engine rumbles
    # Motorcycle engine revs

# solution
class Vehicle:
    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def start_engine(self):
        return "Car engine roars"

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine rumbles"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine revs"

vehicle1 = Car()
vehicle2 = Truck()
vehicle3 = Motorcycle()
vehicles = [vehicle1, vehicle2, vehicle3]
for vehicle in vehicles:
    print(vehicle.start_engine())


print("\r")
# Exercise 4: Dynamic Method Binding
# Create a base class `Shape` with a method `area()` that raises a `NotImplementedError`. Create subclasses `Circle` and `Square` that override `area()` to compute the area based on their dimensions. Use polymorphism to call the `area()` method dynamically on different objects.
    # **Input**: Create instances of `Circle` (radius 3) and `Square` (side 4). Use a loop to call `area()` on both.
    # **Expected Output**:
    # Circle area: 28.27
    # Square area: 16

# solution
import math
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = math.pi
        area = pi * (self.radius**2)
        return f"Circle area: {round(area, 2)}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side**2
        return f"Square area: {area}"

shape1 = Circle(3)
shape2 = Square(4)
shapes = [shape1, shape2]
for shape in shapes:
    print(shape.area())


print("\r")
# Exercise 5: Operator Overloading
# Create a class `Box` that overloads the `+` operator to combine the volumes of two box objects. Each `Box` object should have a length, width, and height. Use polymorphism by defining a custom `__add__()` method.
    # **Input**: Create two `Box` objects with dimensions `(2, 3, 4)` and `(1, 1, 1)` and add them together.
    # **Expected Output**:
    # Combined volume: 25

# solution
class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def __add__(self, val2):
        volume = (self.length * self.width * self.height) + (val2.length * val2.width * val2.height)
        return f"Combined volume: {volume}"

box1 = Box(2, 3, 4)
box2 = Box(1, 1, 1)
print(box1 + box2)


print("\r")
### Exercise 6: E-commerce Polymorphism
# Create a base class `PaymentMethod` with a method `pay()` that prints "Processing payment". Create child classes `CreditCard`, `PayPal`, and `BankTransfer`, each overriding the `pay()` method to process payments differently.
    # **Input**: Call the `pay()` method for each payment method.
    # **Expected Output**:
    # Processing payment via Credit Card
    # Processing payment via PayPal
    # Processing payment via Bank Transfer

# solution
class PaymentMethod:
    def pay(self):
        return "Processing payment"

class CreditCard(PaymentMethod):
    def pay(self):
        return "Processing payment via Credit Card"

class Paypal(PaymentMethod):
    def pay(self):
        return "Processing payment via PayPal"

class BankTransfer(PaymentMethod):
    def pay(self):
        return "Processing payment via Bank Transfer"

pay1 = CreditCard()
pay2 = Paypal()
pay3 = BankTransfer()
payments = [pay1, pay2, pay3]
for payment in payments:
    print(payment.pay())
