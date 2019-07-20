import random

def board(b_dic={'1': '1','2': '2','3': '3','4': '4','5': '5','6': '6',
        '7': '7','8': '8','9': '9' }):
    one = b_dic['1']
    two = b_dic['2']
    three = b_dic['3']
    four = b_dic['4']
    five = b_dic['5']
    six = b_dic['6']
    seven = b_dic['7']
    eight = b_dic['8']
    nine = b_dic['9']
    blist = [[f' {seven} |',f'{eight} |',f'{nine} '],['---','---','---'], [f' {four} |',f'{five} |',f'{six} '],
        ['---','---','---'],[f' {one} |',f'{two} |',f'{three} ']]
    for b in blist:
        print(b[0],b[1],b[2])
    print("\n")

def starting_player():
    num = random.randint(0,101)
    global turn
    global player
    if num%2 != 0:
        turn = 1
        print("Heads! Player 1 goes first:")
    else:
        turn = 2
        print("Tails! Player 2 goes first:")

    i = input(f"Player {turn}: do you want to be X or O? \n")
    if i.lower() == 'x':
        if turn == 2:
            player = ['O','X']
    else:
        if turn == 1:
            player = ['O','X']

def change_turn():
    global turn
    if turn == 1:
        turn == 2
    else:
        turn == 1
    move()

def move():
    board(game_board)
    print(f"Player {turn} it's your turn.")
    if turn == 1:
        letter = player[0]
    else: 
        letter = player[1]

    position = input(f"Which box would you like to put an {letter} in?\n")
    '''
    if int(position) in range(0,10):
        result = check_empty(position)
    else:
        print("I'm sorry, that's not a valid #. Please enter a digit between 1 and 9.")
        move()

    if result == False:
        move()
    '''   
    game_board[position] = position
    print(f"\nYou got it, box {position} is now a {letter}")
    #check_full()
    change_turn()

def check_empty(position):
    return game_board[position] == ' '

def check_full():
    for key in game_board:
        if game_board[key] == ' ':
            return False   
    check_winner()

def start():
    global game_board
    global player
    global turn

    game_board = {'1': ' ','2': ' ','3': ' ','4': ' ','5': ' ','6': ' ',
        '7': ' ','8': ' ','9': ' ' }
    player = ['X','O']
    turn = 0    

    print("Welcome to Tic Tac Toe!")
    print("lets flip a coin to see who goes first:\n")
    starting_player()
    ready = input("Are you ready to play? Y or N: \n")
    if ready.lower() == 'n':
        print("Okay, well come back when you are.")
        exit()

    print("Here is the game board: \n")
    board()

    print("Select the number of the space you would like to mark when it's your turn.")
    print("Ok, let's get started.\n")
    move()

def check_winner():
    if player[0] == game_board[5]:
        w = 'Player 1'
    else: 
        w = 'Player 2'

    if player[0] == game_board[1]:
        x = 'Player 1'
    else: 
        x = 'Player 2'

    if player[0] == game_board[9]:
        y = 'Player 1'
    else: 
        y = 'Player 2'

    if game_board[1] == game_board[5] == game_board[9]:
        print(f'congratulaioins {w} you win!! \nWoohoo!!!')   
    elif game_board[3] == game_board[5] == game_board[7]:
        print(f'congratulaioins {w} you win!! \nWoohoo!!!')    
    elif game_board[1] == game_board[2] == game_board[3]:
        print(f'congratulaioins {x} you win!! \nWoohoo!!!')
    elif game_board[4] == game_board[5] == game_board[6]:
        print(f'congratulaioins {w} you win!! \nWoohoo!!!')
    elif game_board[7] == game_board[8] == game_board[9]:
        print(f'congratulaioins {y} you win!! \nWoohoo!!!')
    elif game_board[1] == game_board[4] == game_board[7]:
        print(f'congratulaioins {x} you win!! \nWoohoo!!!')   
    elif game_board[2] == game_board[5] == game_board[8]:
         print(f'congratulaioins {w} you win!! \nWoohoo!!!')   
    elif game_board[3] == game_board[6] == game_board[9]:
        print(f'congratulaioins {z} you win!! \nWoohoo!!!')
    else:
        print("Awe rats! No winner this match. \nBetter luck next time!!")

    i = input("Rematch? Y or N: \n")
    if i.lower() == 'n':
        exit()
    else:
        start()

#if __name__ == "__main__":
start()



