import pygame
import sys
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
    def __init__(self, image, (x, y), colorkey, adjustment, Door, MOVESPEED): #Door must be in rect format
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
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
        self.dirty = 1


class AnimatedSprite(pygame.sprite.DirtySprite):
    def __init__(self, images, fps=0.3):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.start = pygame.time.get_ticks()
        self.delay = 1000 / fps
        self.last_update = 0
        self.frame = 0
        self.update(pygame.time.get_ticks())

    def update(self, t):
        if t - self.last_update > self.delay:
            self.frame += 1
            if self.frame >= len(self.images):
                self.frame = 0
            self.image = self.images[self.frame]
            self.last_update = t


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
    def __init__(self, image, (x, y), MOVESPEED, selectorimage):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.MOVESPEED = MOVESPEED
        self.selectorimage = pygame.image.load(selectorimage)
        self.selectorrect = self.selectorimage.get_rect()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self, movedir, surface):
        if movedir == 'moveUp':
            self.y += self.MOVESPEED
        elif movedir == 'moveRight':
            self.x -= self.MOVESPEED
        elif movedir == 'moveDown':
            self.y -= self.MOVESPEED
        elif movedir == 'moveLeft':
            self.x += self.MOVESPEED

        pos = (self.x, self.y)
        self.selectorrect.topleft = pos
        surface.blit(self.selectorimage, pos)
        self.dirty = 1
    def update(self):
        self.dirty = 1
