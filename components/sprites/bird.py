import pygame
import sys
import math

# Set bird constants
BIRD_SCALE = 2.5
BIRD_GRAVITY = .3
FLAP_TIME = 80

# Load the bird animation images
birdImages = []
for i in range(3):
    birdImages.append(pygame.image.load("{}/resources/images/bird/{}{}.png".format(sys.path[0], "bird", i)))

# Create a Vector class to store position and velocity
class Vector:

    # Init the vector
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add a vector to this vector
    def add(self, v):
        self.x += v.x
        self.y += v.y

    # get the vector as a list
    def get(self):
        return [self.x, self.y]

# The bird sprite class
class Bird(pygame.sprite.Sprite):

    # Init the bird sprite class
    def __init__(self, pos):
        # Init the extended sprite class
        pygame.sprite.Sprite.__init__(self)

        # Set the position and velocity
        self.pos = Vector(pos[0], pos[1])
        self.vel = Vector(0, 0)

        # set the startXPos to the x position
        self.targetXPos = self.pos.x

        # Reset the frame count for animations
        self._floatFrame = 0
        self._flapFrame = 1

        # Update the extended sprite class, to match the bird class
        self._updateSprite()

    def update(self):
        self.pos.add(self.vel)

        speedX = 1.5
        if(self.pos.x < self.targetXPos):
            self.pos.x += speedX
            if (self.pos.x > self.targetXPos):
                self.pos.x = self.targetXPos
        if(self.pos.x > self.targetXPos):
            self.pos.x -= speedX
            if (self.pos.x < self.targetXPos):
                self.pos.x = self.targetXPos


        self._updateSprite()

    # Update the extended sprite class from the current bird class
    def _updateSprite(self):
        # Set the image to the correct frame to animate flapping
        index = 0
        flapTime = FLAP_TIME / 4
        if (
            (self._flapFrame > flapTime and self._flapFrame <= flapTime * 2) or
            (self._flapFrame > flapTime * 3 and self._flapFrame <= flapTime * 4)
            ):
            index = 1
        elif self._flapFrame > flapTime * 2 and self._flapFrame <= flapTime * 3:
            index = 2

        # Increase the flap frame count, and set it back to 0 if it increases over the FLAP_TIME
        self._flapFrame += 1
        self._flapFrame %= flapTime * 4

        # Get the image
        img = birdImages[index]

        # Find the size
        w, h = img.get_size()
        self.size = (int(w * BIRD_SCALE), int(h * BIRD_SCALE))

        # Scale up the image
        self.image = pygame.transform.scale(img, self.size)
        # Rotate the bird to the correct angle
        angle = math.atan(-self.vel.y * .1)
        self.image = pygame.transform.rotate(self.image, angle / math.pi * 180)
        # Update the position of the extended sprite class
        self.rect = self.image.get_rect()

        self.rect.center = self.pos.get()

    # Animate floating
    def float(self):
        # Calculate the y position
        w, h = pygame.display.get_surface().get_size()
        self.pos.y = (h - 90) / 2 - math.sin(self._floatFrame / 120 * 2 * math.pi) * 30

        # Increate the float frame count and set it back to 0 if it increases over 2 seconds
        self._floatFrame += 1
        self._floatFrame %= 120

    # Make the bird jump
    def jump(self):
        # Set the velocity to make the bird go upwards
        self.vel.y = -7

        #self._flapFrame = 1

    # Apply gravity to the bird
    def gravity(self):
        # Make the bird accelerate downwards
        self.vel.y += BIRD_GRAVITY

    # Test if the bird hits any pipe
    def hitPipes(self, pipes):
        for pipe in pipes:
            # Check if the bird hits the current pipe
            if pipe.rectHit(self.rect):
                # Return true if the bird hit the pipe
                return True

        # Return true if the bird has fallen bellow th ground
        w, h = pygame.display.get_surface().get_size()
        return (self.rect.bottom >= h - 90)

    # Check if the bird should should get a new point
    def getPoint(self, pipes):
        # return the sum of alle the points the bird should get.
        ret = 0
        for pipe in pipes:
            # Add the points from each pipe
            ret += pipe.getPoint(self.rect)
        return ret
