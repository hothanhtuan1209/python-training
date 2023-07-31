"""
Create class Animal to apply polymorphism
"""

class Animal:
    """
    Represents an animal.

    Attributes:
        species (str): The species of the animal.

    Methods:
        __init__(self, species): Initializes an Animal object with the given species.
        make_sound(self): Returns a string representing the sound the animal makes.
    """

    def __init__(self, species):
        """
        Initializes an Animal object with the given species.

        Parameters:
            species (str): The species of the animal.
        """
        self.species = species

    def make_sound(self):
        """
        Returns a string representing the sound the animal makes.
        """
        
        return "make sound"

class Dog(Animal):
    """
    Represents a dog, a type of animal.

    Attributes:
        breed (str): The breed of the dog.

    Methods:
        __init__(self, breed): Initializes a Dog object with the given breed.
        make_sound(self): Returns a string representing the sound of a dog.
    """

    def __init__(self, breed):
        """
        Initializes a Dog object with the given breed.

        Parameters:
            breed (str): The breed of the dog.
        """
        
        super().__init__("Dog")
        self.breed = breed

    def make_sound(self):
        """
        Returns a string representing the sound of a dog.
        """
        
        return "gau gau!"

class Cat(Animal):
    """
    Represents a cat, a type of animal.

    Attributes:
        breed (str): The breed of the cat.

    Methods:
        __init__(self, breed): Initializes a Cat object with the given breed.
        make_sound(self): Returns a string representing the sound of a cat.
    """

    def __init__(self, breed):
        """
        Initializes a Cat object with the given breed.

        Parameters:
            breed (str): The breed of the cat.
        """
        
        super().__init__("Cat")
        self.breed = breed

    def make_sound(self):
        """
        Returns a string representing the sound of a cat.
        """
        
        return "meo meo!"

dog = Dog("Husky")
print(dog.species, dog.breed, dog.make_sound())
