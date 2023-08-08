from random import randint

class Board:
    """
    Main Board. Sets parameters for board type(player of computer)
    Has methods for adding ships and guesses and printing board.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print():
        # Prints column numbers
        print("  " + " ".join(str(i) for i in range(self.size)))

        for i, row in enumerate(self.board):
            # Prints row letter
            print(chr(65 + i) + "  " + " ".join(row))

    def guess():
        # Guesses if you hit or miss the ship
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"
    
    def add_ship():

def play_game():'

def new_game():
    size = 8
    num_ships = 8
    print("=" * 35)
    print("HARD CORE BATTLESHIPS!!")
    print(f"Board Size: {size}. Number of Ships: {num_ships}")
    print("Top Left corner is row: 0, column: 0")
    print("LET'S SEE HOW GOOD YOU ARE?!")
    print("=" * 35)
    player_name = input("Please enter your name:\n")
    print("=" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

new_game()
