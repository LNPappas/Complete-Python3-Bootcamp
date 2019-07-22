import random

def set_turn():
    global turn
    turn = random.randint(1,2)
    print(f"It has been randomly decided that it is Player {turn}'s turn.")

def change_turn():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1

def use_turn():
    global turn
    print(f"It is player {turn}'s turn.")
    change_turn()

turn = 0
set_turn()
use_turn()
use_turn()
use_turn()