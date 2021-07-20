'''
Frankie moves up and down based on the spacebar
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
    frankie_rect.center = pygame.math.Vector2(60,SCREEN_HEIGHT/2)

    velocity = pygame.math.Vector2(0,0) # How much to move each time through the loop
    acceleration = pygame.math.Vector2(0,0) # How much our velocity will change

    clock = pygame.time.Clock()

    state = "start"

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        acceleration.y = 0.35 # 0.5 # Makes frankie go down by default

        # If the spacebar is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if state == "start": # start --> change to playing
                state = "playing"
            elif state == "playing": # playing --> changes acceleration
                acceleration.y = -0.35 # -0.5

        if state == "playing": # change frankie's location
            velocity += acceleration
            frankie_rect = frankie_rect.move(velocity)

        # Clear the screen
        screen.fill((66, 135, 245))
        # Draw frankie on screen and update screen
        screen.blit(frankie, frankie_rect)
        pygame.display.flip()




if __name__ == "__main__":
    main()