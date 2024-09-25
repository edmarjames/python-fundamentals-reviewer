# 1. Creating Sets
# Create a set tech_stack with the values "HTML", "CSS", and "JavaScript".
# Create a set using the set() constructor with the values "Python", "Java", and "C++".
    # Expected Output:
    # {'HTML', 'CSS', 'JavaScript'}
    # {'Python', 'Java', 'C++'}

# solution
tech_stack = {"HTML", "CSS", "JavaScript"}
language_stack = set(("Python", "Java", "C++"))
print(tech_stack)
print(language_stack)


print("\n")
# 2. Accessing Items in a Set
# Loop through the items in the tech_stack set and print each one.
# Check if "CSS" exists in tech_stack.
    # Expected Output:
    # HTML
    # CSS
    # JavaScript
    # True

# solution
for tech in tech_stack:
    print(tech)
    # if "CSS" in tech:
    #     print(True)
print("CSS" in tech_stack)


print("\n")
# 3. Adding and Updating Sets
# Add the item "React" to the tech_stack set.
# Create another set frontend_stack = {"Bootstrap", "Tailwind"} and add its items to tech_stack using the update() method.
    # Expected Output:
    # {'HTML', 'CSS', 'React', 'JavaScript'}
    # {'HTML', 'CSS', 'React', 'Tailwind', 'Bootstrap', 'JavaScript'}

# solution
tech_stack.add("React")
print(tech_stack)
frontend_stack = {"Bootstrap", "Tailwind"}
tech_stack.update(frontend_stack)
print(tech_stack)


print("\n")
# 4. Removing Items
# Remove "Bootstrap" from tech_stack using the remove() method.
# Attempt to discard "Angular" from the set using the discard() method (no error should occur).
# Use the pop() method and print the item that was randomly removed.
    # Expected Output:
    # {'HTML', 'CSS', 'React', 'Tailwind', 'JavaScript'}
    # {'HTML', 'CSS', 'React', 'Tailwind', 'JavaScript'}
    # <random removed item>

# solution
tech_stack.remove("Bootstrap")
print(tech_stack)
tech_stack.discard("Angular")
print(tech_stack)
removed_item = tech_stack.pop()
print(removed_item)


print("\n")
# 5. Set Operations
# Create two sets: set_a = {"apple", "banana", "cherry"} and set_b = {"cherry", "mango", "banana", "pear"}.
# Perform the following operations and print the result:
# union() of set_a and set_b.
# intersection() of set_a and set_b.
# difference() between set_a and set_b.
# symmetric_difference() between set_a and set_b.
    # Expected Output:
    # {'apple', 'banana', 'cherry', 'pear', 'mango'}
    # {'banana', 'cherry'}
    # {'apple'}
    # {'apple', 'pear', 'mango'}

# solution
set_a = {"apple", "banana", "cherry"}
set_b = {"cherry", "mango", "banana", "pear"}
set_c = set_a.union(set_b)
print(set_c)
set_intersection = set_a.intersection(set_b)
print(set_intersection)
set_difference = set_a.difference(set_b)
print(set_difference)
set_sym_difference = set_a.symmetric_difference(set_b)
print(set_sym_difference)


print("\n")
# 6. Update Set with Intersection
# Use intersection_update() on set_a to keep only the items present in both set_a and set_b.
    # Expected Output:
    # {'banana', 'cherry'}

# solution
set_a.intersection_update(set_b)
print(set_a)


print("\n")
# 7. Difference Update
# Use difference_update() on set_a to remove the items present in both set_a and set_b.
    # Expected Output:
    # {'apple'}

# solution
set_a = {"apple", "banana", "cherry"}
set_b = {"cherry", "mango", "banana", "pear"}
set_a.difference_update(set_b)
print(set_a)


print("\n")
# 8. Symmetric Difference Update
# Use symmetric_difference_update() on set_a and set_b to keep only items that are not in both sets.
    # Expected Output:
    # {'apple', 'pear', 'mango'}

# solution
set_a = {"apple", "banana", "cherry"}
set_b = {"cherry", "mango", "banana", "pear"}
set_a.symmetric_difference_update(set_b)
print(set_a)


print("\n")
# 9. Clearing and Deleting Sets
# Clear the contents of the tech_stack set.
# Delete the frontend_stack set.
    # Expected Output:
    # set()
    # NameError: name 'frontend_stack' is not defined

# solution
tech_stack.clear()
print(tech_stack)
del frontend_stack
print(frontend_stack)


