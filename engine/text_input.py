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
        self.text_box = TextBox(self.x, self.y, self.text, self.host)
        self.text_box.width = width
        self.text_box.apply_changes()
        self.bg_sprite = Sprite(self.x, self.y, self.width, self.text_box.sprite.height, self, "TEXTINPUT1",
                                self.text_box.layer-1)


    def make_invisible(self):
        self.text_box.sprite.make_invisible()


    def make_visible(self):
        self.text_box.sprite.make_visible()

    def get_input(self):
        return self.text
