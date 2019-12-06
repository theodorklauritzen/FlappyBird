import pygame
import components as cmp
import sys

SCREEN_DIMENSIONS = (500, 700)

# The main function for the flow of the program
def main():

    # Set up program
    # Init pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode(SCREEN_DIMENSIONS)
    # Change title and incon of the window
    pygame.display.set_caption("Flappy Bird")

    icon = pygame.image.load("{}/resources/images/bird/{}.png".format(sys.path[0], "bird0"))
    pygame.display.set_icon(icon)

    loop(window)

    pygame.quit()

def loop(window):
    while True:

        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

        r = cmp.scenes.start(window, cmp.sprites)
        if (r == "QUIT"):
            return "QUIT"

        if (r[0] != "PLAY"):
            raise Excpetion("the start scene should return QUIT or a list with \"PLAY\"")

        r = cmp.scenes.play(window, cmp.sprites, r[1:])
        if (r == "QUIT"):
            return "QUIT"

if __name__ == "__main__":
    main()
