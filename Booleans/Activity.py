# 1. Basic Boolean Expressions
# Evaluate the following expressions and print the Boolean result:
# 3 > 5
# 10 == 10
    # Expected Output:
    # False
    # True

# solution
print(3 > 5)
print(10 == 10)


print("\n")
# 2. Boolean in Conditional Statements
# Given two variables x = 20 and y = 15, use an if-else statement to check if x is greater than y. Print "x is greater" if true, otherwise print "y is greater or equal".
    # Expected Output:
    # x is greater

# solution
x = 20
y = 15
if x > y:
    print("x is greater")
else:
    print("y is greater or equal")


print("\n")
# 3. Using bool() Function
# Evaluate the following values using the bool() function and print the results:
# 0
# "Hello"
# [] (empty list)
    # Expected Output:
    # False
    # True
    # False

# solution
print(bool(0))
print(bool("Hello"))
print(bool([]))


print("\n")
# 4. True or False with Different Data Types
# Evaluate the truthiness of the following and print the results:
# A non-empty string "Python"
# A number 42
# A list [1, 2, 3]
# An empty dictionary {}
    # Expected Output:
    # True
    # True
    # True
    # False

# solution
print(bool("Python"))
print(bool(42))
print(bool([1, 2, 3]))
print(bool({}))


print("\n")
# 5. Built-in Function isinstance()
# Create a variable num = 50 and check if it is an integer using the isinstance() function.
    # Expected Output:
    # True

# solution
num = 50
print(isinstance(num, int))
