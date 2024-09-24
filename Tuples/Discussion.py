# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable
# Tuples are written with round brackets
shape_tuple = ("Circle", "Square", "Triangle")
print(shape_tuple)
print("\n")

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Ordered it means that the items have a defined order, and that order will not change.
# Unchangeable means that we cannot change, add or remove items after the tuple has been created.
# Allow duplicates since tuples are indexed, they can have items with the same value.

# To determine how many items a tuple has, use the "len()" function.
print(len(shape_tuple))
print("\n")

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
single_tuple_item = ("Trapezoid",)
print(single_tuple_item)
print("\n")

# A tuple can contain different data types.
mixed_tuple = ("Pentagon", 1, False)

# It is also possible to use the "tuple()" constructor to make a tuple.
new_tuple = tuple(("Star", "Diamond", "Hexagon")) # note the double round-brackets
print(new_tuple)
print("\n")

# Access tuple items
# You can access tuple items by referring to the index number, inside square brackets.
print(new_tuple[0])
print("\n")

# Negative indexing means start from the end.
print(new_tuple[-1])
print("\n")

# Range of indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
print(new_tuple[1:2])
print("\n")

# By leaving out the start value, the range will start at the first item.
print(new_tuple[:2])
print("\n")

# By leaving out the end value, the range will go on the end of the tuple.
print(new_tuple[1:])
print("\n")

# Range of negative indexes
# Specify negative indexes if you want to start the search from the end of the tuple.
print(new_tuple[-3: -1])
print("\n")

# Check if item exists
# to determine if a specified item is present in a tuple use the "in" keyword.
print("Star" in new_tuple)
print("\n")

# Change tuple values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
raw_tuple = ("Honda", "Toyota", "Suzuki")
print(raw_tuple)

tuple_to_list = list(raw_tuple)
tuple_to_list.append("Hyundai")
raw_tuple = tuple(tuple_to_list)
print(raw_tuple)
print("\n")

# Add tuple to a tuple
# You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple.
new_single_tuple = ("Ford",)
raw_tuple += new_single_tuple
print(raw_tuple)
print("\n")

# Remove items
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items.
tuple_to_list_2 = list(raw_tuple)
tuple_to_list_2.remove("Suzuki")
raw_tuple = tuple(tuple_to_list_2)
print(raw_tuple)
print("\n")

# Delete a tuple
# You can delete the tuple complete by using the "del" keyword
# del raw_tuple
print(raw_tuple) # this will raise an error because the tuple no longer exists
print("\n")

# Unpacking a tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
# But in Python, we are also allowed to extract the values back into variables. This is called "unpacking".
# note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
(brand1, brand2, brand3, brand4) = raw_tuple
print(brand1, brand2, brand3, brand4)
print("\n")

# Using asterisk
# If the number of variables is less than the number of values, you can add an "*" to the variable name and the values will be assigned to the variable as a list.
(brand1, brand2, *last_brand) = raw_tuple
print(brand1, brand2, last_brand)
print("\n")

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
(brand1, *mid_brand, brand3) = raw_tuple
print(brand1, mid_brand, brand3)
print("\n")

# Loop through a tuple
# You can loop through a tuple items by using a for loop
print("Looping through for loop")
for brand in raw_tuple:
    print(brand)
print("\n")

# Loop through the index numbers
# You can also loop through the tuple items by referring to their index number.
# Use the "range()" and "len()" functions to create a suitable iterable.
print("Looping through index")
for ctr in range(len(raw_tuple)):
    print(raw_tuple[ctr])
print("\n")

# You can loop through the tuple items by using a "while" loop.
# Use the "len()" function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
print("Looping in using while loop")
ctr = 0
while ctr < len(raw_tuple):
    print(raw_tuple[ctr])
    ctr = ctr + 1
print("\n")

# Join tuples
# to join two or more tuples you can use the "+" operator
tuple1 = ("a", "b", "c")
tuple2 = ("A", "B", "C")
tuple3 = tuple1 + tuple2
print(tuple3)
print("\n")

# multiply tuples
# If you want to multiply the content of the tuple a given number of times, you can use the "*" operator.
final_tuple = tuple3 * 2
print(final_tuple)
print("\n")