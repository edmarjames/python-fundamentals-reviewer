# A variable is only available from inside the region it is created. This is called "scope"

# Local scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def test_func():
    x = "Hello"
    print(x)

test_func()
# print(x) -> this will raise an error since x is not defined outside the function.

print("\r")
# Function inside function
# As explained in the example above, the variable "X" is not available outside the function. But it is available for any function inside the function.
def dummy_func():
    x = 1
    def test_func():
        print(x)
    test_func()

dummy_func()

print("\r")
# Global scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
a = "NPC arc"

def npc_func():
    print(">> Print inside a function")
    print(a)

npc_func()
print(">> Print outside a function")
print(a)

print("\r")
# Naming variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables. One available in the global scope and one available in the local scope.
npc = "NPC arc"

def npc_arc_func():
    npc = "NPC arc"
    print(npc)

npc_arc_func()
print(npc)

print("\r")
# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the "global" keyword.
# The "global" keyword makes the variable global.
def my_test_func():
    global test_var
    test_var = 99
    print(test_var)

my_test_func()
print(test_var)

print("\r")
# Nonlocal keyword
# The "nonlocal" keyword is used to work with variables inside nested functions.
# The "nonlocal" keyword makes the variable belong to the outer function.
def outer_func():
    x = "Outer"
    y = "Function"
    def inner_func():
        nonlocal x
        x = "Inner"
    inner_func()
    return x + " " + y

print(outer_func())