from GLOBAL import *
from levels.main_menu import *
from engine.text_box import *


class Window:
    def __init__(self):
        self.window = self
        self.xoff = 0
        self.yoff = 0
        self.width = 1000
        self.height = 500
        self.flags = pg.DOUBLEBUF | pg.HWSURFACE
        self.screen = pg.display.set_mode((self.width, self.height), self.flags, 32)
        self.intro = TextBox(0, 0, "Powered by the KSV Engine", self, APP_["FONT_1"], COLS["WHITE"])
        self.intro.sprite.x = self.width//2 - self.intro.sprite.width // 2
        self.intro.sprite.y = self.height//2 - self.intro.sprite.height // 2
        self.intro.sprite.draw()
        self.update()
        sleep(2)
        self.intro.remove()



    def update(self):
        pg.display.set_caption(f"FPS: {round(APP_['GAMECLOCK'].get_fps(), 1)} - PyPong {VERSION} by {AUTHOR}")
        pg.display.flip()

