'''
Display Frankie the Fox on the screen
Bigger and in the middle
'''

import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    # Initialize pygame library
    pygame.init()

    # Set up a display 800 by 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Put frankie image into a variable
    frankie = pygame.image.load("10-pygame/foxr.gif")

    # Make frankie bigger
    frankie = pygame.transform.rotozoom(frankie, 0, 4)

    # Get frankie's dimensions
    frankie_rect = frankie.get_rect()

    # Move frankie to the middle of the screen
    frankie_rect.centerx = SCREEN_WIDTH/2
    frankie_rect.centery = SCREEN_HEIGHT/2

    # Put frankie onto screen
    screen.blit(frankie, frankie_rect)

    # Update display (so we can see the newly added Frankie)
    pygame.display.flip()

    # Keep our program running
    while True:
        # If the user closes the window, then finish
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

'''
(0,0).............(800,0)
.                   .
.                   .
.                   .
.                   .
.                   .
.                   .
.                   .
(0,600)...........(800,600)

'''



if __name__ == "__main__":
    main()