# A date in Python is not a data type of its own, but we can import a module named "datetime" to work with dates as date objects.
import datetime

current = datetime.datetime.now()
print(current)

print("\r")
# The date contains year, month, day, hour, minute, second and microsecond.
# The "datetime" modules has many methods to return information about the date object.
print(current.year)
print(current.month)
print(current.day)
print(current.strftime("%A"))

print("\r")
# Creating Date Objects
# To create a date, we can use the "datetime()" class (constructor) of the "datetime" module.
# The "datetime()" class requires three parameters to create a date: year, month, day.
# The "datetime()" class also takes parameters for time and timezone (hour, minute, second, microsecond, timezone), but they are optional, and has a default of "0", "None" for timezone.
birthday = datetime.datetime(2001, 2, 14)
print(birthday)

print("\r")
# The strftime() method
# The "datetime" object has a method for formatting date objects into readable strings.
# The method is called "strftime()", and takes one parameter, "format", to specify the format of the returned string.
print(birthday.strftime(f'{"%B"} {"%d"} {"%Y"}'))

# A reference of all the legal format codes:
# https://www.w3schools.com/python/python_datetime.asp