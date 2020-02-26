# A study in the special (magic) Methods in python.
# special methods are methods called by the interpreter
# special methods allow compatable with Python Data Model (or object model)
# data model formalizes interfaces of build blocks of the language (iterators, func, classes...)
# The Python data model is like Python as a framework

import collections
from random import choice

# named tuples are used to build classes of objects that are 
# bundles of attribites without custom methods, like a database record

# use namedtuple to represent cards in a deck 
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    '''
        Deck of cards
        Special Methods: __len__, __getitem__
    '''
    # all card values 2-10 & JQKA
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    # four suits
    suits = 'spades diamonds clubs hearts'.split()

    # create dictionary for spades_high function
    # orders suits from highest to lowest
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    # the double underscore before cards is used to avoid name clashes with names 
    # defined by subclasses
    def __init__(self):
        self.__cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]

    def spades_high(self, card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(FrenchDeck.suit_values) + FrenchDeck.suit_values[card.suit]

if __name__ == "__main__":

    # use __init__ to build a deck
    deck = FrenchDeck()

    # use special method __getitem__ to get card in deck by index
    print('deck[7]: ', deck[7])

    # use special method __len__ to get length of deck
    print('deck length: ', len(deck))

    # use of special methods allows for compatiability with Python data model.
    # example: use choice method from random class on deck
    print("\nThree random cards:")
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))

    # __getitem__ method automaitcally supports slicing. 
    print('\ndeck[:3]: ', deck[:3])

    # __getitem__ allows for iteration.
    print("\niterate deck[:6]: ")
    for c in deck[:6]:
        print(c)

    # __getitem__ allows for reverse iteration.
    print("\nreverse iterate deck[:6]: ")
    for c in reversed(deck[:6]):
        print(c)

    # if no __contains__ method the in operator does a sequential scan
    # works with FrenchDeck() because it is iterable.

    print("\nCard('Q', 'hearts') in deck:")
    print(Card('Q', 'hearts') in deck)

    # spades_high method allows us to use sorted method
    print("\nValue of items lowest to highest")
    for c in sorted(deck, key=deck.spades_high):
        print(c)