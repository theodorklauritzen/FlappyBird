import pygame

def start(window):

    while True:
        # Fill the background
        window.fill((255, 255, 255))

        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

        # Update the screen
        pygame.display.update()
