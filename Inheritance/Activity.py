# 1. **Multiple Levels of Inheritance**
# Create a class `Animal` with a method `make_sound()`. Then create two subclasses, `Mammal` and `Bird`, which inherit from `Animal`. Add a third level of inheritance by creating classes `Dog` and `Parrot` that inherit from `Mammal` and `Bird`, respectively, and override the `make_sound()` method.

# **Example:**
# class Animal:
#     # Base class with method make_sound()

# class Mammal(Animal):
#     # Inherits from Animal

# class Bird(Animal):
#     # Inherits from Animal

# class Dog(Mammal):
#     # Inherits from Mammal

# class Parrot(Bird):
#     # Inherits from Bird

# dog = Dog()
# parrot = Parrot()
# print(dog.make_sound())  # Output: "Bark!"
# print(parrot.make_sound())  # Output: "Squawk!"


# 2. **Call Parent Method from Child Class**
# Create a class `Vehicle` with a method `start_engine()`. Create a child class `Car` that inherits from `Vehicle` and overrides `start_engine()`. In the overridden method, call the parent method using `super()`.

# **Example:**
# class Vehicle:
#     # Base class with start_engine()

# class Car(Vehicle):
#     # Inherits from Vehicle and overrides start_engine()

# car = Car()
# car.start_engine()  # Output: "Engine started (from Vehicle)" followed by "Car engine started"


# 3. **Inheritance and Polymorphism**
# Create a parent class `Shape` with a method `area()`. Create two child classes `Triangle` and `Rectangle` that inherit from `Shape` and override the `area()` method to calculate the area for each shape. Use polymorphism to create a list of different shapes and print their areas.

# **Example:**
# class Shape:
#     # Base class with method area()

# class Triangle(Shape):
#     # Inherits from Shape and overrides area()

# class Rectangle(Shape):
#     # Inherits from Shape and overrides area()

# shapes = [Triangle(10, 5), Rectangle(10, 20)]
# for shape in shapes:
#     print(shape.area())  # Output: "25" for Triangle, "200" for Rectangle


# 4. **Use Inheritance with Class Variables**
# Create a parent class `Person` with a class variable `count` that keeps track of how many `Person` objects have been created. Create a child class `Employee` that inherits from `Person` and make sure the count updates when an employee object is created.

# **Example:**
# class Person:
#     # Class variable count and a constructor

# class Employee(Person):
#     # Inherits from Person

# e1 = Employee("Alice")
# e2 = Employee("Bob")
# print(Person.count)  # Output: 2


# 5. **Method Overriding in a Child Class**
# Create a parent class `Account` with methods `deposit()` and `withdraw()`. Create a child class `SavingsAccount` that overrides the `withdraw()` method to prevent the balance from going below a certain threshold.

# **Example:**
# class Account:
#     # Base class with deposit and withdraw methods

# class SavingsAccount(Account):
#     # Inherits from Account and overrides withdraw

# savings = SavingsAccount(1000)
# savings.withdraw(500)  # Output: "500 withdrawn"
# savings.withdraw(600)  # Output: "Withdrawal denied. Balance cannot go below 100."


# 6. **Inheritance with Class Method**
# Create a parent class `Product` with a class method `total_products()` that keeps track of the number of products created. Create a child class `Electronics` that inherits from `Product` and ensure that the class method still works when creating `Electronics` objects.

# **Example:**
# class Product:
#     # Base class with class method total_products()

# class Electronics(Product):
#     # Inherits from Product

# p1 = Product()
# e1 = Electronics()
# print(Product.total_products())  # Output: 2


# 7. **Use of `super()` in Multi-level Inheritance**
# Create three classes: `Person`, `Student`, and `GraduateStudent`. `GraduateStudent` should inherit from `Student`, which in turn inherits from `Person`. Use `super()` to initialize attributes properly across multiple levels of inheritance.

# **Example:**
# class Person:
#     # Base class with constructor

# class Student(Person):
#     # Inherits from Person and uses super()

# class GraduateStudent(Student):
#     # Inherits from Student and uses super()

# grad = GraduateStudent("John", "Doe", "MSc Computer Science")
# print(grad.full_name())  # Output: "John Doe"
# print(grad.course)  # Output: "MSc Computer Science"


# 8. **Abstract Class with Inheritance**
# Create an abstract class `Vehicle` with an abstract method `fuel_efficiency()`. Create two concrete classes `Car` and `Bike` that inherit from `Vehicle` and provide their own implementation of `fuel_efficiency()`.

# **Example:**
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     # Abstract class with fuel_efficiency method

# class Car(Vehicle):
#     # Inherits from Vehicle and implements fuel_efficiency

# class Bike(Vehicle):
#     # Inherits from Vehicle and implements fuel_efficiency

# car = Car()
# bike = Bike()
# print(car.fuel_efficiency())  # Output: Car's fuel efficiency (e.g., 12 km/l)
# print(bike.fuel_efficiency())  # Output: Bike's fuel efficiency (e.g., 35 km/l)


# 9. **Inheritance with Multiple Child Classes**
# Create a class `Person` with common attributes like name and age. Then create two child classes `Student` and `Teacher`, each having additional attributes such as `course` for students and `subject` for teachers. Both should have a method to introduce themselves.

# **Example:**
# class Person:
#     # Base class with name and age attributes

# class Student(Person):
#     # Inherits from Person and adds course

# class Teacher(Person):
#     # Inherits from Person and adds subject

# student = Student("Jane", 20, "Mathematics")
# teacher = Teacher("Mr. Smith", 40, "Physics")
# print(student.introduce())  # Output: "I am Jane, a 20-year-old student of Mathematics."
# print(teacher.introduce())  # Output: "I am Mr. Smith, a 40-year-old teacher of Physics."


# 10. **Overriding the `__str__()` Method in Child Classes**
# Create a parent class `Book` with attributes `title` and `author`. Then, create a child class `Ebook` that inherits from `Book` and adds a `file_size` attribute. Override the `__str__()` method in both classes to provide meaningful string representations.

# **Example:**
# class Book:
#     # Base class with title and author attributes

# class Ebook(Book):
#     # Inherits from Book and adds file_size

# book = Book("1984", "George Orwell")
# ebook = Ebook("The Hobbit", "J.R.R. Tolkien", "5MB")
# print(book)  # Output: "1984 by George Orwell"
# print(ebook)  # Output: "The Hobbit by J.R.R. Tolkien (5MB)"