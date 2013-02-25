import pygame
from pygame.locals import *

pygame.init()


class Background(pygame.sprite.DirtySprite):          #Sprite for things that move in the background
    def __init__(self, image, (x, y), colorkey, MOVESPEED):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.colorkey = colorkey
        self.MOVESPEED = MOVESPEED
        self.image.set_colorkey(self.colorkey)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, movedir):
        if movedir == 'moveRight':
            self.x -= self.MOVESPEED
        elif movedir == 'moveLeft':
            self.x += self.MOVESPEED
        elif movedir == 'moveUp':
            self.y += self.MOVESPEED
        elif movedir == 'moveDown':
            self.y -= self.MOVESPEED
        pos = (self.x, self.y)
        self.rect.topleft = pos

    def update(self):
        self.dirty = 1


class Character(pygame.sprite.DirtySprite):
    def __init__(self, image, (x, y), colorkey):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.colorkey = colorkey
        self.x = x
        self.y = y
        self.image.set_colorkey(self.colorkey)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.dirty = 1


class House(pygame.sprite.DirtySprite):
    def __init__(self, image, (x, y), colorkey, adjustment, Door, MOVESPEED, Player): #Door must be in rect format
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.Player = Player
        self.adjustment = adjustment
        self.colorkey = colorkey
        self.Door = pygame.Rect(Door)
        self.MOVESPEED = MOVESPEED
        self.image.set_colorkey(self.colorkey)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, movedir):
        if movedir == 'moveRight':
            self.x -= self.MOVESPEED
        elif movedir == 'moveLeft':
            self.x += self.MOVESPEED
        elif movedir == 'moveUp':
            self.y += self.MOVESPEED
        elif movedir == 'moveDown':
            self.y -= self.MOVESPEED
        pos = (self.x, self.y)
        self.Door.topleft = (self.x + self.adjustment[0], self.y+self.adjustment[1])
        self.rect.topleft = pos
        self.dirty = 1

    def update(self):
        if self.Door.colliderect(self.Player.rect):
            self.Collision = True
        self.dirty = 1


class AnimatedSprite(pygame.sprite.DirtySprite):
    def __init__(self, moveLeftimages, moveRightimages, moveUpimages, moveDownimages, movedir, fps=0.3):
        pygame.sprite.Sprite.__init__(self)
        self.movedir = movedir
        self.moveLeftimages = moveLeftimages
        self.moveRightimages = moveRightimages
        self.moveUpimages = moveUpimages
        self.moveDownimages = moveDownimages
        self.start = 0
        self.delay = 10
        self.last_update = 0
        self.frame = 0
        self.framemax = 3
        self.img = self.moveDownimages[0]

    def update(self, movedir):
        if movedir == 'moveUp':
            if self.frame != 0:
                self.img = pygame.image.load(self.moveUpimages[self.frame])
                self.delay -= 1
                
                    

class Pointer(pygame.sprite.DirtySprite):
    def __init__(self, image, colorkey):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.colorkey = colorkey
        self.image.set_colorkey(self.colorkey)
        self.rect = self.image.get_rect(topleft=(pygame.mouse.get_pos()))
        self.dirty = 1

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.dirty = 1

    def Clicking(self):
        if pygame.event.get()[MOUSEBUTTONDOWN]: self.Clicking = True
        if pygame.event.get()[MOUSEBUTTONUP]: self.Clicking = False


class Menu(pygame.sprite.DirtySprite):
    def __init__(self, image, (x, y)):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def update(self):
        self.dirty = 1

class NPC(pygame.sprite.DirtySprite):    
    #Sprite for things that move in the background
    def __init__(self, image, (x, y), colorkey, MOVESPEED, Player, Dialogue):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.Collision = False
        self.Talk = False
        self.Dialogue = Dialogue
        self.Player = Player
        self.colorkey = colorkey
        self.MOVESPEED = MOVESPEED
        self.image.set_colorkey(self.colorkey)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, movedir):
        if movedir == 'moveRight':
            self.x -= self.MOVESPEED
        elif movedir == 'moveLeft':
            self.x += self.MOVESPEED
        elif movedir == 'moveUp':
            self.y += self.MOVESPEED
        elif movedir == 'moveDown':
            self.y -= self.MOVESPEED
        pos = (self.x, self.y)
        self.rect.topleft = pos

    def update(self):
        if self.rect.colliderect(self.Player.rect):
            self.Collision = True
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.Talk = True
        else:
            self.Collision = False
        if self.Talk:
            print self.Dialogue
            self.Talk = False
        self.dirty = 1
        
        


class Button(pygame.sprite.DirtySprite):
    def __init__(self, image, x, y, Output):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.Output = Output
        self.rect = self.image.get_rect()
        self.Click = False
    def update(self):
        Cursorpos = pygame.mouse.get_pos()
        if self.rect.collidepoint(Cursorpos):
            self.dirty = 1
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN: self.Click = True
                if event.type == MOUSEBUTTONUP: self.Click = False
        else:
            self.dirty = 0
    
    
        