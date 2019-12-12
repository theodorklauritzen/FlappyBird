import pygame
import sys

# Set the fileMap
fileMap = {
    "flappy bird": "flappyBird",
    "tap": "tap",
    "game over": "gameover",
    "Theodor 2G": "Theodor2G"
}

# The text class to draw text images at the screen
class Text:

    # Init the class
    def __init__(self, text, pos, size):
        # Search for the correct text image
        self.text = None
        self.image = None
        for key in fileMap:
            if(key == text):
                # Set the correct image and text to the given text
                self.text = text
                self.image = pygame.image.load("{}/resources/images/{}.png".format(sys.path[0], fileMap[key]))
                break;

        # Raise error if the text is invalid
        if self.text == None:
            raise Exception("The text: {} is not valid".format(text))

        # Set the position and target position
        self.pos = pos
        self._targetPos = self.pos
        # Set the animation time to 0
        self._timeLeft = 0
        # Scale the text image
        self.image = pygame.transform.scale(self.image, size)

    # Update the text animation
    def update(self):
        # If a slide animation is running, make it slide fancy
        amount = .3
        dir = [
            (self._targetPos[0] - self.pos[0]) * amount,
            (self._targetPos[1] - self.pos[1]) * amount
        ]

        # Update the position of the text
        self.pos = (
            self.pos[0] + dir[0],
            self.pos[1] + dir[1]
        )

    # Draw the text at the screen
    def draw(self, window):
        size = self.image.get_size()
        window.blit(self.image, (self.pos[0] - size[0] / 2, self.pos[1] - size[1] / 2))

    # start a slide animation
    def slideFrom(self, pos, time):
        self.pos = pos
        self._timeLeft = time
