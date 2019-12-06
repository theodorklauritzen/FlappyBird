import pygame
import sys

fileMap = {
    "start": "start",
    "rate": "rate"
}

class Button(pygame.sprite.Sprite):

    def __init__(self, text, pos, size, callback = None):
        pygame.sprite.Sprite.__init__(self)

        self.text = None
        self.image = None
        for key in fileMap:
            if(key == text):
                self.text = text
                self.image = pygame.image.load("{}/resources/images/buttons/{}.png".format(sys.path[0], fileMap[key]))
                break;

        if self.text == None:
            raise Exception("The button: {} is not valid".format(text))

        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.callback = callback

    def update(self):
        pass

    def mouseClick(self, pos):
        if (self.rect.collidepoint(pos)):
            if (not self.callback is None):
                self.callback()
