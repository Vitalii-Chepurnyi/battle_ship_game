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

def valid_row_input(row_input):
    return row_input.upper() in [chr(65 + i) for i in range(8)]

def valid_column_input(col_input, size):
    return col_input.isdigit() and 0 <= int(col_input) < size
            
def play_game(computer_board, player_board):
    """
    Main game loop where players take turns to make guesses until one of the players
    Wins the game or 20 turn are completed.
    """
    max_turns = 20
    turn = 1
    while turn <= max_turns:
        print("\n" + "=" * 15 + f" Turn {turn}" + "=" * 15)
        print("Computer's Board:")
        computer_board.print()
        print("\nYour Board:")
        player_board.print()

        if turn % 2 == 1:
            print("\nComputer's Turn.")
            x, y = random_point(player_board.size), random_point(player_board.size)
            result = player_board.guess(x,y)
            if result == "Hit":
                scores["computer"] += 1
                print("Computer hit one of your ships!")
            else:
                print("Computer missed your ships.")
        else:
            print(f"\nYour Turn (Turns left: {max_turns - turn + 1})")
            while True:
                x_letter = input("Enter the row letter (A to H):")
                y_number = input("Enter the column number (0 to 7):")

                if not valid_row_input(x_letter) or not valid_column_input(y_number, player_board.size):
                    print("Incorrect input. Please try again!")
                else:
                    break
            
            x = letter_to_row_index(x_letter)
            y = number_to_column_index(y_number)

            result = computer_board.guess(x,y)

            if result == "Hit":
                scores["player"] += 1
                print("Congratulations! You hit the computer's ship!")
            else:
                print("You missed the compute's ships.")

        if scores["computer"] == computer_board.num_ships:
            print("\nComputer wins the game!")
            break
        elif scores["player"] == player_board.num_ships:
            print("\nCongratulations! You Win The Game!")
            break   

def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the
    Scores and initializes the boards.
    """
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
