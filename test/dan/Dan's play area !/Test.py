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
Ix, Iy = 335, 175
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
Interior = Background('Interior.png', (Ix, Iy), WHITE, MOVESPEED)
pygame.mouse.set_visible(False)
Backgroundsprites = pygame.sprite.LayeredDirty(Map)
NPCs = pygame.sprite.LayeredDirty(NPC)
Players = pygame.sprite.LayeredDirty(Player)
Objects = pygame.sprite.LayeredDirty(Cursor)
Houses = pygame.sprite.LayeredDirty(House)
Monkeyface = pygame.image.load('Monkeyface.png')
Monkeyface.set_colorkey(WHITE)
InHouse = False
Interiors = pygame.sprite.LayeredDirty(Interior)
Empty = pygame.sprite.LayeredDirty()
Clock = pygame.time.Clock()
MockOutput = DISPLAYSURF.blit(pygame.image.load('Walk 1.png'), (500, 200))
InvButton = Button('Select.png', 750, 150, MockOutput)
Buttonlist = pygame.sprite.LayeredDirty(InvButton)
fps = 60
MenuOpen = False
while 1:

    movement(DISPLAYSURF, Backgroundsprites, Players, Houses, NPCs, Objects)
    
    if Player.rect.colliderect(NPC.rect):
        DISPLAYSURF.blit(Exclaimation, (NPC.x-5, NPC.y-50))
    if Player.rect.colliderect(House.Door):
        InHouse = True
    while MenuOpen:
        UpdateDirty((Backgroundsprites, Houses, NPCs, Players, Empty), DISPLAYSURF)
        OpenMenu('Menu.png', (750, 50), 'Select.png', (750, 50), Buttonlist, WHITE, DISPLAYSURF, 50)
        UpdateDirty((Objects), DISPLAYSURF)
        pygame.display.flip()
    pygame.display.flip()
    Clock.tick(fps)
    while InHouse == True:
        movement(DISPLAYSURF, Interiors, Players, Empty, Empty, Objects)
        pygame.display.flip()
        Clock.tick(fps)