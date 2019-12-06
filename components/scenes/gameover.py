import pygame
import webbrowser

RATE_URL = "https://github.com/theodorklauritzen"

def gameover(window, sprites, s):

    Clock = pygame.time.Clock()

    bird = pygame.sprite.GroupSingle(s[0])
    background = s[1]
    ground = s[2]

    pipes = pygame.sprite.Group()
    for i in s[3]:
        pipes.add(i)

    score = s[4]
    w, h = pygame.display.get_surface().get_size()
    scoreSprite = pygame.sprite.GroupSingle(sprites.Number((w / 2, 270), (w, 50), score))

    gaveoverText = sprites.Text("game over", (w / 2, 150), (400, 100))
    gaveoverText.slideFrom((w / 2, -50), 60)

    def startBtn():
        

    def rateBtn():
        webbrowser.open(RATE_URL)

    buttons = pygame.sprite.Group()
    centerOff = 50
    yPos = 350
    size = (80, 40)
    buttons.add(sprites.Button("start", (w / 2 - centerOff, yPos), size, startBtn))
    buttons.add(sprites.Button("rate", (w / 2 + centerOff, yPos), size, rateBtn))

    while True:
        Clock.tick_busy_loop(60)
        # Loop through all events in pygame
        for event in pygame.event.get():

            # Stop the loop if pygame wants to quit
            if (event.type == pygame.QUIT):
                return "QUIT"

            if (event.type == pygame.MOUSEBUTTONUP):
                for btn in buttons.sprites():
                    btn.mouseClick(pygame.mouse.get_pos())

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
