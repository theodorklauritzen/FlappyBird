import pygame
import sys

# Set the speed and height constant
SPEED = 3
GROUND_HEIGHT = 90

# The Ground class
class Ground:

    height = GROUND_HEIGHT

    # Init the ground class
    def __init__(self):
        # Set the offset to 0
        self.offsetX = 0
        # load the image
        self.image = pygame.image.load("{}/resources/images/{}.png".format(sys.path[0], "ground"))

        # Scale the image
        windowSize = pygame.display.get_surface().get_size()
        imageSize = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (windowSize[0], int(imageSize[1] * windowSize[0] / imageSize[0])))

    # Update the offset to simulate movement
    def update(self):
        w, h = pygame.display.get_surface().get_size()
        # increate the offset and set it to 0 if it is over the width of the screen
        self.offsetX = (self.offsetX + SPEED) % w

    # Draw the ground
    def draw(self, window):
        w, h = pygame.display.get_surface().get_size()
        window.blit(self.image, (w - self.offsetX, h - self.height))
        window.blit(self.image, (-self.offsetX, h - self.height))
