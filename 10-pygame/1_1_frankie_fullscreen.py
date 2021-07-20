'''
Display Frankie the Fox on the screen
'''

# https://pypi.org/project/screeninfo/

import pygame
import sys
from screeninfo import get_monitors

def main():
    # Initialize pygame library
    pygame.init()

    # Set up a display fullscreen
    width = get_monitors()[0].width 
    height = get_monitors()[0].height
    screen = pygame.display.set_mode((width, height))

    # Put frankie image into a variable
    frankie = pygame.image.load("10-pygame/foxr.gif")

    # Put frankie onto screen
    frankie_rect = frankie.get_rect()
    screen.blit(frankie, frankie_rect)

    # Update display (so we can see the newly added Frankie)
    pygame.display.flip()

    # Keep our program running
    while True:
        # If the user closes the window, then finish
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()