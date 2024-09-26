# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# To create a class, use the keyword "class".
class TestClass:
    greet = "Hello"

# Create an Object
# Now we can use the class named TestClass to create objects.
a = TestClass()
print(a.greet)

print("\r")
# The __init__() function
# To understand the meaning of classes we have to understand the built-in "__init__()" function.
# All classes have a function called "__init__()", which is always executed when the class is being initiated.
# Use the "__init__()" function to assign values to object properties, or other operations that are necessary to do when the object is being created.
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

h1 = Human("Edmar", 26)
print(h1.name)
print(h1.age)

print("\r")
# The __str__() function
# The "__str__()" function controls what should be returned when the class object is represented as a string.
# If the "__str__()" function is not set, the string representation of the object is returned.
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} - {self.position}"

e1 = Employee("John", "Software Engineer")
print(e1)

print("\r")
# Object methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
class Onboard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def greet(self):
        return f"Hello {self.name}, Welcome to the NPC arc!"
    
o1 = Onboard("Edmar")
print(o1.greet())

print("\r")
# The self parameter
# The "self" parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named "self", you can call it whatever you like, but it has to be the first parameter of any function in the class.
class Thingamabob:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        consonants = ["a", "e", "i", "o", "u"]
        lower_title = self.title.lower()
        con = "an" if lower_title[0] in consonants else "a"            
        return f"This is called {con} {self.title}"
    
t1 = Thingamabob("Aglet")
t2 = Thingamabob("Zipper")
print(t1)
print(t2)

print("\r")
# Modify Object Properties
# You can modify properties on objects like this
class Pet:
    def __init__(self, name, color, age):
        self.name = name        
        self.color = color
        self.age = age

    def __str__(self):
        return f"Hello {self.name} - {self.color}"
    
nova = Pet("Nova", "White", 7)
print(f"Nova is color {nova.color}")
nova.color = "Brownish White"
print(f"Nova is color {nova.color} now")

# Delete Object Properties
# You can delete properties on objects by using the "del" keyword.
del nova.age
# print(nova.age) - this will raise an error

# Delete Objects
# You can delete objects by using the "del" keyword.
del t2
# print(t2) - - this will raise an error

# The pass statement
# class definitions cannot be empty, but if you for some reason have a "class" definition with no content, put in the "pass" statement to avoid getting an error.
class Test:
    pass