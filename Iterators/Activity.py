# 1. **Custom Iterator for Fibonacci Sequence**
# Create a custom iterator class `Fibonacci` that generates numbers in the Fibonacci sequence up to a certain number of terms.

# **Example:**
# class Fibonacci:
#     # Implement __iter__() and __next__()

# fib = Fibonacci(10)  # Iterator for first 10 Fibonacci numbers
# for num in fib:
#     print(num)  

# # Expected Output: 
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


# 2. **Prime Number Iterator**
# Create an iterator class `PrimeIterator` that generates prime numbers up to a specified limit. The iterator should stop when the next prime number would exceed the limit.

# **Example:**
# class PrimeIterator:
#     # Implement __iter__() and __next__()

# prime_iter = PrimeIterator(50)
# for prime in prime_iter:
#     print(prime)

# # Expected Output:
# # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47


# 3. **Reverse String Iterator**
# Create a custom iterator class `ReverseString` that takes a string and iterates over its characters in reverse order.

# **Example:**
# class ReverseString:
#     # Implement __iter__() and __next__()

# reverse_str = ReverseString("OpenAI")
# for char in reverse_str:
#     print(char)

# # Expected Output:
# # I
# # A
# # n
# # e
# # p
# # O


# 4. **Custom Range Iterator**
# Create a custom iterator class `MyRange` that behaves like Python’s built-in `range()` function, but for every iteration, it skips by two (i.e., 0, 2, 4, 6, ...). Implement this iterator such that it works with a start and end value.

# **Example:**
# class MyRange:
#     # Implement __iter__() and __next__()

# my_range = MyRange(0, 10)
# for num in my_range:
#     print(num)

# # Expected Output:
# # 0, 2, 4, 6, 8


# 5. **Cycle Iterator**
# Create an iterator class `CycleIterator` that takes a list and loops through it indefinitely. Add a stop condition so that the iteration stops after 10 iterations.

# **Example:**
# class CycleIterator:
#     # Implement __iter__() and __next__()

# cycle = CycleIterator([1, 2, 3])
# for num in cycle:
#     print(num)

# # Expected Output:
# # 1, 2, 3, 1, 2, 3, 1, 2, 3, 1


# 6. **Nested List Iterator**
# Create an iterator class `NestedListIterator` that takes a nested list and iterates through all the elements, flattening the list as it goes.

# **Example:**
# class NestedListIterator:
#     # Implement __iter__() and __next__()

# nested_list = NestedListIterator([[1, 2], [3, 4], [5, 6]])
# for item in nested_list:
#     print(item)

# # Expected Output:
# # 1, 2, 3, 4, 5, 6


# 7. **Squares Iterator**
# Create an iterator class `SquareIterator` that generates the square of each number up to a given limit.

# **Example:**
# class SquareIterator:
#     # Implement __iter__() and __next__()

# squares = SquareIterator(5)  # Squares of 1 to 5
# for num in squares:
#     print(num)

# # Expected Output:
# # 1, 4, 9, 16, 25


### 8. **Character Filter Iterator**
# Create an iterator class `CharFilterIterator` that takes a string and a character as input and iterates over only the occurrences of the specified character in the string.

# **Example:**
# class CharFilterIterator:
#     # Implement __iter__() and __next__()

# char_filter = CharFilterIterator("hello world", "o")
# for char in char_filter:
#     print(char)

# # Expected Output:
# # o
# # o


### 9. **Even Numbers Iterator with StopIteration**
# Create an iterator class `EvenNumbers` that generates even numbers from a given start number, but stops after reaching a specified limit by raising a `StopIteration`.

# **Example:**
# class EvenNumbers:
#     # Implement __iter__() and __next__()

# evens = EvenNumbers(2, 20)
# for num in evens:
#     print(num)

# # Expected Output:
# # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20


### 10. **Random Number Iterator**
# Create an iterator class `RandomIterator` that generates a specified number of random integers between 1 and 100. Use the `random` module to generate the numbers.

# **Example:**
# import random

# class RandomIterator:
#     # Implement __iter__() and __next__()

# random_iter = RandomIterator(5)
# for num in random_iter:
#     print(num)

# # Expected Output:
# # (5 random integers between 1 and 100)