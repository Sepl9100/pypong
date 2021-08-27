import PIL.Image as Image
import PIL
import pygame as pg
import os
import webbrowser
import random
from time import sleep
import pickle
from sys import exit
import selectors
import time
import threading

AUTHOR = "Sebastian Reichl"
VERSION = 2.4

pg.init()


APP_ = {
    "GAMECLOCK": pg.time.Clock(),
    "NETWORK_CLOCK": pg.time.Clock(),
    "FONT_1": pg.font.SysFont('Bahnschrift', 30),
    "FONT_2": pg.font.SysFont('Bahnschrift', 17),
    "MAX_FPS": 60,
    "NETWORK_TPS": 32
}

BACKGROUNDS = {
    "MAIN_MENU_PATH": "DATA/textures/living_room.png",
    "MAIN_MENU": None,
    "OPTIONS_PATH": "DATA/textures/mountain_bg.png",
    "OPTIONS": None
}

COLS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "BUTTON": (255, 0, 0),
    "HOVER": (75, 225, 255),
    "CLICK": (50, 150, 255),
    "CYAN": (0, 255, 255),
    "GREEN": (0, 255, 0),
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255)
}

TEXT = [{}]

GAME = {
    "GAME": {}
}

with open("DATA/userdata.ksv", "rb") as file:
    USERDATA = pickle.load(file)

# create Render Layers
RENDERLAYERS = []
for i in range(200):
    RENDERLAYERS.append([])

COLLIDERS = []

ENTITIES = []

SPRITES = []

AIS = []

SINGLE_LISTS = [COLLIDERS, ENTITIES, SPRITES, AIS]

'''
USERDATA = {
    "MOUSE": False,
    "PADDLE_COL": COLS["WHITE"],
    "USERNAME": "Player"
}
with open("DATA/userdata.ksv", "wb") as file:
    pickle.dump(USERDATA, file, pickle.HIGHEST_PROTOCOL)
'''


def clear_lists():
    for layer in RENDERLAYERS:
        for sprite in layer:
            del sprite
        layer.clear()
    for list in SINGLE_LISTS:
        for item in list:
            del item
        list.clear()


def empty():
    pass
