# An if statement is written by using the "if" keyword.
a = 99
b = 11
if a > b:
    print("A is greater than B")
print("\n")

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# If statement without indentation will raise an error
# if a > b:
# print("A is greater than B")

# Elif
# The "elif" keyword in Python's way of saying "if the previous conditions were not true, then try this condition".
c = 66
d = 66
if c > d:
    print("C is greater than D")
elif c == d:
    print("C and D are equal")
print("\n")

# Else
# The "else" keyword catches anything which isn't caught by the preceding conditions.
e = 90
f = 80
if f > e:
    print("F is greater than E")
elif f == e:
    print("F and E are equal")
else:
    print("E is greater than F")
print("\n")

# Short hand if
# If you have only one statement to execute, you can put it on the same line as the if statement.
if e > f: print("E is greater than F")
print("\n")

# Short hand if else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
print("E is greater than F") if e > f else print("F is greater than E")
print("\n")

# And
# The "and" keyword is a logical operator, and is used to combine conditional statements.
list_one = []
list_two = []

if len(list_one) == 0 and len(list_two) == 0:
    print("Both list are empty")
print("\n")

# Or
# The "or" keyword is a logical operator, and is used to combine conditional statements.
if len(list_one) == 0 or len(list_two) == 0:
    print("Either one of the list is empty")
print("\n")

# Not
# The "not" keyword is a logical operator, and is used to reverse the result of the conditional statement.
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
print("\n")

# Nested if
# You can have "if" statements inside "if" statements, this is called nested "if" statements.
x = 50
if x > 30:
    print("Above 30")
    if x > 40:
        print("Above 40")
    else:
        print("But not above 50")
print("\n")

# The pass statement
# if statement cannot be empty, but if you for some reason have an "if" statement with no content, put in the "pass" statement to avoid getting an error.
if x == 50:
    pass