# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax:
    # lambda arguments : expression

x = lambda a : a * 2
print(x(6))

print("\r")
# Lambda functions can take any number of arguments.
y = lambda a, b : a + b
print(y(99, 12))

print("\r")
# Why use Lambda functions
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
def my_func(n):
  return lambda a : a * n

my_doubler = my_func(2)
my_tripler = my_func(3)

print(my_doubler(11))
print(my_tripler(11))