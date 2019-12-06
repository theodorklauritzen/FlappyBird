import pygame
import sys
import math

SPACE_BETWEEN_DIGITS = 3

numImages = []
for i in range(10):
    numImages.append(pygame.image.load("{}/resources/images/numbers/{}.png".format(sys.path[0], i)))

class Number(pygame.sprite.Sprite):

    def __init__(self, pos, size, num = 0):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        w, h = numImages[0].get_size()
        scale = size[1] / h
        self._digitSize = (int(w * scale), size[1])

        self.setNum(num)

    def setNum(self, num):
        self.num = num

        log = 0
        if num > 0:
            log = math.log10(num)
        digitsNum = math.floor(log + 1)
        digits = []
        currNum = num
        for i in range(digitsNum):
            digits.append(currNum % 10)
            currNum = currNum // 10

        digitImgs = []
        for i in reversed(digits):
            digitImgs.append(numImages[i])

        self.image.fill((0, 0, 0, 0))

        totalLength = (self._digitSize[0] + SPACE_BETWEEN_DIGITS) * len(digitImgs) - SPACE_BETWEEN_DIGITS
        startPos = (self.rect.w - totalLength) / 2

        for i in range(0, len(digitImgs)):
            img = pygame.transform.scale(digitImgs[i], self._digitSize)
            self.image.blit(img, (startPos + i * (self._digitSize[0] + SPACE_BETWEEN_DIGITS), 0))


    def update(self):
        pass
