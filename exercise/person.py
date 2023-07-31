"""
Create class person and compare the ages of 2 object
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def age():
    if person_1.age > person_2.age:
        return True
    else:
        return False

person_1 = Person('Hieu', 20)
person_2 = Person('Hien', 30)

print(age())
