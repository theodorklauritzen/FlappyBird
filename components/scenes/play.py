import pygame

def play(window, sprites, s):

    Clock = pygame.time.Clock()

    bird = pygame.sprite.GroupSingle(s[0])
    background = s[1]
    ground = s[2]

    pipes = pygame.sprite.Group()

    pipeDistance = 200
    speed = 2
    pipeTime = 200 / speed
    frame = 0

    score = 0

    while True:
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

            if (event.type == pygame.KEYDOWN):
                bird.sprite.jump()

        if (frame == 0):
            pipes.add(sprites.Pipe())

        frame = (frame + 1) % pipeTime

        background.update()
        background.draw(window)

        pipes.update()
        pipes.draw(window)

        ground.update()
        ground.draw(window)

        bird.sprite.gravity()
        hit = bird.sprite.hitPipes(pipes.sprites())
        score += bird.sprite.getPoint(pipes.sprites())
        bird.update()
        bird.draw(window)

        # Update the screen
        pygame.display.update()

        if hit:
            return (
                "GAMEOVER",
                bird.sprite,
                background,
                ground,
                pipes.sprites(),
                score
            )
