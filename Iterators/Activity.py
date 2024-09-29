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

# solution
class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            a = self.a
            c = self.a + self.b
            self.a, self.b = self.b, c
            self.count += 1
            return a
        else:
            raise StopIteration

fib = Fibonacci(10)
for num in fib:
    print(num)


print("\r")
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

# solution
class PrimeIterator(object):
    def __init__(self, n):
        self.max = n

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            i = 2
            while i < (self.n//2+1):
                if self.n % i == 0:
                    self.n = self.n+1
                    if self.n > self.max:
                        raise StopIteration
                    i = 1
                i += 1
            else:
                return self.n
        else:
            raise StopIteration

prime_iter = PrimeIterator(50)
for prime in prime_iter:
    print(prime)


print("\r")
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

# solution
class ReverseString(object):
    def __init__(self, input_str):
        self.str = input_str
        self.ctr = len(input_str)

    def __iter__(self):
        return self

    def __next__(self):
        while self.ctr > 0:
            self.ctr -= 1
            return self.str[self.ctr]
        else:
            raise StopIteration

reverse_str = ReverseString("OpenAI")
for char in reverse_str:
    print(char)


print("\r")
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

# solution
class MyRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            x = self.start
            self.start += 2
            return x
        else:
            raise StopIteration

my_range = MyRange(0, 10)
for num in my_range:
    print(num)


print("\r")
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

# solution
class CycleIterator(object):
    def __init__(self, num_list):
        self.num_list = num_list
        self.ctr = 0
        self.index_ctr = 0

    def __iter__(self):
        return self

    def __next__(self):
        num_len = len(self.num_list)

        if self.ctr < 10:
            index = self.index_ctr
            self.ctr += 1
            self.index_ctr += 1
            if index == num_len -1:
                self.index_ctr = 0
            return self.num_list[index]
        else:
            raise StopIteration

cycle = CycleIterator([1, 2, 3])
for num in cycle:
    print(num)


print("\r")
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

# solution
# class NestedListIterator:
#     def __init__(self, nested_list):
#         self.nested_list = nested_list
#         self.ctr = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if len(self.nested_list) > 0:
#             for ctr in range(0, len(self.nested_list)):
#                 if self.nested_list[ctr]:
#                     for ctr1 in range(0, len(self.nested_list[ctr])):
#                         pop_item = self.nested_list[ctr].pop(-1)
#                         return pop_item
#                 else:
#                     del self.nested_list[ctr]
#         else:
#             raise StopIteration

class NestedListIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.outer_idx = 0
        self.inner_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_idx < len(self.nested_list):
            if self.inner_idx >= len(self.nested_list[self.outer_idx]):
                self.outer_idx += 1
                self.inner_idx = 0
            else:
                element = self.nested_list[self.outer_idx][self.inner_idx]
                self.inner_idx += 1
                return element
        raise StopIteration

nested_list = NestedListIterator([[1, 2], [3, 4], [5, 6]])
for item in nested_list:
    print(item)


print("\r")
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

# solution
class SquareIterator(object):
    def __init__(self, max_num):
        self.max_num = max_num
        self.min_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.min_num <= self.max_num:
            val = self.min_num
            self.min_num += 1
            return val**2
        else:
            raise StopIteration

squares = SquareIterator(5)
for num in squares:
    print(num)


print("\r")
# 8. **Character Filter Iterator**
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

# solution
class CharFilterIterator(object):
    def __init__(self, input_string, input_char):
        self.input_string = input_string
        self.input_char = input_char
        self.ctr = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.ctr < len(self.input_string):
            ctr_holder = self.ctr
            self.ctr += 1
            if self.input_char != self.input_string[ctr_holder]:
                continue
            else:
                return self.input_string[ctr_holder]
        else:
            raise StopIteration

char_filter = CharFilterIterator("hello world", "o")
for char in char_filter:
    print(char)


print("\r")
# 9. **Even Numbers Iterator with StopIteration**
# Create an iterator class `EvenNumbers` that generates even numbers from a given start number, but stops after reaching a specified limit by raising a `StopIteration`.
    # **Example:**
    # class EvenNumbers:
    #     # Implement __iter__() and __next__()

    # evens = EvenNumbers(2, 20)
    # for num in evens:
    #     print(num)

    # # Expected Output:
    # # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

# solution
class EvenNumbers(object):
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.min_num <= self.max_num:
            val = self.min_num
            self.min_num += 2
            return val
        else:
            raise StopIteration

evens = EvenNumbers(2, 20)
for num in evens:
    print(num)


print("\r")
# 10. **Random Number Iterator**
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

# solution
import random
class RandomIterator(object):
    def __init__(self, max_count):
        self.max_count = max_count
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.max_count:
            self.counter += 1
            return random.randrange(1, 100)
        else:
            raise StopIteration

random_iter = RandomIterator(5)
for num in random_iter:
    print(num)