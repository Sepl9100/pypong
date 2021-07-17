import PIL.Image as Image
import PIL
import pygame as pg
import os
from threading import *
import webbrowser
import random
from time import sleep

AUTHOR = "Sebastian Reichl"
VERSION = 2.2

pg.init()


APP_ = {
    "GAMECLOCK": pg.time.Clock(),
    "FONT_1": pg.font.SysFont('Bahnschrift', 30),
    "FONT_2": pg.font.SysFont('Bahnschrift', 17),
    "MAX_FPS": 60,
}

COLS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "BUTTON": (255, 0, 0),
    "HOVER": (75, 225, 255),
    "CLICK": (50, 150, 255)
}

TEXT = [{}]

GAME = {
    "GAME": {}
}


# create Render Layers
RENDERLAYERS = []
for i in range(200):
    RENDERLAYERS.append([])

COLLIDERS = []

ENTITIES = []

SPRITES = []

AIS = []




