# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# To create a module just save the code you want in a file with the extension ".py"
# We can use the module we just created by using the "import" statement.
# note: when using a function from a module, use the syntax "module_name.function_name"
import module

test_func = module.print_func()
print(test_func)

print("\r")
# Variables in module
# The module can contain function, as already described, but also variables of all types (arrays, dictionaries, objects, etc).
long_string = module.long_string
print(long_string)

print("\r")
# You can name the module file whatever you like, but it must have the file extension ".py".
# You can create an alias when you import a module, by using the "as" keyword.
import alias_module as mod
import pprint

people_dict = mod.people
pprint.pprint(people_dict)

print("\r")
# Using the dir() function
# There is a built-in function to list all the function names in a module. The "dir()" function.
all_content = dir(mod)
print(all_content)

print("\r")
# Import from module
# You can choose to import only parts from a module, by using the "from" keyword.
# note: When importing using the "from" keyword, do not use the module name when referring to elements in the module. Example "nested_dict" not "alias_module.nested_dict"
from alias_module import nested_dict

pprint.pprint(nested_dict)