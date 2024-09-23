# Write a Python script that:

# Accepts a number from the user as a string input.
# Convert the string to an integer, float, and back to a string.
# Print the values after each conversion along with their types.

str_input = input()

int_input = int(str_input)
print(f"{int_input} - {type(int_input)}")

float_input = float(str_input)
print(f"{float_input} - {type(float_input)}")

str_input = str(str_input)
print(f"{str_input} - {type(str_input)}")