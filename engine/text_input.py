from GLOBAL import *
from engine.sprites import *
from engine.text_box import *


class TextInputBox:
    def __init__(self, x, y, width, host):
        self.x = x
        self.y = y
        self.width = width
        self.host = host
        self.text = ""
        self.is_visible = True

        self.text_box = TextBox(self.x, self.y, self.text, self.host)
        self.text_box.width = width
        self.text_box.apply_changes()
        self.bg1_sprite = Sprite(self.x-5, self.y-5, self.width+10, self.text_box.sprite.height+10,
                                self.host, "TEXTINPUTSHADER1", self.text_box.layer-2)
        self.bg2_sprite = Sprite(self.x, self.y, self.width, self.text_box.sprite.height,
                                 self.host, "TEXTINPUTSHADER2", self.text_box.layer-1)
        self.bg2_sprite.fill_color(COLS["WHITE"])

        self.active = False


    def update(self, event, mx, my):
        if self.is_visible:
            if pg.mouse.get_pressed()[0] == 1:
                if self.bg2_sprite.rect.collidepoint((mx, my)):
                    self.active = True
                else:
                    self.active = False

            if self.active:
                self.bg1_sprite.fill_color(COLS["CYAN"])
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                        self.text_box.text = self.text
                        self.text_box.apply_changes()
            else:
                self.bg1_sprite.fill_color(COLS["BLACK"])


    def forcetext_update(self):
        self.text_box.text = self.text
        self.text_box.apply_changes()


    def make_invisible(self):
        self.bg1_sprite.make_invisible()
        self.bg2_sprite.make_invisible()
        self.text_box.sprite.make_invisible()
        self.is_visible = False


    def make_visible(self):
        self.bg1_sprite.make_visible()
        self.bg2_sprite.make_visible()
        self.text_box.sprite.make_visible()
        self.is_visible = True

    def get_input(self):
        return self.text


