import pygame
import sys

# The speed for the background
SPEED = 1

# The background class
class Background:

    # Init the background
    def __init__(self):
        # Set the offset to 0
        self.offsetX = 0
        # Load the image
        self.image = pygame.image.load("{}/resources/images/{}.png".format(sys.path[0], "background"))

        # Scale the image to the screen
        size = pygame.display.get_surface().get_size()
        self.image = pygame.transform.scale(self.image, size)

    # Update the background
    def update(self):
        # Update the offset to simulate movement
        w, h = pygame.display.get_surface().get_size()
        self.offsetX = (self.offsetX + SPEED) % w

    # Draw the background
    def draw(self, window):
        w, h = pygame.display.get_surface().get_size()
        window.blit(self.image, (w - self.offsetX, 0))
        window.blit(self.image, (-self.offsetX, 0))
