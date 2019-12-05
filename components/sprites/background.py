import pygame
import sys

SPEED = .07

class Background:

    def __init__(self):
        self.offsetX = 0
        self.image = pygame.image.load("{}/resources/images/{}.png".format(sys.path[0], "background"))

        size = pygame.display.get_surface().get_size()
        self.image = pygame.transform.scale(self.image, size)

    def update(self):
        w, h = pygame.display.get_surface().get_size()
        self.offsetX = (self.offsetX + SPEED) % w

    def render(self, window):
        w, h = pygame.display.get_surface().get_size()
        window.blit(self.image, (w - self.offsetX, 0))
        window.blit(self.image, (-self.offsetX, 0))
