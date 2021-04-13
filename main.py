# Pong Version 1.0 by Sebastian Reichl

import pygame as pg
from time import sleep
import random

WIDTH = 800
HEIGHT = 400
BORDER_LENGTH = 20
FRAMERATE = 50


class Border:
    def __init__(self, x, y, länge, breite):
        pg.draw.rect(screen, pg.Color("white"), pg.Rect(x, y, länge, breite))


class Ball:
    RADIUS = 10

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.moving = False

    def show(self, color):
        global screen
        pg.draw.circle(screen, color, (self.x, self.y), Ball.RADIUS)

    def update(self):
        global LIVES, SCORE, VELOCITY, pong
        if not self.moving:
            return
        newx = self.x + self.vx
        newy = self.y + self.vy
        if newx < BORDER_LENGTH+Ball.RADIUS:
            self.vx = -self.vx
        elif newy < BORDER_LENGTH+Ball.RADIUS or newy > HEIGHT-BORDER_LENGTH-Ball.RADIUS:
            self.vy = -self.vy
        elif newx+Ball.RADIUS > WIDTH-Paddle.WIDTH:
            if abs(newy-paddle.y) <= Paddle.HEIGHT//2:
                SCORE += 1
                VELOCITY += 0.5
                self.vx += 0.5
                self.vy += 0.5
                #pong.play()
                self.vx = -self.vx
            else:
                LIVES -= 1
                self.show(pg.Color("black"))
                self.__init__(WIDTH-Ball.RADIUS-Paddle.WIDTH, random.randint(BORDER_LENGTH+self.RADIUS, HEIGHT-BORDER_LENGTH-self.RADIUS), -VELOCITY, -VELOCITY)
                self.show(pg.Color("white"))
        else:
            self.show(pg.Color("black"))
            self.x = newx
            self.y = newy
            self.show(pg.Color("white"))


class Paddle:
    WIDTH = 20
    HEIGHT = 80

    def __init__(self, y):
        self.y = y

    def show(self, color):
        global screen
        pg.draw.rect(screen, color, pg.Rect(WIDTH-self.WIDTH, self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))

    def update(self):
        newy = pg.mouse.get_pos()[1]
        if BORDER_LENGTH+self.HEIGHT//2 <= newy <= HEIGHT-BORDER_LENGTH-self.HEIGHT//2:
            self.show(pg.Color("black"))
            self.y = newy
            self.show(pg.Color("white"))


def show(text, x, y):
    pg.font.init()
    font = pg.font.SysFont(pg.font.get_default_font(), 25)
    surf = font.render(text, False, pg.Color("black"), pg.Color("white"))
    screen.blit(surf, (x, y))


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(pg.Color("black"))
pg.display.set_caption("Pong 1.0 by Sebastian Reichl")
clock = pg.time.Clock()


def game():
    global ball, paddle, pong, LIVES, SCORE, VELOCITY, highscore
    LIVES = 5
    SCORE = 0
    VELOCITY = 8

    screen.fill(pg.Color("black"))
    border_top = Border(0, 0, WIDTH, BORDER_LENGTH)
    border_left = Border(0, 0, BORDER_LENGTH, HEIGHT)
    border_bottom = Border(0, HEIGHT-BORDER_LENGTH, WIDTH, BORDER_LENGTH)

    ball = Ball(WIDTH-Ball.RADIUS-Paddle.WIDTH, random.randint(BORDER_LENGTH+Ball.RADIUS, HEIGHT-BORDER_LENGTH-Ball.RADIUS), -VELOCITY, -VELOCITY)
    ball.show(pg.Color("white"))

    paddle = Paddle(HEIGHT//2)
    paddle.show(pg.Color("white"))

    # pong = pg.mixer.Sound("order_pong.wav")

    while True:
        if LIVES < 1:
            screen.fill(pg.Color("red"))
            show("YOU LOST!", 0, 0)
            if SCORE > int(highscore):
                highscore = SCORE
                file = open("data", "w")
                file.write(str(highscore))
                file.close()
                show("NEW HIGHSCORE!", WIDTH//2-20, HEIGHT//2)
            pg.display.flip()
            sleep(3)
            break
        else:
            show("Lives {}, Score {}".format(LIVES, SCORE), 0, 0)
            e = pg.event.poll()
            if e.type == pg.QUIT:
                pg.quit()
                quit()
            elif e.type == pg.MOUSEBUTTONDOWN:
                ball.moving = not ball.moving
            clock.tick(FRAMERATE)
            ball.update()
            paddle.update()
            pg.display.flip()
    main_menu()


def main_menu():
    global highscore
    file = open("data", "r")
    highscore = file.readline()
    file.close()
    if highscore == '':
        highscore = 0

    while True:
        screen.fill(pg.Color("black"))
        show("Main Menu", 0, 0)
        show("Play the Game", 85, 70)
        show(f"Your current highscore: {highscore}", 45, 160)

        mx, my = pg.mouse.get_pos()                     # get and safe mouse position

        button = pg.Rect(50, 100, 200, 50)              # button
        if button.collidepoint((mx, my)):
            if click:
                game()
        pg.draw.rect(screen, pg.Color("red"), button)
        click = False

        e = pg.event.poll()
        if e.type == pg.QUIT:
            pg.quit()
            quit()
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                click = True
        clock.tick(FRAMERATE)
        pg.display.flip()
    pg.quit()


main_menu()
