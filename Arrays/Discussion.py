# Python does not have a built-in support for Arrays, but Python Lists can be used instead.
# Arrays are used to store multiples values in one single variable.
cars = ["Honda", "Toyota", "Hyundai", "Suzuki"]

# Access the elements of an Array
# You refer to an array element by referring to the index number.
print(cars[0])

print("\r")
# The length of an Array
# Use the "len()" method to return the length of an array.
# The length of an array is always one more than the highest array index.
print(len(cars))

print("\r")
# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
for car in cars:
    print(car)

print("\r")
# Adding Array elements
# You can use the "append()" method to add an element to an array.
cars.append("MG")
print(cars)

print("\r")
# Removing Array elements
# You can use the "pop()" method to remove an element from the array.
cars.pop(-1)
print(cars)

# You can also use the "remove()" method to remove an element from the array.
# note: the "remove()" method only removes the first occurrence of the specified value.
cars.remove("Suzuki")
print(cars)