import pygame
import sys
import math

# Set the constants for the Number class
SPACE_BETWEEN_DIGITS = 3

# Load the number images
numImages = []
for i in range(10):
    numImages.append(pygame.image.load("{}/resources/images/numbers/{}.png".format(sys.path[0], i)))

# The Number sprite class
class Number(pygame.sprite.Sprite):

    # Init the Number sprite class
    def __init__(self, pos, size, num = 0):
        # Init the extended sprite class
        pygame.sprite.Sprite.__init__(self)

        # Create a surface to draw on
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Set the digit size
        w, h = numImages[0].get_size()
        scale = size[1] / h
        self._digitSize = (int(w * scale), size[1])

        # Set the current number to num
        self.setNum(num)

    def setNum(self, num):
        # Set the local num to to given num
        self.num = num

        # Calculate the numer of digits
        log = 0
        if num > 0:
            log = math.log10(num)
        digitsNum = math.floor(log + 1)

        # Create a reversed list with all the digits
        digits = []
        currNum = num
        for i in range(digitsNum):
            digits.append(currNum % 10)
            currNum = currNum // 10

        # Create a list with all the images in the correct order
        digitImgs = []
        for i in reversed(digits):
            digitImgs.append(numImages[i])

        # Fill the suface to alpha
        self.image.fill((0, 0, 0, 0))

        # Calculate the numer size in pixels
        totalLength = (self._digitSize[0] + SPACE_BETWEEN_DIGITS) * len(digitImgs) - SPACE_BETWEEN_DIGITS
        # Calculate the start position of the drawing
        startPos = (self.rect.w - totalLength) / 2

        # Draw the digit images on the surface
        for i in range(0, len(digitImgs)):
            img = pygame.transform.scale(digitImgs[i], self._digitSize)
            self.image.blit(img, (startPos + i * (self._digitSize[0] + SPACE_BETWEEN_DIGITS), 0))

    # Update the Number sprite
    def update(self):
        pass
