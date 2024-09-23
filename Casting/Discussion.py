# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:
    # int() - constructs an integer number from an integer literal, a float literal(by removing all decimals), or a string literal(providing the string represents a whole number)
    # float() - constructs a float number from an integer literal, a float literal or a string literal(providing the string represents a float or an integer)
    # str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals.

x = int(1)
y = int(2.8)
z = int("3")

print(x, y, z)

x_float = float(1)
y_float = float(2.8)
z_float = float("3")

print(x_float, y_float, z_float)

x_str = str(1)
y_str = str(2.8)
z_str = str("3")

print(x_str, y_str, z_str)