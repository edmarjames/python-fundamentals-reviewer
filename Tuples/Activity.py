# 1. Creating Tuples
# Create a tuple shapes with the values "Circle", "Square", and "Triangle".
# Create a tuple using the tuple() constructor with values "Red", "Green", and "Blue".
    # Expected Output:
    # ('Circle', 'Square', 'Triangle')
    # ('Red', 'Green', 'Blue')

# solution
shape_tuple = ("Circle", "Square", "Triangle")
print(shape_tuple)
color_tuple = tuple(("Red", "Green", "Blue"))
print(color_tuple)


print("\r")
# 2. Accessing Items
# Access the second item of the shapes tuple.
# Access the last item using negative indexing.
    # Expected Output:
    # Square
    # Triangle

# solution
print(shape_tuple[1])
print(shape_tuple[-1])


print("\r")
# 3. Slicing Tuples
# Retrieve the first two items from the shapes tuple.
# Get all items from the second item to the end.
    # Expected Output:
    # ('Circle', 'Square')
    # ('Square', 'Triangle')

# solution
print(shape_tuple[:2])
print(shape_tuple[1:])


print("\r")
# 4. Check Item Existence
# Check if "Circle" is in the shapes tuple.
    # Expected Output:
    # True

# solution
print("Circle" in shape_tuple)


print("\r")
# 5. Modify Tuples (Workaround)
# Convert the shapes tuple to a list, add the item "Hexagon", then convert it back to a tuple.
    # Expected Output:
    # ('Circle', 'Square', 'Triangle', 'Hexagon')

# solution
shape_tuple_list = list(shape_tuple)
shape_tuple_list.append("Hexagon")
shape_tuple = tuple(shape_tuple_list)
print(shape_tuple)


print("\r")
# 6. Unpacking Tuples
# Unpack the shapes tuple into three variables shape1, shape2, and shape3.
# Use the * operator to unpack the shapes tuple so that the first item is assigned to one variable, and the remaining items are assigned to another variable as a list.
    # Expected Output:
    # Circle Square Triangle
    # Circle ['Square', 'Triangle']

# solution
(shape1, shape2, shape3, last_shape) = shape_tuple
print(shape1, shape2, shape3)
(shape1, *mid_shape, last_shape) = shape_tuple
print(shape1, mid_shape)


print("\r")
# 7. Looping through Tuples
# Loop through the shapes tuple using:
# A for loop.
# A while loop.
    # Expected Output:
    # Circle
    # Square
    # Triangle

    # Circle
    # Square
    # Triangle

# solution
for shape in shape_tuple:
    print(shape)
print("\r")

ctr = 0
while ctr < len(shape_tuple):
    print(shape_tuple[ctr])
    ctr = ctr + 1


print("\r")
# 8. Joining Tuples
# Join two tuples brands1 = ("Nike", "Adidas") and brands2 = ("Puma", "Reebok") using the + operator.
    # Expected Output:
    # ('Nike', 'Adidas', 'Puma', 'Reebok')

# solution
brands1 = ("Nike", "Adidas")
brands2 = ("Puma", "Reebok")
final_tuple = brands1 + brands2
print(final_tuple)


print("\r")
# 9. Multiplying Tuples
# Multiply the brands1 tuple by 3 using the * operator.
    # Expected Output:
    # ('Nike', 'Adidas', 'Nike', 'Adidas', 'Nike', 'Adidas')

# solution
print(brands1 * 3)

