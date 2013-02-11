import sys
import pygame
from Spritestash import *
from pygame.locals import *

pygame.init()

ScreenWH = ((800, 600))
Titledisplay = pygame.display.set_mode(ScreenWH)
BLACK, WHITE = (0, 0, 0), (250, 250, 250)
Titledisplay.fill(BLACK)
#Images
Selector = pygame.image.load('C:\Users\Dan\PycharmProjects\Prototype\Images\Selector.png')
Titlescreen = pygame.image.load('C:\Users\Dan\PycharmProjects\Prototype\Images\Titlescreen.png')
Cursor = Pointer('C:\Users\Dan\PycharmProjects\Prototype\Images\mouse.png', WHITE)
#Music
Music = pygame.mixer.music.load('C:\Users\Dan\PycharmProjects\Prototype\Music\Music.mp3')
pygame.mixer.music.play(-1, 0)
#Variables
Click = False
pygame.mouse.set_visible(False)

while 1:
    Cursorpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            Click = True
        if event.type == MOUSEBUTTONUP:
            Click = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    Titledisplay.blit(Titlescreen, (-50, -50))
    if 330 < Cursorpos[0] < 518 and 450 < Cursorpos[1] < 500:
        Titledisplay.blit(Selector, (330, 450))
        if Click > 0:
            execfile('C:\Users\Dan\PycharmProjects\Prototype\Python files\Movement.py')
    if 330 < Cursorpos[0] < 518 and 500 < Cursorpos[1] < 600:
        Titledisplay.blit(Selector, (330, 500))
        if Click > 0:
            pygame.quit()
            sys.exit()

    Cursor.update(Titledisplay)
    pygame.display.update()

