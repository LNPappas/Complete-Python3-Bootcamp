from card import Card

class Player():


    def __init__(self, name):
        self.hand = Card()
        self.name = name


    def deal(self):
        self.hand.get_card()
        print(f"The {self.name} had been delt the:", self.hand.c)
        if self.hand.total >= 21:
            return 'n'
        else:
            return 'x'


    def get_hand(self):
        print(f"\nThe {self.name}'s hand is:\n", self.hand.full_hand)
        print("for a total of:", self.hand.total, "\n")


    def hit(self):
        self.get_hand()
        if self.name == 'Dealer':
            self.deal()
        else:
            i = input("Would you like to hit? y or n: \n").lower()
            if i == 'y':
                i = self.deal()
                print(i)
                if i == 'n':
                    pass
                else:
                    self.hit()
        
                
    def check_bust(self):
        return self.hand.total > 21

            



