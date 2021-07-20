'''
Introduction to the clock
'''

import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frankie = pygame.image.load("10-pygame/foxr.gif")

    frankie = pygame.transform.rotozoom(frankie, 0, 4)
    frankie_rect = frankie.get_rect()

    frankie_rect.centerx = SCREEN_WIDTH/2
    frankie_rect.centery = SCREEN_HEIGHT/2

    wall = pygame.Rect(100,100,10,10)

    clock = pygame.time.Clock()

    while True:
        clock.tick(10)
        #clock.tick(60) # <--- compare the speeds here!!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Rotate frankie
        frankie = pygame.transform.rotozoom(frankie, 90, 1)

        # Grow wall
        wall.height = wall.height * 1.5

        screen.fill((66, 135, 245))
        pygame.draw.rect(screen, (38, 115, 46), wall)
        screen.blit(frankie, frankie_rect)
        pygame.display.flip()



if __name__ == "__main__":
    main()