# 1. Grading System
# Create a program that takes a student’s score (out of 100) and assigns a letter grade based on the following criteria:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: below 60
# Additionally, print out a special message if the score is exactly 100: "Perfect Score!"
    # Scenario 1: Input: score = 95
    # Expected Output: Grade: A

    # Scenario 2: Input: score = 85
    # Expected Output: Grade: B

    # Scenario 3: Input: score = 75
    # Expected Output: Grade: C

    # Scenario 4: Input: score = 65
    # Expected Output: Grade: D

    # Scenario 5: Input: score = 55
    # Expected Output: Grade: F

    # Scenario 6: Input: score = 100
    # Expected Output: Grade: A
    # Perfect Score!

# solution
def compute_grades(grade):
    if grade < 60:
        final_grade = "F"
    elif grade >= 60 and grade <= 69:
        final_grade = "D"
    elif grade >= 70 and grade <= 79:
        final_grade = "C"
    elif grade >= 80 and grade <= 89:
        final_grade = "B"
    elif grade >= 90:
        final_grade = "A"

    return final_grade

print("Kindly enter the grade: ")
grade_input = int(input())
final_grade = compute_grades(grade_input)
print(f"Grade: {final_grade}")
if grade_input == 100:
    print("Perfect Score!")


print("\n")
# 2. Nested Conditions: Movie Ticket Pricing
# Create a program that calculates the price of a movie ticket based on a person's age and membership status:
# Age < 12: ticket price = $5
# Age 12–59: ticket price = $10
# Age 60 and above: ticket price = $7
# If the person is a member, apply a 20% discount on the ticket price.
# Use nested if statements to calculate the final ticket price and print it.
    # Scenario 1: Input: age = 10, is_member = False
    # Expected Output: Final Ticket Price: $5

    # Scenario 2: Input: age = 25, is_member = True
    # Expected Output: Final Ticket Price: $8.0  # (20% discount on $10)

    # Scenario 3: Input: age = 65, is_member = False
    # Expected Output: Final Ticket Price: $7

    # Scenario 4: Input: age = 70, is_member = True
    # Expected Output: Final Ticket Price: $5.6  # (20% discount on $7)

# solution
def compute_ticket_price(age, is_member):    
    if age < 12:
        price = 5
    elif age >= 12 and age <= 59:
        price = 10
    elif age >= 60:
        price = 7

    if is_member:
        savings = (price / 100) * 20
        final_price = price - savings
    else:
        final_price = price

    return final_price

print("Kindly enter the age:")
age_input = int(input())
print("Are you a member? If no, just press enter:")
member_input = bool(input())
computed_price = compute_ticket_price(age_input, member_input)
print(f"Final Ticket Price: ${computed_price}")


print("\n")
# 3. Complex List Comparison
# Write a program that takes two lists of integers as input, compares their contents, and prints:
# "Same length, same values" if both lists have the same length and identical values in the same positions.
# "Same length, different values" if both lists have the same length but different values.
# "Different length" if the lists have different lengths.
# Include a condition where if both lists are empty, print "Both lists are empty".

    # Scenario 1: Input: list1 = [1, 2, 3], list2 = [1, 2, 3]
    # Expected Output: Same length, same values

    # Scenario 2: Input: list1 = [1, 2, 3], list2 = [1, 2, 4]
    # Expected Output: Same length, different values

    # Scenario 3: Input: list1 = [1, 2, 3, 4], list2 = [1, 2, 3]
    # Expected Output: Different length

    # Scenario 4: Input: list1 = [], list2 = []
    # Expected Output: Both lists are empty

# solution
def check_list(list1, list2):
    result_str_list = []

    if len(list1) != 0 and len(list2) != 0 and len(list1) == len(list2):
        result_str_list.append("Same Length")        
        if list1 == list2:
            result_str_list.append("same values")
        else:
            result_str_list.append("different values")

    elif len(list1) != len(list2):
        result_str_list.append("Different length")
    elif len(list1) == 0 and len(list2) == 0:
        result_str_list.append("Both lists are empty")
    
    if len(result_str_list) > 1:
        return ", ".join(result_str_list)
    else:
        return result_str_list[0]

print(check_list([1, 2, 3], [1, 2, 3]))
print(check_list([1, 2, 3], [1, 2, 4]))
print(check_list([1, 2, 3, 4], [1, 2, 3]))
print(check_list([], []))


print("\n")
# 4. Logic Gate Simulator
# Implement a simple logic gate simulator. The program should ask the user for two boolean inputs (True or False) and perform the following logical operations:
# AND
# OR
# NOT on the first input
# Use conditional statements to print the results of the operations.

    # Scenario 1: Input: input1 = True, input2 = False
    # Expected Output:
    # AND: False
    # OR: True
    # NOT input1: False

    # Scenario 2: Input: input1 = False, input2 = False
    # Expected Output:
    # AND: False
    # OR: False
    # NOT input1: True

    # Scenario 3: Input: input1 = True, input2 = True
    # Expected Output:
    # AND: True
    # OR: True
    # NOT input1: False

# solution
def logic_gate(input1, input2):
    if input1.lower() == "true":
        input1 = True
    else:
        input1 = False

    if input2.lower() == "true":
        input2 = True
    else:
        input2 = False

    print(f"AND: {input1 and input2}")
    print(f"OR: {input1 or input2}")
    print(f"NOT input1: {not input1}")    

print("Kindly enter True or False")
first_input = input()
print("Kindly enter True or False")
second_input = input()

print("\n")
logic_gate(first_input, second_input)