# Write a Python program that:

# Declares a list with at least five different data types (e.g., string, integer, float, boolean, list).
# Print the type of each element in the list using the type() function.

data_type_list = [
    "Edmar",
    24,
    101.1,
    True,
    [1, 2, 3]
]

name, age, station, bool_value, num_list = data_type_list

print(type(name))
print(type(age))
print(type(station))
print(type(bool_value))
print(type(num_list))