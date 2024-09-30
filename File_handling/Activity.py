# Exercise 1: Reading from a File
# You are given a text file called **"example.txt"** with the following content:
# Python is a great programming language.
# It is widely used in web development, data science, and automation.
# Write a Python program that reads the file and prints its content to the console.

    # **Expected Output**:
    # Python is a great programming language.
    # It is widely used in web development, data science, and automation.

# solution
example_file = open("example.txt")
print(example_file.read())
example_file.close()
# Alternative solution
# "with" statement will automatically close the file even if an exception occurs
# with open("example.txt") as example_file:
#     print(example_file.read())


print("\r")
# Exercise 2: Reading Specific Characters
# Using the same file **"example.txt"**, write a Python program that reads and prints only the first 20 characters of the file.

    # #### **Expected Output**:
    # Python is a great pro

# solution
example_file = open("example.txt")
print(example_file.read(20))
example_file.close()


print("\r")
# Exercise 3: Reading Line by Line
# Write a Python program that reads **"example.txt"** line by line and prints each line.

    # #### **Expected Output**:
    # Python is a great programming language.
    # It is widely used in web development, data science, and automation.

# solution
example_file = open("example.txt")
for line in example_file:
    print(line.strip())
example_file.close()


print("\r")
# Exercise 4: Appending to a File
# You are given an existing text file called **"notes.txt"**. Write a Python program to append the line **"Learning file handling in Python."** to the end of the file. After appending, read and print the entire content of the file.

    # #### **Expected Output**:
    # (assuming the initial content of **"notes.txt"** is)
    # Today I learned about lists.

    # Output after appending:
    # Today I learned about lists.
    # Learning file handling in Python.

# solution
notes_file = open("notes.txt", "a")
notes_file.write("\rLearning file handling in Python.")
notes_file.close()

notes_file = open("notes.txt")
print(notes_file.read())
notes_file.close()


print("\r")
# Exercise 5: Overwriting a File
# Write a Python program that opens **"notes.txt"** and overwrites its content with **"All previous content has been erased."** Then, read and print the file content after the overwrite.

    # #### **Expected Output**:
    # All previous content has been erased.

# solution
notes_file = open("notes.txt", "w")
notes_file.write("All previous content has been erased.")
notes_file.close()

notes_file = open("notes.txt")
print(notes_file.read())
notes_file.close()


print("\r")
# Exercise 6: Creating a New File
# Write a Python program that creates a new file called **"my_diary.txt"** and writes the following text into it:
# Today I started learning about file handling in Python.
# Then, read and print the content of **"my_diary.txt"**.

    # #### **Expected Output**:
    # Today I started learning about file handling in Python.

# solution
diary_file = open("my_diary.txt", "w")
diary_file.write("Today I started learning about file handling in Python.")
diary_file.close()

diary_file = open("my_diary.txt")
print(diary_file.read())
diary_file.close()


print("\r")
# Exercise 7: Checking if a File Exists
# Write a Python program that checks if the file **"my_diary.txt"** exists. If it does, print **"File exists"**. If it doesn't, print **"File does not exist"**.

    # #### **Expected Output**:
    # File exists

# solution
import os
if os.path.exists("my_diary.txt"):
    print("File exists")
else:
    print("File does not exist")


print("\r")
# Exercise 8: Deleting a File
# Write a Python program that deletes the file **"my_diary.txt"**. Before deleting, make sure to check if the file exists. If it exists, delete it and print **"File deleted successfully"**. If it doesn’t exist, print **"File does not exist"**.

    # #### **Expected Output**:
    # File deleted successfully

# solution
if os.path.exists("my_diary.txt"):
    os.remove("my_diary.txt")
    print("File deleted successfully")
else:
    print("File does not exist")


print("\r")
# Exercise 9: Deleting a Folder
# Write a Python program that creates a folder called **"temp_folder"**. Then, write code to delete this folder if it is empty. Print **"Folder deleted"** if the folder was successfully deleted, otherwise print **"Folder is not empty"**.

# solution
os.makedirs("temp_folder")
if os.path.exists("temp_folder") and len(os.listdir("temp_folder")) == 0:
    os.rmdir("temp_folder")
    print("Folder deleted")
else:
    print("Folder is not empty")