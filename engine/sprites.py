from GLOBAL import *


def get_scale(path):  # Function to get x and y scale of a given picture
    img = PIL.Image.open(path)
    length, width = img.size
    return [length, width]


class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, host, sp_id, layer=10):
        pg.sprite.Sprite.__init__(self)
        self.host = host
        self.id = sp_id

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.layer = layer
        self.host = host
        self.color = ""
        self.img_path = ""
        self.rendertype = None
        self.scale_to_surface = False
        self.is_visible = True

        self.init2()

    def init2(self):

        RENDERLAYERS[self.layer].append(self)
        SPRITES.append(self)
        self.screen = self.host.window.screen

        self.surface = pg.Surface((self.width, self.height))  # create a Surface with given data
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



    def fill_color(self, color):
        self.rendertype = "color"
        self.color = color
        self.surface.fill(self.color)

    def delete(self):
        try:
            RENDERLAYERS[self.layer].remove(self)
            SPRITES.remove(self)
            del self
        except:
            pass

    def save(self):
        GAME["GAME"][self.id] = {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "layer": self.layer,
            "color": self.color,
            "image": self.img_path,
            "rendertype": self.rendertype,
            "scale_to_surface": self.scale_to_surface
        }

    def load(self):
        ser_inst = GAME["GAME"][self.id]
        self.x = ser_inst["x"]
        self.y = ser_inst["y"]
        self.width = ser_inst["width"]
        self.height = ser_inst["height"]
        self.layer = ser_inst["layer"]
        self.color = ser_inst["color"]
        self.rendertype = ser_inst["rendertype"]
        self.fill_image(ser_inst["image"], ser_inst["scale_to_surface"])

        self.init2()
        print("loaded " + self.id + ":\n" + str(ser_inst))
        if self.rendertype == "color":
            self.fill_color(pg.Color("red"))

        if self.rendertype == "image":
            self.fill_image(ser_inst["image"], ser_inst["scale_to_surface"])




    def draw(self):
        self.rect.x = round(self.x + self.host.xoff)
        self.rect.y = round(self.y + self.host.yoff)
        self.screen.blit(self.surface, self.rect)

    def fill_image(self, path, scale_to_surface):
        self.rendertype = "image"
        self.scale_to_surface = scale_to_surface
        self.img_path = path
        if not scale_to_surface:                                        # override self.heigt and self.width to the
            self.surface = pg.image.load(path).convert_alpha()          # size of the image
            self.rect = self.surface.get_rect()
            self.width, self.height = get_scale(path)
        else:
            source_scale = get_scale(path)
            img = pg.image.load(path).convert_alpha()
            self.surface = pg.transform.scale(img, (int(source_scale[0]*(self.width/source_scale[0])),
                                              int(source_scale[1]*(self.height/source_scale[1]))))


    def fill_text(self, text, font, color=COLS["BLACK"]):
        self.rendertype = "text"
        self.text_color = color
        self.surface = font.render(text, True, self.text_color)
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

    def make_visible(self):
        if not self.is_visible:
            RENDERLAYERS[self.layer].append(self)
            self.is_visible = True

    def make_invisible(self):
        if self.is_visible:
            RENDERLAYERS[self.layer].remove(self)
            self.is_visible = False