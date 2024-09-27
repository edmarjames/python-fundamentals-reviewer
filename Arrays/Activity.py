# 1. **Find the Longest String**
# Write a Python function that takes an array of strings and returns the longest string in the array.
    # **Example:**
    # cars = ["Honda", "Toyota", "Hyundai", "Suzuki"]
    # print(find_longest(cars))  # Output: "Hyundai"

# solution
cars = ["Honda", "Toyota", "Hyundai", "Suzuki"]
find_longest = max(cars, key = lambda car : len(car))
print(find_longest)


print("\r")
# 2. **Find the Second Largest Number**
# Given an array of numbers, write a Python function that returns the second-largest number.
    # **Example:**
    # numbers = [10, 45, 22, 35, 50, 75, 100]
    # print(second_largest(numbers))  # Output: 75

# solution
def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort(reverse = True)
    return numbers[1]

numbers = [10, 45, 22, 35, 50, 75, 100]
print(second_largest(numbers))


print("\r")
# 3. **Merge Two Arrays and Sort**
# Write a function that takes two arrays, merges them into one, and returns the merged array in sorted order.
    # **Example:**
    # arr1 = [1, 5, 9]
    # arr2 = [2, 6, 8, 10]
    # print(merge_and_sort(arr1, arr2))  # Output: [1, 2, 5, 6, 8, 9, 10]

# solution
def merge_and_sort(arr1, arr2):
    final_arr = arr1 + arr2
    final_arr.sort()
    return final_arr

arr1 = [1, 5, 9]
arr2 = [2, 6, 8, 10]
print(merge_and_sort(arr1, arr2))


print("\r")
# 4. **Remove Duplicates from an Array**
# Write a function that removes all duplicates from a given array.
    # **Example:**
    # nums = [1, 2, 2, 3, 4, 4, 5]
    # print(remove_duplicates(nums))  # Output: [1, 2, 3, 4, 5]

# solution
def remove_duplicates(nums):
    remove_duplicates = list(set(nums))
    return remove_duplicates

nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))


print("\r")
# 5. **Array Rotation**
# Write a Python function that rotates an array by a given number of steps to the right.
    # **Example:**
    # arr = [1, 2, 3, 4, 5]
    # steps = 2
    # print(rotate_array(arr, steps))  # Output: [4, 5, 1, 2, 3]

# solution
def rotate_array(arr, steps):
    for ctr in range(0, steps):
        last_element = arr[-1]
        arr.pop(-1)
        arr.insert(0, last_element)
    return arr

arr = [1, 2, 3, 4, 5]
steps = 2
print(rotate_array(arr, steps))


print("\r")
# 6. **Find Missing Number in a Sequence**
# Given an array of numbers from 1 to `n` (where one number is missing), write a function to find the missing number.
    # **Example:**
    # numbers = [1, 2, 4, 5, 6]
    # print(find_missing(numbers))  # Output: 3

# solution
def find_missing(numbers):
    ctr = 0
    counter = 1
    while ctr < len(numbers):
        if counter == numbers[ctr]:
            ctr += 1
            counter += 1
            continue
        else:
            return counter

numbers = [1, 2, 4, 5, 6]
print(find_missing(numbers))


print("\r")
# 7. **Split an Array into Even and Odd Numbers**
# Write a function that splits an array into two separate arrays: one containing even numbers and the other containing odd numbers.
    # **Example:**
    # numbers = [1, 2, 3, 4, 5, 6]
    # print(split_even_odd(numbers))  # Output: ([2, 4, 6], [1, 3, 5])

# solution
def split_even_odd(numbers):
    is_even = []
    is_odd = []
    for num in numbers:
        if num %2 == 0:
            is_even.append(num)
        else:
            is_odd.append(num)
    final = is_even, is_odd
    return tuple(final)

numbers = [1, 2, 3, 4, 5, 6]
print(split_even_odd(numbers))


print("\r")
# 8. **Count Occurrences of an Element**
# Write a function that counts how many times a specific element appears in an array.
    # **Example:**
    # arr = [3, 4, 3, 2, 1, 3, 4]
    # print(count_occurrences(arr, 3))  # Output: 3

# solution
def count_occurrences(arr, num):
    return arr.count(num)

arr = [3, 4, 3, 2, 1, 3, 4]
print(count_occurrences(arr, 3))


print("\r")
# 9. **Sum of All Elements**
# Write a Python function that returns the sum of all elements in an array.
    # **Example:**
    # nums = [10, 20, 30, 40]
    # print(sum_array(nums))  # Output: 100

# solution
def sum_array(num):
    return sum(num)

nums = [10, 20, 30, 40]
print(sum_array(nums))


print("\r")
# 10. **Check if an Array is a Subset of Another**
# Write a function that checks whether one array is a subset of another array.
    # **Example:**
    # arr1 = [1, 2, 3]
    # arr2 = [1, 2, 3, 4, 5]
    # print(is_subset(arr1, arr2))  # Output: True

    # arr1 = [1, 6, 3]
    # arr2 = [1, 2, 3, 4, 5]
    # print(is_subset(arr1, arr2))  # Output: False

# solution
def is_subset(arr1, arr2):
    for item in arr1:
        if arr1[item] == arr2[item]:
            return True
        else:
            return False

arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]
print(is_subset(arr1, arr2))

arr3 = [1, 6, 3]
arr4 = [1, 2, 3, 4, 5]
print(is_subset(arr3, arr4))