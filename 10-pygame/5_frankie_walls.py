'''
Frankie moves around by the arrow keys
Make sure Frankie doesn't fall off the screen
'''

import pygame
import sys

# import these key values so we can use them
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frankie = pygame.image.load("10-pygame/foxr.gif")

    # Make frankie bigger and centred
    frankie = pygame.transform.rotozoom(frankie, 0, 4)
    frankie_rect = frankie.get_rect()
    frankie_rect.centerx = SCREEN_WIDTH/2
    frankie_rect.centery = SCREEN_HEIGHT/2

    walls = [
        # Rect(x_start, y_start, width, height)
        pygame.Rect(200,200,400,10),
        pygame.Rect(200,200,10,200),
        pygame.Rect(0,0,SCREEN_WIDTH,1),
        pygame.Rect(0,0,1,SCREEN_HEIGHT),
        pygame.Rect(SCREEN_WIDTH,0,1,SCREEN_HEIGHT),
        pygame.Rect(0,SCREEN_HEIGHT,SCREEN_WIDTH,1)
    ]

    move_inc = 20 # A move in any direction will be 20 pixels
    x_mov = 0
    y_mov = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_DOWN]:
                # Update frankie's rect
                # If the rect now collides with a barrier, then undo the update
                y_mov = move_inc
                while y_mov > 0:
                    # Check that we haven't collided yet
                    if frankie_rect.collidelist(walls) == -1 :
                        frankie_rect.centery += 1
                        y_mov -= 1
                    else:
                        # Do this if we collided
                        frankie_rect.centery -= 1
                        break # exits this while loop. Could also accomplish this by y_mov = 0

            if pressed_keys[K_UP]:
                y_mov = move_inc
                while y_mov > 0:
                    # Check that we haven't collided yet
                    if frankie_rect.collidelist(walls) == -1 :
                        frankie_rect.centery -= 1
                        y_mov -= 1
                    else:
                        # Do this if we collided
                        frankie_rect.centery += 1
                        break # exits this while loop. Could also accomplish this by y_mov = 0
            if pressed_keys[K_LEFT]:
                x_mov = move_inc
                while x_mov > 0:
                    # Check that we haven't collided yet
                    if frankie_rect.collidelist(walls) == -1 :
                        frankie_rect.centerx -= 1
                        x_mov -= 1
                    else:
                        # Do this if we collided
                        frankie_rect.centerx += 1
                        break # exits this while loop. Could also accomplish this by x_mov = 0
            if pressed_keys[K_RIGHT]:
                x_mov = move_inc
                while x_mov > 0:
                    # Check that we haven't collided yet
                    if frankie_rect.collidelist(walls) == -1 :
                        frankie_rect.centerx += 1
                        x_mov -= 1
                    else:
                        # Do this if we collided
                        frankie_rect.centerx -= 1
                        break # exits this while loop. Could also accomplish this by x_mov = 0


        # Clear the screen
        screen.fill((66, 135, 245))
        # Draw our walls on the screen
        for wall in walls:
            pygame.draw.rect(screen, (38, 115, 46), wall)
        # Draw frankie on screen and update screen
        screen.blit(frankie, frankie_rect)
        pygame.display.flip()




if __name__ == "__main__":
    main()