import re
# **Exercise 1: Greeting with Error Handling**
# Write a program that asks the user for their name and greets them. If the user inputs an empty string, raise an exception saying "Name cannot be empty."

    # #### **Expected Input**:
    # - User input: `"John"`

    # #### **Expected Output**:
    # Hello, John!

    # #### **Input**:
    # - User input: `""`

    # #### **Expected Output**:
    # Error: Name cannot be empty.

# solution
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        raise ValueError("Error: Name cannot be empty.")

name_input = input("Kindly enter your name: ")

try:
    greet(name_input)
except ValueError as e:
    print(f"Error: {e}")

# Alternative solution
# def greet(name):
#     if name:
#         print(f"Hello, {name}!")
#     else:
#         print("Name cannot be empty.")

# name_input = input("Kindly enter your name: ")
# greet(name_input)


print("\r")
# **Exercise 2: Age Validator**
# Ask the user to enter their age. If they enter a non-integer value, handle the exception and print "Please enter a valid number." If the age is negative or zero, raise an exception that says, "Age must be a positive number."

    # #### **Expected Input**:
    # - User input: `25`

    # #### **Expected Output**:
    # You are 25 years old.

    # #### **Input**:
    # - User input: `"abc"`

    # #### **Expected Output**:
    # Please enter a valid number.

    # #### **Input**:
    # - User input: `-3`

    # #### **Expected Output**:
    # Error: Age must be a positive number.

# solution
def age_validator(age_input):
    if re.match(r"-*\d", age_input):
        if int(age_input) <= 0:
            print("Error: Age must be a positive number.")
        else:
            print(f"You are {age_input} years old.")
    else:
        print("Please enter a valid number.")

age_input = input("Kindly enter your age: ")
age_validator(age_input)

# Alternative solution
# def age_validator(age_input):
#     try:
#         age = int(age_input)
#         if age <= 0:
#             raise ValueError("Age must be a positive number.")
#         print(f"You are {age} years old.")
#     except ValueError:
#         print("Please enter a valid number.")

# age_input = input("Kindly enter your age: ")
# age_validator(age_input)


print("\r")
# **Exercise 3: Number Squaring with Input**
# Create a program that asks the user for a number, squares it, and displays the result. If the user provides anything other than a number, catch the exception and print an error message.

    # #### **Expected Input**:
    # - User input: `4`

    # #### **Expected Output**:
    # The square of 4 is 16.

    # #### **Input**:
    # - User input: `"xyz"`

    # #### **Expected Output**:
    # Error: Please enter a valid number.

# solution
def square_num(input_num):
    try:
        num = int(input_num)
        print(f"The square of {num} is {num**2}")
    except ValueError:
        print("Error: Please enter a valid number.")

num_input = input("Kindly enter any number: ")
square_num(num_input)

# Alternative solution
# def square_num(input_num):
#     if re.match(r"\d", input_num):
#         input_num = int(input_num)
#         print(f"The square of {input_num} is {input_num**2}")
#     else:
#         print("Please enter a valid number.")

# num_input = input("Kindly enter any number: ")
# square_num(num_input)


print("\r")
# **Exercise 4: File Reader with Input**
# Ask the user for a filename and attempt to read its contents. Handle exceptions if the file does not exist and print an error message.

    # #### **Expected Input**:
    # - User input: `"example.txt"` (assuming file exists)

    # #### **Expected Output**:
    # File Contents:
    # [contents of the file]

    # #### **Input**:
    # - User input: `"nonexistent.txt"` (file doesn't exist)

    # #### **Expected Output**:
    # Error: The file 'nonexistent.txt' does not exist.

# solution
def read_file(file_name):
    try:
        read_file = open(f"{file_name}.txt")
        print(read_file.read())
        read_file.close()
    except FileNotFoundError:
        print(f"Error: The file {file_name}.txt does not exist.")

file_name = input("Kindly enter the file name: ")
read_file(file_name)


print("\r")
# **Exercise 5: Number List Input**
# Ask the user to input a series of comma-separated numbers. Convert them into a list of integers. If the user provides invalid input (e.g., letters), catch the exception and print an error message.

    # #### **Expected Input**:
    # - User input: `"3, 6, 9"`

    # #### **Expected Output**:
    # You entered: [3, 6, 9]

    # #### **Input**:
    # - User input: `"3, a, 9"`

    # #### **Expected Output**:
    # Error: Please enter valid numbers only.

# solution
def to_list(user_input):
    try:
        # Convert input to a list of integers
        number_list = [int(item.strip()) for item in user_input.split(",")]
        print(f"You entered: {number_list}")
    except ValueError:
        print("Error: Please enter valid numbers only.")

user_input = input("Kindly enter multiple numbers (comma-separated): ")
to_list(user_input)

# Alternative solution
# def to_list(user_input):
#     to_list = user_input.split(", ")
#     invalid_char = ""
#     for item in to_list:
#         match_res = re.match(r"\d", item)
#         if match_res is None: invalid_char = "Please enter valid numbers only."
#     if invalid_char:
#         print("Please enter valid numbers only.")
#     else:
#         print(to_list)

# user_input = input("Kindly enter multiple numbers: ")
# to_list(user_input)