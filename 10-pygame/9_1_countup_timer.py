# Get the starting time, then each loop, get how long since that start
# and display that as time since start

import pygame

print("running countup timer")
pygame.init()
screen = pygame.display.set_mode((800, 600))

text = ''
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)


run = True
start_ticks=pygame.time.get_ticks() #starter tick
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
            text = str(seconds)
        if e.type == pygame.QUIT: 
            run = False

    # Clear screen, fill with background colour
    screen.fill((255, 255, 255))
    # Put the text (counter) on the screen
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    # Display the screen
    pygame.display.flip()