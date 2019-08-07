from player import Player
from bet import Bet

if __name__ == "__main__":

    bet = Bet()

    while True:

        bet.make_bet()
        if bet.wager == 0:
            i = input("\n Would you still like to play? y or n:\n").lower()
            if i == 'y':
                bet.make_bet()
            else:
                exit()
        
        player = Player('Player')
        dealer = Player('Dealer')

        for i in range(0,2):
            player.deal()
            dealer.deal()


        if player.hand.total < 21:
            print("\nThe Dealer's current total is:", dealer.hand.total)
            player.hit()

        if player.check_bust == True:
            print("\nSorry, you lost. Better luck next time!")
            bet.loose()
        elif player.hand.total == 21:
            print("\nBLACK JACK!! YOU WIN!!!!")
            bet.win()
        else:
            while dealer.hand.total <= player.hand.total:
                dealer.hit()
            if dealer.hand.total <= 21:
                print("\nLooks like the dealer wins this round. Better luck next time!!!")
                bet.loose()
            else:
                print("\nThe dealer busted! YOU WIN!!!")
                bet.win()

        print("\nFINAL RESULTS:")
        player.get_hand()
        dealer.get_hand()
        bet.get_wager()
        bet.total()

        replay = input("\n Would you like to play again? y or n:\n").lower()
        if replay == 'y':
            player.hand.deck.shuffle()
        else:
            break
            
