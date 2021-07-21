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
        bg = "DATA/textures/mountain_bg.png"
        source_scale = get_scale(bg)
        img = pg.image.load(bg).convert_alpha()
        self.background = pg.transform.scale(img, (int(source_scale[0] * (self.window.width / source_scale[0])),
                                                   int(source_scale[1] * (self.window.height / source_scale[1]))))

        self.button_options = Button(10, 10, 150, 60, "Main Menu", self, lambda: {self.clear(), levels.main_menu.MainMenu(self.window)})

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
        self.button_options.draw_button(self.mx, self.my)

    def draw(self):
        self.window.screen.fill(("black"))
        self.window.screen.blit(self.background, (0, 0))
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



