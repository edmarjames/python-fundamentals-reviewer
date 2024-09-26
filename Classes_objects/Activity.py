# 1. **Create a Class with Multiple Methods**
# Create a `Rectangle` class with attributes for length and width. Add methods to calculate the perimeter and area of the rectangle.
    # **Example:**
    # class Rectangle:
    #     # Your implementation here
    # rect1 = Rectangle(10, 5)
    # print(rect1.area())       # Output: 50
    # print(rect1.perimeter())  # Output: 30

# solution
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)
    
    def get_area(self):
        return self.length * self.width

rect1 = Rectangle(10, 5)
print(rect1.get_area())
print(rect1.get_perimeter())


print("\r")
# 2. **Class Inheritance**
# Create a base class `Animal` with methods like `sound()`. Then create two derived classes: `Dog` and `Cat`, which should inherit from `Animal` and override the `sound()` method.
    # **Example:**
    # class Animal:
    #     # Base class with a method sound()

    # class Dog(Animal):
    #     # Inherits from Animal

    # class Cat(Animal):
    #     # Inherits from Animal

    # dog = Dog("Buddy")
    # cat = Cat("Whiskers")
    # print(dog.sound())  # Output: "Woof!"
    # print(cat.sound())  # Output: "Meow!"

# solution
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)        

    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)        

    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.sound())
print(cat.sound())


print("\r")
# 3. **Implement a Bank Account Class**
# Create a `BankAccount` class that has methods for depositing and withdrawing money. Implement balance checks to prevent overdrafts.
    # **Example:**
    # class BankAccount:
    #     # Your implementation here

    # account = BankAccount("Edmar", 1000)
    # account.deposit(500)
    # print(account.balance)  # Output: 1500
    # account.withdraw(2000)  # Output: "Insufficient balance!"
    # print(account.balance)  # Output: 1500

# solution
class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def balance(self):
        return self.amount
    
    def deposit(self, deposit_amount):
        self.amount = self.amount + deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.amount:
            self.amount = self.amount - withdraw_amount
        else:
            print("Insufficient balance!") 
        
account = BankAccount("Edmar", 1000)
account.deposit(500)
print(account.balance())
account.withdraw(2000)
print(account.balance())


print("\r")
# 4. **Class with Private Attributes**
# Create a class `Student` with private attributes `name` and `grade`. Write methods to access and modify these private attributes safely.
    # **Example:**
    # class Student:
    #     # Your implementation here

    # s1 = Student("John", 85)
    # print(s1.get_grade())  # Output: 85
    # s1.set_grade(90)
    # print(s1.get_grade())  # Output: 90

# solution
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, new_grade):
        self.__grade = new_grade

s1 = Student("John", 85)
print(s1.get_grade())
s1.set_grade(90)
print(s1.get_grade())


print("\r")
# 5. **Polymorphism in Action**
# Create a base class `Shape` with a method `area()`. Then, create derived classes `Circle` and `Square`, each implementing their version of the `area()` method.
    # **Example:**
    # class Shape:
    #     # Base class with method area()

    # class Circle(Shape):
    #     # Derived class for Circle

    # class Square(Shape):
    #     # Derived class for Square

    # circle = Circle(5)  # Circle with radius 5
    # square = Square(4)  # Square with side 4
    # print(circle.area())  # Output: 78.5 (approx)
    # print(square.area())  # Output: 16

# solution
import math
class Shape:
    def area():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = math.pi
        area = pi * (self.radius**2)
        return round(area, 1)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):        
        area = self.side * self.side
        return area
    
circle = Circle(5) 
square = Square(4)
print(circle.area())
print(square.area())


print("\r")
# 6. **Class with Static and Class Methods**
# Create a class `Employee` with a class variable `num_employees` that keeps track of the number of employees. Add a static method to calculate a bonus and a class method to get the number of employees.
    # **Example:**
    # class Employee:
    #     # Your implementation here

    # e1 = Employee("Alice", 5000)
    # e2 = Employee("Bob", 6000)
    # print(Employee.num_employees)       # Output: 2
    # print(Employee.calculate_bonus(10))  # Output: 500 (for example)

# solution
class Employee:
    num_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_employees += 1                

    @staticmethod
    def calculate_bonus(salary, bonus_percentage):
        return salary * (bonus_percentage / 100)

    @classmethod
    def get_num_employees(cls):
        return cls.num_employees
        
e1 = Employee("Alice", 5000)
e2 = Employee("Bob", 6000)
print(Employee.get_num_employees())      
print(Employee.calculate_bonus(e1.salary, 10))
print(Employee.calculate_bonus(e2.salary, 15))


print("\r")
### 7. **String Representation with `__str__`**
# Write a class `Book` that includes attributes for title, author, and year. Override the `__str__()` method to print the book's details in a formatted string.
    # **Example:**
    # class Book:
    #     # Your implementation here
    # book = Book("The Alchemist", "Paulo Coelho", 1988)
    # print(book)  # Output: "The Alchemist by Paulo Coelho (1988)"

# solution
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
book = Book("The Alchemist", "Paulo Coelho", 1988)
print(book)


print("\r")
### 8. **Compare Objects Using `__eq__`**
# Create a `Point` class with x and y coordinates. Override the `__eq__()` method to compare two `Point` objects for equality.
    # **Example:**
    # class Point:
    #     # Your implementation here

    # p1 = Point(3, 4)
    # p2 = Point(3, 4)
    # p3 = Point(5, 6)
    # print(p1 == p2)  # Output: True
    # print(p1 == p3)  # Output: False

# solution
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(5, 6)
print(p1 == p2)
print(p1 == p3)


print("\r")
### 9. **Destructor (`__del__`)**
# Write a class `File` that simulates opening and closing a file. Implement the `__del__()` method to close the file when the object is deleted.
    # **Example:**
    # class File:
    #     # Your implementation here

    # file = File("sample.txt")
    # del file  # Output: "File closed"

# solution
class File:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("File closed")

file = File("sample.txt")
del file


print("\r")
### 10. **Class Composition**
# Create a class `Person` that has an instance of another class `Address`. The `Address` class should store the city and country of the person.
    # **Example:**
    # class Address:
    #     # Your implementation here

    # class Person:
    #     # Your implementation here

    # addr = Address("Manila", "Philippines")
    # person = Person("Edmar", addr)
    # print(person.get_address())  # Output: "Edmar lives in Manila, Philippines"

# solution
class Address:
    def __init__(self, city, country):        
        self.city = city
        self.country = country
    
class Person():
    def __init__(self, name, address):        
        self.name = name
        self.address = address

    def get_address(self):
        return f"{self.name} lives in {self.address.city}, {self.address.country}"

addr = Address("Manila", "Philippines")
person = Person("Edmar", addr)
print(person.get_address())
