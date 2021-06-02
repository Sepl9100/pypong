from GLOBAL import *
from engine.sprites import *
from engine.button import *
from engine.text_box import *
from engine.ai import *
from engine.entity import *
from levels.game_sp import *


class MainMenu:
    def __init__(self, window):
        self.open = True
        self.window = window
        self.click = False

        self.text_main = TextBox(300, 290, "PyPong 2.0", self)
        self.text_coming_soon_1 = TextBox(560, 175, "Coming Soon", self)
        self.text_coming_soon_2 = TextBox(560, 285, "Coming Soon", self)

        self.text_coming_soon_1.sprite.make_invisible()
        self.text_coming_soon_2.sprite.make_invisible()

        self.button_play = Button(750, 50, 200, 70, "Singleplayer", self, self.game_sp)
        self.button_play_multi = Button(750, 160, 200, 70, "Multiplayer", self, self.text_coming_soon_1.sprite.make_visible)
        self.button_highscore = Button(750, 270, 200, 70, "Highscores", self, self.text_coming_soon_2.sprite.make_visible)
        self.button_quit = Button(750, 380, 200, 70, "Quit", self, self.clear)

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
        self.button_play_multi.draw_button(self.mx, self.my)
        self.button_highscore.draw_button(self.mx, self.my)
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

    def game_sp(self):
        self.clear()
        Game_SP(self.window)

