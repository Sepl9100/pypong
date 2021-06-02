import time

from GLOBAL import *
from engine.sprites import *
from engine.button import *
from engine.text_box import *
from engine.ai import *
from engine.entity import *
from assets.paddle import *
from assets.ball import *
import levels.main_menu


class Game_SP:
    def __init__(self, window):
        self.open = True
        self.window = window

        self.xoff = 0
        self.yoff = 0

        self.border_length = 20

        self.border_top = Entity(0, 0, self.window.width, self.border_length, self)
        self.border_left = Entity(0, 0, self.border_length, self.window.height, self)
        self.border_bottom = Entity(0, self.window.height-self.border_length, self.window.width, self.border_length, self)

        self.border_top.sprite.fill_color("white")
        self.border_left.sprite.fill_color("white")
        self.border_bottom.sprite.fill_color("white")

        self.border_top.give_collision()
        self.border_left.give_collision()
        self.border_bottom.give_collision()

        self.borders = []
        self.borders.append(self.border_top.collider)
        self.borders.append(self.border_left.collider)
        self.borders.append(self.border_bottom.collider)


        self.text_top = TextBox(self.border_length, 0, "Lives: 0 | Score: 0 | Velocity: 0", self, APP_["FONT_2"])
        self.text_bottom = TextBox(self.border_length, self.window.height-self.border_length-1,
                                   "Controls: w/s or arrow up/down. Start/Pause with space",
                                   self, APP_["FONT_2"])

        self.paddle = Paddle(self.window.height//2, self.border_length, self)
        self.ball = Ball(self.window.width-self.paddle.width*3, random.randint(
                        self.border_length, self.window.height-self.border_length*2), -4, 4, self.borders, self.paddle, self)

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
        if self.ball.lives > 0:
            if self.event.type == pg.KEYDOWN:
                if self.key[pg.K_SPACE]:
                    self.ball.moving = not self.ball.moving
            self.paddle.update(self.key)
            self.ball.update()
            self.text_top.text = f"Lives: {self.ball.lives} | Score: {self.ball.score} | Velocity: {abs(self.ball.vx)}"
            self.text_top.apply_changes()
        else:
            self.window.screen.fill(("red"))
            self.text_game_over = TextBox(self.window.width//2.5, self.window.height//2.5, "GAME OVER!", self, APP_["FONT_1"])
            self.text_game_over.sprite.draw()
            pg.display.flip()
            time.sleep(3)
            self.main_menu()


    def draw(self):
        self.window.screen.fill(("black"))
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):
        self.open = False
        for layer in RENDERLAYERS:
            layer.clear()

    def main_menu(self):
        self.clear()
        levels.main_menu.MainMenu(self.window)