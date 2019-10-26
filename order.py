import random
from map import get_number
from math import inf as infinity
from board import game_board, make_board
from victor import minmax
from victor import empty_cells
from draw_game import Draw
import pygame
from pygame.locals import *
import pygame
from map import get_number
from turn_place import place
from board import game_board, make_board
from victor import win_lose

fps_clock = pygame.time.Clock()


def person(a, b, gameend, draw_game, turn, board):
    while (gameend == False):
        if (turn == 'user'):
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    print(event.pos)
                    number = get_number(event.pos[0], event.pos[1])
                    flag, board = place(board, number, a)
                    if (flag != True):
                        continue
                    else:
                        draw_game.draw_stone(number)

        elif(turn !='user'):
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    print(event.pos)
                    number = get_number(event.pos[0], event.pos[1])
                    flag, board = place(board, number, a)
                    if (flag != True):
                        continue
                    else:
                        draw_game.draw_stone(number)

            game_board(board)
            turn = 'com'
        else:
            turn = 'user'
        pygame.display.update()
        fps_clock.tick(60)

def computer(a, b, draw_game,turn, board):
    print("Hi")
    while(1):
        print("turn", turn)
        if (turn == 'user'):
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    print(event.pos)
                    number = get_number(event.pos[0], event.pos[1])
                    print(number)
                    flag, board = place(board, number, a)
                    print("flag", flag)
                    if(flag != True):
                        continue
                    else:
                        print("draw stond")
                        draw_game.draw_stone(number)

                game_board(board)
                if (win_lose(turn, board, a, b) == True):
                    print('YOU WIN')
                    break
                turn = 'com'
        else:
            turn = 'user'

        pygame.display.update()
        fps_clock.tick(60)



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

def main():
    a, b = ask()
    use, com = order()
    turn = 0
    board = make_board()

    if (use == 0):
        turn = 'use'
    else:
        turn = 'com'

    gameend = False

    window_width = 800
    window_height = 500
    board_width = 500
    bg_color = (128, 128, 128)
    fps = 90
    fps_clock = pygame.time.Clock()

    pygame.init()
    surface =pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption("Omok game")
    surface.fill(bg_color)
    draw_game = Draw(surface)
    draw_game.init_game()

    number = -10
    while(True):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                print(event.pos)
                number = get_number(event.pos[0], event.pos[1])
                print("number ", number)
                break
        if(number > 0):
            break

        pygame.display.update()
        fps_clock.tick(fps)


    if (number == 9):
        print("computer")
        computer(a, b, draw_game, turn, board)
    elif (number == 10):
        print("person")
        person(a, b, gameend, draw_game, turn, board)

main()
