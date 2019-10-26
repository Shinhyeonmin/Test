def place(board, user_num, a):

    if (board[user_num] == '%'):
        board[user_num] = a
        return True, board

    else:
        print("choose again")
        return False, board