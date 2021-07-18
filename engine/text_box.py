from GLOBAL import *
from engine.sprites import *


class TextBox:
    def __init__(self, x, y, text, host, font=APP_["FONT_1"], color=COLS["BLACK"]):
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.text = text
        self.host = host
        self.layer = 105
        self.font = font
        self.color = color

        self.sprite = Sprite(self.x, self.y, 1, 1, self.host, "TEXTBOX_1", self.layer)
        self.sprite.fill_text(self.text, self.font, self.color)


    def apply_changes(self):
        self.sprite.fill_text(self.text, self.font, self.color)

    def remove(self):
        try:
            RENDERLAYERS[self.layer].remove(self.sprite)
            del self
        except:
            pass

