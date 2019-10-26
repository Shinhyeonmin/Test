from GAME.Tic_Tac_toc.board import check_game

def evaluate(a, b, board):
    if(check_game(b, board)):
        score = 1
    elif(check_game(a, board)):
        score=-1
    else:
        score=0
    return score