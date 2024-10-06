# 1: Cube of a Number
# Create a lambda function that takes a single number as an argument and returns its cube.
    # Input: 3
    # Expected Output:
    # 27

# solution
cube = lambda x : x**3
print(cube(3))


print("\r")
# 2: Concatenate Strings
# Write a lambda function that takes two strings as arguments and concatenates them with a space in between.
    # Input: "Hello", "World"
    # Expected Output:
    # "Hello World"

# solution
concatenator = lambda a, b : f"{a} {b}"
print(concatenator("Hello", "World"))


print("\r")
# 3: Filter Odd Numbers
# Given a list of integers, use a lambda function inside the filter() function to extract all odd numbers from the list.
    # Input: [1, 2, 3, 4, 5, 6, 7]
    # Expected Output:
    # [1, 3, 5, 7]

# solution
num_list = [1, 2, 3, 4, 5, 6, 7]
filter_odd = list(filter(lambda n : n % 2 == 1, num_list))
print(filter_odd)


print("\r")
# 4: Find Maximum in a List of Tuples
# Given a list of tuples, where each tuple contains two numbers, write a lambda function that returns the tuple with the highest sum of its two elements.
    # Input: [(1, 5), (2, 3), (7, 2)]
    # Expected Output:
    # (1, 5)

# solution
input_tup = [(1, 5), (2, 3), (7, 2)]
input_tup.sort(key = lambda tup : sum(tup))
max_sum = input_tup[-1]
print(max_sum)


print("\r")
# 5: Sort Strings by Length
# Write a lambda function to sort a list of strings by their length.
    # Input: ["apple", "kiwi", "banana"]
    # Expected Output:
    # ['kiwi', 'apple', 'banana']

# solution
fruit_list = ["apple", "kiwi", "banana"]
fruit_list.sort(key = lambda fruit : len(fruit))
print(fruit_list)


print("\r")
# 6: Multiply All Elements by a Constant
# Write a lambda function inside the map() function to multiply each element in a list of numbers by a constant value, say 5.
    # Input: [1, 2, 3, 4]
    # Expected Output:
    # [5, 10, 15, 20]

# solution
multiplier = 5
int_list = [1, 2, 3, 4]
result = list(map(lambda n : n * multiplier, int_list))
print(result)


print("\r")
# 7: Find the Shortest Word
# Given a list of words, use a lambda function to find the shortest word in the list.
    # Input: ["sun", "moon", "star"]
    # Expected Output:
    # "sun"

# solution
stars_list = ["sun", "moon", "star"]
stars_list.sort(key = lambda star : len(star))
shortest = stars_list[0]
print(shortest)


print("\r")
# 8: Apply a Discount
# Write a lambda function that takes a price and a discount percentage and returns the final price after applying the discount.
    # Input: Price: 100, Discount: 20%
    # Expected Output:
    # 80.0

# solution
discounted_price = lambda price, discount : price - (price / 100) * discount
print(discounted_price(100, 20))


print("\r")
# 9: Sort a Dictionary by Values
# Given a dictionary, use a lambda function to sort it by its values in descending order.
    # Input: {"a": 3, "b": 1, "c": 2}
    # Expected Output:
    # [('a', 3), ('c', 2), ('b', 1)]

# solution
input_dict = {"a": 3, "b": 1, "c": 2}
sorted_dict = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_dict)


print("\r")
# 10: Combine Lambda with reduce() to Sum a List
# Using the reduce() function along with a lambda function, find the sum of all numbers in a list.
    # Input: [1, 2, 3, 4]
    # Expected Output:
    # 10

# solution
from functools import reduce
to_sum_list = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, to_sum_list)
print(total)