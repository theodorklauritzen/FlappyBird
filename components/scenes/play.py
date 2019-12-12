import pygame

# The play scene function
def play(window, sprites, s):

    # init the clock
    Clock = pygame.time.Clock()

    # store sprites from previous scenes in variables
    bird = pygame.sprite.GroupSingle(s[0])
    background = s[1]
    ground = s[2]

    # Create a pipe group
    pipes = pygame.sprite.Group()

    # Set pipe constants, and set the framcount to 0
    pipeDistance = 230
    speed = 3
    pipeTime = int(pipeDistance / speed)
    frame = 0

    # Create a score variable, and a number sprite with the score
    score = 0
    w, h = pygame.display.get_surface().get_size()
    scoreSprite = pygame.sprite.GroupSingle(sprites.Number((w / 2, 50), (w, 50), score))

    # Start the loop for the play scene
    while True:
        # Prevent the game from running faster than 60 fps
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

            # If any key is pressed, make the bird jump
            if (event.type == pygame.KEYDOWN):
                bird.sprite.jump()

        # If the frame count is 0, add a new pipe
        if (frame == 0):
            pipes.add(sprites.Pipe())

        # Increment the frame count, and set it to 0 if it has passed the pipeTime
        frame = (frame + 1) % pipeTime

        # Update and draw background and alle sprites
        background.update()
        background.draw(window)

        pipes.update()
        pipes.draw(window)

        ground.update()
        ground.draw(window)

        # Apply gravity to the bird
        bird.sprite.gravity()
        # Check ig the bird has hit a pipe
        hit = bird.sprite.hitPipes(pipes.sprites())
        # Check if the score should increment
        p = bird.sprite.getPoint(pipes.sprites())
        # Increment the score if the bird has got a new point
        if p > 0:
            score += p
            # Set the number sprite to show the new score
            scoreSprite.sprite.setNum(score)

        # Update and draw the number sprite
        scoreSprite.update()
        scoreSprite.draw(window)

        # Update and draw the bird
        bird.update()
        bird.draw(window)

        # Update the screen
        pygame.display.update()

        # If the bird has collided with a pipe, return to main and sytart the gameover scene
        if hit:
            return (
                "GAMEOVER",
                bird.sprite,
                background,
                ground,
                pipes.sprites(),
                score
            )
