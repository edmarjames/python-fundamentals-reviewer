# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called "json", which can be used to work with JSON data.
import json

# Convert JSON to Python
# If you have a JSON string, you can parse it by using the "json.loads()" method.
import pprint
json_sample = '{ "name":"John", "age":30, "city":"New York"}'

to_dict = json.loads(json_sample)
print(type(to_dict))
pprint.pprint(to_dict)

print("\r")
# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the "json.dumps()" method.
dict_sample = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

to_json = json.dumps(dict_sample)
print(type(to_json))
pprint.pprint(to_json)

# You can convert Python objects of the following types, into JSON strings:
    # dict
    # list
    # tuple
    # string
    # int
    # float
    # True
    # False
    # None

# When you convert from Python to JSON, Python objects are converted into the JSON equivalent.
# dict -> object
# list -> array
# tuple -> array
# str -> string
# int -> number
# float -> number
# True -> true
# False -> false
# None -> null

print("\r")
# Format the result
# The "json.dumps()" method has a parameter to make it easier to read the result.
# Use the "indent" parameter to define the numbers of indents.
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x, indent=5))

print("\r")
# You can also define the separators, default is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values.
print(json.dumps(x, indent=5, separators=("* ", "= ")))

# Order the result
# The "json.dumps()" method has parameter to order the keys in the result.
# Use the "sort_keys" parameter to specify if the result should be sorted or not.
print(json.dumps(x, indent=5, sort_keys=True))