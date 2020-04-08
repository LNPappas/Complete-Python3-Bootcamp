from Deck import Deck
from random import choice

class Dealer:
    def __init__(self):
        self.deck = Deck()

    def __len__(self):
        return len(self.deck)

    def deal(self):
        c = choice(self.deck)
        self.deck.deal(c)
        return c

if __name__ == "__main__":
    dealer = Dealer()
    print(len(dealer))
    d = dealer.deal()

    print(d)
    print(len(dealer))