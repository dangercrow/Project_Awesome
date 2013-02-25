import pygame, sys
from pygame.locals import *

pygame.init()


def UpdateDirty(Spritelist, surface): #Updates all dirty sprites in Spritelist
    for i in Spritelist:
        i.update()
        i.draw(surface)


def movement(Display, Backgrounds, Players, Houses, NPCs, Cursor):
    """All sprite inputs have to be in DirtySprite format and in a LayeredDirty group,
       Creates a loop and detects keyboard inputs, controls with WASD but can be configured later"""
    BLACK = (0, 0, 0)
    MenuOpen = False
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
            if event.key == K_TAB:
                MenuOpen = True
                return MenuOpen
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
    
    
def OpenMenu(Menuimage, Menucoords, Selector_img, Selectcoords, Buttonlist, colorkey, surface, MOVESPEED):
    Menuimg = pygame.image.load(Menuimage)
    Selector_img = pygame.image.load(Selector_img)
    Menuimg.set_colorkey(colorkey)
    Selector_img.set_colorkey(colorkey)
    Menurect = Menuimg.get_rect()
    Selector_rect = Selector_img.get_rect()
    (pos_x, pos_y) = Selector_rect.topleft
    Cursorpos = pygame.mouse.get_pos()
    MenuEnter, MenuExit = False, False
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w: pos_y -= MOVESPEED
            if event.key == K_s: pos_y += MOVESPEED
            if event.key == K_a: pos_x -= MOVESPEED
            if event.key == K_d: pos_x += MOVESPEED
            if event.key == K_RETURN: MenuEnter = True
            if event.key == K_TAB: MenuOpen = False
            if event.key == K_BACKSPACE: MenuExit = True
        if event.type == KEYUP:
            if event.key == K_RETURN: MenuEnter = False
            if event.key == K_BACKSPACE: MenuExit = False
        if event.type == MOUSEBUTTONDOWN: Click = True
        if event.type == MOUSEBUTTONUP: Click = False
    for i in Buttonlist:
        if i.dirty:
            if i.Click > 0 or (i.rect.collidepoint(pos_x, pos_y) and MenuEnter):
                i.Output
    surface.blit(Menuimg, Menucoords)
    surface.blit(Selector_img, Selectcoords)