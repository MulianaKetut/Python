# -*- coding: utf-8 -*-
"""Python_Adv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19kK4s3RD2kF9I8K6rdg6F1WB0KZgiK9V

# Advanced Python

## Using Generators

Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.
"""

def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'

my_generator()

"""In the above example we create a simple generator using the yield statements. We can use it in a for loop just like we use any other iterators."""

for char in my_generator():
  print(char)

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(5,10):
  print(i, end=' ')

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
  print(i, end=" ")

"""Understanding Generators
So far, you’ve learned about the two primary ways of creating generators: by using generator functions and generator expressions. You might even have an intuitive understanding of how generators work. Let’s take a moment to make that knowledge a little more explicit.

Generator functions look and act just like regular functions, but with one defining characteristic. Generator functions use the Python yield keyword instead of return. Recall the generator function you wrote earlier:

```py
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

This looks like a typical function definition, except for the Python yield statement and the code that follows it. yield indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.

Instead, the state of the function is remembered. That way, when next() is called on a generator object (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again. Since generator functions look like other functions and act very similarly to them, you can assume that generator expressions are very similar to other comprehensions available in Python.

**Functions**

Before you can understand decorators, you must first understand how functions work. For our purposes, a function returns a value based on the given arguments. Here is a very simple example:

```py
>>> def add_one(number):
...     return number + 1

>>> add_one(2)
3
```

## First-Class Objects

In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on). Consider the following three functions:
"""

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

"""Here, say_hello() and be_awesome() are regular functions that expect a name given as a string. The greet_bob() function however, expects a function as its argument. We can, for instance, pass it the say_hello() or the be_awesome() function:"""

greet_bob(say_hello)

greet_bob(be_awesome)

"""## Inner Functions

It’s possible to define functions inside other functions. Such functions are called inner functions. Here’s an example of a function with two inner functions:
"""

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()

"""## Returning Functions From Functions

Python also allows you to use functions as return values. The following example returns one of the inner functions from the outer parent() function:


"""

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

"""Note that you are returning first_child without the parentheses. Recall that this means that you are returning a reference to the function first_child. In contrast first_child() with parentheses refers to the result of evaluating the function. This can be seen in the following example:"""

first = parent(1)
first()

"""## Simple Decorators

Now that you’ve seen that functions are just like any other object in Python, you’re ready to move on and see the magical beast that is the Python decorator. Let’s start with an example:
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

say_whee()

"""However, wrapper() has a reference to the original say_whee() as func, and calls that function between the two calls to print().

Put simply: decorators wrap a function, modifying its behavior.

The way you decorated say_whee() above is a little clunky. First of all, you end up typing the name say_whee three times. In addition, the decoration gets a bit hidden away below the definition of the function.

Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax. The following example does the exact same thing as the first decorator example:
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

"""So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a decorator to a function.

## More Example
"""

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

"""This formula is a good boilerplate template for building more complex decorators."""

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)

waste_some_time(999)