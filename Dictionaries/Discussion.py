# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.
data_dict = {
    "name": "Edmar",
    "age": 26,
    "occupation": "Software Engineer"
}
print(data_dict)
print("\r")

# Ordered, when we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Changeable means that we can change, add or remove items after the dictionary has been created.
# Duplicates not allowed, means that it cannot have two items with the same key.

# Dictionary items are presented in key:value paris, and can be referred to by using the key name.
print(data_dict["name"])
print("\r")

# To determine how many items a dictionary has, use the "len()" function.
print(len(data_dict))
print("\r")

# It is also possible to use the "dict()" constructor to make a dictionary.
new_data_dict = dict(name = "Jane", age = 20, last_name = "Doe")
print(new_data_dict)
print("\r")

# Accessing items
# You can access the items of a dictionary by referring to its key name, inside square brackets.
print(new_data_dict["age"])

# There is also a method called "get()" that will give you the same result.
age = new_data_dict.get("age", 0)
print(age)
print("\r")

# Get keys
# the "keys()" method will return a list of all keys in the dictionary.
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
all_keys = new_data_dict.keys()
print(all_keys)
print("\r")

# Get values
# the "values()" method will return a list of all the values in the dictionary.
# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
all_values = new_data_dict.values()
print(all_values)
print("\r")

# Get items
# the "items()" method will return each item in a dictionary, as tuples in a list
# The returned list is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
all_items = new_data_dict.items()
print(all_items)
print("\r")

# To determine is a specified key is present in a dictionary use the "in" keyword.
print("age" in new_data_dict)
print("\r")

# Change values
# You can change the value of a specific item by referring to its key name.
new_data_dict["age"] = 21
print(new_data_dict)
print("\r")

# The "update()" method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
new_data_dict.update({"name": "James"})
print(new_data_dict)
print("\r")

# Adding items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it.
new_data_dict["occupation"] = "Scrum Master"
print(new_data_dict)
print("\r")

# The "update()" method will update the dictionary with the items from the given argument. If the item does not exist, the item will be added.
new_data_dict.update({"gender": "Male"})
print(new_data_dict)
print("\r")

# Removing items
# There are several methods to remove items from a dictionary.

# The "pop()" method removes the item with the specified key name.
new_data_dict.pop("occupation")
print(new_data_dict)
print("\r")

# The "popitem()" method removes the last inserted item
new_data_dict.popitem()
print(new_data_dict)
print("\r")

# The "del" keyword removes the item with the specified key name.
del new_data_dict["age"]
print(new_data_dict)
print("\r")

# The "del" keyword can also delete the dictionary completely.
# del new_data_dict
print(new_data_dict) # this will raise an error because new_data_dict no longer exists
print("\r")

# The "clear()" method empties the dictionary.
new_data_dict.clear()
print(new_data_dict)
print("\r")

# Loop through a dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are method to return the values as well.
pokemon_dict = {
    "Pikachu": "Yellow",
    "Bulbasaur": "Green",
    "Charmander": "Orange",
    "Squirtle": "Blue"
}
for pokemon in pokemon_dict:
    print(pokemon)
print("\r")

# You can also use the "values()" method to return values of a dictionary.
for pokemon in pokemon_dict.values():
    print(pokemon)
print("\r")

# You can use the "keys()" method to return the keys of a dictionary.
for pokemon in pokemon_dict.keys():
    print(pokemon)
print("\r")

# Loop through both keys and values, by using the "items()" method.
for pokemon in pokemon_dict.items():
    print(pokemon)
print("\r")

# Copy a dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because dict2 will only be reference to dict1, and change made in dict1 will automatically also be made in dict2.
# One way is to use the built-in Dictionary method "copy()".
pokemon_dict_copy = pokemon_dict.copy()
pokemon_dict_copy["Gengar"] = "Violet"
print(pokemon_dict)
print(pokemon_dict_copy)
print("\r")

# Another way to make a copy is to use the built-in function "dict()".
pokemon_dict_copy_dict = dict(pokemon_dict)
pokemon_dict_copy_dict["Rayquaza"] = "Green"
print(pokemon_dict)
print(pokemon_dict_copy_dict)
print("\r")

# Nested dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Access items in nested dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary.
print(my_family["child1"]["name"])
print(my_family["child2"]["name"])
print("\r")

# Loop through nested dictionaries.
# You can loop through a dictionary by using the "items()" method like this.
for child, value in my_family.items():
    print(child)
    for details in value:
        print(f"{details}: {value[details]}")