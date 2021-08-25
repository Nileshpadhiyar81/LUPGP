#______________STEP 1___________________
# Write a function that can print out a board.
# Set your board as a list,
# where each index 1-9 corresponds with a number on a number pad
# You get a 3 by 3 board representation.

# from IPython.display import clear_output
def display_board(board):
    # clear_output()
    print('-----------')
    print('    |   |')
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('    |   |')
    print('-----------')
    print('    |   |')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('    |   |')
    print('-----------')
    print('    |   |')
    print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('    |   |')
    print('-----------')

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)






#______________STEP 2___________________
# Write a function that can take in a player input & assign thier marker as 'X' or 'O'.
# player1 = input("Please pick a marker 'X' or 'O' ")
# player2 = int(input("Please enter a number"))
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1 : Do you want to be X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
# player_input()






#______________STEP 3___________________
# Write a function that takes in the board list object , a marker ('X' or 'O'), DESIRED NUMBER (1-9)
def place_marker(board, marker, position):
    board[position] = marker
# place_marker(test_board, '$', 8)
# display_board(test_board)





#______________STEP 4___________________
# Write a function takes in a board & check to see if someone has wons ?
def check_wineer(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
# check_wineer(test_board,'X')

#______________STEP 5___________________
# write a function that uses the random module to randomly decied which player goes first ?
# You may want to lookup random.randint() return a string of which player went first ?
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'



#______________STEP 6___________________
# Write a function that returns a boolean indicating whether a space on the board is freely available ?

def space_check(board, position):
    return board[position] == ' '






#______________STEP 7___________________
# step:7 : Write a function that check if the board is full & return a boolean value . True is full, otherwise False
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True






#______________STEP 8___________________
# Step 8: Write a function that asks for a player's next position (as a number 1-9)
# And then uses the function from step 6 to check if its a free position.
# If it is, then return the position for later use.
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choice your next position (1-9)'))
    return position



#______________STEP 9___________________
# Write a function that asks the player if they want to play again and return a boolean.
# if they want to play again and return a boolean True if they do want to play again..
def replay():
    print("do you want to play again yes or no")
    a = input().lower().startswith('y')
    if a:
        print("okay we go again")
        return True
    else:
        print("Thanks")
        return False



#______________STEP 10___________________
# Here Use the while loops & the functions you've made to run the game

print('Welcome to Tic Tac Toe')
start=True
while start:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()

    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if check_wineer(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player1 You have won the game !')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw !')
                    break

                else:
                    turn = 'Player 2'
        if turn == 'Player 2':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if check_wineer(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player2 You have won the game !')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw !')
                    break

                else:
                    turn = 'Player 1'
    if replay():
        start = True
    else:
        start = False






