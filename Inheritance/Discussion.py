# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# "Parent class" is the class being inherited from, also called base class.
# "Child class" is the class that inherits from another class, also called derived class.

# Create a parent class
# Any class can be a parent class, so the syntax is the same as creating any other class.
class Human:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name

    def print_name(self):
        print(f"{self.fname} {self.lname}")

h1 = Human("Edmar", "Bautista")
h1.print_name()

# Create a child class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.
class Pupil(Human):
    pass

p1 = Pupil("John", "Doe")
p1.print_name()

# Add the __init__() function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the "__init__()" function to the child class
# When you add the "__init__()" function, the child class will no longer inherit the parent's "__init__()" function.
# To keep the inheritance of the parent's "__init__()" function, add a call to the parent's "__init__()" function.
class Worker(Human):
    def __init__(self, first_name, last_name):
        Human.__init__(self, first_name, last_name)

# Use the super() function
# Python also has a "super()" function that will make the child class inherit all the methods and properties from its parent.
# By using the "super()" function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
class Teacher(Human):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

# Add properties
class Student(Human):
    def __init__(self, first_name, last_name, course):
        super().__init__(first_name, last_name)
        self.course = course

s1 = Student("Jane", "Doe", "Computer Science")
print(s1.course)

# Add methods
# note: If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
class Trainee(Human):
    def __init__(self, first_name, last_name, training):
        super().__init__(first_name, last_name)
        self.training = training

    def welcome_greeting(self):
        print(f"Welcome {self.fname} {self.lname} to {self.training}")

t1 = Trainee("James", "Smith", "Web Development")
t1.welcome_greeting()