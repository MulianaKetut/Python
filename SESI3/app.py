# Example of Function Creation
print('===Contoh-1===')


def my_function(p, l):
    '''Function to calculate area of a square'''
    print("p * l = ", p * l)


p = 3
l = 4
my_function(p, l)

print('\n===Contoh-2===')


def printme(str_input):
    '''This prints a passed string into this function'''
    print(str_input)


# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")
printme(190)


# function definition here
print('\n===Contoh-3===')


def changeMe(myList):
    '''This changes a passed list into this function'''
    myList = myList+[1, 2, 3, 4]
    return myList


# Now you can call changeMe function
myList = [10, 20, 30]
print("Values outside the function - before : ", myList)
myList = changeMe(myList)
print("Values outside the function - after  : ", myList)

print('\n===Contoh-4===')


def savePersonalInfo(name, age):
    print('name', name)
    print('age', age)


# parameter diperhatikan harus sesuai urutan
# karena bisa masuk ke field mana saja
savePersonalInfo('Ketut', 22)
# atau bisa seperti ini
savePersonalInfo(age=17, name='Lucy')

print('\n===Contoh-5===')
# Function definition is here


def printme(str_input):
    '''This prints a passed string into this function'''
    print(str_input)


# Now you can call printme function
printme("Hello")

# # This syntax will give you an error
# printme()

print('\n===Contoh-6===')
# Function definition is here


def calculate_rect(length, width):
    '''This function is used to calculate area of rectangle'''
    print('Area : ', length*width)


# Define parameters
length = 100
width = 20

# Call calculate_rect
calculate_rect(length, width)

# # This syntax will give you an error
# calculate_rect(length)

print('\n===Contoh-7===')
# Function definition is here
# non-default (tidak ada nilai awal harus lebih dulu)


def printinfo(name, age=26):
    '''This prints a passed info into this function'''
    print("Name : ", name)
    print("Age  : ", age)
    print("")


# Now you can call printinfo function
printinfo(age=50, name="hacktiv8")
printinfo(name="hacktiv")


print('\n===Contoh-8===')
# Function definition is here
# bintang satu * itu tuple


def printinfo(arg1, *vartuple):
    # def printinfo(arg1, arg2, arg3, arg4):
    '''This prints a variable passed arguments'''
    print('arg1     : ', arg1)
    print('vartuple : ', vartuple)
    print(type(vartuple))
    print('')

    for var in vartuple:
        print('isi vartuple : ', var)


# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50, "a")


print('\n===Contoh-9===')
# Create a function with nonkeyword variables
# ** => untuk menampung dictionary (dict)
def person_car(total_data, **kwargs):
    '''Create a function to print who owns what car'''
    print('Total Data : ', total_data)
    for key, value in kwargs.items():
        print('Person : ', key)
        print('Car    : ', value)
        print(type(kwargs))
        print('')


person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)

# Parameters (jimmy='chevrolet', frank='ford', tina='honda') will be equal to
# kwargs = {
#     'jimmy': 'chevrolet',
#     'frank': 'ford',
#     'tina': 'honda'
# }


print('\n===Contoh-10===')
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))


print('\n===Contoh-11===')
# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total

# Now you can call sum function
total = sum(10, 20)
print("Result function : ", total)


print('\n===Contoh-12===')
# Declare a global variable
total = 0

# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)

# Call a function
sum( 10, 20 )
print("Outside the function global total : ", total)


print('\n===Contoh-13===')
# Declare a global variable
total = 0

# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
   return total

# Call a function
print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)


print('\n===Contoh-14===')
# Example of docstring in a function

def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''

  num3 = num1 + num2
  return num3

  # Syntax to get explanation/docstring from a particular module/function/class

print(sum_number.__doc__)