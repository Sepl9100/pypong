from GLOBAL import *
from engine.sprites import *
from engine.button import *
from engine.text_box import *
from engine.ai import *
from engine.entity import *
from engine.text_input import *
from levels.main_menu import *


class Options:
    def __init__(self, window):
        self.open = True
        self.window = window




        self.xoff = 0
        self.yoff = 0

        while self.open:  # starting the menu loop
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])  # tick the clock

            self.mx, self.my = pg.mouse.get_pos()  # get and handle user inputs
            self.event = pg.event.poll()
            self.key = pg.key.get_pressed()

            if self.event.type == pg.QUIT:
                self.open = False

            self.update()  # update the game
            self.draw()  # draw the menu
            self.window.update()  # update the window


    def update(self):
        pass

    def draw(self):
        self.window.screen.fill((0, 100, 0))
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):
        self.open = False
        for layer in RENDERLAYERS:
            layer.clear()
        ENTITIES.clear()
        AIS.clear()
        COLLIDERS.clear()

    def main_menu(self):
        self.clear()
        levels.main_menu.MainMenu(self.window)