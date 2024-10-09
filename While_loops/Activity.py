# 1. Find the First Multiple of 7
# Write a program that uses a while loop to find the first multiple of 7 between 1 and 100. Once you find it, stop the loop using the break statement.
    # Expected Output:
    # The first multiple of 7 is: 7

# solution
def get_first_multiple():
    ctr = 1
    while ctr <= 100:
        if ctr %7 == 0:
            print(f"The first multiple of 7 is: {ctr}")
            break
        ctr += 1

get_first_multiple()


print("\r")
# 2. Skipping Even Numbers
# Write a program that prints all odd numbers from 1 to 20 using a while loop. Use the continue statement to skip even numbers.
    # Expected Output:
    # 1
    # 3
    # 5
    # 7
    # 9
    # 11
    # 13
    # 15
    # 17
    # 19

# solution
def skip_even_numbers():
    ctr = 1
    while ctr < 20:
        if ctr %2 == 0:
            ctr += 1
            continue
        print(ctr)
        ctr += 1

skip_even_numbers()


print("\r")
# 3. Countdown Timer
# Write a while loop that counts down from 10 to 0 and prints each number. When it reaches 0, print "Blast off!" using the else statement after the loop ends.
    # Expected Output:
    # 10
    # 9
    # 8
    # 7
    # 6
    # 5
    # 4
    # 3
    # 2
    # 1
    # 0
    # Blast off!

# solution
def countdown_timer():
    ctr = 10
    while ctr >= 0:
        print(ctr)
        ctr -= 1
    else:
        print("Blast off!")

countdown_timer()


print("\r")
# 4. Sum of Numbers Until 50
# Write a program that calculates the sum of numbers starting from 1 and keeps adding them until the sum exceeds 50. Use a while loop to do this and print the sum.
    # Expected Output:
    # Sum: 55

# solution
def sum_of_fifty():
    ctr = 0
    sum_of_fifty = 0
    while ctr <= 50:
        ctr += 1
        sum_of_fifty += ctr
        if sum_of_fifty > 50:
            break
    print(sum_of_fifty)

sum_of_fifty()


print("\r")
# 5. Infinite Loop Guard
# Write a program that simulates an infinite loop (e.g., while True), but safely breaks out of the loop after printing "Still running..." five times. Use the break statement to exit the loop.
    # Expected Output:
    # Still running...
    # Still running...
    # Still running...
    # Still running...
    # Still running...
    # Loop has been stopped after 5 iterations.

def infinite_loop_guard():
    ctr = 0
    while ctr < 5:
        print("Still running...")
        if ctr == 5:
            break
        ctr += 1
    else:
        print("Loop has been stopped after 5 iterations")

infinite_loop_guard()