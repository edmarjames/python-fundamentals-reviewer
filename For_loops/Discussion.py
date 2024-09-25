# A "for" loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the "for" keyword in other programming languages, and works more like an iterator method as found in other object-oriented programming languages.
# With the "for" loop we can execute a set of statements, once for each item in a list, tuple set etc.
# The "for" loop does not require an indexing variable to set beforehand.
mc_brands = ["Honda", "Yamaha", "Suzuki"]
for brand in mc_brands:
    print(brand)

print("\n")
# Looping through a string
# Even strings are iterable objects, they contain a sequence of characters.
for char in "Click":
    print(char)

print("\n")
# The break statement
# With the "break" statement we can stop the loop before it has looped through all the items.
for brand in mc_brands:
    print(brand)
    if brand == "Yamaha":
        break

print("\n")
# The continue statement
# With the "continue" statement we can stop the current iteration of the loop, and continue with the next.
for brand in mc_brands:    
    if brand == "Yamaha":
        continue
    print(brand)

print("\n")
# The range() function
# To loop through a set of code a specified number of times, we can use the "range()" function.
# The "range()" function returns sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for i in range(8):
    print(i)

print("\n")
# The "range()" function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(1, 6), which means values from 1 to 6 (but not including 6).
for i in range(1, 6):
    print(i)

print("\n")
# The "range()" function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for i in range(2, 30, 3):
    print(i)

print("\n")
# Else in a for loop
# The "else" keyword in a for loop specifies a block of code to be executed when the loop is finished.
# note: the "else" block will not be executed if the loop is stopped by a "break" statement.
for ctr in range(0, 25, 5):
    print(ctr)
else:
    print("The loop is finished")

print("\n")
# Nested loops
# A nested loop is a loop inside a loop
# The inner loop will be executed one time for each iteration of the outer loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print("\n")
# The pass statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the "pass" statement to avoid getting an error.
for x in range(100):
    pass