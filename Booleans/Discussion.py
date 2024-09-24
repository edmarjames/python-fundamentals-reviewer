# Boolean represents one of two values -> "True" or "False"
# You can evaluate any expression in Python, and get one of two answers, "True" or "False".
# When you compare two values, the expression is evaluated and Python returns the Boolean answer.
print(1 < 2)
print(1 == 0)
print("\n")

# When you run a condition in an if statement, Python return "True" or "False"
a = 99
b = 55

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
print("\n")

# Evaluate values and variables
# The "bool()" function allows you to evaluate any value, and give you "True" or "False" in return.
print(bool(1))
print(bool(0))
print("\n")

# Most values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0
# Any list, tuple, set and dictionary are True, except empty ones

print(bool("string"))
print(bool(1))
print(bool([26, "Edmar"]))

print(bool(""))
print(bool(0))
print(bool([]))
print("\n")

# Python also has many built-in functions that return a boolean value, like the "isinstance()" function, which can be used to determine if an object is of a certain data type.
num = 100
print(isinstance(num, int))