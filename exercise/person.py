"""
Create class person and compare the ages of 2 object
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

person_1 = Person('Hieu', 20)
person_2 = Person('Hien', 30)

if person_1 > person_2:
    print('Person 1')
else:
    print('Person 2')

print(Person.__gt__(person_1, person_2))
