from GLOBAL import *
from engine.entity import *
from engine.line_path import *


class AI:
    def __init__(self, x, y, width, height, host, collision=False, layer=0):
        self.x = x
        self.y = y
        self.host = host
        self.layer = layer
        self.collision = collision

        self.entity = Entity(self.x, self.y, width, height, self.host, self.layer)
        if self.collision:
            self.entity.give_collision()
        self.rect = self.entity.rect

        self.needs_update = False

        AIS.append(self)

    def goto(self, xdest, ydest, back=False, repeat=False, disappear=True):
        self.needs_update = True
        self.xdest = xdest
        self.ydest = ydest
        self.x_original = self.rect.x
        self.y_original = self.rect.y

        self.back = back
        self.repeat = repeat
        self.disappear = disappear
        self.path = line_path(self.rect.x, self.rect.y, xdest, ydest)
        self.counter = 0
        self.counter_end = len(self.path)-1
        self.go_back = False
        if not self.back:
            self.repeat = False

    def update(self, speed):
        self.speed = speed
        if self.needs_update:
            if not self.go_back:
                self.entity.place(self.path[self.counter][0], self.path[self.counter][1])
                self.counter += 1
                if self.counter >= self.counter_end:
                    if self.back:
                        self.go_back = True
                    if not self.repeat and not self.back:
                        self.needs_update = False
                        if not self.back:
                            if self.disappear:
                                self.entity.sprite.fill_image("DATA/textures/transparent.png", True)
            else:
                self.entity.place(self.path[self.counter][0], self.path[self.counter][1])
                self.counter -= 1
                if self.rect.x <= self.x_original and self.rect.y <= self.y_original:
                    self.go_back = False
                    if not self.repeat:
                        self.needs_update = False
                        if self.disappear:
                            self.entity.sprite.fill_image("DATA/textures/transparent.png", True)
            if self.speed > 1:
                self.speed -= 1
                self.update(self.speed)

