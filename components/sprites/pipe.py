import pygame
import sys
import random

# Set the constants
SPACE = 150
PIPE_WIDTH = 65
PIPE_MARGIN = 60
POINT_OFFSET = 30

# Set the speed
speed = 3

# Load the sprite images
upperImage = pygame.image.load("{}/resources/images/pipes/{}.png".format(sys.path[0], "pipeUpper"))
lowerImage = pygame.image.load("{}/resources/images/pipes/{}.png".format(sys.path[0], "pipeLower"))

# The pipe class which extends the pygame sprite class
class Pipe(pygame.sprite.Sprite):

    # Init the Pipe sprite class
    def __init__(self):
        # Init the sprite class
        pygame.sprite.Sprite.__init__(self)

        # Create a surface with a constant width, and a height as the screen
        w, h = pygame.display.get_surface().get_size()
        self.image = pygame.Surface((PIPE_WIDTH, h), pygame.SRCALPHA)
        # Set the position to outside the screen at the right side
        self.rect = self.image.get_rect()
        self.rect.topleft = (w, 0)

        # Calculate the height of the space
        self.hight = PIPE_MARGIN + SPACE / 2 + random.random() * (h - 90 - 2 * PIPE_MARGIN - SPACE)

        # Scale the upper image, and draw it on the surface at the correct place
        uImgSize = upperImage.get_size()
        # Calculate the scale for the pipe images
        imgScale = PIPE_WIDTH / uImgSize[0]
        uImg = pygame.transform.scale(upperImage, (int(uImgSize[0] * imgScale), int(uImgSize[1] * imgScale)))
        uImgSize = uImg.get_size()
        self.image.blit(uImg, (0, self.hight - SPACE / 2 - uImgSize[1]))

        # Scale the lower image and draw it on the surface at the correct place
        lImgSize = lowerImage.get_size()
        #imgScale = PIPE_WIDTH / lImgSize[0]
        lImg = pygame.transform.scale(lowerImage, (int(lImgSize[0] * imgScale), int(lImgSize[1] * imgScale)))
        self.image.blit(lImg, (0, self.hight + SPACE / 2))

        # Set the counted valiable to False
        # this is used to check if it is counted in the score
        self.counted = False

    # Update the position of the pipe
    def update(self):
        self.rect.topleft = (self.rect.x - speed, 0)

        # If the pipe is outside the screen at the left side, kill the sprite
        if(self.rect.right < 0):
            self.kill()

    # Check if a rect collides with the pipe
    def rectHit(self, rect):
        # Return true if the rect is colliding with the pipe
        return (
            #self.rect.colliderect(rect) and
            (self.rect.left < rect.right) and
            (self.rect.right > rect.left) and
            (
                (self.hight - SPACE / 2 > rect.top) or
                (self.hight + SPACE / 2 < rect.bottom)
            )
        )

    # Check if the has passed the pipe, and should get a point
    def getPoint(self, rect):
        if (rect.left + POINT_OFFSET > self.rect.right and not self.counted):
            # Add the points for this pipe and mark the pipe as counted
            self.counted = True
            return 1
        return 0

    # Set the speed of all pipes
    @staticmethod
    def setSpeed(_speed):
        speed = _speed
