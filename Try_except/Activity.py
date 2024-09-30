# **Exercise 1: Division with Error Handling**
# Create a function `safe_divide` that takes two numbers as input and returns their division. Implement error handling to manage the following cases:
# 1. If the second number is zero, raise a custom `ZeroDivisionError` with the message `"Cannot divide by zero!"`.
# 2. If any input is not a number, catch a `TypeError` and print `"Both inputs must be numbers!"`.
# 3. Use an `else` block to print `"Division successful!"` when no errors occur.
# 4. Ensure the `finally` block always prints `"Execution completed"`.

    # **Input:**
    # safe_divide(10, 2)
    # safe_divide(10, 0)
    # safe_divide(10, "a")

    # **Expected Output:**
    # Division successful!
    # Execution completed
    # Cannot divide by zero!
    # Execution completed
    # Both inputs must be numbers!
    # Execution completed

# solution
def safe_divide(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Both inputs must be numbers!")
    else:
        print("Division successful!")
    finally:
        print("Execution completed")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "a")


print("\r")
# **Exercise 2: File Operations with Exception Handling**
# Write a function `read_file_content` that:
# 1. Attempts to open a file and read its content.
# 2. Catches a `FileNotFoundError` if the file doesn't exist, and prints `"File not found!"`.
# 3. Catches any other unexpected exception with a generic message `"An error occurred"`.
# 4. Uses an `else` block to print `"File read successfully"` if no errors occur.
# 5. Ensure the `finally` block prints `"File operation finished"`.

    # **Input:**
    # read_file_content("non_existent_file.txt")
    # read_file_content("valid_file.txt")

    # **Expected Output:**
    # File not found!
    # File operation finished
    # File read successfully
    # File operation finished

# solution
def read_file_content(file_name):
    try:
        my_file = open(file_name)
        my_file.read()
        my_file.close()
    except FileNotFoundError:
        print("File not found!")
    except Exception:
        print("An error occurred")
    else:
        print("File read successfully")
    finally:
        print("File operation finished")

read_file_content("non_existent_file.txt")
read_file_content("valid_file.txt")


print("\r")
# **Exercise 3: Custom Error for Age Validation**
# Create a function `validate_age` that takes an age as input. If the age is less than 18, raise an exception with the message `"Age must be at least 18"`. Catch the exception and print the error message. Use the `finally` block to print `"Age validation complete"`.

    # **Input:**
    # validate_age(15)
    # validate_age(20)

    # **Expected Output:**
    # Age must be at least 18
    # Age validation complete
    # Age validation complete

# solution
def validate_age(age_input):
    try:
        if age_input < 18:
            raise ValueError("Age must be at least 18")
    except ValueError as e:
        print(e)
    finally:
        print("Age validation complete")

validate_age(15)
validate_age(20)
# alternative solution
# def validate_age(age_input):
#     try:
#         if age_input < 18:
#             print("Age must be at least 18")
#     finally:
#         print("Age validation complete")


print("\r")
# **Exercise 4: Complex Try-Except with Else and Finally**
# Write a function `process_data` that:
# 1. Tries to convert an input to an integer.
# 2. Catches a `ValueError` if the conversion fails, printing `"Invalid data type. Expected an integer."`
# 3. If the conversion succeeds, use an `else` block to print `"Data processed successfully"`.
# 4. Use a `finally` block to print `"Process completed"`.

    # **Input:**
    # process_data("100")
    # process_data("Hello")

    # **Expected Output:**
    # Data processed successfully
    # Process completed
    # Invalid data type. Expected an integer.
    # Process completed

# solution
def process_data(user_input):
    try:
        converted_val = int(user_input)
    except ValueError:
        print("Invalid data type. Expected an integer.")
    else:
        print("Data processed successfully")
    finally:
        print("Process completed")

process_data("100")
process_data("Hello")


print("\r")
# **Exercise 5: Raising a Custom Exception for Even Number Check**
# Write a function `check_even` that takes a number as input. If the number is not even, raise a custom exception with the message `"Not an even number!"`. Ensure that this exception is caught and print the error message.

    # **Input:**
    # check_even(4)
    # check_even(5)

    # **Expected Output:**
    # Not an even number!

# solution
def check_even(input_num):
    try:
        if input_num % 2 != 0:
            raise Exception("Not an even number!")
    except Exception as e:
        print(e)

check_even(4)
check_even(5)
# alternative solution
# def check_even(input_num):
#     if input_num %2 != 0:
#         raise Exception("Not an even number!")