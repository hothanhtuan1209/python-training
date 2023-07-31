"""
Create class House and two attribute address, street
"""
class House:
    """
    Represents a house with an address and a street name.

    Attributes:
        address (int): The house number.
        street (str): The name of the street where the house is located.

    Methods:
        __init__(self, address, street): Initializes a House object with the given address and street.
    """

    def __init__(self, address, street):
        """
        Initializes a House object with the given address and street.

        Parameters:
            address (int): The house number.
            street (str): The name of the street where the house is located.
        """
        
        self.address = address
        self.street = street

house_1 = House(55, 'Nui Thanh')
house_2 = House(56, 'Nui Thanh')
