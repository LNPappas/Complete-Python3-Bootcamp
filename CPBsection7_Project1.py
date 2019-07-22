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
        turn = 2
    else:
        turn = 1
    move()

def check_empty(position):
    return game_board[position] == ' '

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

def check_winner(position):
    if turn == 1:
        play = player[0]
    else:
        play = player[1]

    if game_board['1'] == play and game_board['2'] == play and game_board['3'] == play:
        print(f'congratulaioins player {turn}, you win!! \nWoohoo!!!')    
    elif game_board['1'] == play and game_board['4'] == play and game_board['7'] == play:
        print(f'congratulaioins player {turn}, you win!! \nWoohoo!!!')  
    elif game_board['1'] == play and game_board['5'] == play and game_board['9'] == play:
        print(f'congratulaioins player {turn}, you win!! \nWoohoo!!!')
    elif game_board['2'] == play and game_board['5'] == play and game_board['8'] == play:
        print(f'congratulaioins player {turn}, you win!! \nWoohoo!!!')  
    elif game_board['4'] == play and game_board['5']== play  and game_board['6'] == play:
        print(f'congratulaioins player {turn}, you win!! \nWoohoo!!!')  
    elif game_board['3'] == play and game_board['5'] == play and game_board['7'] == play:
        print(f'congratulaioins player {turn}, you win!! \nWoohoo!!!')
    elif game_board['3'] == play and game_board['6'] == play and game_board['9'] == play:
        print(f'congratulaioins player {turn}, you win!! \nWoohoo!!!')
    elif game_board['7'] == play and game_board['8'] == play and game_board['9'] == play:
        print(f'congratulaioins player {turn}, you win!! \nWoohoo!!!')
    else:
        check_full()

    print("\n")
    board(game_board)
    i = input("\nRematch? Y or N: \n")
    if i.lower() == 'n':
        exit()
    else:
        start()

def check_full():
    full = True
    for items in game_board:
        if game_board[items] == ' ':
            full = False
            change_turn()
            move()
    if full == True:
        print("\nAwe rats! No winner this match. \nBetter luck next time!!")

        i = input("Rematch? Y or N: \n")
        if i.lower() == 'n':
            exit()
        else:
            start()

def move():
    board(game_board)
    print(f"Player {turn} it's your turn.")
    if turn == 1:
        letter = player[0]
    else: 
        letter = player[1]

    position = input(f"Which box would you like to put an {letter} in?\n")

    if int(position) in range(0,10):
        result = check_empty(position)
    else:
        print("I'm sorry, that's not a valid #. Please enter a digit between 1 and 9.")
        move()

    if result == False:
        print('Sorry, that box is already full.')
        move()

    game_board[position] = letter
    print(f"\nYou got it, box {position} is now an {letter}\n")
    check_winner(position)


#if __name__ == "__main__":
start()



