"""
Create class person and compare the ages of 2 object
"""

class Person:
    """
    Represents a person with a name and an age.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.

    Methods:
        __init__(self, name, age): Initializes a Person object with the given name and age.
        __gt__(self, other): Compares the age of two Person objects.
    """

    def __init__(self, name, age):
        """
        Initializes a Person object with the given name and age.

        Parameters:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        
        self.name = name
        self.age = age

    def __gt__(self, other):
        """
        Compares the age of two Person objects.

        Parameters:
            other (Person): The other Person object to compare with.

        Returns:
            bool: True if the age of this person is greater than the other person's age, False otherwise.
        """
        
        return self.age > other.age

person_1 = Person('Hieu', 20)
person_2 = Person('Hien', 30)

if person_1 > person_2:
    print('Person 1')
else:
    print('Person 2')

print(Person.__gt__(person_1, person_2))
