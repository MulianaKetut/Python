def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'


my_generator()

for char in my_generator():
    print(char)


def counter_generator(low, high):
    while low <= high:
        yield low
        # print(low, end=' ')
        low += 1

print('== print next')
objectGen = counter_generator(1,5)
print(next(objectGen))
print(next(objectGen))

print('\n== print for')
for i in counter_generator(5, 10):
    print(i, end=' ')

# tak terhingga
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

x= infinite_sequence()
print(next(x))
#looping terus
# for i in infinite_sequence():
#     print(i, end=" ")


def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

def setName(setName):
    return setName('Alvin')

print('\n==>')
print(greet_bob(say_hello))
print(greet_bob(be_awesome))
print(setName(be_awesome))

print('\n===>')
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()


print('\n==>  Returning Functions From Functions')
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
#hrus pakai tutup kurung/ di bind
print(parent(1))
print(first())

print('\n==> Simple Decorators')
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

@my_decorator
def say_auu():
    print("Whee!")

#ini sama dengan @my_decorator
say_whee = my_decorator(say_whee)
say_whee()

print('\n==> auu')
say_auu()

# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator

print('\n===> Time decorator')
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


print(waste_some_time(1))
print(waste_some_time(999))
