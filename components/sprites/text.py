import pygame
import sys

fileMap = {
    "flappy bird": "flappyBird",
    "tap": "tap"
}

class Text:

    def __init__(self, text, pos, size):
        self.text = None
        self.image = None
        for key in fileMap:
            if(key == text):
                self.text = text
                self.image = pygame.image.load("{}/resources/images/{}.png".format(sys.path[0], fileMap[key]))
                break;

        if self.text == None:
            raise Exception("The text: {} is not valid".format(text))

        self.pos = pos
        self.image = pygame.transform.scale(self.image, size)

    def update(self):
        pass

    def draw(self, window):
        size = self.image.get_size()
        window.blit(self.image, (self.pos[0] - size[0] / 2, self.pos[1] - size[1] / 2))
