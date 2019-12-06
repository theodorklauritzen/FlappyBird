import pygame

def start(window, sprites):

    Clock = pygame.time.Clock()

    background = sprites.Background()
    ground = sprites.Ground()
    w, h = pygame.display.get_surface().get_size()
    bird = pygame.sprite.GroupSingle(sprites.Bird((w / 2, (h - 90) / 2)))

    w, h = pygame.display.get_surface().get_size()

    flappyText = sprites.Text("flappy bird", (w / 2, 150), (400, 100))
    tapText = sprites.Text("tap", (w / 2, 450), (200, 100))

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

        flappyText.draw(window)
        tapText.draw(window)

        bird.sprite.float()
        bird.update()
        bird.draw(window)

        # Update the screen
        pygame.display.update()
