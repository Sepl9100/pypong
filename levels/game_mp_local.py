import time
import threading

from GLOBAL import *
from engine.sprites import *
from engine.button import *
from engine.text_box import *
from engine.ai import *
from engine.entity import *
from assets.paddle import *
from assets.ball import *
from levels.game_sp import *
import levels.main_menu


class Game_MP_local:
    def __init__(self, window):
        self.open = True
        self.window = window

        self.xoff = 0
        self.yoff = 0

        self.border_length = 20

        self.border_top = Entity(0, 0, self.window.width, self.border_length, self)
        self.border_bottom = Entity(0, self.window.height - self.border_length, self.window.width, self.border_length, self)

        self.border_top.sprite.fill_color("white")
        self.border_bottom.sprite.fill_color("white")

        self.border_top.give_collision()
        self.border_bottom.give_collision()

        self.borders = []
        self.borders.append(self.border_top.collider)
        self.borders.append(self.border_bottom.collider)

        self.text_top_left = TextBox(self.border_length, 0, "Player 1 - Lives: 0 | Score: 0", self, APP_["FONT_2"])
        self.text_top_right = TextBox(0, 0, "Player 2 - Lives: 0 | Score: 0", self, APP_["FONT_2"])
        self.text_top_right.sprite.x = self.window.width - self.text_top_right.sprite.width - self.border_length
        self.text_top_mid = TextBox(0, 0, "Ball Velocity: 0", self, APP_["FONT_2"])
        self.text_top_mid.sprite.x = self.window.width//2 - self.text_top_mid.sprite.width//2

        self.text_bottom = TextBox(self.border_length, self.window.height - self.border_length - 1,
                                   "Controls: Player 1: w/s - Player 2: arrow up/down - start/pause with space",
                                   self, APP_["FONT_2"])


        while self.open:
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])  # tick the clock

            self.mx, self.my = pg.mouse.get_pos()  # get and handle user inputs
            self.event = pg.event.poll()
            self.key = pg.key.get_pressed()

            if self.event.type == pg.QUIT:
                self.open = False

            self.update()  # update the game
            self.draw()  # draw the game
            self.window.update()  # update the window

    def update(self):
        pass

    def draw(self):
        self.window.screen.fill(("black"))
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()
