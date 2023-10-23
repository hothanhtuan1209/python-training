"""
This module contains a code for exercises 17-1 related to:
Think Python, 2nd Edition
Chapter 17: Classes and Methods

- An __init__ method that initializes an attribute named pouch_contents to an
empty list.
- A method named put_in_pouch that takes an object of any type and adds it to
pouch_contents.
- A __str__ method that returns a string representation of the Kangaroo object
and the contents of the pouch.
"""


class Kangaroo:
    """
    Represents a Kangaroo with a pouch to hold items.

    Attributes:
        pouch_contents (list): A list to hold items in the kangaroo's pouch.
    """

    def __init__(self):
        """
        Initializes a new Kangaroo object with an empty pouch.
        """

        self.pouch_contents = []

    def put_in_pouch(self, item):
        """
        Adds the given item to the pouch_contents list.

        Parameter:
            item: Any object to be added to the kangaroo's pouch.
        """

        self.pouch_contents.append(item)

    def __str__(self):
        """
        Returns a string representation of the Kangaroo object and its pouch
        contents.

        Returns:
            str: A formatted string showing the pouch_contents list.
        """

        return f"Kangaroo object with pouch contents: {self.pouch_contents}"


def main():
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch("apple")
    kanga.put_in_pouch("banana")
    roo.put_in_pouch("joey")

    print(kanga)


if __name__ == "__main__":
    main()
