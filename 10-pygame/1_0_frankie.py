'''
Display Frankie the Fox on the screen
'''

import pygame
import sys

def main():
    # Initialize pygame library
    pygame.init()

    # Set up a display 800 by 600
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))

    # Put frankie image into a variable
    frankie = pygame.image.load("10-pygame/foxr.gif")

    # Put frankie onto screen
    frankie_rect = frankie.get_rect()
    screen.blit(frankie, frankie_rect)
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