#import specific with as
from person import name as pName
from person import devices as pDevice

#import specific
#name ini akan di override
# oleh variabel name yang ada dikelas ini
from person import name, devices
from car import brands

#import all
import person;

#import package
import pkg.mod1
from pkg import mod2

name = 'Ade'
devices = ['laptop', 'smartphone', 'tablet']

def display(arg):
    print(f'arg = {arg}')

display(name)
display(devices)
display(devices[1])

display(pName)
display(pDevice)

#memakai nilai dari variabel lokal pada class ini
display(name)

#jika tidak ada varianel name yang sama
display(brands)

display(person.name)
display(person.devices)

#display package
display(pkg.mod1.kitchen_sets)
display(mod2.artist_kits)


