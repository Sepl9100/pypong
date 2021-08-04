from GLOBAL import *
from online.network import *
from engine.sprites import *
from engine.entity import *
from online.network import *
from engine.text_box import *


class Game_MP_online:
    def __init__(self, window):
        self.open = True
        self.network_run = True
        self.window = window

        self.border_length = 20
        self.border_top = Entity(0, 0, self.window.width, self.border_length, self)
        self.border_bottom = Entity(0, self.window.height - self.border_length, self.window.width, self.border_length,
                                    self)
        self.border_top.sprite.fill_color(COLS["WHITE"])
        self.border_bottom.sprite.fill_color(COLS["WHITE"])
        self.border_top.give_collision()
        self.border_bottom.give_collision()
        self.borders = []
        self.borders.append(self.border_top.collider)
        self.borders.append(self.border_bottom.collider)

        self.text_top_left = TextBox(self.border_length, 0, "Player 1 - Lives: 0 | Score: 0", self, APP_["FONT_2"])
        self.text_top_right = TextBox(0, 0, "Player 2 - Lives: 0 | Score: 0", self, APP_["FONT_2"])
        self.text_top_right.sprite.x = self.window.width - self.text_top_right.sprite.width - self.border_length
        self.text_top_mid = TextBox(0, 0, "Ball Velocity: 0", self, APP_["FONT_2"])
        self.text_top_mid.sprite.x = self.window.width // 2 - self.text_top_mid.sprite.width // 2
        self.text_bottom = TextBox(self.border_length, self.window.height - self.border_length - 1,
                                   "Controls: w/s or arrow up/down", self, APP_["FONT_2"])


        self.xoff = 0
        self.yoff = 0

        self.network = Network()
        self.player = self.network.getPos()
        if self.player is not None:
            print(f"Player {int(self.player)+1} connected")
            if int(self.player) == 0:
                self.enemy_number = 1
            elif int(self.player) == 1:
                self.enemy_number = 0
            self.network.send(f'name={USERDATA["USERNAME"]}')
            self.game = self.network.send(f'pcol={USERDATA["PADDLE_COL"]}')
            #self.test_box.sprite.fill_color(USERDATA["PADDLE_COL"])

            network_thread = threading.Thread(target=self.network_update, daemon=True)
            network_thread.start()

        while self.open:
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])  # tick the clock

            self.mx, self.my = pg.mouse.get_pos()  # get and handle user inputs
            self.event = pg.event.poll()
            self.key = pg.key.get_pressed()

            if self.event.type == pg.QUIT:
                self.clear()
                exit()

            self.update()  # update the game
            self.draw()  # draw the game
            self.window.update()  # update the window

    def update(self):
        if self.player is None:
            self.network_run = False
            clear_lists()
            self.window.screen.fill(COLS["BLACK"])
            self.infobox = TextBox(0, 0, "Server error/offline", self, APP_["FONT_1"], COLS["RED"])
            self.infobox.sprite.x = self.window.width // 2 - self.infobox.sprite.width // 2
            self.infobox.sprite.y = self.window.height // 2 - self.infobox.sprite.height // 2
            self.infobox.sprite.draw()
            self.window.update()
            sleep(3)
            self.clear()
        else:
            try:


                #self.test_box2.sprite.fill_color(self.game.paddle_cols[self.enemy_number])
                box2_cords = self.game.get_player_paddle_pos(self.enemy_number)
                #self.test_box2.place(box2_cords[0], box2_cords[1])

                self.text_top_mid.text = f"Ball Velocity: {abs(1)}"
                self.text_top_left.text = f"{self.game.player_names[0]} - Lives: {self.game.lives[0]} " \
                                          f"| Score: {self.game.scores[0]}"
                self.text_top_right.text = f"{self.game.player_names[1]} - Lives: {self.game.lives[1]} " \
                                           f"| Score: {self.game.scores[1]}"
                self.text_top_right.sprite.x = self.window.width - self.text_top_right.sprite.width - self.border_length
                self.text_top_mid.apply_changes()
                self.text_top_left.apply_changes()
                self.text_top_right.apply_changes()
            except:
                self.player = None

    def network_update(self):
        while self.network_run:
            APP_["NETWORK_CLOCK"].tick(APP_["NETWORK_TPS"])
            try:
                self.network.send(f"x={0}")
                self.network.send(f"y={0}")
                self.game = self.network.send("get")
            except:
                self.player = None


    def draw(self):
        self.window.screen.fill(COLS["BLACK"])
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def clear(self):
        self.open = False
        self.network_run = False
        clear_lists()
