class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print (f"{self.name} says woof!")


d1 = Dog("Tommy", "Labrador", 1.5)
d2 = Dog("Rocky", "Beagle", 2.5)

d1.bark()
d2.bark()