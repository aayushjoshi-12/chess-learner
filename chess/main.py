import pygame
from player import Player
from board import Board

pygame.init()
screen = pygame.display.set_mode((632, 632))
clock = pygame.time.Clock()
running = True

board_img = pygame.image.load("chess/assets/images/board.png").convert()

black = Player(isWhite=False)
white = Player(isWhite=True)

board = Board(blackPlayer=black, whitePlayer=white)
board.display()

while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(board_img, (0,0))
    pygame.display.flip()
    clock.tick(15)

pygame.quit()