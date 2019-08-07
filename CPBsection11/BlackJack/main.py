from player import Player

if __name__ == "__main__":

    while True:

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
        elif player.hand.total == 21:
            print("\nBLACK JACK!! YOU WIN!!!!")
        else:
            while dealer.hand.total <= player.hand.total:
                dealer.hit()
            if dealer.hand.total <= 21:
                print("\nLooks like the dealer wins this round. Better luck next time!!!")
            else:
                print("\nThe dealer busted! YOU WIN!!!")

        print("\nFINAL RESULTS:")
        player.get_hand()
        dealer.get_hand()

        replay = input("\n Would you like to play again? y or n:\n").lower()
        if replay == 'y':
            player.hand.deck.shuffle()
        else:
            break
            
