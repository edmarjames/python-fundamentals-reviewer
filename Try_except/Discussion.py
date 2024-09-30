# The "try" block lets you test a block of code for errors.
# The "except" block lets you handle the error.
# The "else" block let you execute code when there is no error.
# The "finally" block lets you execute code, regardless of the result of the try and except blocks.

# Exception handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
try:
    print(x)
except:
    print("An exception occurred")

# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error.
# print(x) -> this will raise a NameError: name "x" is not defined.

print("\r")
# Many exceptions
# You can define as many exception blocks as you want, if you want to execute a special block of code for a special kind of error.
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")

print("\r")
# Else
# You can use the "else" keyword to define a block of code to be executed if no errors were raised.
try:
    print("Hello NPC arc")
except:
    print("Something went wrong")
else:
    print("Printed successfully")

print("\r")
# Finally
# The "finally" block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(y)
except:
    print("Something went wrong")
finally:
    print("Try except block is finished")

print("\r")
# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw an exception, use the "raise" keyword.
# The "raise" keyword is used to raise an exception.
odd_num = 5
if odd_num %2 != 0:
    raise Exception("The number is not even number")