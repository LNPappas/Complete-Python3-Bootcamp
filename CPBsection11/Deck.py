#Deck Class
from random import randint

class Deck():

    deck = {}
    rank = []
    card = 0
    suit = ''


    def __init__(self):
        self.deck = {'1': 4, '2':4, '3':4, '4':4, '5':4, '6':4, '7':4, '8':4, '9':4, '10':4, '11':4, '12':4, '13':4}
        self.rank = [0, ['clubs','diamonds','spades','hearts'], ['clubs','diamonds','spades','hearts'], ['clubs','diamonds','spades','hearts'],
            ['clubs','diamonds','spades','hearts'],['clubs','diamonds','spades','hearts'],['clubs','diamonds','spades','hearts'],
            ['clubs','diamonds','spades','hearts'],['clubs','diamonds','spades','hearts'],['clubs','diamonds','spades','hearts'],
            ['clubs','diamonds','spades','hearts'],['clubs','diamonds','spades','hearts'],['clubs','diamonds','spades','hearts'],
            ['clubs','diamonds','spades','hearts']]    

    def get_card_number(self):
        while True:
            self.card = str(randint(1,12))
            if self.deck[self.card] > 0:
                self.deck[self.card] = self.deck[self.card] - 1
                break
        self.get_suit()

    def get_suit(self):
        while True:
            num = randint(0,3)
            self.card = int(self.card)
            try:
                self.rank[self.card][num]
            except:
                continue
            else:
                self.suit = self.rank[self.card][num]
                del self.rank[self.card][num]
                break


    def deal(self):
        self.get_card_number()
        return self.card, self.suit

        

            


