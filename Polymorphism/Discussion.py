# The word "polymorphism" means many forms, and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# Class Polymorphism
# Polymorphism is often used in class methods, where we can have multiple classes with the same method name.
# For example, we have three classes SoftwareEngineer, QualityAssurance and BusinessAnalyst and they all have a method called "work()"
class SoftwareEngineer:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Coding")

class QualityAssurance:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Testing")

class BusinessAnalyst:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Planning")

se1 = SoftwareEngineer("Edmar")
qa1 = QualityAssurance("John")
ba1 = BusinessAnalyst("Jane")

for emp in (se1, qa1, ba1):
    emp.work()

print("\r")
# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?
# Yes, the child class will inherit the properties but will override the methods from the parent class with the same name.
class Developer:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Coding") 

class WebDeveloper(Developer):
    def work(self):
        print("Web development")

class MobileDeveloper(Developer):
    def work(self):
        print("Mobile development")

class FrontendDeveloper(Developer):
    def work(self):
        print("Frontend development")

dev1 = WebDeveloper("Edmar")
dev2 = MobileDeveloper("Smith")
dev3 = FrontendDeveloper("Juan")
dev4 = Developer("John")

for emp in (dev1, dev2, dev3, dev4):
    print(f"{emp.name}")
    emp.work()
# In the example above you can see that the child class inherits name, but they override the "work()" method.