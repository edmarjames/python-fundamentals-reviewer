# Strings in python are surrounded by either single or double quotation marks.

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string.
print("It's gonna be fine")
print("He is called 'Mang Kanor'")
print("\r")

# You can assign a multiline string to a variable by using three quotes.
long_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(long_string)
print("\r")

# or three single quotes
long_string2 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(long_string2)
print("\r")

# Strings are arrays, like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
print(long_string[0])
print("\r")

# Looping through a string
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for char in "Edmar":
    print(char)
print("\r")

# String length, to get the length of a string, use the "len()" function.
print(len(long_string))
print("\r")

# Check string
# To check if a certain phrase or character is present in a string, we can use the keyword "in".
print("Lorem" in long_string)
print("\r")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword "not in".
print("Lorem" not in long_string)
print("\r")

# Slicing
# You can return a range of character by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
print(long_string[1:10])
print("\r")

# Slice from the start by leaving out the start index, the range will start at the first character.
print(long_string[:15])
print("\r")

# Slice to the end by leaving out the end index, the range will go to the end.
print(long_string[69:])
print("\r")

# Negative indexing uses negative indexes to start the slice from the end of the string.
hello_string = "Hello World!"
print(hello_string[-5:-1])
print("\r")

# Modify strings
# Python has a set of built-in methods that you can use on strings.

# Upper Case - "upper()" method returns the string in upper case.
print(hello_string.upper())
print("\r")

# Lower Case - "lower()" method returns the string in lower case.
print(hello_string.lower())
print("\r")

# Remove whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The "strip()" method removes any whitespace from the beginning or the end.
hello_string_whitespace = "    Hello, World Again!    "
print(hello_string_whitespace.strip())
print("\r")

# Replace string
# The "replace()" method replaces a string with another string.
print(hello_string_whitespace.strip().replace("Again", "Eeyy"))
print("\r")

# Split string
# The "split()" method returns a list where the text between the specified separator becomes the list items.
# The "split()" method splits the string into substrings if it finds instances of the separator.
print(long_string.split(" "))
print("\r")

# String concatenation
# To concatenate, or combine, two strings you can use the "+" operator.
first_str = "NPC"
second_str = "Arc"
third_str = "Starts"
fourth_str = "Now"
final_str = first_str + " " + second_str + " " + third_str + " " + fourth_str
print(final_str)
print("\r")

# String format
# We can combine strings and numbers by using "f-strings" or the "format()" method!

# F-strings
# F-string was introduced in Python 3.6, and is now the preferred way of formatting strings. To specify a string as an F-string, simply put an "f" in front of the string literal, and add curly brackets "{}" as placeholders for variables and other operations.
age = 26
name = "Edmar"
print(f"My name is {name}, I am {age} years old")
print("\r")

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like ".2f" which means fixed point number with 2 decimals.
amount = 100
print(f"His allowance for today is {amount:.2f}")

# A placeholder can contain Python code, like math operations.
print(f"For tomorrow it will be {amount * 2} since he will be commute a lot")
print("\r")

# Escape characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash "\" followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes.
text = "They want to be called as \"Batang Quiapo\" since they are a known notorious group in that place"
print(text)