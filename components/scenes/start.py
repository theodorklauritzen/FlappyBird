import pygame

# The start scene function, for the start of the game
def start(window, sprites, s):

    # init the clock
    Clock = pygame.time.Clock()

    # Create the background, and a bird sprite
    background = sprites.Background()
    ground = sprites.Ground()
    w, h = pygame.display.get_surface().get_size()
    bird = pygame.sprite.GroupSingle(sprites.Bird((w / 2, (h - 90) / 2)))

    w, h = pygame.display.get_surface().get_size()

    # Create text sprites
    flappyText = sprites.Text("flappy bird", (w / 2, 150), (400, 100))
    tapText = sprites.Text("tap", (w / 2, 450), (200, 100))
    authorText = sprites.Text("Theodor 2G", (w / 2 + 130, 205), (100, 30))

    # Start the loop for the start scene
    while True:
        # Prevent the game from running faster than 60 fps
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

            # If the keyboard is pressed or the mouse is pressed, start the PLAY scene
            if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN):
                # Change the XPos to the bird
                bird.sprite.targetXPos = 80
                # Make the bird jump
                bird.sprite.jump()

                # return to main, and start the PLAY scene
                return (
                    "PLAY",
                    bird.sprite,
                    background,
                    ground
                )

        # Update and draw the background and all sprites
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
