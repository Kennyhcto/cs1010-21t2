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

    # Calculate the edges, where Frankie's centre can safely go
    top_edge = 0 + frankie_rect.height/2
    bottom_edge = SCREEN_HEIGHT - frankie_rect.height/2
    left_edge = 0 + frankie_rect.width/2
    right_edge = SCREEN_WIDTH - frankie_rect.width/2

    while True:
        for event in pygame.event.get():
            #print(f"{event=}")
            if event.type == pygame.QUIT:
                sys.exit()

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_DOWN]:
                # If in moving down, frankie's center goes off the 'bottom_edge'
                # (where the center can safely go)
                # then only move frankie to that bottom edge (and no further)
                # else, move frankie a whole 20 pixels
                if frankie_rect.centery + 20 > bottom_edge:
                    frankie_rect.centery = bottom_edge
                else:
                    frankie_rect.centery = frankie_rect.centery + 20
            if pressed_keys[K_UP]:
                # Same as above, but for moving up
                if frankie_rect.centery - 20 < top_edge:
                    frankie_rect.centery = top_edge
                else:
                    frankie_rect.centery = frankie_rect.centery - 20
            if pressed_keys[K_LEFT]:
                # Same as above, but for moving left
                if frankie_rect.centerx - 20 < left_edge:
                    frankie_rect.centerx = left_edge
                else:
                    frankie_rect.centerx = frankie_rect.centerx - 20
            if pressed_keys[K_RIGHT]:
                # Same as above, but for moving right
                if frankie_rect.centerx + 20 > right_edge:
                    frankie_rect.centerx = right_edge
                else:
                    frankie_rect.centerx = frankie_rect.centerx + 20


        # Clear the screen
        screen.fill((66, 135, 245))
        # Draw frankie on screen and update screen
        screen.blit(frankie, frankie_rect)
        pygame.display.flip()




if __name__ == "__main__":
    main()