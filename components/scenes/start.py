import pygame

def start(window, sprites, s):

    Clock = pygame.time.Clock()

    background = sprites.Background()
    ground = sprites.Ground()
    w, h = pygame.display.get_surface().get_size()
    bird = pygame.sprite.GroupSingle(sprites.Bird((w / 2, (h - 90) / 2)))

    w, h = pygame.display.get_surface().get_size()

    flappyText = sprites.Text("flappy bird", (w / 2, 150), (400, 100))
    tapText = sprites.Text("tap", (w / 2, 450), (200, 100))
    authorText = sprites.Text("Theodor 2G", (w / 2 + 130, 205), (100, 30))

    while True:
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

            if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN):
                bird.sprite.targetXPos = 80
                bird.sprite.jump()

                return (
                    "PLAY",
                    bird.sprite,
                    background,
                    ground
                )

        background.update()
        background.draw(window)

        ground.update()
        ground.draw(window)

        flappyText.draw(window)
        tapText.draw(window)
        authorText.draw(window)

        bird.sprite.float()
        bird.update()
        bird.draw(window)

        # Update the screen
        pygame.display.update()
