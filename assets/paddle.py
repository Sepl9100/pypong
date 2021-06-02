from engine.entity import *
from GLOBAL import *


class Paddle:
    def __init__(self, y, borderlength, host):
        self.width = 20
        self.height = 80
        self.y = y
        self.borderlength = borderlength
        self.host = host
        self.window = host.window
        self.entity = Entity(self.window.width-self.width, self.y-self.height//2, self.width, self.height, self.host)
        self.entity.give_collision()
        self.entity.sprite.fill_color(COLS["WHITE"])

    def update(self, key_press):
        newy = 0
        if key_press[pg.K_w] or key_press[pg.K_UP]:
            newy -= 10
        if key_press[pg.K_s] or key_press[pg.K_DOWN]:
            newy += 10
        if (key_press[pg.K_w] or key_press[pg.K_UP]) and (key_press[pg.K_s] or key_press[pg.K_DOWN]):
            newy = 0
        self.entity.move(0, newy)

