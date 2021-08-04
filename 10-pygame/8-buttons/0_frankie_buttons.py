'''
Frankie moves around by the arrow keys
'''

import pygame
import sys
from pygame.constants import MOUSEBUTTONDOWN
import random

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

MENU_BUTTONS = {
    # x start, x end, y start, y end
    'top':(SCREEN_WIDTH-100, SCREEN_WIDTH, 0, 40),
    'middle':(SCREEN_WIDTH-100, SCREEN_WIDTH, 60, 100),
    'bottom':(SCREEN_WIDTH-100, SCREEN_WIDTH, 120, 160),
}



def bottom_button_clicked():
    pass

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frankie = pygame.image.load("10-pygame/foxr.gif")

    # Make frankie bigger and centred
    frankie = pygame.transform.rotozoom(frankie, 0, 4)
    frankie_rect = frankie.get_rect()
    frankie_rect.centerx = SCREEN_WIDTH/2
    frankie_rect.centery = SCREEN_HEIGHT/2

    background_colour = (66, 135, 245)

    sysfont = pygame.font.get_default_font()

    while True:
        for event in pygame.event.get():
            #print(f"{event=}")
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                #print(f"{event.pos=}")
                
                # (x,y) is where the mouse clicked
                x,y = event.pos
                for button,location in MENU_BUTTONS.items():

                    # x1,x2,y1,y2 show the bounds of the button we are looking at
                    x1,x2,y1,y2 = location

                    '''

                    x1,y1........x2,y1
                    .                .
                    .                .
                    .                .
                    .                .
                    x1,y2........x2,y2


                    '''

                    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                        if button == 'top':
                            # Set background to random colour
                            background_colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                        elif button == 'middle':
                            # Put Frankie on a random spot on the screen
                            frankie_rect.center = (random.randint(0,SCREEN_WIDTH), random.randint(0,SCREEN_HEIGHT))
                        else:
                            bottom_button_clicked()

        
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_DOWN]: # K_DOWN means down arrow
                frankie_rect.centery = frankie_rect.centery + 20
            if pressed_keys[K_UP]: # K_UP means up arrow
                frankie_rect.centery = frankie_rect.centery - 20
            if pressed_keys[K_LEFT]: # K_LEFT means left arrow
                frankie_rect.centerx = frankie_rect.centerx - 20
            if pressed_keys[K_RIGHT]: # K_RIGHT means right arrow
                frankie_rect.centerx = frankie_rect.centerx + 20


        # Clear the screen
        screen.fill(background_colour)
        

        for button in MENU_BUTTONS:
            x1, x2, y1, y2 = MENU_BUTTONS[button]
            pygame.draw.rect(screen, (38, 115, 46), pygame.Rect(x1,y1,x2-x1,y2-y1))
            img = sysfont.render(sysfont, True, (0,0,0))
            rect = img.get_rect()
            pygame.draw.rect(img, (0,0,0), rect, 1)
            
        # Draw frankie on screen and update screen
        screen.blit(frankie, frankie_rect)
        pygame.display.flip()




if __name__ == "__main__":
    main()