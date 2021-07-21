from GLOBAL import *
from engine.Window import *
import engine.sprites
import cProfile

c_profile = True


class App:
    def __init__(self):
        Main_Window = Window()  # initialise the window
        BACKGROUNDS["MAIN_MENU"] = Main_Window.load_background(BACKGROUNDS["MAIN_MENU_PATH"])
        BACKGROUNDS["OPTIONS"] = Main_Window.load_background(BACKGROUNDS["OPTIONS_PATH"])
        MainMenu(Main_Window)  # start the main menu with th window


if c_profile:
    cProfile.run("App()")
else:
    App()
pg.quit()