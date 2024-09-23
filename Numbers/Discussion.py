# There are three numeric types in Python
    # int
    # float
    # complex

# Variable of numeric types are created when you assign a value to them.
x = 1 #int
y = 2.5 #float
z = 1j #complex

# Int - int or integer, is a whole number, positive or negative, without decimals, of unlimited length.
a = 1
b = 111111222222
c = -111111

print(type(a))
print(type(b))
print(type(c))

# Float - or floating point number is a number, positive or negative, containing one or more decimals.
d = 1.11
e = 2.22
f = -66.69

print(type(d))
print(type(e))
print(type(f))

# float can also be scientific numbers with an "e" to indicate the power of 10.
g = 35e3
h = 12e4
i = -87.7e100

print(type(g))
print(type(h))
print(type(i))

# Complex - are written with a "j" as the imaginary part.
k = 3+5j
l = 5j
m = -5j

print(type(k))
print(type(l))
print(type(m))

# Type conversion
# You can convert from one type to another with the int(), float(), and complex() methods. 
# Note: You cannot convert complex numbers into another number type.
a1 = float(a)
d1 = int(d)
b1 = complex(b)

print(type(a1))
print(type(d1))
print(type(b1))

# Random number
# Python does not have a "random()" function to make a random number, but Python has a built-in module called "random" that can be used to make random numbers.
import random
print(random.randrange(1, 10))