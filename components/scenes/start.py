import pygame

def start(window, sprites):

    Clock = pygame.time.Clock()

    background = sprites.Background()
    ground = sprites.Ground()
    w, h = pygame.display.get_surface().get_size()
    bird = pygame.sprite.GroupSingle(sprites.Bird((w / 2, (h - 90) / 2)))

    while True:
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

        background.update()
        background.draw(window)

        ground.update()
        ground.draw(window)

        bird.sprite.float()
        bird.update()
        bird.draw(window)

        # Update the screen
        pygame.display.update()
