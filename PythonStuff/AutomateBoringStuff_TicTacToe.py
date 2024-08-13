# #############################################
# TIC-TAC-TOE game
# #############################################

# Data structures
# ###############

# 1. the game board
theBoard_dict = {
                 'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                 'low-L': ' ', 'low-M': ' ', 'low-R': ' '
                 }

# 2. the players
Player_tuple = ( 'X','O',)

# 3. the winning conditions
WinningConditions_tuple = (
                            ('top-L','top-M','top-R',),
                            ('mid-L','mid-M','mid-R',),
                            ('low-L','low-M','low-R',),
                            ('top-L','mid-L','low-L',),
                            ('top-M','mid-M','low-M',),
                            ('top-R','mid-R','low-R',),
                            ('top-L','mid-M','low-R',),
                            ('top-R','mid-M','low-L',),
                          )




# Functions
# #########

# 1. Display the current game board
def show_board(board):
    print (board['top-L'],'|',board['top-M'],'|',board['top-R'])
    print('- + - + -')
    print (board['mid-L'],'|',board['mid-M'],'|',board['mid-R'])
    print('- + - + -')
    print (board['low-L'],'|',board['low-M'],'|',board['low-R'])

# 2. Check winning conditions
def check_winningconditions(board,player):
    for conditions in WinningConditions_tuple:
        key1,key2,key3 = conditions
        if (board[key1] == board[key2] == board[key3] == player):
            return True
    return False


        





# Main program
# ############

show_board(theBoard_dict)

for possible_turns in range(len(theBoard_dict)):
    Turn = Player_tuple[(possible_turns%2)]
    print('Turn is for player ', Turn)
    while True:
        BoardField = input('Which field do you want to move on? : ')
        if theBoard_dict[BoardField] == ' ':
            theBoard_dict[BoardField] = Turn
            break
        else:
            print('That field is already taken. Pick another one.')
    show_board(theBoard_dict)
    if check_winningconditions(theBoard_dict,Turn):
        print('Excellent!', Turn , 'won this game!')
        break

