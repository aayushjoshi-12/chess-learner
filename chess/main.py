import pygame

pygame.init()
screen = pygame.display.set_mode((631, 632))
clock = pygame.time.Clock()
running = True

board_img = pygame.image.load("chess/assets/images/board.png").convert()

while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(board_img, (0,0))
    pygame.display.flip()
    clock.tick(15)

pygame.quit()