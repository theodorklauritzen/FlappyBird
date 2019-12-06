import pygame

def start(window, sprites):

    Clock = pygame.time.Clock()

    background = sprites.Background()
    ground = sprites.Ground()
    bird = pygame.sprite.GroupSingle(sprites.Bird())

    while True:
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

        background.update()
        background.render(window)

        ground.update()
        ground.render(window)

        bird.update()
        bird.draw(window)

        # Update the screen
        pygame.display.update()
