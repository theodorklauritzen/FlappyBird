import pygame
import sys
import math

BIRD_SCALE = 2.5
BIRD_GRAVITY = .3
FLAP_TIME = 80

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

        self.targetXPos = self.pos.x

        self._floatFrame = 0
        self._flapFrame = 1

        self._updateSprite()

    def update(self):
        self.pos.add(self.vel)

        speedX = 1.5
        if(self.pos.x < self.targetXPos):
            self.pos.x += speedX
            if (self.pos.x > self.targetXPos):
                self.pos.x = self.targetXPos
        if(self.pos.x > self.targetXPos):
            self.pos.x -= speedX
            if (self.pos.x < self.targetXPos):
                self.pos.x = self.targetXPos


        self._updateSprite()

    def _updateSprite(self):
        index = 0
        flapTime = FLAP_TIME / 4
        if (
            (self._flapFrame > flapTime and self._flapFrame <= flapTime * 2) or
            (self._flapFrame > flapTime * 3 and self._flapFrame <= flapTime * 4)
            ):
            index = 1
        elif self._flapFrame > flapTime * 2 and self._flapFrame <= flapTime * 3:
            index = 2

        self._flapFrame += 1
        self._flapFrame %= flapTime * 4


        img = birdImages[index]

        w, h = img.get_size()
        self.size = (int(w * BIRD_SCALE), int(h * BIRD_SCALE))

        self.image = pygame.transform.scale(img, self.size)
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

        #self._flapFrame = 1

    def gravity(self):
        self.vel.y += BIRD_GRAVITY

    def hitPipes(self, pipes):
        for pipe in pipes:
            if pipe.rectHit(self.rect):
                return True

        w, h = pygame.display.get_surface().get_size()
        return (self.rect.bottom >= h - 90)

    def getPoint(self, pipes):
        ret = 0
        for pipe in pipes:
            ret += pipe.getPoint(self.rect)
        return ret
