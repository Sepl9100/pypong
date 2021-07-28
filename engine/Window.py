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
        # Fake Loading / Intro
        self.intro = TextBox(0, 0, "Powered by the KSV Engine", self, APP_["FONT_1"], COLS["WHITE"])
        self.intro.sprite.x = self.width//2 - self.intro.sprite.width // 2
        self.intro.sprite.y = self.height//2 - self.intro.sprite.height // 2
        self.intro.sprite.draw()
        self.intro_ai = AI(100, 100, 10, 10, self)
        self.intro_ai.entity.sprite.fill_color(COLS["GREEN"])
        self.intro_ai.goto(200, 200, True, True, True)

        sleep_thread = threading.Thread(target=self.wait, args=(10, ))
        sleep_thread.start()
        while not self.done:
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])
            self.screen.fill(("black"))
            self.intro_ai.update(1)
            self.intro_ai.entity.sprite.draw()
            self.update()

        self.intro.remove()



    def update(self):
        pg.display.set_caption(f"FPS: {round(APP_['GAMECLOCK'].get_fps(), 1)} - PyPong {VERSION} by {AUTHOR}")
        pg.display.flip()


    def load_background(self, path):
        source_scale = get_scale(path)
        img = pg.image.load(path).convert_alpha()
        return pg.transform.scale(img, (int(source_scale[0]*(self.width/source_scale[0])),
                                              int(source_scale[1]*(self.height/source_scale[1]))))

    def wait(self, seconds):
        self.done = False
        sleep(seconds)
        self.done = True
