import sys

# read aja
try:
    f = open("Hack8_Sample_Text.txt", encoding='utf-8')
    print(f.read())
    # perform file operations
finally:
    f.close()

# w = write
with open("sample.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")


try:
    f = open("sample.txt", 'r', encoding='utf-8')
    print(f.read())
finally:
    f.close()

try:
    f = open("sample.txt", 'r', encoding='utf-8')
    print(f.readline())
finally:
    f.close()


# error exception
print('=== Error Exception ===')

# custom exception


def os_interaction():
    print('win' in sys.platform)
    assert (
        'win' in sys.platform), "This code runs on Windows only. Custom exception line 38"
    assert ('linux' in sys.platform), "Function can only run on Linux systems. Custom exception line 38"
    assert ('windows' in sys.platform), "This code runs on Windows only. Custom exception line 38"
    print('Doing something.')


try:
    os_interaction()
except:
    print('ini error')
    print('Windows function was not executed')

print('===>')
try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('The os_interaction() function was not executed')

print('\n== File nor found! ===')
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

# gabungan
try:
    os_interaction()
    with open('file.log') as file:
        read_data = file.read()
        print(read_data)
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('os_interaction() function was not executed')


# gabungan complite
# Have a look at the following example:
print('\n=== Error Exception And Open File ===')
try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    finally:
        file.close()
finally:
    print('Cleaning up, irrespective of any exceptions.')


print('\n=== Test ===')

def checkCoins(coins):
    assert(coins == 12), "some coins fell down on the way"

coins = 10
try:
    checkCoins(coins)
    #if true
    print(coins)
except AssertionError as error:
    print(error)
