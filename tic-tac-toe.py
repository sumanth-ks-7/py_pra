#  Display Board fucntion of tic-tac-toe game:
# The function accepts one parameter containing the board's current status and prints it out to the console.
from random import randrange
def Dispaly_Board(board):
    print("+-------" * 3,"+",sep="")
    for row in range(3):
        print("|       " * 3,"|",sep="")
        for col in range(3):
            print("|    " + str(board[row][col]) + "  ",end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

# Enter a move
# The function accepts the board current status, asks the user about their move, checks the input and updates the board according to the user's decision.
def Enter_Move(board):
    ok = False
    while not ok:
        move = input("Enter your move: ")
        ok  = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Not a correct move - repeat your move")
            continue
        move = int(move) - 1
        row = move // 3
        column = move % 3
        sign = board[row][column]
        ok = sign not in ['O', 'X']
        if not ok:
            print("Field alredy occupied")
            continue
        board[row][column] = 'O'
        if move == "q":
            print("Game Quit!!!")
            break

# Make list of free fields
#  The function browses the board, builds a list of all the free squares and the list consists of tuples, while each tuple is a pair of row-column numbers.
def Make_ListOf_Free_Fields(board):
    free = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['O', 'X']:
                free.append((row, column))
    return free


# Victory for 
# The function analyzes the board status to check if the player using 'O's or 'X's has won the game.
def Victory_For(board, sign):
    if sign == 'X':
        who = 'me'
    elif sign == 'O':
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
        if board[rc][rc] != sign:
            cross1 = False
        if board[2 - rc][2 - rc] != sign:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


# Draw move
# The function draws the computer's move and updates the board.
def Draw_Move(board):
    free = Make_ListOf_Free_Fields(board)
    cmt = len(free)
    if cmt > 0:
        this = randrange(cmt)
        row, column = free[this]
        board[row][column] = 'X'


# Main Program
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
free = Make_ListOf_Free_Fields(board)
Human_Turn = True
while len(free):
    Dispaly_Board(board)
    if Human_Turn:
        Enter_Move(board)
        victor = Victory_For(board, 'O')
    else:
        Draw_Move(board)
        victor = Victory_For(board, 'X')
    if victor != None:
        break
    Human_Turn = not Human_Turn
    free = Make_ListOf_Free_Fields(board)


Dispaly_Board(board)
if victor == 'you':
    print("You Won!")
elif victor == 'me':
    print("I won")
else:
    print("Tie!")