import pygame
import sys
import random

pygame.init()

windowheight = 500
windowwidth = 500

window = pygame.display.set_mode((windowwidth, windowheight))


def main():
    textfont = pygame.font.SysFont("arial", 40)

    running = True

    color = 'White'
    color2 = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    hazardx = 100
    hazardy = 100
    hazardspeed = 0.000001

    x = 200
    y = 200
    width = 20
    height = 20
    vel = 0.1

    X = 400
    Y = 400
    money = 0

    score = []

    highest = 0

    pygame.draw.rect(window, color2, pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()

    clock = pygame.time.Clock()

    dead = False
    active = False
    collected = True
    done = False

    start_ticks = pygame.time.get_ticks()

    while running:
        clock.tick()
        if dead == False:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        hazardxround = round(hazardx)
        hazardyround = round(hazardy)
        if collected == True:
            coinx = random.randint(20, windowwidth - 20)
            coiny = random.randint(20, windowheight - 20)
            collected = False
        window.fill(color)
        if seconds < 10:
            hazardspeed = 0.02
        elif seconds < 20:
            hazardspeed = 0.03
        elif seconds < 30:
            hazardspeed = 0.04
        elif seconds < 40:
            hazardspeed = 0.05
        elif seconds < 50:
            hazardspeed = 0.06
        img = textfont.render(str(money), True, (0, 0, 0))
        window.blit(img, (20, 20))
        if dead == True:
            text = ('You Lose')
            text2 = ('Press space to restart')
            highest = str(highest)
            text3 = (highest)
            text4 = ('Highscore:')
            textd1 = textfont.render(text, 1, (255, 0, 0))
            textd2 = textfont.render(text2, 1, (255, 0, 0))
            textd3 = textfont.render(text3, 1, (255, 0, 0))
            textd4 = textfont.render(text4, 1, (255, 0, 0))
            window.blit(textd1, (200, 200))
            window.blit(textd2, (70, 300))
            window.blit(textd3, (300, 400))
            window.blit(textd4, (100, 400))
        if dead == False:
            pygame.draw.circle(window, (255, 255, 38), (coinx, coiny), 10)
        if dead == False:
            pygame.draw.rect(window, (0, 0, 255), [hazardx, hazardy, 50, 50], 0)
            if hazardx > x:
                hazardx -= hazardspeed
            if hazardy > y:
                hazardy -= hazardspeed
            if hazardx < x:
                hazardx += hazardspeed
            if hazardy < y:
                hazardy += hazardspeed
        if x >= hazardxround and x <= hazardxround + 50:
            if y >= hazardyround and y <= hazardyround + 50:
                dead = True
        if dead == True and done == False:
            f = open('highscore.txt', 'r')
            score = []
            for line in f:
                line = line.strip('\n')
                if line != score:
                    score.append(line)
            done = True
            f.close()
            f = open('highscore.txt', 'w')
            for i in score:
                i = int(i)
                if i > highest:
                    highest = i
            money = int(money)
            if money > highest:
                money = str(money)
                f.write(money)
            else:
                highest = str(highest)
                f.write(highest)
            f.close()

        if x >= coinx and x <= coinx + 20:
            if y >= coiny and y <= coiny + 20:
                money = int(money)
                money += 1
                collected = True
        elif x + 20 >= coinx and x + 20 <= coinx + 20:
            if y + 20 >= coiny and y + 20 <= coiny + 20:
                money = int(money)
                money += 1
                collected = True
        if dead == False:
            pygame.draw.rect(window, (0, 0, 0), (x, y, width, height))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            y += vel
        if dead == True:
            if keys[pygame.K_SPACE]:
                main()


main()
