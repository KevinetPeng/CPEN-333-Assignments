# student name: Kevin Peng
# student number: 94742293

# A command-line Tic-Tac-Toe game 
import random

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 

def init() -> None:
    """ prints the banner messages 
        and prints the intial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    print("\n")

    # print board values and horizontal divides (if not last line)
    for i in range(0, 9, 3):
      print(f"   {board[i]} | {board[i+1]} | {board[i+2]}    {i} | {i+1} | {i+2}")
      if i < 6:
        print("   --+---+--    --+---+--")

    print("\n")


def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    while True:
        try:
            move = int(input("Next move for X (state a valid cell num):"))

            # check that input is within bounds of board and not previously played
            if move in played or move < 0 or move > 8:
                print("Must enter a valid cell number")
            else:
                print(f"You chose cell {move}")

                played.add(move)
                board[move] = 'X'

                printBoard()

                break

        except:
            # casting to int will throw error for non-integer input
            print("Must be an integer")


def computerNextMove() -> None:
    """ Computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """
    # random in range 0-8 not including those in the already played set
    move = random.choice([x for x in range(0, 9) if x not in played])

    print(f"Computer chose cell {move}")
    played.add(move)
    board[move] = 'O'

    printBoard()


def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise """

    # 3 row checks
    for row_index in range (0, 9, 3):
        count = 0

        for i in range(row_index, row_index + 3):
            if board[i] == who:
                count += 1
            else:
                break
        
        if count == 3:
            return True

    # 3 col checks
    for col_index in range (0, 3):
        count = 0

        for i in range(col_index, 9, 3):
            if board[i] == who:
                count += 1
            else:
                break
        
        if count == 3:
            return True
    
    # 1st diagonal check
    if board[0] == who and board[4] == who and board[8] == who:
        return True

    # 2nd diagonal check
    if board[2] == who and board[4] == who and board[6] == who:
        return True

    # if we haven't returned true by this point, return false
    return False

def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """
    # check if won
    if hasWon(who):
        if who == 'X':
            print("You won! Thanks for playing.")
        else:
            print("You lost! Thanks for playing.")

        return True
    
    # check if draw
    if len(played) == 9:
        print("A draw! Thanks for playing.")
        return True

    return False

if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate