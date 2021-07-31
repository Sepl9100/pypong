from GLOBAL import *
from online.network import *
from engine.sprites import *
from engine.entity import *
from online.network import *
from engine.text_box import *


class Game_MP_online:
    def __init__(self, window):
        self.open = True
        self.window = window

        self.border_length = 20

        self.border_top = Entity(0, 0, self.window.width, self.border_length, self)
        self.border_bottom = Entity(0, self.window.height - self.border_length, self.window.width, self.border_length,
                                    self)

        self.border_top.sprite.fill_color("white")
        self.border_bottom.sprite.fill_color("white")

        self.border_top.give_collision()
        self.border_bottom.give_collision()

        self.borders = []
        self.borders.append(self.border_top.collider)
        self.borders.append(self.border_bottom.collider)

        self.x_test = 10
        self.y_test = 10

        self.xoff = 0
        self.yoff = 0

        self.network = Network()
        self.player = self.network.getPos()
        if self.player is not None:
            print(f"Player {int(self.player)+1} connected")

        while self.open:
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])  # tick the clock

            self.mx, self.my = pg.mouse.get_pos()  # get and handle user inputs
            self.event = pg.event.poll()
            self.key = pg.key.get_pressed()

            if self.event.type == pg.QUIT:
                exit()

            self.update()  # update the game
            self.draw()  # draw the game
            self.window.update()  # update the window

    def update(self):
        if self.player is None:
            clear_lists()
            self.window.screen.fill(("black"))
            self.infobox = TextBox(0, 0, "Server error/offline", self, APP_["FONT_1"], COLS["RED"])
            self.infobox.sprite.x = self.window.width//2 - self.infobox.sprite.width//2
            self.infobox.sprite.y = self.window.height//2 - self.infobox.sprite.height//2
            self.infobox.sprite.draw()
            self.window.update()
            sleep(3)
            self.clear()
        else:
            try:
                self.game = self.network.send("get")
                if self.key[pg.K_w]:
                    self.x_test += 10
                    self.y_test += 10
                    self.network.send(f"x={self.x_test}")
                    self.network.send(f"y={self.y_test}")
                print(self.game.get_player_paddle_pos(0))
                print(self.game.get_player_paddle_pos(1))
            except:
                self.player = None




    def draw(self):
        self.window.screen.fill(("black"))
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):
        self.open = False
        clear_lists()
