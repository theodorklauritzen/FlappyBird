import pygame
import webbrowser

# The URL which the rate button opens
RATE_URL = "https://github.com/theodorklauritzen/FlappyBird"

# The gamveover scene function
def gameover(window, sprites, s):

    # init the clock
    Clock = pygame.time.Clock()

    # store sprites from previous scenes in variables
    bird = pygame.sprite.GroupSingle(s[0])
    background = s[1]
    ground = s[2]

    pipes = pygame.sprite.Group()
    for i in s[3]:
        pipes.add(i)

    # Print the score and create a number sprite
    score = s[4]
    print("SCORE: {}".format(score))
    w, h = pygame.display.get_surface().get_size()
    scoreSprite = pygame.sprite.GroupSingle(sprites.Number((w / 2, 270), (w, 50), score))

    # Create a gameover prite and make it slide in
    gaveoverText = sprites.Text("game over", (w / 2, 150), (400, 100))
    gaveoverText.slideFrom((w / 2, -50), 60)

    # The function which is executed when the start button is clicked
    def startBtn():
        # Create a new bird to send to the PLAY scene
        b = sprites.Bird((-20, (h - 90) / 2))
        b.targetXPos = 80

        # Return to main to start the PLAY scene
        return (
            "NEW_SCENE",
            "PLAY",
            b,
            background,
            ground
        )

    # The function which is executed when the rate button is clicked
    def rateBtn():
        # Open the rate URL in a webbrowser
        webbrowser.open(RATE_URL)

    # Create a button group, with a start and rate button
    buttons = pygame.sprite.Group()
    centerOff = 50
    yPos = 350
    size = (80, 40)
    buttons.add(sprites.Button("start", (w / 2 - centerOff, yPos), size, startBtn))
    buttons.add(sprites.Button("rate", (w / 2 + centerOff, yPos), size, rateBtn))

    # Remeber the start time
    startTime = pygame.time.get_ticks()

    # Start the loop for the gameover scene
    while True:
        # Prevent the game from running faster than 60 fps
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

            # If the mous is pressed sende the mouse position to all buttons, to check if they are clicked
            if (event.type == pygame.MOUSEBUTTONUP):
                for btn in buttons.sprites():
                    r = btn.mouseClick(pygame.mouse.get_pos())
                    # If the button returns a tuple with arguments for a new scene, return to main
                    if (
                        (not r is None) and
                        (type(r) == tuple) and
                        (len(r) >= 2) and
                        (r[0] == "NEW_SCENE")
                        ):
                        return r[1:]

            # If the keyboard is pressed, and the living time for the scene has passed 500 ms, start the PLAY scene
            if (event.type == pygame.KEYUP):
                if (pygame.K_SPACE and pygame.time.get_ticks() > 500 + startTime):
                    return startBtn()[1:]

        # Draw the background, all sprites and update the gameover text
        background.draw(window)
        pipes.draw(window)
        ground.draw(window)
        gaveoverText.update()
        gaveoverText.draw(window)
        buttons.draw(window)
        scoreSprite.draw(window)
        bird.draw(window)

        # Update the screen
        pygame.display.update()
