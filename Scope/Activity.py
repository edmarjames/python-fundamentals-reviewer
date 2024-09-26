# Exercise 1: Local and Global Scope Interaction
# Create a function `calculate_total()` that multiplies two numbers, `a` and `b`, defined inside the function. Use a global variable `multiplier` and multiply the result of `a * b` by `multiplier` before returning it.
# **Input**: Set `multiplier = 2` globally, then call `calculate_total()`.
# **Expected Output**: 
# The result is: 20


# Exercise 2: Nested Function and Variable Shadowing
# Create a function `outer()` that defines a local variable `x = 5`. Inside it, define a nested function `inner()` that redefines `x` as `x = 10`. Call `inner()` and print the value of `x` both before and after calling `inner()` from within `outer()`.
# **Input**: Call `outer()`.
# **Expected Output**: 
# x before inner(): 5
# x after inner(): 10


# Exercise 3: Global Keyword Usage
# Create a function `set_value()` that uses the `global` keyword to set a global variable `counter`. The function should increase `counter` by 1 each time it is called. After calling the function three times, print the value of `counter`.
# **Input**: Call `set_value()` three times.
# **Expected Output**:
# 3


# Exercise 4: Nonlocal Keyword in Nested Functions
# Create an outer function `outer_func()` that initializes a variable `count = 0`. Inside it, define a nested function `increase_count()` that uses the `nonlocal` keyword to modify `count`. The `increase_count()` function should increase `count` by 1 each time it is called. Return the final value of `count` after calling `increase_count()` three times from within `outer_func()`.
# **Input**: Call `outer_func()`.
# **Expected Output**:
# 3


# Exercise 5: Multiple Scopes and Keyword Behavior
# Create a function `change_global()` that contains a local variable `a = 5`. Inside it, use a nested function `inner()` to declare `a` as global and set it to `10`. Call `inner()` and print the value of `a` both within the function and after calling it globally.
# **Input**: Call `change_global()` and then print `a` globally.
# **Expected Output**:
# Inside function: 10
# Outside function: 10


# Exercise 6: Function Inside Function with Independent Scope
# Create a function `greet_person()` that takes a person's name as an argument. Inside it, define another function `display_message()` that returns a greeting message using the person's name. Return the result of `display_message()` from `greet_person()`.
# **Input**: Call `greet_person("Edmar")`.
# **Expected Output**:
# Hello Edmar!


### Exercise 7: Experimenting with Nonlocal and Global Keywords
# Create two functions: `outer_function()` and `inner_function()`. `outer_function()` should define a local variable `value = 10`, and `inner_function()` should use both `nonlocal` and `global` keywords to modify `value` and a global variable `global_value`. Call `inner_function()` inside `outer_function()` and print both variables inside and outside the functions.
# **Input**: Call `outer_function()` and print `global_value`.
# **Expected Output**:
# Inside inner_function: 20
# Global value: 30