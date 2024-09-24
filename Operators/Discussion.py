# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups.
    # Arithmetic operators
    # Assignment operators
    # Comparison operators
    # Logical operators
    # Identity operators
    # Membership operators
    # Bitwise operators

# Arithmetic Operators are used with numeric values to perform common mathematical operations.

print(1 + 2) # Addition
print(3 - 2) # Subtraction
print(4 * 3) # Multiplication
print(4 / 4) # Division
print(5 % 4) # Modulus
print(2**3) # Exponential
print(13 // 3) # Floor division
print("\n")

# Assignment operators are used to assign values to variables.

x = 1 # assignment operator
print(x)

x += 1 # addition assignment operator
print(x)

x -= 1 # subtraction assignment operator
print(x)

x *= 2 # multiplication assignment operator
print(x)

x /= 2 # division assignment operator
print(x)

x %= 1 # modulo assignment operator
print(x)
print("\n")

# Comparison Operators are used to compare two values.
a = 5 
b = 10

print(a == b) # equal
print(a != b) # not equal
print(a > b) # greater than
print(a < b) # less than
print(a >= b) # greater than or equal
print(a <= b) # less than or equal
print("\n")

# Logical Operators are used to combine conditional statements
a1 = 5
b1 = 10

print(a == 5 and a1 == 5) # and -> returns True if both statements are true
print(a == 5 or a1 == 5) # or -> returns True if one of the statements are true
print(not(a == 5)) # not -> reverse the result, returns False if the result is true
print("\n")

# Identity Operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
print(a is a) # is -> returns True if both variables are the same object
print(a is not b) # is not -> returns True if both variables are not the same object
print("\n")

# Membership operators are used to test if a sequence is presented in an object
num_list = [1, 2, 3, 4, 5]
print(a in num_list) # in -> returns True if a sequence with the specified value is present in the object
print(a not in num_list) # in -> returns True if a sequence with the specified value is not present in the object