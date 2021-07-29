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

        self.intro_blocks = []
        for i in range(10):
            intro_block = AI(50 + 100*i, 20, 10, 10, self)
            intro_block2 = AI(50 + 100*i, 480, 10, 10, self)
            self.intro_blocks.append(intro_block)
            self.intro_blocks.append(intro_block2)
        for block in self.intro_blocks:
            if self.intro_blocks.index(block) % 2 == 0:
                block.entity.sprite.fill_color(COLS["RED"])
            else:
                block.entity.sprite.fill_color(COLS["GREEN"])
            block.goto(self.width//2, self.height//2, True)

        sleep_thread = threading.Thread(target=self.wait, args=(0.1, ))
        sleep_thread.start()
        while not self.done:
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])
            self.event = pg.event.poll()
            if self.event.type == pg.QUIT:
                exit()

            self.screen.fill(("black"))

            for block in self.intro_blocks:
                block.update(5.1)
                block.entity.sprite.draw()
            self.intro.sprite.draw()
            self.update()

        for block in self.intro_blocks:
            block.entity.sprite.delete()
            del block
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
