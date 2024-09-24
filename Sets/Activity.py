# 1. Creating Sets
# Create a set tech_stack with the values "HTML", "CSS", and "JavaScript".
# Create a set using the set() constructor with the values "Python", "Java", and "C++".
# Expected Output:
# {'HTML', 'CSS', 'JavaScript'}
# {'Python', 'Java', 'C++'}


# 2. Accessing Items in a Set
# Loop through the items in the tech_stack set and print each one.
# Check if "CSS" exists in tech_stack.
# Expected Output:
# HTML
# CSS
# JavaScript
# True


# 3. Adding and Updating Sets
# Add the item "React" to the tech_stack set.
# Create another set frontend_stack = {"Bootstrap", "Tailwind"} and add its items to tech_stack using the update() method.
# Expected Output:
# {'HTML', 'CSS', 'React', 'JavaScript'}
# {'HTML', 'CSS', 'React', 'Tailwind', 'Bootstrap', 'JavaScript'}


# 4. Removing Items
# Remove "Bootstrap" from tech_stack using the remove() method.
# Attempt to discard "Angular" from the set using the discard() method (no error should occur).
# Use the pop() method and print the item that was randomly removed.
# Expected Output:
# {'HTML', 'CSS', 'React', 'Tailwind', 'JavaScript'}
# {'HTML', 'CSS', 'React', 'Tailwind', 'JavaScript'}
# <random removed item>


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


# 6. Update Set with Intersection
# Use intersection_update() on set_a to keep only the items present in both set_a and set_b.
# Expected Output:
# {'banana', 'cherry'}


# 7. Difference Update
# Use difference_update() on set_a to remove the items present in both set_a and set_b.
# Expected Output:
# {'apple'}


# 8. Symmetric Difference Update
# Use symmetric_difference_update() on set_a and set_b to keep only items that are not in both sets.
# Expected Output:
# {'apple', 'pear', 'mango'}


# 9. Clearing and Deleting Sets
# Clear the contents of the tech_stack set.
# Delete the frontend_stack set.
# Expected Output:
# set()
# NameError: name 'frontend_stack' is not defined


