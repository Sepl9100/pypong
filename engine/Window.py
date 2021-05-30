from GLOBAL import *
from levels.main_menu import *


class Window:
    def __init__(self):

        self.width = 1000
        self.height = 500
        self.flags = pg.DOUBLEBUF | pg.HWSURFACE
        self.screen = pg.display.set_mode((self.width, self.height), self.flags, 32)
        pg.display.flip()

    def update(self):
        pg.display.set_caption(f"FPS: {round(APP_['GAMECLOCK'].get_fps(), 1)} - PyPong {VERSION} by {AUTHOR}")
        pg.display.flip()

