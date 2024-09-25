# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Function is defined using the "def" keyword
def first_function():
    print("NPC Arc")

# To call a function, use the function name followed by parenthesis.
first_function()

print("\n")
# Arguments
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# Arguments are often shortened to args in Python documentations.
def print_name(name):
    print(f"My name is {name}")

print_name("Edmar")
print_name("James")
print_name("Bautista")

print("\n")
# Number of arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def print_full_name(first_name, middle_name, last_name):
    print(f"My name is {first_name} {middle_name} {last_name}")

print_full_name("Edmar James", "Bermejo", "Bautista")

print("\n")
# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a "*" before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly.
# Arbitrary arguments are often shortened to *args in Python documentations.
def my_hobbies(*hobbies):
    print("The following are my hobbies")
    for hobby in hobbies:
        print(hobby)

my_hobbies("Reading", "Cycling", "Motorcycling", "Coding")

print("\n")
# Keyword arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
# The phrase keyword arguments are often shortened to kwargs in Python documentations.
def fav_color(color1, color2, color3):
    print(f"My most favorite color is {color1}")

fav_color(color2 = "Cyan", color1 = "Celeste green", color3 = "Blue green")

print("\n")
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk "**" before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly.
# Arbitrary keyword arguments are often shortened to **kwargs in Python documentations.
def print_details(**detail):
    print(f"My name is {detail['name']}")
    print(f"I am a {detail['occupation']}")

print_details(name = "Edmar", occupation = "Software Engineer")

print("\n")
# Default parameter value
# We can assign a default value to a parameter so that it will be the fallback value if the argument is not provided.
# If we call the function without or missing an argument, it will use the default value.
def print_city(city = "Taguig"):
    print(f"I live in {city}")

print_city("Makati")
print_city()

print("\n")
# Passing a list as an argument
# You can send any data types of argument to a function (string, number, list, dictionary, etc.) and it will be treated as the same dta type inside the function.
def fav_food(foods):
    print("Here are some of my favorite foods")
    for food in foods:
        print(food)

fav_food(["Pares", "Beef Steak", "Beef broccoli", "Lasagna"])

print("\n")
# Return values
# To let a function return a value, use the "return" statement.
def my_age():
    return 26

print(f"My age is {my_age()}")

print("\n")
# The pass statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the "pass" statement to avoid getting an error.
def pass_function():
    pass

print("\n")
# Positional-only arguments
# You can specify that a function can have only positional arguments, or only keyword arguments.
# To specify that a function can have only positional arguments, add ", /" after the arguments.
# Without the ", /" you are actually allowed to use keyword arguments even if the function expects positional arguments.
# But when adding the ", /" you will get an error if you try to send a keyword argument.
def pos_args_function(arg1, /):
    print(arg1)

pos_args_function(1)

print("\n")
# Keyword-only arguments
# To specify that a function can have only keyword arguments, add "*," before the arguments.
# Without the "*," you are allowed to use positional arguments even if the function expects keyword arguments.
# But when adding the "*," you will get an error if you try to send a positional argument.
def keyword_args_function(*, key1):
    print(key1)

keyword_args_function(key1 = 2)

print("\n")
# Combine positional-only and keyword-only
# You can combine the two argument types in the same function.
# Any argument before the ",/" are positional-only and any argument after the "*," are keyword only.
def combi_args_func(a, b, /, *, c, d):
    print(a - b - c - d)

combi_args_func(90, 10, c = 20, d = 30)