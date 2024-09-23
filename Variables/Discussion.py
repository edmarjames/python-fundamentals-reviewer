# Variables are containers for storing data values.
# A variable is created the moment you first assign a value to it.
x = 1
y = "Jane"
print(x, y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 2
y = "Doe"
print(x, y)


# Single of Double Quotes
# String variables can be declared either by using single or double quotes:
a = "Anthony"
b = 'Bernadette'


# Case-sensitive
# Variable name are case-sensitive
# C will not overwrite c
c = 3
C = "Cat"
print(c, C)


# Variable names
# Rules for Python variables
    # A variable name must start with a letter of the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscore (A-z, 0-9, and _)
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords (https://www.w3schools.com/python/python_ref_keywords.asp)

# Sample legal variables
my_var = "Value 1"
_my_var = "Value 2"
my_var2 = "Value 3"
My_Var = "Value 4"

print(my_var)
print(_my_var)
print(my_var2)
print(My_Var)


# Multi Words Variable Names
# Variable names with more than one word can be difficult to read, there are several techniques you can use to make them more readable:

# Camel Case - each word, expect the first, starts with a capital letter:
myVar = "Camel Case"

# Pascal Case - each word starts with a capital letter.
MyVar = "Pascal Case"

# Snake Case - each word is separated by an underscore character:
my_variable = "Snake Case"

print(myVar)
print(MyVar)
print(my_variable)


# Assign Multiple Values
# Python allows you to assign values to multiple variables in one line. Make sure the number of variables matches the number of values, or else you will get an error.
x, y, z = 1, 2, 3
print(x, y, z)


# One value to multiple variables
# You can assign the same value to multiple variables in one line.
d = e = f = "NPC"
print(d)
print(e)
print(f)


# Unpack a collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called "unpacking".
fruits = ["Watermelon", "Kiwi", "Grapes"]
w, k, g = fruits
print(w)
print(k)
print(g)


# Output variables
# The python "print()" function is often used to output variables
test = "Python is amazing"
print(test)

# In the "print()" function, you output multiple variables, separated by comma.
print(w, k, g)

# You can also use "+" operator to output multiple variables:
print(w + k + g)

# For numbers, the "+" character works as a mathematical operator
f = 10
g = 90
print(f + g)

#NOTES: in the "print()" function, when you try to combine a string and a number with the "+" operator, Python will give you an error, the best way to output multiple variables in the "print()" function is to separate them with commas, which even support different data types.
print(test, f, g)


# Global variables
# Variables that are created outside of a function are known as global variables. Global variables can be used by everyone, both inside functions and outside.

# If you create a variable with the same name inside a function, this variable will be local, and can be only be used inside the function. The global variable name will remain as it was, global and with the original value.

glob_var = "Awesome"

def my_func():
    glob_var = "Interesting"
    print("Python is " + glob_var)

my_func()
print("Python is " + glob_var)


# The global keyword
# normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the "global" keyword

g = "Fantastic"
def my_func_2():
    global g
    g = "Powerful"

my_func_2()
print("Python is " + g)

# Also, use the "global" keyword if you want to change a global variable inside a function. To change the value of a global variable inside a function, refer to the variable by using the "global" keyword 

