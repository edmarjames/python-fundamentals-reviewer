# 1. Filter and Print Prime Numbers
# Write a program that uses a for loop to print all prime numbers between 1 and 50.
    # Expected Output:
    # 2
    # 3
    # 5
    # 7
    # 11
    # 13
    # 17
    # 19
    # 23
    # 29
    # 31
    # 37
    # 41
    # 43
    # 47

# solution
def get_prime_numbers():
    prime_numbers = []
    for num in range(1, 50):
        if num == 0 or num == 1:
            continue
        else:
            for i in range(2, int(num/2)+1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers

prime_numbers = get_prime_numbers()
print(prime_numbers)


print("\r")
# 2. String Reversal
# Write a program that loops through a string (inputted by the user) and prints its reverse without using slicing ([::-1]).
    # Expected Output: If the input is "Python", the output should be
    # n
    # o
    # h
    # t
    # y
    # P

# solution
def reverse_string(input):
    str_list = []
    for char in input:
        str_list.append(char)

    str_list.reverse()
    for char in str_list:
        print(char)

print("Kindly input any string:")
str_input = input()
reverse_string(str_input)


print("\r")
# 3. Print the Fibonacci Sequence
# Using a for loop, print the first 10 numbers of the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, 13, 21, 34).
    # Expected Output:
    # 0
    # 1
    # 1
    # 2
    # 3
    # 5
    # 8
    # 13
    # 21
    # 34

# solution
def get_fibonacci():
    fib_series = [0, 1]
    for ctr in range(2, 10):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

result = get_fibonacci()
print(result)


print("\r")
# 4. Multiplication Table
# Write a program that prints a multiplication table for numbers 1 to 5 using nested loops.
    # Expected Output:
    # 1 x 1 = 1
    # 1 x 2 = 2
    # 1 x 3 = 3
    # 1 x 4 = 4
    # 1 x 5 = 5
    # 2 x 1 = 2
    # 2 x 2 = 4
    # ...
    # 5 x 4 = 20
    # 5 x 5 = 25

# solution
def multiplication_table():
    for ctr1 in range(1, 6):
        for ctr2 in range(1, 6):
            product = ctr1 * ctr2
            print(f"{ctr1} x {ctr2} = {product}")

multiplication_table()


print("\r")
# 5. Sum of Numbers (Skipping Multiples of 3)
# Write a program that loops through numbers from 1 to 30 and calculates the sum, but skips numbers that are multiples of 3 using continue.
    # Expected Output:
    # Sum of numbers excluding multiples of 3: 375

# solution
def sum_of_numbers():
    sum_val = 0
    for ctr in range(1, 31):
        if ctr %3 != 0:
            sum_val += ctr
    return sum_val

result = sum_of_numbers()
print(f"Sum of numbers excluding multiples of 3: {result}")


print("\r")
# 6. Palindrome Checker
# Write a program that loops through a list of strings and checks if each string is a palindrome (a word that reads the same backward as forward). Print whether each word is a palindrome or not.
    # Expected Output:
    # racecar is a palindrome
    # hello is not a palindrome
    # level is a palindrome

# solution
def palindrome_checker(str_input):
    result_str = ""
    for ctr in range(0, int(len(str_input)/2)):
        if str_input[ctr] != str_input[len(str_input)-ctr-1]:
            result_str = f"{str_input} is not a palindrome"
        else:
            result_str = f"{str_input} is a palindrome"
    return result_str

print(palindrome_checker("racecar"))
print(palindrome_checker("hello"))
print(palindrome_checker("level"))


print("\r")
# 7: Skip and Stop
# Write a for loop that iterates through numbers from 1 to 20, printing each number. Skip numbers divisible by 4 using continue, and stop the loop completely if you encounter a number divisible by 7 using break.
    # Expected Output:
    # 1
    # 2
    # 3
    # 5
    # 6

# solution
def skip_and_stop():
    for ctr in range(1, 21):
        if ctr %4 == 0:
            continue
        elif ctr %7 == 0:
            break
        else:
            print(ctr)

skip_and_stop()
