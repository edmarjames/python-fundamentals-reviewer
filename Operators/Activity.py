# 1. Arithmetic Operators
# Perform the following arithmetic operations:
# Add 7 and 3
# Subtract 10 from 25
# Multiply 6 by 4
# Divide 15 by 3
# Find the modulus (remainder) when 14 is divided by 5
# Compute 2 raised to the power of 4
# Perform floor division of 22 by 7
    # Expected Output:
    # 10
    # 15
    # 24
    # 5.0
    # 4
    # 16
    # 3

# solution
print(7 + 3)
print(25 - 10)
print(6 * 4)
print(15 / 3)
print(14 % 5)
print(2**4)
print(22 // 7)


print("\n")
# 2. Assignment Operators
# Start with x = 5 and perform the following assignments:
# Add 3 to x (x += 3)
# Subtract 2 from x (x -= 2)
# Multiply x by 4 (x *= 4)
# Divide x by 2 (x /= 2)
# Find the modulus when x is divided by 3 (x %= 3)
    # Expected Output:
    # 8
    # 6
    # 24
    # 12.0
    # 0.0

# solution
x = 5
x += 3
print(x)
x -= 2
print(x)
x *= 4
print(x)
x /= 2
print(x)
x %= 3
print(x)


print("\n")
# 3. Comparison Operators
# Compare the following values and print the Boolean result:
# 7 == 7
# 5 != 10
# 8 > 12
# 15 < 20
# 25 >= 25
# 18 <= 12
    # Expected Output:
    # True
    # True
    # False
    # True
    # True
    # False

# solution
print(7 == 7)
print(5 != 10)
print(8 > 12)
print(15 < 20)
print(25 >= 25)
print(18 <= 12)


print("\n")
# 4. Logical Operators
# Given x = 7 and y = 10, evaluate the following expressions:
# x == 7 and y == 10
# x == 5 or y == 10
# not(x == 7)
    # Expected Output:
    # True
    # True
    # False

# solution
x = 7
y = 10
print(x == 7 and y == 10)
print(x == 5 or y == 10)
print(not x == 7)


print("\n")
# 5. Identity Operators
# Use the following variables: a = 5 and b = a. Test the identity of the variables:
# Check if a is b
# Check if a is not b
    # Expected Output:
    # True
    # False
    
# solution
a = 5
b = a
print(a is b)
print(a is not b)


print("\n")
# 6. Membership Operators
# Given lst = [2, 4, 6, 8, 10], test the following membership:
# Check if 4 is in lst
# Check if 7 is not in lst
    # Expected Output:
    # True
    # True

# solution
test_list = [2, 4, 6, 8, 10]
print(4 in test_list)
print(7 not in test_list)



