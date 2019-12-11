import pygame
import sys
import random

SPACE = 150
PIPE_WIDTH = 65
PIPE_MARGIN = 60
POINT_OFFSET = 30

speed = 3

upperImage = pygame.image.load("{}/resources/images/pipes/{}.png".format(sys.path[0], "pipeUpper"))
lowerImage = pygame.image.load("{}/resources/images/pipes/{}.png".format(sys.path[0], "pipeLower"))

class Pipe(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        w, h = pygame.display.get_surface().get_size()
        self.image = pygame.Surface((PIPE_WIDTH, h), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = (w, 0)

        self.hight = PIPE_MARGIN + SPACE / 2 + random.random() * (h - 90 - 2 * PIPE_MARGIN - SPACE)

        uImgSize = upperImage.get_size()
        imgScale = PIPE_WIDTH / uImgSize[0]
        uImg = pygame.transform.scale(upperImage, (int(uImgSize[0] * imgScale), int(uImgSize[1] * imgScale)))
        uImgSize = uImg.get_size()
        self.image.blit(uImg, (0, self.hight - SPACE / 2 - uImgSize[1]))

        lImgSize = lowerImage.get_size()
        #imgScale = PIPE_WIDTH / lImgSize[0]
        lImg = pygame.transform.scale(lowerImage, (int(lImgSize[0] * imgScale), int(lImgSize[1] * imgScale)))
        self.image.blit(lImg, (0, self.hight + SPACE / 2))

        self.counted = False

    def update(self):
        self.rect.topleft = (self.rect.x - speed, 0)

        if(self.rect.right < 0):
            self.kill()

    def rectHit(self, rect):
        return (
            #self.rect.colliderect(rect) and
            (self.rect.left < rect.right) and
            (self.rect.right > rect.left) and
            (
                (self.hight - SPACE / 2 > rect.top) or
                (self.hight + SPACE / 2 < rect.bottom)
            )
        )

    def getPoint(self, rect):
        if (rect.left + POINT_OFFSET > self.rect.right and not self.counted):
            self.counted = True
            return 1
        return 0



    @staticmethod
    def setSpeed(_speed):
        speed = _speed
