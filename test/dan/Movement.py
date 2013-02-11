import sys
import pygame
from pygame.locals import *

pygame.init()
from Spritestash import *

WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
pygame.display.set_caption('Project Awesome')
ScreenWH = ((800, 600))
DISPLAYSURF = pygame.display.set_mode(ScreenWH) #Surface
DISPLAYSURF.fill(BLACK)

Menu = pygame.image.load('C:\Users\Dan\PycharmProjects\Prototype\Images\Menu.png').convert()
Menuselect = pygame.image.load('C:\Users\Dan\PycharmProjects\Prototype\Images\Select.png').convert()
Menuinventory = pygame.image.load('C:\Users\Dan\PycharmProjects\Prototype\Images\Inventory.png').convert()
StretchedInventory = pygame.transform.scale(Menuinventory, (300, 300))
Exclaimation = pygame.image.load('C:\Users\Dan\PycharmProjects\Prototype\Images\Emark.png').convert()
Exclaimation.set_colorkey(WHITE)
Cursor = Pointer('C:\Users\Dan\PycharmProjects\Prototype\Images\mouse.png', WHITE)
pygame.mouse.set_visible(False)

#Movement/position variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 5
Mapx, Mapy = 0, 0
NPCx, NPCy = (Mapx + 300), (Mapy + 300)
Exclaimationx, Exclaimationy = NPCx, NPCy - 20

#Sprite classes
Player = Character('C:\Users\Dan\PycharmProjects\Prototype\Images\Walk-4.gif', (400, 300), WHITE)
Map = Background('C:\Users\Dan\PycharmProjects\Prototype\Images\Map.jpg', (Mapx, Mapy), 1071, 603, MOVESPEED)
NPC = NPC('C:\Users\Dan\PycharmProjects\Prototype\Images\Monkey.png', (Mapx + 300, Mapy + 300),WHITE, MOVESPEED)
Backgroundsprites = pygame.sprite.Group(NPC, Map)
Backbutton = pygame.image.load('C:\Users\Dan\PycharmProjects\Prototype\Images\Backbutton.png')

#FPS control
FPS = 30
fpsClock = pygame.time.Clock()

#Menu variables
menu = False
menuUp = False
menuDown = False
menuLeft = False
menuRight = False
menuEnter = False
menuExit = False
menuInventory = False
selecty = 50
selectx = 600
Click = False

#Game loop
while True:
    Cursorpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            Click = True
        if event.type == MOUSEBUTTONUP:
            Click = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
            if event.key == K_TAB:
                menu = True
                while menu == True:
                    Cursorpos = pygame.mouse.get_pos()      #Menu is open here, pauses game.
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_UP or event.key == ord('w'):
                                menuDown = False
                                menuUp = True
                            if event.key == K_DOWN or event.key == ord('s'):
                                menuUp = False
                                menuDown = True
                            if event.key == K_RIGHT or event.key == ord('d'):
                                menuLeft = False
                                menuRight = True
                            if event.key == K_LEFT or event.key == ord('a'):
                                menuRight = False
                                menuLeft = True
                            if event.key == K_RETURN:
                                menuEnter = True
                            if event.key == K_BACKSPACE:
                                menuExit = True
                            if event.key == K_TAB:
                                menu = False
                                break
                        if event.type == MOUSEBUTTONDOWN:
                            Click = True
                        if event.type == MOUSEBUTTONUP:
                            Click = False
                            menuExit = False

                        if event.type == KEYUP:
                            if event.key == K_LEFT or event.key == ord('a'):
                                menuLeftLeft = False
                            if event.key == K_RIGHT or event.key == ord('d'):
                                menuRight = False
                            if event.key == K_UP or event.key == ord('w'):
                                menuUp = False
                            if event.key == K_DOWN or event.key == ord('s'):
                                menuDown = False
                            if event.key == K_RETURN:
                                menuEnter = False
                            if event.key == K_BACKSPACE:
                                menuExit = False

                        if menuUp > 0 and selecty > 50:
                            selecty -= 50
                        if menuDown > 0 and selecty < 250:
                            selecty += 50
                        if selecty == 150 and menuEnter > 0:
                            menuInventory = True
                        if menuExit > 0:
                            menuInventory = False
                        if 672 > Cursorpos[0] > 600 and 150 < Cursorpos[1] < 188:
                            selecty = 150
                            if Click > 0:
                                menuInventory = True

                    DISPLAYSURF.fill(BLACK)
                    Map.update(DISPLAYSURF)
                    NPC.update(DISPLAYSURF)
                    Player.update(DISPLAYSURF)
                    DISPLAYSURF.blit(Menu, (600, 50))
                    DISPLAYSURF.blit(Menuselect, (selectx, selecty))
                    if menuInventory > 0:
                        DISPLAYSURF.blit(StretchedInventory, (200, 50))
                        DISPLAYSURF.blit(Backbutton, (200, 50))
                        if 238 > Cursorpos[0] > 200 and 50 < Cursorpos[1] < 75:
                            if Click > 0:
                                menuExit = True
                    Cursor.update(DISPLAYSURF)
                    pygame.display.update()

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False

    if moveDown > 0:
        Map.move(3)
        NPC.move(3)
    if moveUp > 0:
        Map.move(1)
        NPC.move(1)
    if moveLeft > 0:
        Map.move(4)
        NPC.move(4)
    if moveRight > 0:
        Map.move(2)
        NPC.move(2)

    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    DISPLAYSURF.fill(BLACK)
    Map.update(DISPLAYSURF)
    NPC.update(DISPLAYSURF)
    if pygame.sprite.collide_rect(NPC, Player) > 0:
        DISPLAYSURF.blit(Exclaimation, (300, 300))
    Player.update(DISPLAYSURF)
    Cursor.update(DISPLAYSURF)
    pygame.display.update()
    fpsClock.tick(FPS)

