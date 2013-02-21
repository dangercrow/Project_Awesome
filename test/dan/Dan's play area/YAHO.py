import pygame
import math
import random
from pygame.locals import *
pygame.init()
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
pi = math.pi
Display = pygame.display.set_mode((800, 600))
Display.fill(BLACK)
fpsClock = pygame.time.Clock()
fpsimage = pygame.image.load('fps.png')
sizeimage = pygame.image.load('size.png')
plus = pygame.image.load('plus.png')
plus2rect = pygame.Rect(750, 550, 47, 43)
plus1rect = pygame.Rect(750, 50, 47, 43)
minus1rect = pygame.Rect(750, 100, 47, 43)
minus2rect = pygame.Rect(700, 550, 47, 43)
thickness = 2
minus = pygame.image.load('minus.png')
fps = 60
Music = pygame.mixer.music.load('Hey.mp3')
pygame.mixer.music.play(-1, 0)
arcangle = 0
arcangle2 = 0
Back = False
Click = False
circles = False
lines = False
while 1:
    randcoords1 = (0, random.randint(0, 600))
    randcoords2 = (800, random.randint(0, 600))
    randcoords3 = (random.randint(0, 800), 600)
    randcoords4 = (random.randint(0, 800), 0)
    r, g, b = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
    Randcolour = (r, g, b)
    Cursorpos = pygame.mouse.get_pos()
    mouserect = pygame.Rect(Cursorpos[0], Cursorpos[1], 10, 10)
    arcangle -= 1.5
    arcangle2 +=1.5
    arcrect = ((Cursorpos[0]-25), (Cursorpos[1]-25), 50, 50)
    arcrect2 = ((Cursorpos[0]-37.5), (Cursorpos[1]-37.5), 75, 75)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            Click = True
        if event.type == MOUSEBUTTONUP:
            Click = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                Display.fill(BLACK)
            if event.key == K_RETURN:
                Back = True
            if event.key == K_BACKSPACE:
                Back = False
            if event.key == K_c:
                circles = True
            if event.key == K_l:
                lines = True
            if event.key == K_TAB:
                lines = False
                circles = False
    if Back:
        Display.fill(BLACK)
    if circles:
        pygame.draw.arc(Display, Randcolour, arcrect, arcangle, arcangle+1, 2)
        pygame.draw.arc(Display, Randcolour, arcrect2, arcangle2, arcangle2+0.5, 4)
    if lines:
        pygame.draw.line(Display, (Randcolour), (randcoords1), Cursorpos, thickness)
        pygame.draw.line(Display, (Randcolour), (randcoords2), Cursorpos, thickness)
        pygame.draw.line(Display, (Randcolour), (randcoords3), Cursorpos, thickness)
        pygame.draw.line(Display, (Randcolour), (randcoords4), Cursorpos, thickness)
    if Click:
        if mouserect.colliderect(plus1rect):
            fps += 10
        if mouserect.colliderect(minus1rect):
            fps -= 10
        if mouserect.colliderect(plus2rect):
            thickness += 1
        if mouserect.colliderect(minus2rect):
            thickness -= 1
    Display.blit(sizeimage, (650, 500))
    Display.blit(fpsimage, (700, 0))
    Display.blit(minus, (700, 550))
    Display.blit(plus, (750, 550))
    Display.blit(plus, (750, 50))
    Display.blit(minus, (750, 100))
    pygame.display.flip()
    fpsClock.tick(fps)