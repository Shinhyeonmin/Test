import pygame
from map import get_pos_from_number
from map import get_number

grid_size = 90

WHITE = (225, 225, 225)
GREEN = (0, 225, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)

class Draw(object):
    def __init__(self,surface):
        white_img = pygame.image.load('./image/white.png')
        black_img = pygame.image.load('./image/black.png')
        board_img = pygame.image.load('./image/tic_tac_toe_board.png')
        self.white_img = pygame.transform.scale(white_img, (grid_size, grid_size))
        self.black_img = pygame.transform.scale(black_img, (grid_size, grid_size))
        self.last_w_img = pygame.image.load('./image/white_a.png')
        self.last_b_img = pygame.image.load('./image/black_a.png')
        self.board_img = pygame.transform.scale(board_img, (300, 300))
        self.surface = surface
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.font_1 = pygame.font.Font("freesansbold.ttf", 50)

    def init_game(self):
        self.draw_board()
        self.draw_font()
        self.draw_font_1()

    def draw_board(self):
        self.surface.blit(self.board_img, (0, 0))

    def draw_font(self):
        textSurfaceObj = self.font.render('user V.S. com', True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 100)
        self.surface.blit(textSurfaceObj, textRectObj)

    def draw_font_1(self):
        textSurfaceObj = self.font_1.render('user1 V.S. user2', True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (535 , 200)
        self.surface.blit(textSurfaceObj, textRectObj)

    def draw_stone(self, number):
        img = [self.black_img, self.white_img, self.last_b_img, self.last_w_img]
        x, y= get_pos_from_number(number)
        self.surface.blit(img[0], (x, y))