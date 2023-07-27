"""
This module contains a code for exercises 18-3 related to:
Think Python, 2nd Edition
Chapter 18: Inheritance

A complete version of the Card, Deck and Hand classes in this chapter.
"""


import random

class Card(object):
    """Represents a standard playing card.

    Attributes:
      suit (int): An integer representing the suit of the card (0-3).
      rank (int): An integer representing the rank of the card (1-13).
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Returns a human-readable string representation of the card
        """
        
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        """
        Compares this card to other, first by suit, then rank.

        Returns:
            bool: True if this card is less than other card; False otherwise.
        """
        
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        else:
            return self.rank < other.rank

    def __eq__(self, other):
        """
        Checks if this card is equal to other card.

        Returns:
            bool: True if this card is equal to other card; False otherwise.
        """
        
        return self.suit == other.suit and self.rank == other.rank

class Deck(object):
    """
    Represents a deck of cards.

    Attributes:
        cards (list): List of Card objects representing the deck.
    """

    def __init__(self):
        self.cards = []
        
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns a string representation of the deck."""
        res = [str(card) for card in self.cards]
        
        return '\n'.join(res)

    def add_card(self, card):
        """
        Adds a card to the deck.

        Parameter:
            card (Card): The Card object to be added to the deck.
        """
        
        self.cards.append(card)

    def remove_card(self, card):
        """
        Removes a card from the deck.

        Parameter:
            card (Card): The Card object to be removed from the deck.
        """
        
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """
        Removes and returns a card from the deck.

        Parameter:
            i (int): The index of the card to pop (default is -1, the last card).

        Returns:
            Card: The popped Card object.
        """
        
        return self.cards.pop(i)

    def shuffle(self):
        """
        Shuffles the cards in this deck.
        """
        
        random.shuffle(self.cards)

    def sort(self):
        """
        Sorts the cards in ascending order.
        """
        
        self.cards.sort()

    def move_cards(self, hand, num):
        """
        Moves the given number of cards from the deck into the Hand.

        Parameters:
            hand (Hand): The destination Hand object.
            num (int): The number of cards to move.
        """
        
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """
    Represents a hand of playing cards.
    """

    def __init__(self, label=''):
        self.cards = []
        self.label = label

def find_defining_class(obj, method_name):
    """
    Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    Parameters:
        obj (object): Any python object.
        method_name (str): The method name as a string.

    Returns:
        class: The class object that provides the method definition,
               or None if not found.
    """
    
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    
    return None

def main():
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 5)
    hand.sort()
    print(hand)

if __name__ == '__main__':
    main()
