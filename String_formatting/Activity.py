# Exercise 1: Simple String Formatting with Variables
# You are given two variables:
# first_name = "John"
# last_name = "Doe"
# Write an f-string that prints: "Hello, my name is John Doe."
    # #### **Expected Output**:
    # Hello, my name is John Doe.

# solution
first_name = "John"
last_name = "Doe"
print(f"Hello, my name is {first_name} {last_name}")


print("\r")
# Exercise 2: Formatting Numerical Values
# You have the following values:
# distance_km = 1500
# time_hours = 5
# Use an f-string to print: "The average speed is 300.00 km/h."
# Make sure the speed is formatted to two decimal places.
    # #### **Expected Output**:
    # The average speed is 300.00 km/h.


distance_km = 1500
time_hours = 5
print(f"The average speed is {distance_km / time_hours:.2f} km/h")


print("\r")
# Exercise 3: Conditional Placeholder in F-string
# Given the variable:
# score = 75
# Use an f-string to print whether the score passes or fails. A passing score is 70 or higher.
    # Expected output: "The student has passed." or "The student has failed."
    # #### **Expected Output**:
    # The student has passed.

# solution
score = 75
print(f"The student has {'failed ' if score < 70 else 'passed'}.")


print("\r")
# Exercise 4: Comma Formatting for Large Numbers
# You are given:
# salary = 1200000
# Use an f-string to print: "The employee's salary is 1,200,000 dollars."
    # #### **Expected Output**:
    # The employee's salary is 1,200,000 dollars.

# solution
salary = 1200000
print(f"The employee's salary is {salary:,} dollars.")


print("\r")
# Exercise 5: Perform Operations Inside F-strings
# You have the following data:
# price_per_item = 45.75
# quantity = 10
# Use an f-string to calculate the total price and print: "The total price for 10 items is 457.50 dollars."
# Make sure the total is formatted to two decimal places.
    # #### **Expected Output**:
    # The total price for 10 items is 457.50 dollars.

# solution
price_per_item = 45.75
quantity = 10
print(f"The total price for {quantity} items is {price_per_item * quantity:.2f} dollars.")


print("\r")
# Exercise 6: Function Calls Inside F-strings
# You have a function that converts miles to kilometers:
# def miles_to_km(miles):
#     return miles * 1.60934
# Use an f-string to print: "The distance is 32.19 kilometers." when the input distance is 20 miles.
    # #### **Expected Output**:
    # The distance is 32.19 kilometers.

# solution
def miles_to_km(miles):
    return miles * 1.60934

print(f"The distance is {miles_to_km(20):.2f} kilometers.")


print("\r")
# Exercise 7: Using `format()` Method
# Given the following variables:
# product = "Laptop"
# price = 999.99
# Use the `format()` method to print: "The price of the Laptop is 999.99 dollars."
    # #### **Expected Output**:
    # The price of the Laptop is 999.99 dollars.

# solution
product = "Laptop"
price = 999.99
print("The price of the {} is {} dollars.".format(product, price))


print("\r")
# Exercise 8: Named Indexes in `format()`
# You are placing a food order. Use the `format()` method with named indexes to print: "I ordered a Burger and Fries for lunch."
# lunch_order = "I ordered a {main} and {side} for lunch"
    # #### **Expected Output**:
    # I ordered a Burger and Fries for lunch.

# solution
print("I ordered a {main} and {side} for lunch.".format(main = "Burger", side = "Fries"))