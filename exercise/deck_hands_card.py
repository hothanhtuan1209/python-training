"""
This module contains a code for exercises 18-2 related to:
Think Python, 2nd Edition
Chapter 18: Inheritance

Takes two parameters: the number of hands and the number of cards per hand,
create the appropriate number of Hand objects, deal the appropriate number 
of cards per hand, and return a list of Hands.
"""

import random

class Card:
    """
    Represents a playing card.
    """

    def __init__(self, rank, suit):
        """
        Initializes a Card object with the given rank and suit.

        Parameters:
            rank (str): The rank of the card.
            suit (str): The suit of the card.
        """
        
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """
        Returns a string representation of the Card object.

        Returns:
            str: A formatted string representing the card.
        """
        
        return f"{self.rank} of {self.suit}"

class Deck:
    """
    Represents a deck of playing cards.

    Attributes:
        cards (list): A list of Card objects representing the deck.

    Methods:
        __init__: Initializes a Deck object with a standard deck of 52 cards.
        shuffle: Shuffles the deck randomly.
        deal_hands: Deals hands of playing cards from the deck.

    """

    def __init__(self):
        """
        Initializes a Deck object with a standard deck of 52 cards.
        """
        
        ranks = [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
            
        self.shuffle()

    def shuffle(self):
        """
        Shuffles the deck randomly.
        """
        
        random.shuffle(self.cards)

    def deal_hands(self, num_hands, cards_per_hand):
        """
        Deals hands of playing cards from the deck.

        Parameters:
            num_hands (int): The number of hands to be dealt.
            cards_per_hand (int): The number of cards per hand.

        Returns:
            list: A list of Hand objects, each representing a hand of playing cards.
        """
        
        hands = []
                    
        for i in range(num_hands):
            hand_cards = []
                        
            for j in range(cards_per_hand):
                if self.cards:
                    hand_cards.append(self.cards.pop())
                else:
                    break
                        
            hands.append(Hand(hand_cards))
                    
        return hands

class Hand:
    """
    Represents a hand of playing cards.

    Attributes:
        cards (list): A list of Card objects representing the hand.

    Methods:
        __init__: Initializes a Hand object with the given cards.
        __str__: Returns a string representation of the Hand object.
    """

    def __init__(self, cards=[]):
        """
        Initializes a Hand object with the given cards.

        Parameters:
            cards (list): A list of Card objects representing the hand.
        """
        
        self.cards = cards

    def __str__(self):
        """
        Returns a string representation of the Hand object.

        Returns:
            str: A formatted string representing the hand.
        """
        
        hand_str = "\n".join(str(card) for card in self.cards)
        
        return f"--------\n{hand_str}\n"

def main():
    deck = Deck()
    num_hands = 10
    cards_per_hand = 2
    hands = deck.deal_hands(num_hands, cards_per_hand)

    for i, hand in enumerate(hands, 1):
        print(f"Hand {i}\n{hand}")

if __name__ == "__main__":
    main()
