import pygame

def start(window, sprites):

    background = sprites.Background()

    while True:
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

        background.update()
        background.render(window)

        # Update the screen
        pygame.display.update()
