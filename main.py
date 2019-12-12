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

    # Load and set the icon
    icon = pygame.image.load("{}/resources/images/bird/{}.png".format(sys.path[0], "bird0"))
    pygame.display.set_icon(icon)

    # start the game scenes
    loop(window)

    # Quit pygame, to prepare to stop the game
    pygame.quit()

def loop(window):
    # Set the first scene
    r = ["START"]

    while True:
        # Run the game until one scene asks to quit
        # Start the next scene

        if r[0] == "START":
            r = cmp.scenes.start(window, cmp.sprites, r[1:])
        elif r[0] == "PLAY":
            r = cmp.scenes.play(window, cmp.sprites, r[1:])
        elif r[0] == "GAMEOVER":
            r = cmp.scenes.gameover(window, cmp.sprites, r[1:])
        else:
            # Raise an error if teh next scene is invalid
            raise Exception("The scene {} is not valid".format(r[0]))

        # Quit the game if one scenes asks to quit the game
        if (r == "QUIT"):
            return "QUIT"

# start the main function if the file is not imported as a library
if __name__ == "__main__":
    main()
