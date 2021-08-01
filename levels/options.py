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
        self.color_chosen = USERDATA["PADDLE_COL"]
        self.mouse_toggled = USERDATA["MOUSE"]

        self.button_mainmenu = Button(10, 10, 170, 60, "main menu", self, lambda: {self.clear()})
        self.text_input_info = TextBox(self.window.width-200, 20, "online name", self, APP_["FONT_2"])
        self.input_name = TextInputBox(self.window.width-250, 50, 200, self)
        self.input_name.text = USERDATA["USERNAME"]
        self.input_name.forcetext_update()
        self.text_color_info = TextBox(self.window.width-230, 120, "selected paddle color", self, APP_["FONT_2"])
        self.sprite_paddle_color_bg = Sprite(self.window.width-200, 160, 100, 100, self, "paddle_col_info")
        self.sprite_paddle_color = Sprite(self.sprite_paddle_color_bg.x+5, self.sprite_paddle_color_bg.y+5,
                                           90, 90, self, "paddle_col_info", 11)

        self.text_color_select = TextBox(10, 120, "change paddle color (press 'save' after selecting a color):",
                                         self, APP_["FONT_2"])
        self.button_color_white = Button(10, 170, 150, 60, "white", self, lambda: {self.chose_color(COLS["WHITE"])})
        self.button_color_red = Button(180, 170, 150, 60, "red", self, lambda: {self.chose_color(COLS["RED"])})
        self.button_color_green = Button(350, 170, 150, 60, "green", self, lambda: {self.chose_color(COLS["GREEN"])})
        self.button_color_blue = Button(520, 170, 150, 60, "blue", self, lambda: {self.chose_color(COLS["BLUE"])})

        self.button_toggle_mouse = ToggleButton(180, self.window.height//1.3, 400, 65, "use mouse to control paddle",
                                                self, lambda: empty())
        self.button_toggle_mouse.toggled = self.mouse_toggled

        self.button_save = Button(self.window.width-250, self.window.height//1.3, 200, 65,
                                  "save", self, self.safe_user_config)


        while self.open:  # starting the menu loop
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])  # tick the clock

            self.mx, self.my = pg.mouse.get_pos()  # get and handle user inputs
            self.event = pg.event.poll()
            self.key = pg.key.get_pressed()

            if self.event.type == pg.QUIT:
                exit()

            self.update()  # update the game
            self.draw()  # draw the menu
            self.window.update()  # update the window


    def update(self):
        self.button_mainmenu.draw_button(self.mx, self.my)
        self.input_name.update(self.event, self.mx, self.my)
        self.button_save.draw_button(self.mx, self.my)
        self.button_color_white.draw_button(self.mx, self.my)
        self.button_color_red.draw_button(self.mx, self.my)
        self.button_color_green.draw_button(self.mx, self.my)
        self.button_color_blue.draw_button(self.mx, self.my)
        self.sprite_paddle_color.fill_color(self.color_chosen)
        self.button_toggle_mouse.draw_button(self.mx, self.my)

    def draw(self):
        self.window.screen.fill(COLS["BLACK"])
        self.window.screen.blit(BACKGROUNDS["OPTIONS"], (0, 0))
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):
        self.open = False
        clear_lists()

    def safe_user_config(self):
        USERDATA["MOUSE"] = self.button_toggle_mouse.toggled
        USERDATA["USERNAME"] = self.input_name.text
        USERDATA["PADDLE_COL"] = self.color_chosen
        with open("DATA/userdata.ksv", "wb") as file:
            pickle.dump(USERDATA, file, pickle.HIGHEST_PROTOCOL)

    def chose_color(self, col):
        self.color_chosen = col
