class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    # Instance method
    # f for format print
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# object
# set properties di init
miles = Dog('Miles', 4)
buddy = Dog('Buddy', 9)

# panggil atribut/properti
# jika pakai object
print("Name: ", miles.name)
print("Age: ", miles.age)

# jika pakai methos get
print("Name: ", buddy.getName())
print("Age: ", buddy.getAge())

# jika memanggil properti yg didefenisikan
print('species :', buddy.species)

print(miles.description())

print(miles.speak('Auuu'))

# check class
print(type(miles) is Dog)

# check class
print(isinstance(miles, Dog))

