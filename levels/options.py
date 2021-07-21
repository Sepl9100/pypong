import levels.main_menu
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

        self.button_options = Button(10, 10, 150, 60, "main menu", self, lambda: {self.clear()})
        self.text_input_info = TextBox(self.window.width-200, 20, "online name", self, APP_["FONT_2"])
        self.input_name = TextInputBox(self.window.width-250, 50, 200, self)
        self.input_name.text = USERDATA["USERNAME"]
        self.input_name.forcetext_update()

        self.button_safe = Button(self.window.width-250, self.window.height//1.3, 200, 60,
                                  "save", self, lambda: print("nein"))


        while self.open:  # starting the menu loop
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])  # tick the clock

            self.mx, self.my = pg.mouse.get_pos()  # get and handle user inputs
            self.event = pg.event.poll()
            self.key = pg.key.get_pressed()

            if self.event.type == pg.QUIT:
                self.clear()

            self.update()  # update the game
            self.draw()  # draw the menu
            self.window.update()  # update the window


    def update(self):
        self.button_options.draw_button(self.mx, self.my)
        self.input_name.update(self.event, self.mx, self.my)
        self.button_safe.draw_button(self.mx, self.my)

    def draw(self):
        self.window.screen.fill(("black"))
        self.window.screen.blit(BACKGROUNDS["OPTIONS"], (0, 0))
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):
        self.open = False
        clear_lists()



