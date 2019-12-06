import pygame

def play(window, sprites, s):

    Clock = pygame.time.Clock()

    bird = pygame.sprite.GroupSingle(s[0])
    background = s[1]
    ground = s[2]

    while True:
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

            if (event.type == pygame.KEYDOWN):
                bird.sprite.jump()

        background.update()
        background.draw(window)

        ground.update()
        ground.draw(window)

        bird.sprite.gravity()
        bird.update()
        bird.draw(window)

        # Update the screen
        pygame.display.update()
