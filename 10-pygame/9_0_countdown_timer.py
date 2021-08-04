# Uses the clock to limit the pace of the game loop. Subtract one from the counter each time.

import pygame

print("running countdown timer")
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

counter = 20 # starting value of timer
text = '10'.rjust(3) # text to display
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)


run = True
while run:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            if counter > 0:
                text = str(counter).rjust(3)
            else:
                text = "boom!"
        if e.type == pygame.QUIT: 
            run = False

    # Clear screen, fill with background colour
    screen.fill((255, 255, 255))
    # Put the text (counter) on the screen
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    # Display the screen
    pygame.display.flip()
    