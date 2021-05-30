from GLOBAL import *
from engine.Window import *
import cProfile

c_profile = True


class App:
    def __init__(self):
        Main_Window = Window()  # initialise the window

        MainMenu(Main_Window)  # start the main menu with th window


if c_profile:
    cProfile.run("App()")
else:
    App()
pg.quit()