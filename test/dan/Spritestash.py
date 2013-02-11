import pygame
import sys
from pygame.locals import *

pygame.init()


class Background(pygame.sprite.Sprite):          #Sprite for moving backgrounds
    def __init__(self, image, (x, y), WIDTH, HEIGHT, MOVESPEED):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.Mapx = x
        self.Mapy = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.rect = (self.Mapx, self.Mapy, self.WIDTH, self.HEIGHT, 603)
        self.MOVESPEED = MOVESPEED

    def move(self, movedir):
        if movedir == 2:
            self.Mapx -= self.MOVESPEED
        elif movedir == 4:
            self.Mapx += self.MOVESPEED
        elif (movedir == 1):
            self.Mapy += self.MOVESPEED
        elif (movedir == 3):
            self.Mapy -= self.MOVESPEED

    def update(self, surface):
        surface.blit(self.image, (self.Mapx, self.Mapy))


class Character(pygame.sprite.Sprite):
    def __init__(self, image, (x, y), Colorkey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.Colorkey = Colorkey
        self.x = x
        self.y = y
        self.image.set_colorkey(self.Colorkey)
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
    def update(self, surface):
        surface.blit(self.image, (self.x, self.y))


class NPC(pygame.sprite.Sprite):
    def __init__(self, image, (x, y), colorkey,  MOVESPEED):
        pygame.sprite.Sprite.__init__(self)
        self.NPCx = x
        self.NPCy = y
        self.topleft = (self.NPCx, self.NPCy)
        self.MOVESPEED = MOVESPEED
        self.image = pygame.image.load(image)
        self.colorkey = colorkey
        self.image.set_colorkey(self.colorkey)
        self.rect = self.image.get_rect(topleft = (self.topleft))
    def move(self, movedir):
        if movedir == 2:
            self.NPCx -= self.MOVESPEED
        elif movedir == 4:
            self.NPCx += self.MOVESPEED
        elif movedir == 1:
            self.NPCy += self.MOVESPEED
        elif movedir == 3:
            self.NPCy -= self.MOVESPEED
    def update(self, surface):
        surface.blit(self.image, (self.NPCx, self.NPCy))


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps=0.3):
        pygame.sprite.Sprite.__init__(self)
        self._images = images
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0
        self.update(pygame.time.get_ticks())

    def update(self, t):
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images):
                self._frame = 0
            self.image = self._images[self._frame]
            self._last_update = t


class Pointer(pygame.sprite.Sprite):
    def __init__(self, image, Colorkey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.Colorkey = Colorkey
        self.image.set_colorkey(self.Colorkey)
        self.rect = self.image.get_rect()

    def update(self, surface):
        pos = pygame.mouse.get_pos()
        surface.blit(self.image, pos)

