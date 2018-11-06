
class Board():

    def __init__(self):
        self.board = [ \
            [(0,0), (1, 0), (2, 0)], \
            [(0,1), (1, 1), (2, 1)], \
            [(0,2), (1, 2), (2, 2)] \
            ]
        self.length = 3
        self.height = 3

    def printprettyboard(self):
        for i in range(self.height):
            print (self.board[i])

    def is_spot_available(self,location_tuple):
        tupleavailable = False
        for i in range(self.height):
            for j in range(self.length):
                if self.board[i][j] == location_tuple:
                    tupleavailable = True
        return tupleavailable

    def add_play(self,letter,location):
        for i in range(self.length):
            for j in range(self.height):
                if self.board[i][j] == location:
                    self.board[i][j] = letter


class Player():

    def __init__ (self,name,letter):
        self.name = name
        self.letter = letter

    def choose_location(self):
        self.location = input('{}, choose your coordinates in format "#,#": '.format(self.name))   ##NEED TO DEFINE PLAYER
        return self.location


class Game():

    def __init__(self, name1 = "Player 1", name2 = "Player2"):
        self.player1 = Player(name1,"  X  ")
        self.player2 = Player(name2,"  O  ")


    def convert_to_list(self,locationraw):
        location_list = locationraw.split(',')
        for i in range(len(location_list)):
            location_list[i] = location_list[i].strip()
        return location_list

    def is_valid_int_input(self,locationraw):
        list_loc = self.convert_to_list(locationraw)
        is_valid = True
        if len(list_loc) != 2:
            is_valid = False
        elif not list_loc[0].isdigit():
            is_valid = False
        elif not list_loc[1].isdigit():
            is_valid = False
        return is_valid

    def list_to_int_tuple(self,locationraw):
        location_list = self.convert_to_list(locationraw)
        newtuple = (int(location_list[0]), int(location_list[1]))
        return newtuple


    def check_for_winner(self,player,board):
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

    def playttt(self):
        gameboard = Board()
        gameboard.printprettyboard()
        iswinner = False
        i = 0
        while i < 9:
            if i % 2 == 0:
                player = self.player1
            else:
                player = self.player2
            location = player.choose_location()
            if location == "":
                print("you quit!")
                i += 100
                break
            elif self.is_valid_int_input(location) == False:
                print("Location not valid. Try again.")
            elif gameboard.is_spot_available(self.list_to_int_tuple(location)) == False:
                print("Location not available. Try again")
            elif gameboard.is_spot_available(self.list_to_int_tuple(location)):
                gameboard.add_play(player.letter,self.list_to_int_tuple(location))
                i += 1
                if self.check_for_winner(player.letter,gameboard.board):
                    print ("{} wins!".format(player.name))
                    iswinner = True
                    i += 100
            gameboard.printprettyboard()
        if iswinner == False:
            print("Tie!")



game = Game()
game.playttt()


#breaks when no numbers in tuples
#doesnt work with ending with quits!
