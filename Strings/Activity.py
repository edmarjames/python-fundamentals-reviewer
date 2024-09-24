# 1. Basic String Handling
# Create a string with the value "Learning Python is fun!".
# Print the string using both single and double quotes in different statements.
    # Expected Output:
    # 'Learning Python is fun!'
    # "Learning Python is fun!"

# Solution
test_str = "Learning Python is fun!"
print(f"'{test_str}'")
print(f"\"{test_str}\"")


print("\n")
# 2. Multiline String
# Assign a multiline string to a variable using triple quotes.
# Print the multiline string.
    # Expected Output:
    # "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit,\nsed do eiusmod tempor incididunt\nut labore et dolore magna aliqua."

# solution
multiline_string = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(multiline_string)


print("\n")
# 3. Accessing String Characters
# Given the string "Python", print the first and last characters of the string.
    # Expected Output:
    # P
    # n

# solution
str_py = "Python"
print(str_py[0])
print(str_py[-1])


print("\n")
# 4. String Loop
# Loop through the string "Exercise" and print each character on a new line.
    # Expected Output:
    # E
    # x
    # e
    # r
    # c
    # i
    # s
    # e

# solution
exercise_str = "Exercise"
for char in exercise_str:
    print(char)


print("\n")
# 5. String Length
# Create a string variable that holds "Programming is exciting!".
# Print the length of the string.
    # Expected Output:
    # 24

# solution
len_string = "Programming is exciting!"
print(len(len_string))


print("\n")
# 6. Check Substring
# Check if the word "exciting" is in the string "Programming is exciting!".
    # Expected Output:
    # True

# solution
print("exciting" in "Programming is exciting!")


print("\n")
# 7. Slicing Strings
# Slice the string "Hello, Python" to print "Hello", "Python", and "o, Pyt".
    # Expected Output:
    # Hello
    # Python
    # o, Pyt

# solution
hello_string = "Hello, Python"
print(hello_string[:5])
print(hello_string[7:])
print(hello_string[-2:-1])
print(hello_string[7:10])


print("\n")
# 8. String Modifications
# Convert the string "hello WORLD" to uppercase, lowercase, and strip any surrounding whitespaces from the string " hello Python ".
    # Expected Output:
    # HELLO WORLD
    # hello world
    # hello Python

# solution
to_modify_str = "hello WORLD"
to_strip_str = " hello Python "
print(to_modify_str.upper())
print(to_modify_str.lower())
print(to_strip_str.strip())


print("\n")
# 9. Replace and Split
# Replace the word "World" in the string "Hello, World!" with "Python".
# Split the string "Learn to code in Python" into a list of words.
    # Expected Output:
    # Hello, Python!
    # ['Learn', 'to', 'code', 'in', 'Python']

# solution
raw_str = "Hello, World!"
replaced_str = raw_str.replace("World", "Python")
split_str = "Learn to code in Python"
list_str = split_str.split(" ")
print(replaced_str)
print(list_str)


print("\n")
# 10. String Concatenation
# Concatenate the following strings: "Python", "is", "awesome", and "!" into a single string with spaces between each word.
    # Expected Output:
    # Python is awesome !

# solution
print("Python", "is", "awesome", "!")


print("\n")
# 11. String Formatting with f-strings
# Use an f-string to print "My name is John and I am 30 years old."
# Use f-string modifiers to print 45.6789 rounded to 2 decimal places.
    # Expected Output:
    # My name is John and I am 30 years old.
    # 45.68

# solution
name = "John"
age = 30
num_value = 45.6789
print(f"My name is {name} and I am {age} years old.")
print(f"{num_value:.2f}")


print("\n")
# 12. Escape Characters
# Print the following sentence with quotes: "I love programming in Python".
    # Expected Output:
    # "I love programming in Python"

# solution
print("\"I love programming in Python\"")

