import random
from math import inf as infinity

def ask():
    while(True):
        print('O or X??:')
        a = input()
        b = 0
        if(a == 'O'):
            b = 'X'
            print('You:0  computer:X')
            break
        elif(a == 'X'):
            b = 'O'
            print('You:X  computer:O')
            break
        else:
            print('choose again')
    return(a,b)
def order():
    com =0
    use = random.randrange(0,2)
    if(use==0):
        com=1
    elif(use==1):
        com = 0
    return (use,com)

def place():
    while (True):
        user_num = int(input())
        if (user_num <= 8 and user_num >= 0):
            if (board[user_num] == '%'):
                board[user_num] = a
                break
        else:
            print('choose again')

a, b = ask()
use,com = order()
turn = 0

if(use == 0):
    turn ='use'
else:
    turn = 'com'


board =['%', '%', '%', '%', '%', '%', '%', '%', '%']
def game_board():

    for s in range(0,9,3):
        print(board[s], board[s+1], board[s+2])
game_board()
def check_game(use):
    if ((board[0] == use and board[1] == use and board[2] == use)
            or (board[3] == use and board[4] == use and board[5] == use)
            or (board[6] == use and board[7] == use and board[8] == use)
            or (board[0] == use and board[4] == use and board[8] == use)
            or (board[2] == use and board[4] == use and board[6] == use)
            or (board[0] == use and board[3] == use and board[6] == use)
            or (board[1] == use and board[4] == use and board[7] == use)
            or (board[2] == use and board[5] == use and board[8] == use)):
        return True
    else:
        return False

def win_lose():
    if(turn == 'user'):
        use = b
    else:
        use = a
    print(use)
    if ((board[0] == use and board[1] == use and board[2] == use)
            or (board[3] == use and board[4] == use and board[5] == use)
            or (board[6] == use and board[7] == use and board[8] == use)
            or (board[0] == use and board[4] == use and board[8] == use)
            or (board[2] == use and board[4] == use and board[6] == use)
            or (board[0] == use and board[3] == use and board[6] == use)
            or (board[1] == use and board[4] == use and board[7] == use)
            or (board[2] == use and board[5] == use and board[8] == use)):
        print("use")
        return True
    else:
        return False


def empty_cells():
    cells = []
    for i, y in enumerate(board):
        if (y == '%'):
            cells.append(i)
    return cells


def minmax(state, depth, player):

    if player == "com":
        best = [-1, -infinity]
        mark = b
    else:
        best = [-1, +infinity]
        mark = a

    if depth == 0 or check_game(mark):
        score = evaluate()
        return [-1, score]

    for cell in empty_cells():
        location = cell
        if(player == "com"):
            makr = b
        else:
            makr = a
        board[location] = makr

        if (player == "com"):
            player = "user"
        else:
            player = "com"
        score = minmax(state, depth - 1, player)
        board[location] = "%"
        score[0] = location
        if player == "com":
            if (score[1] > best[1]):
                print("HI")
                best = score  # max
        else:
            if(score[1] < best[1]):
                best = score  # min
    return best
gameend = False

def evaluate():
    if(check_game(b)):
        score = 1
    elif(check_game(a)):
        score=-1
    else:
        score=0
    return score

while(gameend==False):

    depth = len(empty_cells())

    if(turn == 'user'):
        print('Where will you put')
        place()
        game_board()
        if(win_lose()==True):
            print('YOU WIN')
            break
        turn = 'com'
    else:
        print('com')
        if depth == 9:
            location = random.randrange(0,3)
        else:
            move = minmax(board, depth, b)
            print("move", move)
            board[move[0]] = b
        if(win_lose()):
            print('conuputer win')
        else:
            print('user turn')
        turn = 'user'