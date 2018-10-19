def add_letter(letter,board,location):
    newboard = board
    for i in range(len(board)):
        for int in range(len(board[i])):
            if board[i][int] == location:
                newboard[i][int] = letter
    return newboard
    '''
    letter = X or O
    board = list of lists
    location = tuple
    '''

def tuple_available(board,location):
    tupleavailable = False
    for i in range(len(board)):
        for int in range(len(board[i])):
            if board[i][int] == location:
                tupleavailable = True
    return tupleavailable


def tupleit(locationupto9):
    nums = []
    for item in locationupto9:
        if item.isdigit():
            nums.append(item)
    return (int(nums[0]),int(nums[1]))
    '''
    this won't work for any matrix where digits are greater than 9
    '''

def printprettyboard(board):
    for i in range(len(board)):
        print (board[i])


def check_for_winner(player,board):
    winner = False
    for i in range(len(board)):
        winninglist = [player, player,player]
        if winninglist == board[i]:
            winner = True
            break
    if winner == False:
        if board[0][0] == board[1][0] == board[2][0] == player:
            winner = True
        if board[0][1] == board[1][1] == board[2][1] == player:
            winner = True
        if board[0][2] == board[1][2] == board[2][2] == player:
            winner = True
        if board[0][0] == board[1][1] == board[2][2] == player:
            winner = True
        if board[0][2] == board[1][1] == board[2][0] == player:
            winner = True
    return winner


def play_ttt():
    board = [ \
            [(0,0), (1, 0), (2, 0)], \
            [(0,1), (1, 1), (2, 1)], \
            [(0,2), (1, 2), (2, 2)] \
            ]
    printprettyboard(board)
    iswinner = False
    inplay = True
    while inplay == True:
        for i in range(9):
            if i % 2 == 0:
                player = '  X  '
            else:
                player = '  O  '
            location = input('Player {}, choose your coordinates: '.format(player))
            if location == "":
                print("you quit!")
                inplay = False
                iswinner = "other"
                break
            elif len(location) < 5:
                break  #THIS SHOULD BE DIFFERENT! BC IF LENGTH LSSS THAN 5, should go back to input, not break whole for loop
            elif location[0] != "(" or location[2] != "," or location[4] != ")":
                 break
            location = tupleit(location)
            if tuple_available(board,location):
                    board = add_letter(player,board,location)
                    inplay = False
                    if check_for_winner(player,board):
                        print ("Player {} wins!".format(player))
                        printprettyboard(board)
                        iswinner = True
                        break
            else:
                print("Slot not available! Try again.")
            printprettyboard(board)
    if iswinner == False:
        print("Tie!")

play_ttt()
#breaks when no numbers in tuples
#doesnt work with ending with quits!
