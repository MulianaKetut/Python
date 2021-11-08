# contoh
print('Looping')
print('\n===Contoh-1===')
n = 5
while n > 0:
    n -= 1
    print(n)

print('==>')
i = 1
while i < 6:
    print(i)
    i += 1

# contoh-2
print('\n===Contoh-2===')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break  # Break Statement
    print(n)
print('Loop ended.')
print('==>')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

# contoh-3
print('\n===Contoh-3===')
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

print('==>')
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

# contoh-5
print('\n===Contoh-5===')
print('loop forever')
# while True:
#     print('foo')

# contoh-6
print('\n===Contoh-6===')
age = 20
gender = 'M'
if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')

print('==>')
a = ['foo', 'bar']

while len(a):
    print(a.pop(0))

    b = ['baz', 'qux']

    while len(b):
        print('>', b.pop(0))

# contoh-7
print('\n===Contoh-7===')
n = 5
while n > 0:
    n -= 1
    print(n)

# contoh-8
print('\n===Contoh-8===')
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

print('==>')
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

print('==>')
for k in d:
    print(d[k])

print('==>')
for k in d.values():
    print(k)

print('==>')
for k, v in d.items():
    print(k, ":", v)

# contoh-9
print('\n===Contoh-9===')
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

print('==>')
for k in d:
    print(d[k])

print('==>')
for v in d.values():
    print(v)

# contoh-10
print('\n===Contoh-10===')
for n in (0, 1, 2, 3, 4):
    print(n)

print('==>')
x = range(5)
for n in x:
    print(n)

print('==>')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

print('==>')
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

print('==>')
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') 


# contoh-11
print('\n===Contoh-11===')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

print('==>')
i = 0
while i < 5:
    j = 0
    while j < 3:
        print(i, j)
        j += 1

        if(j == 2):
            continue

        print('----')
    i += 1


# contoh-12
print('\n===Contoh-12===')
x = range(5)
for n in x:
    print(n)
print('==>')
x = range(2,8)
for n in x:
    print(n)
print('==>')
x = range(0, 100, 20)
for n in x:
    print(n)