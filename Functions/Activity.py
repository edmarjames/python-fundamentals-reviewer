# 1. Calculate Factorial Using Recursion
# Write a function factorial(n) that takes a number n and returns its factorial using recursion. The factorial of a number is the product of all positive integers up to that number.
    # Expected Output:
    # factorial(5)  # 120
    # factorial(3)  # 6

# solution
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * factorial(n -1))

print(factorial(5))
print(factorial(3))


print("\n")
# 2. Sum of Arbitrary Arguments
# Write a function sum_all(*args) that accepts any number of numeric arguments and returns their sum. If no arguments are passed, return 0.
    # Expected Output:
    # sum_all(1, 2, 3)  # 6
    # sum_all(4, 5)     # 9
    # sum_all()         # 0

# solution
def sum_all(*args):
    sum_val = 0
    if len(args) == 0:
        return 0
    else:
        for num in args:
            sum_val += num
        return sum_val

print(sum_all(1, 2, 3))
print(sum_all(4, 5))
print(sum_all())


print("\n")
# 3. Default Values and Custom Greeting
# Write a function greet_user(name, greeting="Hello") that takes a user's name and an optional greeting. If no greeting is provided, the function should use "Hello" as the default greeting.
    # Expected Output:
    # greet_user("Edmar")               # Hello, Edmar!
    # greet_user("James", "Welcome")    # Welcome, James!

# solution
def greet_user(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet_user("Edmar")
greet_user("James", "Welcome")


print("\n")
# 4. User Profile Using Keyword Arguments
# Write a function create_profile(**kwargs) that accepts arbitrary keyword arguments to build a user profile. The function should print the user's details.
    # Expected Output:
    # create_profile(name="Edmar", age=26, profession="Software Engineer")
    # # Output:
    # # User Profile:
    # # name: Edmar
    # # age: 26
    # # profession: Software Engineer

# solution
def create_profile(**kwargs):
    print("User Profile:")
    print(f"name: {kwargs['name']}")
    print(f"age: {kwargs['age']}")
    print(f"profession: {kwargs['profession']}")

create_profile(name = "Edmar", age = 26, profession = "Software Engineer")


print("\n")
# 5. Return a Function’s Documentation
# Write a function docstring(func) that accepts a function as an argument and returns its docstring.
    # Expected Output:
    # def example_func():
    #     """This is an example function."""
    #     pass

    # print(docstring(example_func))  
    # # Output: This is an example function.

# solution
def docstring(func):
    return func.__doc__

def sample_func():
    """This is an example function."""
    pass

print(docstring(sample_func))


print("\n")
# 6. Find Maximum Using Positional-Only Arguments
# Write a function find_max(a, b, /) that only accepts positional arguments and returns the maximum of the two numbers.
    # Expected Output:
    # find_max(10, 20)    # 20
    # find_max(5, -10)    # 5

# solution
def find_max(a, b, /):
    return max(a, b)

print(find_max(10, 20))
print(find_max(5, -10))


print("\n")
# 7. Combine Positional and Keyword Arguments
# Write a function calculate_area(length, width, /, *, unit="square meters") that calculates and prints the area of a rectangle using the provided length and width. The unit of the area is optional and defaults to "square meters".
    # Expected Output:
    # calculate_area(5, 10)                   # Area: 50 square meters
    # calculate_area(3, 7, unit="sq. feet")   # Area: 21 sq. feet

# solution
def calculate_area(length, width, /, *, unit="square meters"):
    area = length * width
    return f"Area: {area} {unit}"

print(calculate_area(5, 10))
print(calculate_area(3, 7, unit="sq. feet"))


print("\n")
# 8. List Manipulation Function
# Write a function modify_list(lst, action="add", value=0) that modifies a list. The function should:
# Add value to the list if action is "add".
# Remove value from the list if action is "remove".
# If the action is not specified, it should add the value by default.
    # Expected Output:
    # lst = [1, 2, 3]
    # modify_list(lst, "add", 4)        # lst becomes [1, 2, 3, 4]
    # modify_list(lst, "remove", 2)     # lst becomes [1, 3, 4]

# solution
def modify_list(num_list, action="add", value=0):
    if action == "add":
        num_list.append(value)
    elif action == "remove":
        num_list.remove(value)
    print(num_list)

num_list = [1, 2, 3]
modify_list(num_list, "add", 4)
modify_list(num_list, "remove", 2)