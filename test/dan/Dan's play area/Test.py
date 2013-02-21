import pygame
from Spritestash import *
from FunctLib import *

pygame.init()
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
pygame.display.set_caption('Project Awesome')
ScreenWH = ((800, 600))
DISPLAYSURF = pygame.display.set_mode(ScreenWH) #Surface
DISPLAYSURF.fill(BLACK)

#Movement/position variables
MOVESPEED = 2
Mapx, Mapy = 0, 0
NPCx, NPCy = 300, 300
Housex, Housey = 100, 100
Dialogue = 'Hello there, friend ! Would you like to taste my honey?'

#Sprite class
Exclaimation = pygame.image.load('Emark.png')
Player = Character('Walk 1.png', (400, 300), WHITE)
Map = Background('Field.png', (Mapx, Mapy), WHITE, MOVESPEED)
NPC = NPC('Monkey.png', (NPCx, NPCy), WHITE, MOVESPEED, Player, Dialogue)
House = House('House.png', (Housex, Housey), WHITE, (89, 135), (Housex, Housey, 16, 27), MOVESPEED, Player)
Cursor = Pointer('Cursor.png', WHITE)
pygame.mouse.set_visible(False)
Menu = Menu('Menu.png', (500, 50), MOVESPEED, 'Selector.png')
Backgroundsprites = pygame.sprite.LayeredDirty(Map)
NPCs = pygame.sprite.LayeredDirty(NPC)
Players = pygame.sprite.LayeredDirty(Player)
Objects = pygame.sprite.LayeredDirty(Cursor)
Menus = pygame.sprite.LayeredDirty(Menu)
Houses = pygame.sprite.LayeredDirty(House)
Monkeyface = pygame.image.load('Monkeyface.png')
Monkeyface.set_colorkey(WHITE)

while 1:

    movement(DISPLAYSURF, Backgroundsprites, Players, Houses, NPCs, Objects, Menus)
    pygame.display.flip()