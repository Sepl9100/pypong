from GLOBAL import *
from engine.sprites import *
from engine.button import *
from engine.text_box import *
from engine.ai import *
from engine.entity import *


class MainMenu:
    def __init__(self, window):
        self.open = True
        self.window = window
        self.click = False
        self.play_exit = False

        self.button_play = Button(750, 120, 200, 70, "Singleplayer", self, lambda: (self.clear()))
        self.button_options = Button(750, 250, 200, 70, "Options", self, lambda: (print("Optionen")))
        self.button_quit = Button(750, 310, 200, 70, "Quit", self, lambda: (self.clear()))

        self.ai = AI(80, 450, 40, 100, self)
        self.ai.entity.sprite.fill_image("DATA/textures/test_img_sebif.png", False)

        self.xoff = 0
        self.yoff = 0

        bg = "DATA/textures/living_room.png"
        source_scale = get_scale(bg)
        img = pg.image.load(bg).convert_alpha()
        self.background = pg.transform.scale(img, (int(source_scale[0]*(self.window.width/source_scale[0])),
                                              int(source_scale[1]*(self.window.height/source_scale[1]))))

        while self.open:    # starting the menu loop
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
        self.button_play.draw_button(self.mx, self.my)
        self.button_options.draw_button(self.mx, self.my)
        self.button_quit.draw_button(self.mx, self.my)

    def draw(self):
        # reset screen
        self.window.screen.fill(("black"))
        self.window.screen.blit(self.background, (0, 0))
        # draw all sprites
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):                        # stop the game loop and clear all render layers
        self.open = False
        for layer in RENDERLAYERS:
            layer.clear()


