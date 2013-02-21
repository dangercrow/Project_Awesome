import pygame, sys
from pygame.locals import *

pygame.init()


def UpdateDirty(Spritelist, surface): #Updates all dirty sprites in Spritelist
    for i in Spritelist:
        i.update()
        i.draw(surface)


def movement(Display, Backgrounds, Players, Houses, NPCs, Cursor, Menu):
    """All sprite inputs have to be in DirtySprite format and in a LayeredDirty group,
       Creates a loop and detects keyboard inputs, controls with WASD but can be configured later"""
    BLACK = (0, 0, 0)
    menuopen = False
    Display.fill(BLACK)
    Movingsprites = (Backgrounds, Houses, NPCs)
    Cursorpos = pygame.mouse.get_pos()
    Backgrounds.clear(Display, Display)
    Houses.clear(Display, Display)
    NPCs.clear(Display, Display)
    Players.clear(Display, Display)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if pygame.key.get_pressed()[K_TAB]:
        menuopen = True
    while menuopen == True:
        if pygame.key.get_pressed()[K_a]:
            for i in Menu:
                i.move('moveLeft', Display)
        if pygame.key.get_pressed()[K_d]:
            for i in Menu:
                i.move('moveRight', Display)
        if pygame.key.get_pressed()[K_w]:
            for i in Menu:
                i.move('moveUp', Display)
        if pygame.key.get_pressed()[K_s]:
            for i in Menu:
                i.move('moveDown', Display)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    menuopen = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            UpdateDirty((Backgrounds, Houses, NPCs, Players, Menu, Cursor), Display)
            pygame.display.flip()
    if pygame.key.get_pressed()[K_a]: # Movement key detection and movement
        for i in Movingsprites:
            for j in i:
                j.move('moveLeft')
    if pygame.key.get_pressed()[K_d]:
        for i in Movingsprites:
            for j in i:
                j.move('moveRight')
    if pygame.key.get_pressed()[K_w]:
        for i in Movingsprites:
            for j in i:
                j.move('moveUp')
    if pygame.key.get_pressed()[K_s]:
        for i in Movingsprites:
            for j in i:
                j.move('moveDown')
    UpdateDirty((Backgrounds, Houses, NPCs, Players, Cursor), Display)


def movement(Display, Backgrounds, Players, Houses, NPCs, Cursor, Menu):
    """All sprite inputs have to be in DirtySprite format and in a LayeredDirty group,
       Creates a loop and detects keyboard inputs, controls with WASD but can be configured later"""
    BLACK = (0, 0, 0)
    menuopen = False
    Display.fill(BLACK)
    Movingsprites = (Backgrounds, Houses, NPCs)
    Cursorpos = pygame.mouse.get_pos()
    Backgrounds.clear(Display, Display)
    Houses.clear(Display, Display)
    NPCs.clear(Display, Display)
    Players.clear(Display, Display)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if pygame.key.get_pressed()[K_TAB]:
        menuopen = True
    while menuopen == True:
        if pygame.key.get_pressed()[K_a]:
            for i in Menu:
                i.move('moveLeft', Display)
        if pygame.key.get_pressed()[K_d]:
            for i in Menu:
                i.move('moveRight', Display)
        if pygame.key.get_pressed()[K_w]:
            for i in Menu:
                i.move('moveUp', Display)
        if pygame.key.get_pressed()[K_s]:
            for i in Menu:
                i.move('moveDown', Display)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    menuopen = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            UpdateDirty((Backgrounds, Houses, NPCs, Players, Menu, Cursor), Display)
            pygame.display.flip()
    if pygame.key.get_pressed()[K_a]: # Movement key detection and movement
        for i in Movingsprites:
            for j in i:
                j.move('moveLeft')
    if pygame.key.get_pressed()[K_d]:
        for i in Movingsprites:
            for j in i:
                j.move('moveRight')
    if pygame.key.get_pressed()[K_w]:
        for i in Movingsprites:
            for j in i:
                j.move('moveUp')
    if pygame.key.get_pressed()[K_s]:
        for i in Movingsprites:
            for j in i:
                j.move('moveDown')
    UpdateDirty((Backgrounds, Houses, NPCs, Players, Cursor), Display)