# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consists of the methods "__iter__()" and "__next__()".

# Iterator VS Iterable
# lists, tuple, dictionaries and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a "iter()" method which is used to get an iterator.
my_list = ["Apple", "Banana", "Cherry"]
myit = iter(my_list)

print(next(myit))
print(next(myit))
print(next(myit))

print("\r")
# Even strings are iterable objects, and can return an iterator.
my_str = "NPC arc"
str_itr = iter(my_str)
print(next(str_itr))
print(next(str_itr))
print(next(str_itr))
print(next(str_itr))
print(next(str_itr))
print(next(str_itr))
print(next(str_itr))

print("\r")
# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        return x

my_class = MyNumbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print("\r")
# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration

my_class = MyNumbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)