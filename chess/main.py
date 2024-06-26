import pygame
from player import Player
from board import Board

pygame.init()
screen = pygame.display.set_mode((632, 632))
clock = pygame.time.Clock()
running = True

board_img = pygame.image.load("chess/assets/images/board.png").convert()

black = Player(is_white=False)
white = Player(is_white=True)
board = Board(black_player=black, white_player=white)
whites_turn = True
board.display()

while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if whites_turn: white.make_move()
    else: black.make_move()

    whites_turn = not whites_turn

    screen.blit(board_img, (0,0))
    pygame.display.flip()
    clock.tick(15)

pygame.quit()