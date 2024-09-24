# Sets are used to store multiple items in a single variable
# A set is a collection which is unordered, unchangeable, and unindexed.
# Sets are written with curly brackets.
new_set = {"HTML", "CSS", "Javascript"}
print(new_set)
print("\n")

# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered means that the items in a set do not have a defined order. Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Unchangeable means that we cannot change the items after the set has been created.
# Duplicates not allowed means that it cannot have two items with the same value.
# note: duplicate values will be ignored.
# note: the values "True" and "1" are considered the same value in sets, and are treated as duplicates.
set_with_true_and_one = {True, 1, "Morning", "Afternoon", "Evening"}
print(set_with_true_and_one)
print("\n")

# note: the values "False" and "0" are considered the same value in sets, and are treated as duplicates.
set_with_false_and_zero = {False, 0, "Ohayou", "Konbanwa"}
print(set_with_false_and_zero)
print("\n")

# To determine how many items as set has, use the "len()" function.
print(len(new_set))
print("\n")

# A set can contain different data types.
mixed_set = {True, 2, "Edmar"}

# It is also possible to use the "set()" constructor to make a set.
brand_set = set(("Asus", "Gigabyte", "MSI"))
print(brand_set)
print("\n")

# Access items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through a set items using a for loop, or ask if a specified value is present in a set, by using the "in" keyword.
for brand in brand_set:
    print(brand)
print("\n")
print("MSI" in brand_set)
print("\n")

# Add items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the "add()" method
brand_set.add("ASRock")
print(brand_set)
print("\n")

# Add sets
# To add items from another set into the current set, use the "update()" method.
new_brand_set = {"Biostar", "Acer"}
brand_set.update(new_brand_set)
print(brand_set)
print("\n")

# Remove item
# To remove an item in a set, use the "remove()" or the "discard()" method.
# note: if the item to remove does not exist, "remove()" will raise an error.
brand_set.remove("Acer")
print(brand_set)
print("\n")

# note: if the item to remove does not exist, "discard()" will not raise an error.
brand_set.discard("Nokia")
print(brand_set)
print("\n")

# You can also use the "pop()" method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the "pop()" method is the removed item.
# note: sets are unordered, so when using the "pop()" method, you do not know which item that gets removed.
removed_item = brand_set.pop()
print(removed_item)
print("\n")

# The "clear()" method empties the set.
new_brand_set.clear()
print(new_brand_set)
print("\n")

# The "del" keyword will delete the set completely.
# del new_brand_set
print(new_brand_set) # this will raise an error because the set no longer exists
print("\n") 

# Loop sets
# You can loop through the set items by using the for loop.
for brand in brand_set:
    print(brand)
print("\n") 

# Join sets
# There are several ways to join two or more sets in Python.

# The "union()" and "update()" method joins all items from both sets
# The "intersection()" method keeps only the duplicates.
# The "difference()" method keeps the items from the first set that are not in the other set(s)
# The "symmetric_difference()" method keeps all items except the duplicates.

# Union
# The "union()" method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# You can use the "|" operator instead of the "union()" method, and you will get the same result.
set3 = set1 | set2
print(set3)
print("\n") 

# Join a set and a tuple with "union()" method
# The "union()" method allows you to join a set with other data types, like lists or tuples.\
# note: the "|" operator only allows you to join sets with sets, and not with other data types like you can with the "union()" method.
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
print("\n") 

# Update
# The "update()" changes the original set, and does not return a new set.
# note: both "union()" and "update()" will exclude any duplicate items.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
print("\n") 

# Intersection
# The "intersection()" method will return a new set, that only contains tha items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
print("\n") 

# You can use the "&" operator instead of the "intersection()" method, and you will get the same result.
set3 = set1 & set2
print(set3)
print("\n") 
# note: The "&" operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# The "intersection_update()" method will also keep only the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
print("\n")

# Difference
# The "difference()" method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
print("\n")

# You can use the "-" operator instead of "difference()" method, and you will get the same result.
set3 = set1 - set2
print(set3)
print("\n")
# note: the "-" operator only allows you to join sets with sets, and not with other data types like you can with the "difference()" method.

# The "difference_update()" method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
print("\n")

# Symmetric Differences
# The "symmetric_differences()" method will keep only the element that are not present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
print("\n")

# You can use the "^" operator instead of the "symmetric_difference()" method, and you will get the same result.
set3 = set1 ^ set2
print(set3)
print("\n")
# note: the "^" operator only allows you to join sets with sets, and not with other data types like you can with the "symmetric_difference()" method.

# The "symmetric_difference_update()" method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
print("\n")