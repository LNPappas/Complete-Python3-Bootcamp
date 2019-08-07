from deck import Deck

class Card():


    def __init__(self):
        self.deck = Deck()
        self.hand = []
        self.full_hand= []
        self.total = 0
        self.c = ' '


    def get_card(self):
        card, suit = self.deck.deal()
        self.add(card, suit)


    def add(self, card, suit):
        if card == 11:
            self.hand.append(card)
            card = 'Ace'
        elif card == 12:
            self.hand.append(10)
            card = 'Jack'
        elif card == 13:
            self.hand.append(10)
            card = 'Queen'
        elif card == 14:
            self.hand.append(10)
            card = 'King'
        else:
            self.hand.append(card)
        self.c = str(card) + ' of ' + suit
        self.full_hand.append(self.c)
        self.sum()
    

    def sum(self):
        self.total = 0
        for c in range(0, len(self.hand)): 
            self.total = self.total + self.hand[c]
        self.check_bust()


    def check_bust(self): 
        if self.total > 21:
            self.aces()


    def aces(self):
        index = 0
        for index, num  in enumerate(self.hand):
            if num == 11:
                self.hand[index] = 1
                self.new_sum()

    
    def new_sum(self):
        self.total = 0
        for x in range(0, len(self.hand)): 
            self.total = self.total + self.hand[x]

        



