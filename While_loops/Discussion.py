# With the "while" loop we can execute a set of statements as long as a condition is true.
# note: remember to increment your incrementor variable to avoid infinite loop.
ctr = 0
while ctr <= 10:
    print(ctr)
    ctr += 1
    
print("\n")
# The break statement
# With the "break" statement we can stop the loop even if the while condition is true.
ctr1 = 0
while ctr1 <= 10:
    print(ctr1)
    if ctr1 == 6:
        break
    ctr1 += 1

print("\n")
# The continue statement
# With the "continue" statement we can stop the current iteration, and continue with the next.
ctr2 = 0
while ctr2 <= 10:
    ctr2 += 1    
    if ctr2 == 3:
        continue
    print(ctr2)

print("\n")
# The else statement
# With the "else" statement we can run a block of code once when the condition is no longer true.
ctr4 = 0
while ctr4 < 10:
    print(ctr4)
    ctr4 += 1
else:
    print("Counter is no longer less than 10")