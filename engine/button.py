from GLOBAL import *
from engine.sprites import *


class Button:

    def __init__(self, x, y, width, height, text, host, function):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.function = function
        self.host = host
        self.clicked = False
        self.layer = 100
        self.is_visible = True

        self.colored = True
        self.click_color = COLS["CLICK"]
        self.hover_color = COLS["HOVER"]
        self.button_color = COLS["BUTTON"]
        self.click_img_path = "DATA/textures/transparent_2.png"
        self.hover_img_path = "DATA/textures/transparent_3.png"
        self.button_img_path = "DATA/textures/transparent_4.png"

        self.sprite = Sprite(self.x, self.y, self.width, self.height, self.host, "BUTTON", self.layer)
        # create shaders
        self.shader1 = Sprite(self.x, self.y, self.width, 2, self.host, "1", self.layer)
        self.shader2 = Sprite(self.x, self.y, 2, self.height, self.host, "2", self.layer)
        self.shader3 = Sprite(self.x, (self.y + self.height), self.width+2, 2, self.host, "3", self.layer)
        self.shader4 = Sprite((self.x + self.width), self.y, 2, self.height, self.host, "4", self.layer)

        self.shader1.fill_color(COLS["WHITE"])
        self.shader2.fill_color(COLS["WHITE"])
        self.shader3.fill_color(COLS["BLACK"])
        self.shader4.fill_color(COLS["BLACK"])

        self.add_text(self.text)

    def draw_button(self, mx, my):
        if self.is_visible:
            if self.sprite.rect.collidepoint((mx, my)):
                if pg.mouse.get_pressed()[0] == 1:
                    self.clicked = True
                    self.click_sprite()
                elif pg.mouse.get_pressed()[0] == 0 and self.clicked:
                    self.clicked = False
                    self.function()
                else:
                    self.hover_sprite()
            else:
                self.button_sprite()
                self.clicked = False

    def add_text(self, text):
        self.text = text
        self.text_sprite = Sprite(self.x, self.y, 1, 1, self.host, "BUTTON_TEXT", self.layer+1)
        self.text_sprite.fill_text(text, APP_["FONT_1"])
        self.text_sprite.x = (self.x + int(self.width/2)-int(self.text_sprite.width/2))
        self.text_sprite.y = self.y + self.height//4


    def remove_text(self):
        try:
            RENDERLAYERS[self.layer+1].remove(self.text_sprite)
            del self.text_sprite
        except:
            pass


    def click_sprite(self):
        if self.colored:
            self.sprite.fill_color(self.click_color)
        else:
            self.sprite.fill_image(self.click_img_path, True)

    def hover_sprite(self):
        if self.colored:
            self.sprite.fill_color(self.hover_color)
        else:
            self.sprite.fill_image(self.hover_img_path, True)

    def button_sprite(self):
        if self.colored:
            self.sprite.fill_color(self.button_color)
        else:
            self.sprite.fill_image(self.button_img_path, True)

    def delete(self):
        self.sprite.delete()
        self.shader1.delete()
        self.shader2.delete()
        self.shader3.delete()
        self.shader4.delete()
        self.remove_text()
        try:
            del self
        except:
            pass

    def make_invisible(self):
        self.shader1.make_invisible()
        self.shader2.make_invisible()
        self.shader3.make_invisible()
        self.shader4.make_invisible()
        self.sprite.make_invisible()
        self.text_sprite.make_invisible()
        self.is_visible = False

    def make_visible(self):
        self.sprite.make_visible()
        self.shader1.make_visible()
        self.shader2.make_visible()
        self.shader3.make_visible()
        self.shader4.make_visible()
        self.text_sprite.make_visible()
        self.is_visible = True