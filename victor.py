from board import check_game
from Score_calculation import evaluate
from board import game_board
from math import inf as infinity

def win_lose(turn,board,a,b):
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

def empty_cells(board):
    cells = []
    for i, y in enumerate(board):
        if (y == '%'):
            cells.append(i)
    return cells

def minmax(depth, player, a, b, board):

    if player == "com":
        best = [-1, -infinity]
        mark = b
    else:
        best = [-1, +infinity]
        mark = a

    if depth == 0 or check_game(mark, board):
        score = evaluate( a, b, board)
        return [-1, score]

    for cell in empty_cells(board):
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
        score = minmax(depth - 1, player, a, b, board)
        board[location] = "%"
        score[0] = location
        if player == "com":
            if (score[1] > best[1]):
                print("HI")
                best = score  # max
        else:
            if(score[1] < best[1]):
                best = score  # min
        print(best)
    return best
