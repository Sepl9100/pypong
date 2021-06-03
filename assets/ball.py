from engine.entity import *
from GLOBAL import *


class Ball:
    def __init__(self, x, y, vx, vy, borders, paddle, host):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.host = host
        self.borders = borders
        self.paddle = paddle
        self.moving = False
        self.radius = 10
        self.lives = 5
        self.score = 0
        self.v_increase_per_score = 0.5

        self.entity = Entity(self.x, self.y, self.radius*2, self.radius*2, self.host)
        self.entity.give_collision()

        circle = pg.Surface((self.radius*2, self.radius*2))
        pg.draw.circle(circle, COLS["WHITE"], (self.radius, self.radius), self.radius)
        self.entity.sprite.surface = circle


    def update(self):
        if not self.moving:
            return
        if self.entity.rect.x+self.radius*2 > 1000-self.paddle.width:
            self.moving = False
            self.lives -= 1
            self.vx = -self.vx
            self.vy = -self.vy
            self.entity.place(self.x, random.randint(
                    self.host.border_length, self.host.window.height-self.host.border_length*2))
        elif not self.entity.move(round(self.vx), round(self.vy)):
            if self.entity.collider.last_collider == self.borders[0] or self.entity.collider.last_collider \
                    == self.borders[2]:
                self.vy = -self.vy
            elif self.entity.collider.last_collider == self.borders[1]:
                self.vx = -self.vx
            elif self.entity.collider.last_collider == self.paddle.entity.collider:
                self.score += 1
                if abs(self.vx) == 8:
                    self.v_increase_per_score /= 2
                if self.vx < 0:
                    self.vx -= self.v_increase_per_score
                elif self.vx > 0:
                    self.vx += self.v_increase_per_score
                if self.vy < 0:
                    self.vy -= self.v_increase_per_score
                elif self.vy > 0:
                    self.vy += self.v_increase_per_score
                self.vx = -self.vx
