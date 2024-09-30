# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating and deleting files.

# The key function for working with files in Python is the "open()" function.
# The "open()" function takes two parameters; filename and mode.
# There are four different methods (modes) for opening a file.
    # "r" - Read -> Default value. opens a file for reading, error if the file does not exist.
    # "a" - Append -> opens a file for appending, creates the file if it does not exist.
    # "w" - Write -> opens a file for writing, creates the file if it does not exist.
    # "x" - Create -> creates the specified file, returns an error if the file exist.

# In addition you can specify if the file should be handled as binary or text mode.
    # "t" - Text -> Default value. Text mode
    # "b" - Binary -> Binary mode (e.g. images)

file = open("demo.txt")
file.close()

# File open
# To open a file, use the built-in "open()" function.
# The "open()" function returns a file object, which has a "read()" method for reading the content of the file.
file = open("demo.txt")
print(file.read())

# If the file is located in a different location, you will have to specify the file path.
# file = open("/Desktop/git/python-fundamentals-reviewer/Json/users.json")

print("\r")
# Read only parts of the file
# By default the "read()" method returns the whole text, but you can also specify how many characters you want to return.
print("Reading per character")
file = open("demo.txt")
print(file.read(10))

print("\r")
# Read lines
# You can return one line by using the "readline()" method.
file = open("demo.txt")
print("Reading per line")
print(file.readline())

# By calling "readline()" two times, you can read the two first lines.
print("Reading per line")
print(file.readline())
print(file.readline())

print("\r")
# By looping through the lines of the file, you can read the whole file, line by line.
file = open("demo.txt")
print("Reading by looping")
for line in file:
    print(line)

# Close files
# It is a good practice to always close the file when you are done with it.
file.close()

# File write
# To write to an existing file, you must add a parameter to the "open()" function.
    # "a" - Append - will append to the end of the file
    # "w" - Write - will overwrite any existing content

# Append a new line
append_file = open("demo.txt", "a")
append_file.write("\rMore content")
append_file.close()

file = open("demo.txt")
print(file.read())
file.close()

print("\r")
# Overwrite the content
write_file = open("demo.txt", "w")
write_file.write("The whole content is now overwritten")
write_file.close()

file = open("demo.txt")
print(file.read())
file.close()

# Create a new file
# To create a new file in Python, use the "open()" method, with one of the following parameters.
    # "x" - Create -> will create a file, returns an error if the file exist
    # "a" - Append -> will create a file if the specified file does not exist
    # "w" - Write -> Will create a file if the specified file does not exist

new_file = open("demo_new.txt", "w")
new_file.write("New file, new content!")
new_file.close()

new_file = open("demo_new.txt")
print(new_file.read())
new_file.close()

# Delete file
# To delete a file, you must import the OS module, and run its "os.remove()" function.
import os
new_file = open("demo_new_new.txt", "w")
new_file.write("New file, new content!")
new_file.close()

# Check if file exist
# To avoid getting an error, you might want to check if the file exists before you try to delete it.
if os.path.exists("demo_new_new.txt"):
    print("Deleting file")
    os.remove("demo_new_new.txt")
else:
    print("The file does not exist")

# Delete folder
# To delete an entire folder, use the "os.rmdir()" method
# You can only remove empty folders
# os.rmdir("sample_folder")