import pygame
import components as cmp

SCREEN_DIMENSIONS = (500, 800)

# The main function for the flow of the program
def main():

    # Set up program
    # Init pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode(SCREEN_DIMENSIONS)
    # Change title and incon of the window
    pygame.display.set_caption("Flappy Bird")

    loop(window)

def loop(window):
    while True:

        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

        r = cmp.scenes.start(window)
        if (r == "QUIT"):
            return "QUIT"

if __name__ == "__main__":
    main()
