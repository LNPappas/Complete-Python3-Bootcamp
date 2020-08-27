import collections

# practice with collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    rank = [str(n) for n in range(1,11)] + list('JQKA')
    suit = "Spades Diamonds Hearts Club".split()
    value = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self.__cards = [Card(r, s) for r in self.rank for s in self.suit]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]

    def __val__(self, card):
        rValue = self.rank.index(card.rank)
        return rValue*len(self.value) + self.value(card.suit)

    def deal(self, card):
        self.__cards.remove(card)