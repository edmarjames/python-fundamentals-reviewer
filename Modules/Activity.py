# Exercise 1: Creating and Importing a Module
# **Task**: Create a module file `math_operations.py` containing two functions: `add(a, b)` and `multiply(a, b)`. In your main script, import this module and call both functions to print the results.
    # **Input**: Use `add(3, 5)` and `multiply(4, 6)` after importing the module.
    # **Expected Output**:
    # 8
    # 24

# solution
import math_operations
op1 = math_operations.add(3, 5)
op2 = math_operations.multiply(4, 6)
print(op1)
print(op2)


print("\r")
# Exercise 2: Variables in Modules
# **Task**: Extend the `math_operations.py` module by adding a variable `PI = 3.14159`. Import this variable into your script and print its value.
    # **Expected Output**:
    # 3.14159

# solution
pi = math_operations.PI
print(pi)


print("\r")
# Exercise 3: Module Alias
# **Task**: Import the `math_operations.py` module using an alias `mo`. Call the `add()` function from the module using the alias.
    # **Input**: Use `mo.add(10, 20)`.
    # **Expected Output**:
    # 30

# solution
import math_operations as mo
op3 = mo.add(10, 20)
print(op3)


print("\r")
# Exercise 4: Using `dir()` Function
    # **Task**: Import your `math_operations` module and use the `dir()` function to list all the attributes and methods in the module. Print the output.
    # **Expected Output**: (The exact list will depend on your module's content)
    # ['PI', 'add', 'multiply', ...]

# solution
content = dir(math_operations)
print(content)


print("\r")
# Exercise 5: Importing Specific Parts from a Module
# **Task**: Import only the `multiply` function from the `math_operations` module using the `from` keyword. Call it directly without using the module name.
    # **Input**: Use `multiply(2, 3)`.
    # **Expected Output**:
    # 6

# solution
from math_operations import multiply
product = multiply(2, 3)
print(product)


print("\r")
# Exercise 6: Module with a Dictionary
    # **Task**: Create a module called `data_storage.py` containing a dictionary `employee_info = {'name': 'Alice', 'age': 30, 'role': 'Developer'}`. Import the dictionary into your script and use the `pprint` module to print it.
    # **Expected Output**:
    # {'age': 30, 'name': 'Alice', 'role': 'Developer'}

# solution
import data_storage
import pprint
pprint.pprint(data_storage.employee_info)