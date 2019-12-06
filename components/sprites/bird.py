import pygame
import sys
import math

BIRD_XPOS = 100
BIRD_SCALE = 2.5
BIRD_GRAVITY = .3

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


    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector(0, 0)

        self._updateSprite()

        self._floatFrame = 0

    def update(self):
        self.pos.add(self.vel)

        self._updateSprite()

    def _updateSprite(self):
        w, h = birdImages[0].get_size()
        self.size = (int(w * BIRD_SCALE), int(h * BIRD_SCALE))

        self.image = pygame.transform.scale(birdImages[0], self.size)
        angle = math.atan(-self.vel.y * .1)
        self.image = pygame.transform.rotate(self.image, angle / math.pi * 180)
        self.rect = self.image.get_rect()

        self.rect.center = self.pos.get()

    def float(self):
        w, h = pygame.display.get_surface().get_size()
        self.pos.y = (h - 90) / 2 - math.sin(self._floatFrame / 120 * 2 * math.pi) * 30

        self._floatFrame += 1
        self._floatFrame %= 120

    def jump(self):
        self.vel.y = -7

    def gravity(self):
        self.vel.y += BIRD_GRAVITY
