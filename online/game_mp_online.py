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

        self.test_box = Entity(self.window.width//2, self.window.height//2, 50, 50, self, 10)
        self.test_box.sprite.fill_color(COLS["GREEN"])

        self.xoff = 0
        self.yoff = 0

        self.network = Network()
        self.player = self.network.getPos()
        print(self.player)

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
            self.infobox = TextBox(0, 0, "Server offline", self, APP_["FONT_1"], COLS["RED"])
            self.infobox.sprite.x = self.window.width//2 - self.infobox.sprite.width//2
            self.infobox.sprite.y = self.window.height//2 - self.infobox.sprite.height//2
            self.infobox.sprite.draw()
            self.window.update()
            sleep(3)
            self.clear()
        else:
            if self.key[pg.K_w]:
                self.test_box.move(0, -10)
            if self.key[pg.K_s]:
                self.test_box.move(0, 10)
            if self.key[pg.K_a]:
                self.test_box.move(-10, 0)
            if self.key[pg.K_d]:
                self.test_box.move(10, 0)

    def draw(self):
        self.window.screen.fill(("black"))
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):
        self.open = False
        clear_lists()
