import pygame
import sys

SPEED = 2
GROUND_HIGHT = 90

class Ground:

    hight = GROUND_HIGHT

    def __init__(self):
        self.offsetX = 0
        self.image = pygame.image.load("{}/resources/images/{}.png".format(sys.path[0], "ground"))

        windowSize = pygame.display.get_surface().get_size()
        imageSize = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (windowSize[0], int(imageSize[1] * windowSize[0] / imageSize[0])))

    def update(self):
        w, h = pygame.display.get_surface().get_size()
        self.offsetX = (self.offsetX + SPEED) % w

    def draw(self, window):
        w, h = pygame.display.get_surface().get_size()
        window.blit(self.image, (w - self.offsetX, h - self.hight))
        window.blit(self.image, (-self.offsetX, h - self.hight))
