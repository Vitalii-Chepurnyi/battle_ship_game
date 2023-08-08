from random import randint

scores = {"computer": 0, "player": 0}

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
    
    def add_ship(self, x, y, type="computer"):
        # Add ships to the board
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"

def letter_to_row_index(letter):
    #Converts a letter (a,b,c ...) to the row index (0,1,2 ...)
    return ord(letter.upper()) - 65

def number_to_column_index(number):
    #Converts a number (0,1,2 ...) to the column index (0,1,2 ...)
    return int(number)
    
def random_point(size):
    # Returns a random point on the board
    return randint(0, size - 1)
    
def populate_board(board):
    # Randomly add ships to the board
    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)
        if (x, y) not in board.ships:
            board.add_ship(x, y)
            
#def play_game():'

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

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

new_game()
