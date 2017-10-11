import pygame

pygame.init()
clock = pygame.time.Clock()


# colors
FON = [0, 0, 0]
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the height and width of the screen
SIZE = [1000, 900]

# screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("my game")

# add fon photo, need add animation on winter -> clouds move
DISPLAYSURF = pygame.display.set_mode(SIZE, 0, 0)
cran = pygame.image.load('crane.jpg').convert()


# position of red dot
i = 10
j = 10




done = False


while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop


# keyboard control
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 i -= 15
#             elif event.key == pygame.K_RIGHT:
#                 i += 15
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_DOWN:
#                 j += 15
#             if event.key == pygame.K_UP:
#                 j -= 15
        player_position = pygame.mouse.get_pos()
        x = player_position[0]
        y = player_position[1]





# fon of game
    DISPLAYSURF.fill(FON)
    DISPLAYSURF.blit(cran, [0, 0])

    pygame.display.update()
    pygame.draw.circle(DISPLAYSURF, RED, [x, y], 5)







    pygame.display.flip()
    clock.tick(20)
pygame.quit()


