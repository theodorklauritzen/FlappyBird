import pygame
import sys

BIRD_XPOS = 100

birdImages = []
for i in range(3):
    birdImages.append(pygame.image.load("{}/resources/images/bird/{}{}.png".format(sys.path[0], "bird", i)))


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def get(self):
        return [self.x, self.y]

class Bird(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        w, h = pygame.display.get_surface().get_size()
        self.pos = Vector(BIRD_XPOS, (h - 90) / 2)
        self.vel = Vector(0, 0)

        self.image = birdImages[0].copy()
        self.rect = self.image.get_rect()

    def update(self):
        self.pos.add(self.vel)

        self._updateSpritePos()

    def _updateSpritePos(self):
        self.rect.center = self.pos.get()
