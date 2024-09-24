# List are used to store multiple items in a single variable.
# List are created using square brackets.
fruit_list = ["Apple", "Banana", "Kiwi"]
print(fruit_list)
print("\n")

# List items are ordered, changeable and allow duplicate values.
# List items are indexed, the first item has index [0]
# ordered means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.
# changeable means that we can change, add, and remove items in a list after it has been created.
# allow duplicates since list are indexed, list can have items with the same value.

# List length
# To determine how many items a list has, use the "len()" function
print(len(fruit_list))
print("\n")

# List items
# List items can be of any data type
mixed_list = [24, "Edmar", "Software Engineer"]

# The list() constructor
# It is also possible to use the "list()" constructor when creating a new list.
new_list = list(("Red", "Green", "Blue", "Purple")) # note the double round-brackets
print(new_list)
print("\n")

# Access items
# List items are indexed and you can access them by referring to the index number.
print(new_list[0])

# Negative indexing means start from the end.
print(new_list[-1])
print("\n")

# Range of indexes
# You can specify a range of indexes by specifying where to start and where to end the range. The return value will be a new list with the specified items.
print(new_list[1:3])

# By leaving out the start value, the range will start at the first item.
print(new_list[:3])

# By leaving out the end value, the range will go on the end of the list.
print(new_list[1:])
print("\n")

# Range of negative indexes
# Specify negative indexes if you want to start the search from the end of the list.
print(new_list[-3: -1])
print("\n")

# Check if item exists
# To determine if a specified item is present in a list use the "in" keyword
print("Red" in new_list)
print("\n")

# Change item value
# To change the value of a specific item, refer to the index number.
new_list[0] = "Yellow"
print(new_list)
print("\n")

# Change a range of item values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.
new_list[1:3] = ["Yellow Green", "Blue Green"]
print(new_list)
print("\n")

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.
new_list[1:3] = ["Yellow Green", "Blue Green", "Lavender"]
print(new_list)
print("\n")

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.
new_list[1:3] = ["Yellow Green"]
print(new_list)
print("\n")

# Insert items
# To insert a new list item, without replacing any of the existing values, we can use the "insert()" method.
new_list.insert(0, "Black")
print(new_list)
print("\n")

# Append items
# To add an item to the end of the list, use the "append()" method
new_list.append("White")
print(new_list)
print("\n")

# Extend list
# To append elements from another list to the current list, use the "extend()" method. The elements will be added to the end of the list.
new_colors = ["Tangerine", "Fuchsia"]
new_list.extend(new_colors)
print(new_list)
print("\n")

# Remove specified item
# The "remove()" method removes the specified item.
# If there are more than one item with the specified value, it will remove the first occurrence.
new_list.remove("Black")
print(new_list)
print("\n")

# Remove specified index
# The "pop()" method removes an item using it's index
new_list.pop(1)
print(new_list)
print("\n")

# If you do not specify the index, the "pop()" method removes the last item.
new_list.pop()
print(new_list)
print("\n")

# Other way to delete an item
# The "del" keyword also removes an item using it's index
# The "del" keyword can also delete the list completely.
del new_list[0]
print(new_list)
print("\n")

# Clear the list
# The "clear()" method empties the list. The list still remains, but it has not content.
# new_list.clear()
print(new_list)
print("\n")

# Loop through a list
# You can loop through the list items by using a "for" loop
print("Looping in using for loop")
for colors in new_list:
    print(colors)
print("\n")

# You can also loop through the list items by referring to their index number.
# Use the "range()" and "len()" functions to create a suitable iterable.
print("Looping in using range")
for ctr in range(len(new_list)):
    print(new_list[ctr])
print("\n")

# You can loop through the list items by using a "while" loop.
# Use the "len()" function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
print("Looping in using while loop")
ctr = 0
while ctr < len(new_list):
    print(new_list[ctr])
    ctr = ctr + 1
print("\n")

# list comprehension offers the shortest syntax for looping through lists.
print("Looping in using list comprehension")
[print(item) for item in new_list]
print("\n")

# list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
new_color_list = [color for color in new_list if "r" in color]
print(new_color_list)
print("\n")

# Syntax
# new_list = [expression for item in iterable if condition == True]

# expression - is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.
# iterable - can be any iterable object, like a list, tuple, set etc.
# condition - is like a filter that only accepts the items that evaluate to True

# Sort lists
# List objects have a "sort()" method that will sort the list alphanumerically, ascending by default.
new_list.sort()
print(new_list)
print("\n")

# To sort descending, use the keyword argument "reverse = True"
new_list.sort(reverse = True)
print(new_list)
print("\n")

# Case insensitive sort
# By default the "sort()" method is case sensitive, resulting in all capital letters being sorted before lower case letters. 
# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use "str.lower" as a key function.
case_sensitive_list = ["Apple", "banana", "Calamansi", "dalandan"]
case_sensitive_list.sort(key = str.lower)
print(case_sensitive_list)
print("\n")

# Reverse order
# The "reverse()" method reverses the current sorting order of th elements.
case_sensitive_list.reverse()
print(case_sensitive_list)
print("\n")

# Copy Lists
# You cannot copy a list simply by typing list2 = list1, because list2 will only be reference to list1, and changes made in list1 will automatically also be made in list2
# You can use the built-in list method "copy()" to copy a list.
name_list = ["John", "Jane", "James"]
name_list_copy = name_list.copy()
name_list_copy.append("Joseph")

print(name_list)
print(name_list_copy)
print("\n")

# Another way to make a copy is to use the built-in method "list()"
name_list_copy_list = list(name_list)
print(name_list_copy_list)
print("\n")

# You can also make a copy of a list by using the ":" (slice) operator
name_list_copy_slice = name_list[:]
print(name_list_copy_slice)
print("\n")

# Join list
# There are several ways to join, or concatenate, two or more list in Python.
# One of the easiest ways are by using the "+" operator.
first_list = ["Samsung", "Motorola", "Lenovo"]
second_list = ["Oppo", "Huawei", "Xiaomi"]
final_list = first_list + second_list

print(final_list)
print("\n")

# You can also use the "extend()" method, where the purpose is to add elements from one list to another list.
final_list_copy = first_list.copy()
final_list_copy.extend(second_list)
print(final_list_copy)
print("\n")