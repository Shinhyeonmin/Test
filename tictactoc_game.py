import random

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
        if (user_num <= 8 or user_num >= 0):
            if (board[user_num] == '%'):
                board[user_num] = a
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
    for s in range(0,3):
        print(board[s], board[s+1], board[s+2])

gameend = False
while(gameend==False):
    if(turn == 'user'):
        print('Where will you put')
        place()
    else:
        print('com')
