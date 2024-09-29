# **Exercise 1: Finding Min and Max**
# Create a function that accepts a list of numbers and returns both the minimum and maximum values using the `min()` and `max()` functions.
    # **Input**:
    # [3, 7, 2, 8, 5]
    # **Expected Output**:
    # Min: 2
    # Max: 8

# solution
def get_min_max(num_list):
    return [min(num_list), max(num_list)]

min_num, max_num = get_min_max([3, 7, 2, 8, 5])
print(f"Min: {min_num}")
print(f"Max: {max_num}")


print("\r")
# **Exercise 2: Absolute Value Calculator**
# Write a function that takes an integer input and returns its absolute value using the `abs()` function.
    # **Input**:
    # -45
    # **Expected Output**:
    # Absolute value: 45

# solution
def get_abs(num_input):
    return abs(num_input)

abs_value = get_abs(-45)
print(abs_value)


print("\r")
# **Exercise 3: Power Function**
# Create a program that takes two numbers as input, `x` and `y`, and returns the value of `x` raised to the power of `y` using the `pow()` function.
    # **Input**:
    # x = 3
    # y = 4
    # **Expected Output**:
    # Result: 81

# solution
def get_raised_val(x, y):
    return pow(x, y)

raised_val = get_raised_val(3, 4)
print(raised_val)


print("\r")
# **Exercise 4: Square Root Finder**
# Write a function that accepts a number and returns its square root using `math.sqrt()`.
    # **Input**:
    # 16
    # **Expected Output**:
    # Square root: 4.0

# solution
import math
def get_squared(input_num):
    return math.sqrt(input_num)

squared = get_squared(16)
print(squared)


print("\r")
# **Exercise 5: Rounding Numbers**
# Create a function that accepts a floating-point number and returns both:
# 1. The smallest integer greater than or equal to the number using `math.ceil()`.
# 2. The largest integer less than or equal to the number using `math.floor()`.
    # **Input**:
    # 5.9
    # **Expected Output**:
    # Ceiling: 6
    # Floor: 5

# solution
def get_ceil_floor(value):
    return [math.ceil(value), math.floor(value)]

ceil_val, floor_val = get_ceil_floor(5.9)
print(f"Ceiling: {ceil_val}")
print(f"Floor: {floor_val}")


print("\r")
# **Exercise 6: Calculate Circle Area**
# Create a function that calculates the area of a circle given its radius. Use the formula `area = π * r^2` and the constant `math.pi`.
    # **Input**:
    # radius = 7
    # **Expected Output**:
    # Area of circle: 153.94

# solution
def get_circle_area(radius):
    return round(math.pi * (radius**2), 2)

circle_area = get_circle_area(7)
print(f"Area of circle: {circle_area}")


print("\r")
# **Exercise 7: Hypotenuse Calculator**
# Using the `math.sqrt()` function, create a function that calculates the hypotenuse of a right triangle given the lengths of the other two sides. The formula is `hypotenuse = sqrt(a^2 + b^2)`.
    # **Input**:
    # a = 3
    # b = 4
    # **Expected Output**:
    # Hypotenuse: 5.0

# solution
def get_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

tri_hypotenuse = get_hypotenuse(3, 4)
print(f"Hypotenuse: {tri_hypotenuse}")


print("\r")
# **Exercise 8: Using the Power of π**
# Write a program that prints the value of π up to 5 decimal places using `math.pi`.
    # **Expected Output**:
    # Pi: 3.14159

# solution
def format_pi():
    return round(math.pi, 5)

print(format_pi())