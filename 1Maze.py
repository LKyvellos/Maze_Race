import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1820,980))
done = False

#player cords:
x=60
y=60
x1=310
y1=310
timer1 = time.time()
stopwatch1 = time.time()
timerUpdated = 0

timer2 = time.time()
stopwatch2 = time.time()
timerUpdated1 = 0

Highscore = 9999

clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((0,0,0))
    Font = pygame.font.SysFont("wacky", 120, True, True)
    Title = Font.render("L.K.Mazerunner ap ta lidl", True, (225,225,225))
    screen.blit(Title,(240,490))




    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]: y=y-5
    if pressed[pygame.K_s]: y=y+5
    if pressed[pygame.K_a]: x=x-5
    if pressed[pygame.K_d]: x=x+5

    if pressed[pygame.K_i]: y1=y1-5
    if pressed[pygame.K_k]: y1=y1+5
    if pressed[pygame.K_j]: x1=x1-5
    if pressed[pygame.K_l]: x1=x1+5

    player1 = pygame.draw.rect(screen, (101,205,205), pygame.Rect(x, y, 50, 50))
    player2 = pygame.draw.rect(screen, (200, 50, 205), pygame.Rect(x1, y1, 50, 50))

    wall1 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(0,0, 1820,50))
    wall2 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(0, 0, 50, 980))
    wall3 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(0, 930, 1820, 50))
    wall4 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(1770, 0, 50, 980))

    wall5 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(125,0, 50,300))
        #katw
    wall6 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(125, 250, 300, 50))
        #deksia
    wall7 = pygame.draw.rect(screen, (149,129,0), pygame.Rect(125,370, 50,450))
        #katw
    wall8 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(125, 370, 300, 50))
        #deksia
    wall9 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(125, 800, 350, 50))
        #deksia
    wall10 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(550, 800, 450, 50))
        #deksia
    wall11 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(425, 600, 50, 200))
        #panw
    wall12 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(425, 600, 400, 50))
        #deksia
    wall13 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(775, 250, 50, 350))
        #panw
    wall14 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(900, 250, 200, 50))
        # deksia
    wall15 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(900, 125, 500, 50))
        # deksia
    wall16 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(550, 710, 500, 20))
        #deksia
    wall17 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(1000, 710, 50, 300))
        #katw
    wall18 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(900, 250, 50, 475))
        #katw
    wall19 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(1175, 250, 500, 50))
        #deksia
    wall20 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(1175, 250, 50, 500))
        # katw
    wall21 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(1175, 825, 50, 200))
        # katw
    wall21 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(1500, 825, 50, 200))
        # katw
    wall22 = pygame.draw.rect(screen, (149, 129, 0), pygame.Rect(375, 250, 50, 170))
        # katw
    final = pygame.draw.rect(screen, (50, 200, 50), pygame.Rect(1715, 875, 50, 50))

    if player1.colliderect(wall1) or player1.colliderect(wall2) or player1.colliderect(wall3) or player1.colliderect(wall4) or player1.colliderect(wall5) or player1.colliderect(wall6) or player1.colliderect(wall7) or player1.colliderect(wall8) or player1.colliderect(wall9) or player1.colliderect(wall10) or player1.colliderect(wall11) or player1.colliderect(wall12) or player1.colliderect(wall13) or player1.colliderect(wall14) or player1.colliderect(wall15) or player1.colliderect(wall16) or player1.colliderect(wall17) or player1.colliderect(wall18) or player1.colliderect(wall19) or player1.colliderect(wall20) or player1.colliderect(wall21):
        if pressed[pygame.K_w]: y = y + 5
        if pressed[pygame.K_s]: y = y - 5
        if pressed[pygame.K_a]: x = x + 5
        if pressed[pygame.K_d]: x = x - 5

    if player1.colliderect(final):
        x = 60
        y = 60
        x1 = 310
        y1 = 310
        timer1 = time.time()
        timerUpdated = round(timer1 - stopwatch1,2)
        stopwatch1 = time.time()

    Font1 = pygame.font.SysFont("comicsansms", 20,True, True)
    Time1 = Font1.render("Time for player1: " + str(timerUpdated), True, (0,140,225))
    screen.blit(Time1,(100, 300))


    if player2.colliderect(wall1) or player2.colliderect(wall2) or player2.colliderect(wall3) or player2.colliderect(wall4) or player2.colliderect(wall5) or player2.colliderect(wall6) or player2.colliderect(wall7) or player2.colliderect(wall8) or player2.colliderect(wall9) or player2.colliderect(wall10) or player2.colliderect(wall11) or player2.colliderect(wall12) or player2.colliderect(wall13) or player2.colliderect(wall14) or player2.colliderect(wall15) or player2.colliderect(wall16) or player2.colliderect(wall17) or player2.colliderect(wall18) or player2.colliderect(wall19) or player2.colliderect(wall20) or player2.colliderect(wall21):
        if pressed[pygame.K_i]: y1 = y1 + 3
        if pressed[pygame.K_k]: y1 = y1 - 3
        if pressed[pygame.K_j]: x1 = x1 + 3
        if pressed[pygame.K_l]: x1 = x1 - 3

    if player2.colliderect(final):
        x1 = 310
        y1 = 310
        x = 60
        y = 60
        timer2 = time.time()
        timerUpdated1 = round(timer2 - stopwatch2,2)
        stopwatch2 = time.time()
    Font2 = pygame.font.SysFont("comicsansms", 20,True, True)
    Time2 = Font2.render("Time for player2: " + str(timerUpdated1), True, (0,140,225))
    screen.blit(Time2,(500, 300) )


    Font8 = pygame.font.SysFont("comicsansms", 20, True, True)
    Time8 = Font8.render("Highscore: " + str(Highscore), True, (0, 140, 225))
    screen.blit(Time8, (600, 100))

    if timerUpdated > timerUpdated1:
        Font3 = pygame.font.SysFont("comicsansms", 100, True, True)
        Time3 = Font3.render("player one wins", True, (0, 140, 225))
        screen.blit(Time3, (800, 100))

    elif timerUpdated < timerUpdated1:
        Font5 = pygame.font.SysFont("comicsansms", 100, True, True)
        Time5 = Font5.render("player two wins", True, (0, 140, 225))
        screen.blit(Time5, (800, 100))


    if timerUpdated < Highscore:
        Font6 = pygame.font.SysFont("comicsansms", 100, True, True)
        Time6 = Font6.render("New Highscore from player 1" + str(timerUpdated), True, (0, 140, 225))
        screen.blit(Time6, (900, 100))
        Highscore = timerUpdated
    if timerUpdated1 < Highscore:
        Font7 = pygame.font.SysFont("comicsansms", 100, True, True)
        Time7 = Font7.render("New Highscore from player 2" + str(timerUpdated1), True, (0, 140, 225))
        screen.blit(Time7, (900, 100))
        Highscore = timerUpdated1


    pygame.display.flip()
    clock.tick(60)


