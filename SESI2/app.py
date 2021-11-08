# contoh
print('Conditions, Control Flow')
print('\n===Contoh-1===')
x = 0
y = 5

if x < y:                            # Truthy
    print('yes x < y')

if y < x:                            # Falsy
    print('yes y < x')

if x:                                # Falsy
    print('yes x')

if y:                                # Truthy
    print('yes y')

if 'aul' in 'grault':                # Truthy
    print('yes aul in grault')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes quux in array')


# contoh-2
print('\n===Contoh-2===')
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')

print('After conditional')

# contoh-3
print('\n===Contoh-3===')
# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:  # x
    print('Outer condition is true')  # x

    if 10 > 20:  # x
        print('Inner condition 1')  # x

    print('Between inner conditions')  # x

    if 10 < 20:  # x
        print('Inner condition 2')  # x

    print('End of outer condition')  # x
print('After outer condition')  # x

# contoh-4
print('\n===Contoh-4===')
x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

print('==>')
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

print('==>')
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")

# contoh-5
print('\n===Contoh-5===')
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")

print('==>')
name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

print('==>')
if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")

# contoh-5
print('\n===Contoh-5===')
if 'f' in 'foo':
    print('1')
    print('2')
    print('3')
print('==>')
if 'z' in 'foo':
    print('1')
    print('2')
    print('3')
print('==>')
x = 2

if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')
print('==>')
x = 3

if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')
print('==>')
x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')

# contoh-6
print('\n===Contoh-6===')
raining = False
print("Let's go to the", 'beach' if not raining else 'library')
print('==>')
raining = True
print("Let's go to the", 'beach' if not raining else 'library')
print('==>')
age = 12
s = 'age is teen' if age < 21 else 'age is adult'
print(s)
print('==>')
print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')

# contoh-7
print('\n===Contoh-7===')
if True:
    pass
print('foo')
