class Bet():


    money = 0.00


    def __init__(self):
        self.wager = 0.00


    def add(self):
        try:
            i = input("How much would you like to add?\n")
            i = float(i)
            self.money = self.money + i
            return self.money
        except:
            print("Sorry, could you please enter the amount in numerical form?")
            self.add()

    
    def loose(self):
        self.money = self.money - self.wager


    def check_funds(self):
        if self.money < self.wager:
            print("\nI'm sorry, you don't have enough money in your account to make that bet.")
            i = input("Would you like to add funds? y or n:\n").lower()
            if i == 'y':
                m = self.add()
                self.make_bet()
            if i == 'n':
                x = input("Not a big spender I see.\nOkay, would you like to make a smaller bet? y or n:\n").lower()
                if x == 'y':
                    self.make_bet()
                if x == 'n':
                    print("Ok, well come back when you're ready to play.")
                    self.wager = 0.00
                else:
                    self.make_bet()
            else:
                self.check_funds()


    
    def make_bet(self):
        try:
            self.total()
            i = input("How much would you like to bet?\n")
            i = float(i)
            self.wager = i
            self.check_funds()
            self.get_wager()
        except:
            print("Sorry, could you please enter the amount in numerical form?\n")
            self.make_bet()


    def total(self):
        print(f"\nYou account total is currently ${self.money}\n")

    
    def get_wager(self):
        print(f'\nYou have bet ${self.wager} on this game.\n')


    def win(self):
        self.money = self.money + self.wager
                
