import pygame

def play(window, sprites, s):

    Clock = pygame.time.Clock()

    bird = pygame.sprite.GroupSingle(s[0])
    background = s[1]
    ground = s[2]

    pipes = pygame.sprite.Group()

    pipeDistance = 230
    speed = 3
    pipeTime = int(pipeDistance / speed)
    frame = 0

    score = 0
    w, h = pygame.display.get_surface().get_size()
    scoreSprite = pygame.sprite.GroupSingle(sprites.Number((w / 2, 50), (w, 50), score))

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
        p = bird.sprite.getPoint(pipes.sprites())
        if p > 0:
            score += p
            scoreSprite.sprite.setNum(score)

        scoreSprite.update()
        scoreSprite.draw(window)

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
