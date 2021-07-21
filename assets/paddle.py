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
        self.entity.sprite.fill_color(USERDATA["PADDLE_COL"])


