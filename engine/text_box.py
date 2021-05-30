from GLOBAL import *
from engine.sprites import *


class TextBox:
    def __init__(self, x, y, text, host):
        self.x = x
        self.y = y
        self.text = text
        self.host = host
        self.layer = 105

        self.sprite = Sprite(self.x, self.y, 1, 1, self.host, "TEXTBOX_1", self.layer)
        self.sprite.fill_text(self.text, APP_["FONT_1"])

    def remove(self):
        try:
            RENDERLAYERS[self.layer].remove(self.sprite)
            del self
        except:
            pass

