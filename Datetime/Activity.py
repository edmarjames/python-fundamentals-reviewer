# **Exercise 1: Current Date and Time**
# Create a program that:
# 1. Gets the current date and time using the `datetime` module.
# 2. Prints the current date and time in the format `YYYY-MM-DD HH:MM:SS`.
    # **Expected Output**:
    # 2024-09-27 14:30:45

# solution
from datetime import date, datetime
current = datetime.now()
format_current = current.strftime("%Y-%m-%d %H:%M:%S")
print(format_current)


print("\r")
# **Exercise 2: Extracting Date Components**
# Write a script that:
# 1. Gets the current date and time.
# 2. Extracts and prints the following:
# Current year
# Current month (as a number)
# Current day of the week (as a full name, e.g., Monday)
    # **Expected Output**:
    # Year: 2024
    # Month: 9
    # Day: Friday

# solution
year = current.year
month = current.month
day = current.strftime("%A")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")


print("\r")
# **Exercise 3: Creating a Date Object**
# Create a date object for an important event (e.g., your birthday, a memorable day) using the `datetime()` class. Print this date.
    # **Expected Output**:
    # 2001-02-14 00:00:00

# solution
new_date = datetime(2001, 2, 14)
print(new_date)


print("\r")
# **Exercise 4: Date Formatting with strftime()**
# Given a date object (e.g., `datetime(2023, 12, 25)`), format it into a readable string: `December 25, 2023`. Use `strftime()` with the appropriate format codes.
    # **Expected Output**:
    # December 25, 2023

# solution
date_to_format = datetime(2023, 12, 25)
format_date = date_to_format.strftime("%B %d, %Y")
print(format_date)


print("\r")
# **Exercise 5: Countdown to New Year's**
# Write a script that calculates how many days are left until New Year's Day (January 1st of the next year). Use the current date to compute the difference.
    # **Expected Output**:
    # Days until New Year: 96

# solution
new_year_date = date(2025, 1, 1)
current_date = date.today()
current_date = datetime.today().strftime("%Y-%m-%d")
current_date = current_date.split("-")
current_date = date(int(current_date[0]), int(current_date[1]), int(current_date[2]))
days_left = (new_year_date - current_date).days
print(f"Days until New Year: {days_left}")
# alternative solution
# new_year_date = date(2025, 1, 1)
# current_date = date.today()
# days_left = (new_year_date - current_date).days
# print(f"Days until New Year: {days_left}")


print("\r")
# **Exercise 6: Time Difference Calculator**
# Create two date objects representing two important events (e.g., today and an upcoming event). Calculate and print the number of days between the two events.
    # **Expected Output**:
    # Days until event: 30

# solution
event = "Christmas Day"
upcoming_event = date(2024, 12, 25)
current_date = datetime.today().strftime("%Y-%m-%d")
current_date = current_date.split("-")
current_date = date(int(current_date[0]), int(current_date[1]), int(current_date[2]))
days_left = (upcoming_event - current_date).days
print(f"Days until {event}: {days_left}")
# alternative solution
# current_date = date.today()
# days_left = (new_year_date - current_date).days


print("\r")
# **Exercise 7: Custom Date with Time**
# Create a date and time object representing a specific moment, e.g., `2023-11-05 13:45:30`. Print it in the following format: `Sunday, 5th November 2023, 1:45 PM`.
    # **Expected Output**:
    # Sunday, 5th November 2023, 1:45 PM

# solution
custom_datetime = datetime(2023, 11, 5, 13, 45, 30)
format_date = custom_datetime.strftime("%A, %d %B %Y, %I %M %p")
print(format_date)