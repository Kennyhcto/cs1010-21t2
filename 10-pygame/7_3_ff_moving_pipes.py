import pygame
import sys
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SIZE_OF_GAP = 200

def generate_pipes(bottom_pipe, top_pipe):
    # Create a copy of bottom pipe's rect
    bottom_rect = bottom_pipe.get_rect().copy()
    # Makes the bottom pipe against the bottom of the screen
    bottom_rect.bottom = SCREEN_HEIGHT + random.randint(0,300)
    # Make the bottom pipe just off the right side of the screen
    bottom_rect.x = SCREEN_WIDTH + random.randint(0,30)

    # Create a copy of top pipe's rect
    top_rect = top_pipe.get_rect().copy()
    # Make top pipe SIZE_OF_GAP above the bottom pipe
    top_rect.bottom = bottom_rect.top - SIZE_OF_GAP
    # Align top pipe with bottom one horizontally
    top_rect.x = bottom_rect.x

    # return our new rectangles in a tuple
    return (bottom_rect, top_rect)

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

    # load images of pipes
    bottom_pipe = pygame.image.load("10-pygame/bp.png")
    top_pipe = pygame.image.load("10-pygame/tp.png")

    # create locations where to draw the pipes
    pipe_rects = [generate_pipes(bottom_pipe, top_pipe)]

    clock = pygame.time.Clock()

    state = "start"

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        acceleration.y = 0.35

        # If the spacebar is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if state == "start":
                state = "playing"
            elif state == "playing":
                acceleration.y = -0.35

        if state == "playing":
            velocity += acceleration
            frankie_rect = frankie_rect.move(velocity)
            # move pipes slightly to the left
            for bottom_rect, top_rect in pipe_rects:
                bottom_rect.x -= 2
                top_rect.x -= 2
                bottom_rect.top = SCREEN_HEIGHT/2 + 100*math.sin(pygame.time.get_ticks()/1000)
                top_rect.bottom = bottom_rect.top - SIZE_OF_GAP

            # If the pipes pass the centre of the screen,
            # create another set of pipes, just off the screen
            # pipe_rects[-1] is the last set of pipes we created
            # pipe_rects[-1][0] is the bottom pipe of that tuple
            if pipe_rects[-1][0].centerx <= SCREEN_WIDTH/2:
                pipe_rects.append(generate_pipes(bottom_pipe, top_pipe))

        # Update screen
        screen.fill((66, 135, 245))
        screen.blit(frankie, frankie_rect)
        for bottom_rect, top_rect in pipe_rects:
            screen.blit(bottom_pipe, bottom_rect)
            screen.blit(top_pipe, top_rect)
        pygame.display.flip()




if __name__ == "__main__":
    main()