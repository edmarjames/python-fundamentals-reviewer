# Exercise 1: Polymorphic Employee System
# Create a base class `Employee` with a `work()` method that prints "Working...". Then, create three derived classes: `Manager`, `Designer`, and `Developer`. Each class should override the `work()` method to print job-specific tasks.
# **Input**: Create instances of `Manager`, `Designer`, and `Developer` and call their `work()` method.
# **Expected Output**:
# Managing team
# Designing interfaces
# Writing code


# Exercise 2: Polymorphism with Animal Sounds
# Create a base class `Animal` with a method `make_sound()` that returns "Some sound". Then create child classes `Dog`, `Cat`, and `Cow` that override the `make_sound()` method with their specific sounds: "Bark", "Meow", and "Moo" respectively.
# **Input**: Create a list of animal objects and loop through them, calling `make_sound()` on each.
# **Expected Output**:
# Bark
# Meow
# Moo


### Exercise 3: Vehicle Polymorphism
# Create a base class `Vehicle` with a method `start_engine()` that prints "Engine started". Create child classes `Car`, `Truck`, and `Motorcycle`, each overriding `start_engine()` to print a different engine sound.
# **Input**: Create a list of vehicles (`Car`, `Truck`, `Motorcycle`) and call the `start_engine()` method for each.
# **Expected Output**:
# Car engine roars
# Truck engine rumbles
# Motorcycle engine revs


### Exercise 4: Dynamic Method Binding
# Create a base class `Shape` with a method `area()` that raises a `NotImplementedError`. Create subclasses `Circle` and `Square` that override `area()` to compute the area based on their dimensions. Use polymorphism to call the `area()` method dynamically on different objects.
# **Input**: Create instances of `Circle` (radius 3) and `Square` (side 4). Use a loop to call `area()` on both.
# **Expected Output**:
# Circle area: 28.27
# Square area: 16


### Exercise 5: Operator Overloading
# Create a class `Box` that overloads the `+` operator to combine the volumes of two box objects. Each `Box` object should have a length, width, and height. Use polymorphism by defining a custom `__add__()` method.
# **Input**: Create two `Box` objects with dimensions `(2, 3, 4)` and `(1, 1, 1)` and add them together.
# **Expected Output**:
# Combined volume: 25


### Exercise 6: E-commerce Polymorphism
# Create a base class `PaymentMethod` with a method `pay()` that prints "Processing payment". Create child classes `CreditCard`, `PayPal`, and `BankTransfer`, each overriding the `pay()` method to process payments differently.
# **Input**: Call the `pay()` method for each payment method.
# **Expected Output**:
# Processing payment via Credit Card
# Processing payment via PayPal
# Processing payment via Bank Transfer