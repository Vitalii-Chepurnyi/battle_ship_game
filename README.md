# Hardcore Battleships

Embark on an engaging matitime adventure with our meticulously crafted Battleships game.
Sink your adversary's ships while protecting your own in this classic naval battle.
Experience the thrill of outsmatring your opponent with every move, aiming for victory within 20 intense turns.
Immerse yourselft in the battle, strategize wisely, and relish the excitement of being crowned the ultimate sea commander!

Game link here! ===> [HardCore BattleShips!](https://hardcorebattleships-92d1b8be4b51.herokuapp.com/)

![Alt Text](assets/images/responsive%20battle.jpg)

# How to Play

Set Up the Game:

The game is played on a grid board, where each player has their own fleet of ships hidden from their opponent.
The grid is labeled with letters for rows (A to H) and numbers for columns (0 to 7).

Taking Turns:

Players take turns making guesses by selecting a target on their opponent's board.
Guesses are made by entering a row letter (A to H) and a column number (0 to 7).

Guessing and Results:

After making a guess, the result is revealed:
If the guess hits an opponent's ship, the hit is marked with an "*".
If the guess misses all ships, the miss is marked with an "X".

Winning the Game:

The game continues until one of the following conditions is met:
A player sinks all of their opponent's ships first.
Both players have taken a maximum of 20 turns.

Determining the Winner:

If a player sinks all of their opponent's ships, they win the game.
If 20 turns are completed and no player has won, the player with the higher score wins.
Scores are based on the number of hits on the opponent's ships.

Playing Again:

After the game ends, players can reset the boards and start a new game.
The excitement of each game lies in the strategic choices and the thrill of the unknown.

# Features

<ul>
    <li>Random Board Generation:
        <ol>
            <li>Ships are randomly placed on both the player and computer boards.
            <li>The player cannot see where computer's ships are.
            <li>The boards generate every turn, either player's or computer's.
            <li>Each turn indicated on top of the boards.
        </ol>
</ul>

![Alt Text](assets/images/gen_board_game.jpg)

<ul>
    <li>Indicator for Turns:
        <ol>
            <li>Shows how many turns player have in total.
            <li>Turns are shared with the computer.
            <li>Each turn player or computer takes it brings the amount of turns down.
        </ol>
</ul>

![Alt Text](assets/images/turns.png)