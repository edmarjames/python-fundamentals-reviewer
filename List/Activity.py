# 1. Creating Lists
# Create a list called my_fruits with the values "Apple", "Banana", and "Grape".
# Create a list using the list() constructor with values "Red", "Green", and "Blue".
    # Expected Output:
    # ['Apple', 'Banana', 'Grape']
    # ['Red', 'Green', 'Blue']

# solution
my_fruits = ["Apple", "Banana", "Grape"]
my_colors = list(("Red", "Green", "Blue"))
print(my_fruits)
print(my_colors)


print("\r")
# 2. Accessing Items
# Access the first item of the my_fruits list.
# Access the last item of the list using negative indexing.
    # Expected Output:
    # Apple
    # Grape

# solution
print(my_fruits[0])
print(my_fruits[-1])


print("\r")
# 3. Slicing Lists
# Retrieve the second and third items from the list my_fruits.
# Get all items from the start of the list to the second item.
# Get all items starting from the second item to the end of the list.
    # Expected Output:
    # ['Banana', 'Grape']
    # ['Apple', 'Banana']
    # ['Banana', 'Grape']

# solution
print(my_fruits[1:4])
print(my_fruits[:2])
print(my_fruits[1:])


print("\r")
# 4. Modifying Lists
# Change the first item of my_fruits to "Orange".
# Change the second and third items to "Mango" and "Pineapple".
    # Expected Output:
    # ['Orange', 'Banana', 'Grape']
    # ['Orange', 'Mango', 'Pineapple']

# solution
my_fruits[0] = "Orange"
print(my_fruits)
my_fruits[1:] = ["Mango", "Pineapple"]
print(my_fruits)


print("\r")
# 5. Adding Items
# Add "Cherry" to the end of my_fruits using the append() method.
# Insert "Watermelon" at the beginning of the list using the insert() method.
    # Expected Output:
    # ['Orange', 'Mango', 'Pineapple', 'Cherry']
    # ['Watermelon', 'Orange', 'Mango', 'Pineapple', 'Cherry']

# solution
my_fruits.append("Cherry")
print(my_fruits)
my_fruits.insert(0, "Watermelon")
print(my_fruits)


print("\r")
# 6. Removing Items
# Remove the item "Cherry" from the list using remove().
# Remove the first item using pop().
    # Expected Output:
    # ['Watermelon', 'Orange', 'Mango', 'Pineapple']
    # ['Orange', 'Mango', 'Pineapple']

# solution
my_fruits.remove("Cherry")
print(my_fruits)
my_fruits.pop(0)
print(my_fruits)


print("\r")
# 7. List Operations
# Check if "Orange" is in the list my_fruits.
# Sort the list in ascending order and then in descending order.
    # Expected Output:
    # True
    # ['Mango', 'Orange', 'Pineapple']
    # ['Pineapple', 'Orange', 'Mango']

# solution
print("Orange" in my_fruits)
my_fruits.sort()
print(my_fruits)
my_fruits.sort(reverse = True)
print(my_fruits)


print("\r")
# 8. List Copy
# Copy the my_fruits list using copy() and list().
# Verify that the copied lists are independent by appending "Peach" to the copied list but not the original.
    # Expected Output:
    # ['Orange', 'Mango', 'Pineapple']
    # ['Orange', 'Mango', 'Pineapple', 'Peach']

# solution
my_fruits_copy = my_fruits.copy()
my_fruits_copy.append("Peach")
my_fruits_copy_2 = list(my_fruits)
print(my_fruits_copy_2)
print(my_fruits_copy)


print("\r")
# 9. Joining Lists
# Join two lists phones_1 = ["iPhone", "Samsung"] and phones_2 = ["Nokia", "OnePlus"] using the + operator and extend() method.
    # Expected Output:
    # ['iPhone', 'Samsung', 'Nokia', 'OnePlus']
    # ['iPhone', 'Samsung', 'Nokia', 'OnePlus']

# solution
phones_1 = ["iPhone", "Samsung"]
phones_2 = ["Nokia", "OnePlus"]
final_list = phones_1 + phones_2
print(final_list)
phones_1.extend(phones_2)
print(phones_1)


print("\r")
# 10. Looping through Lists
# Loop through the list my_fruits using:
# A for loop.
# A while loop.
# List comprehension to print all items containing the letter 'a'.
    # Expected Output:
    # Orange
    # Mango
    # Pineapple

    # Orange
    # Mango
    # Pineapple

    # ['Orange', 'Mango', 'Pineapple']

# solution
for fruits in my_fruits:
    print(fruits)
print("\r")

ctr = 0
while ctr < len(my_fruits):
    print(my_fruits[ctr])
    ctr = ctr + 1
print("\r")

fruits_with_a = [fruits for fruits in my_fruits if "a" in fruits]
print(fruits_with_a)