import pygame
import sys

# set the file mat to which files that could be loaded
fileMap = {
    "start": "start",
    "rate": "rate"
}

# The button sprite class
class Button(pygame.sprite.Sprite):

    # Init the button sprite class
    def __init__(self, text, pos, size, callback = None):
        # Init the extended sprite class
        pygame.sprite.Sprite.__init__(self)

        # Set the text to the gived text
        self.text = None
        self.image = None
        # Search for the given text in the fileMap
        for key in fileMap:
            if(key == text):
                # Set the text, and image
                self.text = text
                self.image = pygame.image.load("{}/resources/images/buttons/{}.png".format(sys.path[0], fileMap[key]))
                break;

        # Raise an exception if the text is invalid
        if self.text == None:
            raise Exception("The button: {} is not valid".format(text))

        # scale the image
        self.image = pygame.transform.scale(self.image, size)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.callback = callback

    # Update the text
    def update(self):
        pass

    # Check if the position if inside the button and execute the callback
    def mouseClick(self, pos):
        if (self.rect.collidepoint(pos)):
            if (not self.callback is None):
                return self.callback()
