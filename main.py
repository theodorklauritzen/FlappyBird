import pygame

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

if __name__ == "__main__":
    main()
