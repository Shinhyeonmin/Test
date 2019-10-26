
def make_board():
    board = []

    for i in range(9):
        board.append("%")
    return board
def game_board(board):

    for s in range(0,9,3):
        print(board[s], board[s+1], board[s+2], board)

def check_game(use, board):
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
