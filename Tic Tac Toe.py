# TIC TAC TOE

'''
GAME OVERVIEW ==>

->    Board
->    Display the Board
->    Play Game
->    Handle Turn
->    Check Win
    ->   Check Rows
    ->   Check Columns
    ->   Check Diagonals
->    Check Tie
->    Flip Player
'''



# -----GLOBAL VARIABLES-----

game_still_going = True # Game is still going until someone wins or there is a tie
winner = None # winner
current_player = "X" # who's turn?


# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Function for the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] )
    print(board[3] + "|" + board[4] + "|" + board[5] )
    print(board[6] + "|" + board[7] + "|" + board[8] )


# Start the game
def play_game():

    # Display initial board
    display_board()

    # while the game is still going
    while game_still_going:

        # Handle a turn of 1 player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()
    
    # Game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie")


# Handle a turn of one player
def handle_turn(player):

    # Position Input from user
    print(player + "'s Turn !")
    position = input("Chose a position from 1-9: ")

    valid = False

    # What if user enters Invalid Input like --'123 ', 'abcd ', '!@#$ ', '[:":" ?? ', etc,.
    while not valid:

        # While loop will reun until user enters correct input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input. Chose a position from 1-9: ")
  
        position = int(position) - 1

        # if "-"" is found on board then, X/O can be put
        if board[position] == "-":
            valid = True
        # else X/O can't be put there
        else:
            print("You Can't Go There, Try Again !")

    # Takes the X/O in position after taking input from user
    board[position] = player

    # Display X/O it on the board
    display_board()


# func() for checking if the game has ended
def check_if_game_over():
    check_if_win()
    check_if_tie()


# func() for checking if there is a win
def check_if_win():

    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


# func() For Checking Rows Win
def check_rows():

    # Set GLOBAL VARIABLE (game_still_going) to false
    global game_still_going
    
    # Check if rows are filled and not empty
    row_1 = board[0] == board[1] == board[2] != "-"  # "-" is put here so that
    row_2 = board[3] == board[4] == board[5] != "-"  # row_1 , row_2 , row_3 doesn't
    row_3 = board[6] == board[7] == board[8] != "-"  # think that ' -|-|- ' is a win

    if row_1 or row_2 or row_3:
        game_still_going = False

    # return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


# func() For Checking Columns Win
def check_columns():
    
    # Set GLOBAL VARIABLE (game_still_going) to false
    global game_still_going
    
    # Check if column are filled and not empty
    column_1 = board[0] == board[3] == board[6] != "-"  # "-" is put here so that
    column_2 = board[1] == board[4] == board[7] != "-"  # column_1 , column_2 , column_3 doesn't
    column_3 = board[2] == board[5] == board[8] != "-"  # think that ' -|-|- ' is a win

    if column_1 or column_2 or column_3:
        game_still_going = False

    # return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


# func() For Checking Diagonals Win
def check_diagonals():
        
    # Set GLOBAL VARIABLE (game_still_going) to false
    global game_still_going
    
    # Check if diagonal are filled and not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"  # "-" is put here so that
    diagonal_2 = board[2] == board[4] == board[6] != "-"  # diagonal_1 , diagonal_2 doesn't
                                                          # think that ' -|-|- ' is a win

    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    

    return

# func() For Checking If There Is a Tie
def check_if_tie():

    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


# func() For Fliping The Player
def flip_player():

    global current_player

    # If Current Player was X, the O and Vice-Versa
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

# Calling play_game To Start The Game
play_game()
