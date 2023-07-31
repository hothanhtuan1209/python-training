"""
Create class Person and class Student, class Student inherrits from person class
and adds score attribute, compare scores of 2 students
"""

class Person:
    """
    Represents a person with a name and an age.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.

    Methods:
        __init__(self, name, age): Initializes a Person object with the given name and age.
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

class Student(Person):
    """
    Represents a student, inheriting from the Person class.

    Attributes:
        name (str): The name of the student.
        age (int): The age of the student.
        score (int): The score of the student.

    Methods:
        __init__(self, name, age, score): Initializes a Student object with the given name, age, and score.
        __gt__(self, other): Compares the score of two Student objects.
    """

    def __init__(self, name, age, score):
        """
        Initializes a Student object with the given name, age, and score.

        Parameters:
            name (str): The name of the student.
            age (int): The age of the student.
            score (int): The score of the student.
        """
        
        super().__init__(name, age)
        self.score = score

    def __gt__(self, other):
        """
        Compares the score of two Student objects.

        Parameters:
            other (Student): The other Student object to compare with.

        Returns:
            bool: True if the score of this student is greater than the other student's score, False otherwise.
        """
        
        return self.score > other.score

student_1 = Student('Nam', 6, 7)
student_2 = Student('Hai', 10, 5)

if student_1 > student_2:
    print(student_1.name)
else:
    print(student_2.name)

print(Student.__gt__(student_1, student_2))
