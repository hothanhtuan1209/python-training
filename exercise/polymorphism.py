"""
Create class Animal to apply polymorphism
"""

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "make sound"

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")

        self.breed = breed
    
    def make_sound(self):
        return "gau gau!"
    
class Cat(Animal):
    def __init__(self, breed):
        super().__init__("Cat")

        self.breed = breed
    
    def make_sound(self):
        return "meo meo!"
    
dog = Dog("Husky")
print(dog.species,dog.breed, dog.make_sound())
