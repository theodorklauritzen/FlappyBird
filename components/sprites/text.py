import pygame
import sys

fileMap = {
    "flappy bird": "flappyBird",
    "tap": "tap",
    "game over": "gameover"
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
        self._targetPos = self.pos
        self._timeLeft = 0
        self.image = pygame.transform.scale(self.image, size)

    def update(self):
        amount = .3
        dir = [
            (self._targetPos[0] - self.pos[0]) * amount,
            (self._targetPos[1] - self.pos[1]) * amount
        ]

        self.pos = (
            self.pos[0] + dir[0],
            self.pos[1] + dir[1]
        )


    def draw(self, window):
        size = self.image.get_size()
        window.blit(self.image, (self.pos[0] - size[0] / 2, self.pos[1] - size[1] / 2))

    def slideIn(self, pos, time):
        self.pos = pos
        self._timeLeft = time
