class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound='Auu'):
        return f"{self.name} says {sound}"


# INHERITANCE
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    # def __init__(self, name, age, color='black'):
    #     super.__init__(name, age)
    #     self.color = color

    # def __str__(self):
    #     return f"{self.name} is {self.age} is {self.color}"
    pass

class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
leo = Dachshund('Leo', 5)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(miles.speak())
print(miles.speak('Grrrr'))

print(buddy.name)
print(buddy.speak())

print(jack)
print(jim.speak("Woof"))

# check inherit
print(isinstance(miles, Dog))
print(miles is Dog)

# tambahan init
print(leo.__str__())
