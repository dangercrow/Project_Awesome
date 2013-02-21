import sys
import pygame
from FunctLib import*
from Spritestash import *

pygame.init()

ScreenWH = ((800, 600))
Titledisplay = pygame.display.set_mode(ScreenWH)
BLACK, WHITE = (0, 0, 0), (250, 250, 250)
Titledisplay.fill(BLACK)
#Images
Selector = pygame.image.load('Selector.png')
Selector.set_colorkey(WHITE)
Titlescreen = pygame.image.load('Titlescreen.png')
Cursor = Pointer('Cursor.png', WHITE)

#Music
Music = pygame.mixer.music.load('Music.mp3')
pygame.mixer.music.play(-1, 0)
#Variables
Click = False
pygame.mouse.set_visible(False)
Objects = pygame.sprite.LayeredDirty(Cursor)

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
    if 300 < Cursorpos[0] < 480 and 400 < Cursorpos[1] < 450:
        Titledisplay.blit(Selector, (330, 450))
        if Click > 0:
            execfile('Movement.py')
    if 300 < Cursorpos[0] < 480 and 450 < Cursorpos[1] < 500:
        Titledisplay.blit(Selector, (330, 500))
        if Click > 0:
            pygame.quit()
            sys.exit()
    Cursor.update()
    Obj = pygame.sprite.LayeredDirty(Cursor)
    Obj.draw(Titledisplay)
    pygame.display.update()

