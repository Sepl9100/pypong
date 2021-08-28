from GLOBAL import *
from engine.sprites import *
from engine.button import *
from engine.text_box import *
from engine.ai import *
from engine.entity import *
from engine.text_input import *
from levels.game_sp import *
from levels.game_mp_local import *
from levels.options import *
from online.game_mp_online import *


class MainMenu:
    def __init__(self, window):
        self.open = True
        self.window = window

        # Text / Global
        self.text_main = TextBox(300, 290, f"PyPong {VERSION}       TEST-VERSION", self)
        self.text_coming_soon_1 = TextBox(560, 285, "Coming Soon", self)
        self.text_coming_soon_1.sprite.make_invisible()
        self.button_options = Button(10, 10, 150, 60, "Options", self, lambda: {clear_lists(), Options(self.window),
                                                                                self.__init__(self.window)})

        # Main Menu
        self.button_play = Button(750, 50, 200, 70, "Singleplayer", self, self.game_sp)
        self.button_play_multi = Button(750, 160, 200, 70, "Multiplayer", self, self.game_mp)
        self.button_highscore = Button(750, 270, 200, 70, "Highscores", self, self.text_coming_soon_1.sprite.make_visible)
        self.button_quit = Button(750, 380, 200, 70, "Quit", self, self.clear)
        self.main_menu_items = [self.button_play, self.button_play_multi, self.button_highscore, self.button_quit]

        # Singleplayer
        self.button_play_normal = Button(750, 50, 200, 70, "Normal", self,
                                         lambda: {clear_lists(), Game_SP(self.window, 0), self.__init__(self.window)})
        self.button_play_2balls = Button(750, 160, 200, 70, "2 Balls", self,
                                         lambda: {clear_lists(), Game_SP(self.window, 1), self.__init__(self.window)})
        self.button_back_1 = Button(750, 380, 200, 70, "Go Back", self, self.main_menu)
        self.singleplayer_menu_items = [self.button_play_normal, self.button_play_2balls, self.button_back_1]

        # Multiplayer
        self.button_play_local_pvp = Button(750, 50, 200, 70, "Local PvP", self,
                                            lambda: {clear_lists(), Game_MP_local(self.window), self.__init__(self.window)})
        self.button_play_online_pvp = Button(750, 160, 200, 70, "Online PvP", self,
                                             lambda: {clear_lists(), Game_MP_online(self.window), self.__init__(self.window)})
        self.text_online_info1 = TextBox(745, 240, "You can change your online", self, APP_["FONT_2"])
        self.text_online_info2 = TextBox(752, 260, "appearance in the options", self, APP_["FONT_2"])
        self.multiplayer_menu_items = [self.button_play_local_pvp, self.button_play_online_pvp, self.text_online_info1,
                           self.text_online_info2, self.button_back_1]

        self.ui_items = [self.main_menu_items, self.singleplayer_menu_items, self.multiplayer_menu_items]

        self.xoff = 0
        self.yoff = 0
        self.main_menu()


        while self.open:    # starting the menu loop
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
        self.button_play.draw_button(self.mx, self.my)
        self.button_play_multi.draw_button(self.mx, self.my)
        self.button_highscore.draw_button(self.mx, self.my)
        self.button_quit.draw_button(self.mx, self.my)
        self.button_play_normal.draw_button(self.mx, self.my)
        self.button_play_2balls.draw_button(self.mx, self.my)
        self.button_back_1.draw_button(self.mx, self.my)
        self.button_play_local_pvp.draw_button(self.mx, self.my)
        self.button_play_online_pvp.draw_button(self.mx, self.my)
        self.button_options.draw_button(self.mx, self.my)

    def draw(self):
        # reset screen
        self.window.screen.fill(COLS["BLACK"])
        self.window.screen.blit(BACKGROUNDS["MAIN_MENU"], (0, 0))
        # draw all sprites
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):                        # stop the game loop and clear all render layers
        self.open = False
        clear_lists()
        
    def game_sp(self):
        self.text_coming_soon_1.make_invisible()
        for item in self.main_menu_items:
            item.make_invisible()
        for item in self.multiplayer_menu_items:
            item.make_invisible()
        for item in self.singleplayer_menu_items:
            item.make_visible()

    def main_menu(self):
        for item in self.singleplayer_menu_items:
            item.make_invisible()
        for item in self.multiplayer_menu_items:
            item.make_invisible()
        for item in self.main_menu_items:
            item.make_visible()

    def game_mp(self):
        self.text_coming_soon_1.make_invisible()
        for item in self.main_menu_items:
            item.make_invisible()
        for item in self.singleplayer_menu_items:
            item.make_invisible()
        for item in self.multiplayer_menu_items:
            item.make_visible()

