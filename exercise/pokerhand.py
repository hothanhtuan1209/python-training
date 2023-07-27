"""
This module contains a code for exercises 18-3 related to:
Think Python, 2nd Edition
Chapter 18: Inheritance

An incomplete implementation of a class that represents a poker hand, and
some code that tests it.
"""

from Card import *

class PokerHand(Hand):
    """
    Represents a poker hand.

    Inherits from the Hand class.
    """

    def suit_hist(self):
        """
        Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """
        Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        """
        Builds a histogram of the ranks that appear in the hand.

        Counts the occurrences of each rank in the hand and stores the result in the attribute 'ranks'.
        """
        
        self.ranks = {}
        
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """
        Checks if the hand has a pair.

        Returns:
            bool: True if the hand contains at least one pair (two cards of the same rank), False otherwise.
        """
        
        self.rank_hist()
        
        for rank, count in self.ranks.items():
            if count > 1:
                return True
        
        return False

    def has_twopair(self):
        """
        Checks if the hand has two pairs.

        Returns:
            bool: True if the hand contains two different pairs of cards with the same rank, False otherwise.
        """
        
        self.rank_hist()
        pair_count = 0
        
        for count in self.ranks.values():
            if pair_count >1:
                return True
            if count > 1:
                pair_count += 1
        
        return False

    def has_three_of_a_kind(self):
        """
        Checks if the hand has three of a kind.

        Returns:
            bool: True if the hand contains three cards of the same rank, False otherwise.
        """
        
        self.suit_hist()
        
        for val in self.suits.values():
            if val == 3:
                return True
        
        return False

    def has_flush(self):
        """
        Returns True if the hand has a flush.
        
        Works correctly for hands with 5 or more cards. @
        """
        
        self.suit_hist()
        
        for val in self.suits.values():
            if val >= 5:
                return True
        
        return False
    
    def has_pair(self):
        """
        Returns True if the hand has a pair. @
        """
        
        self.rank_hist()
        
        for val in self.ranks.values():
            if val == 2:
                return True
        
        return False
    
    def has_two_pairs(self):
        """
        Returns True if the hand has two pairs.
        """
        
        self.rank_hist()
        pairs = 0
        
        for val in self.ranks.values():
            if val == 2:
                pairs +=1

        if pairs >= 2:
            return True
        
        return False
    
    def has_three_of_a_kind(self):
        """
        Returns True if the hand has a three of a kind.
        """
        
        self.rank_hist()
        
        for val in self.ranks.values():
            if val == 3:
                return True
        
        return False
    
    def has_straight(self):
        """
        Returns True if the hand has a straight.
        """
        
        self.rank_hist()
        
        if 1 in self.ranks.keys():
            for i in range(self.ranks[1]):
                self.ranks[14] = self.ranks.get(14, 0) + 1
        
        run = 1
        
        for key in sorted(self.ranks.keys()):
            if key + 1 in self.ranks.keys():
                run += 1
                if run == 5:
                    return True
                
            else:
                run = 1
        return False
    
    def has_full_house(self):
        """
        Checks if the hand has a full house.

        A full house consists of a three of a kind and a pair. There are three possible variations
        in a 7-card hand:
        1) Two sets of three cards and an extra card
        2) One three of a kind and two pairs

        Returns:
            bool: True if the hand contains a full house, False otherwise.
        """      
        
        self.rank_hist()
        triples = 0
        
        for val in self.ranks.values():
            if val == 3:
                triples +=1

        if triples == 2:
            return True

        else:
            return (self.has_pair() and self.has_three_of_a_kind()) or (self.has_two_pairs() and self.has_three_of_a_kind())
    
    def has_four_of_a_kind(self):
        """
        Returns True if the hand has a four of a kind.
        """
        
        self.rank_hist()
        
        for val in self.ranks.values():
            if val == 4:
                return True
        
        return False
         
    def has_straight_flush(self):
        
        """
        Returns True if the hand has a straight flush.
        """

        sfs = [[], [], [], []]

        for c in self.cards:
            sfs[c.suit].append(c.rank)
            
            if c.rank == 1:
                sfs[c.suit].append(14)
                
        for sf in sfs:
            if len(sf) < 5:
                pass
            else:
                run = 1
                sf.sort()
                
                for i in range(len(sf) - 1):
                    if sf[i] + 1 == sf[i + 1]:
                        run += 1
                        if run == 5:
                            return True
                    else:
                        run = 1
        
        return False

def classify(self):
    """
    Determines the poker hand classification of the current hand.

    Returns:
        str: A string representing the poker hand classification.
    """
    
    if self.has_straight_flush():
        return "Straight flush"
    
    elif self.has_four_of_a_kind():
        return "Four of a kind"
    
    elif self.has_full_house():
        return "Full house"
    
    elif self.has_flush():
        return "Flush"
    
    elif self.has_straight():
        return "Straight"
    
    elif self.has_three_of_a_kind():
        return "Three of a kind"
    
    elif self.has_two_pairs():
        return "Two pair"
    
    elif self.has_pair():
        return "Pair"
    
    else:
        return "High card"  

def main():
    deck = Deck()
    deck.shuffle()

    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print (hand)
        print ("Hand has flush"), hand.has_flush()
        print ("Hand has pair"), hand.has_pair()
        print ("Has has at least two pair"), hand.has_twopair()
        print ("Hand has 3 of a kind"), hand.has_three_of_a_kind()

if __name__ == '__main__':
    main()
