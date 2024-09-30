# F-Strings
# Allows you to format selected parts of a string.
# To specify a string as an f-string, simply put an "f" in front of the string literal.
template_text = f"Hello world"
print(template_text)

print("\r")
# Placeholders and modifiers
# To format values in an f-string, add placeholders "{}", a placeholder can contain variables, operations, functions, and modifiers to format the value.
year = 5
result = f"He is already working in the industry for {year} years"
print(result)

print("\r")
# A placeholder can also include a modifier to format the value.
# A modifier is included by adding a colon ":" followed by a legal formatting type, like ".2f" which means fixed point number with 2 decimals
text = f"The price of the shoe is {100:.2f} dollars"
print(text)

# Perform Operations in F-string
# You can perform Python operations inside the placeholders.
output = f"The price was {30 * 2:.2f} dollars before"
print(output)

# You can perform "if ...else" statements inside the placeholders.
num = 6
result_num = f"The number is {'even' if num %2 == 0 else 'odd'}"
print(result_num)

print("\r")
# Execute functions in F-strings
# You can execute functions inside the placeholder.
lorem_text = "Lorem ipsum odor amet, consectetuer adipiscing elit."
format_text = f"{lorem_text.title()}"
print(format_text)

fly_result = lambda fly_num: fly_num * 0.3048
fly_test = f"The plane is flying at a {fly_result(30000)} meter altitude"
print(fly_test)

# More modifiers
# There are several other modifiers that can be used to format values.
price = 56000
price_text = f"The price is {price:,} dollars"
print(price_text)

# list of other modifiers
# https://www.w3schools.com/python/python_string_formatting.asp

print("\r")
# String format()
# The "format()" method can still be used, but f-strings are faster and the preferred way to format strings.
# The "format()" method also uses curly brackets as placeholders "{}", but the syntax is slightly different.
gender = "Male"
puppy_gender = "The gender of the puppy is {}".format(gender)
print(puppy_gender)

# Index numbers
# You can use index numbers to be sure the values are placed in the correct placeholders.
apple_q = 10
orange_q = 5
melon_q = 3
fruit_count = "I have {0} Apples, {1} Oranges and {2} Melons".format(apple_q, orange_q, melon_q)
print(fruit_count)

# Named indexes
# You can also use named indexes by entering a name inside the curly brackets, but then you must use the names when you pass the parameter values.
food_order = "I ordered {appetizer}, and {main_course} for dinner"
print(food_order.format(appetizer = "Mushroom soup", main_course = "Garlic chicken"))