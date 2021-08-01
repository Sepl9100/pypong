from GLOBAL import *
from engine.sprites import *
from engine.button import *
from engine.text_box import *
from engine.ai import *
from engine.entity import *
from assets.paddle import *
from assets.ball import *
from levels.game_sp import *
import levels.main_menu


class Game_MP_local:
    def __init__(self, window):
        self.open = True
        self.window = window

        self.xoff = 0
        self.yoff = 0

        self.border_length = 20

        self.border_top = Entity(0, 0, self.window.width, self.border_length, self)
        self.border_bottom = Entity(0, self.window.height - self.border_length, self.window.width, self.border_length,
                                    self)

        self.border_top.sprite.fill_color("white")
        self.border_bottom.sprite.fill_color("white")

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

        self.paddle_right = Paddle(self.window.height // 2, self.border_length, self)
        self.paddle_left = Paddle(self.window.height//2, self.border_length, self)
        self.paddle_left.entity.place(0, self.window.height//2-self.paddle_left.height//2)
        self.paddles = [self.paddle_left, self.paddle_right]

        index1 = random.randint(0, 1)
        index2 = random.randint(0, 1)
        multiplier = [-1, 1]

        self.ball = Ball(self.window.width//2, self.window.height//2, 4*multiplier[index1], 4*multiplier[index2],
                         self.borders, self.paddle_right, self)
        self.ball.half_speed = 6
        self.ball_speed_max = 10

        self.lives_p1 = 5
        self.score_p1 = 0
        self.lives_p2 = 5
        self.score_p2 = 0

        while self.open:
            APP_["GAMECLOCK"].tick(APP_["MAX_FPS"])  # tick the clock

            self.mx, self.my = pg.mouse.get_pos()  # get and handle user inputs
            self.event = pg.event.poll()
            self.key = pg.key.get_pressed()

            if self.event.type == pg.QUIT:
                exit()

            self.update()  # update the game
            self.draw()  # draw the game
            self.window.update()  # update the window

    def update(self):
        if self.lives_p1 > 0 and self.lives_p2 > 0:
            if self.event.type == pg.KEYDOWN:
                if self.key[pg.K_SPACE]:
                    self.ball.moving = not self.ball.moving
            self.paddle_update(self.key)
            self.update_ball()
            self.text_top_mid.text = f"Ball Velocity: {abs(self.ball.vx)}"
            self.text_top_mid.apply_changes()
            self.text_top_left.text = f"Player 1 - Lives: {self.lives_p1} | Score: {self.score_p1}"
            self.text_top_left.apply_changes()
            self.text_top_right.text = f"Player 2 - Lives: {self.lives_p2} | Score: {self.score_p2}"
            self.text_top_right.apply_changes()
        else:
            self.window.screen.fill(("red"))
            if self.score_p1 > self.score_p2:
                winner = 1
            elif self.score_p2 > self.score_p1:
                winner = 2
            elif self.lives_p1 > self.lives_p2:
                winner = 1
            elif self.lives_p2 > self.lives_p1:
                winner = 2

            self.text_game_over = TextBox(0, 0, f"Player {winner} won!", self, APP_["FONT_1"])
            self.text_game_over.sprite.x = self.window.width//2 - self.text_game_over.sprite.width//2

            self.text_game_over_1 = TextBox(0, 0, f"Score: {self.score_p1} - {self.score_p2}", self, APP_["FONT_1"])
            self.text_game_over_1.sprite.x = self.window.width // 2 - self.text_game_over.sprite.width // 2

            self.text_game_over_2 = TextBox(0, 0, f"Lives: {self.lives_p1} - {self.lives_p2}", self, APP_["FONT_1"])
            self.text_game_over_2.sprite.x = self.window.width // 2 - self.text_game_over.sprite.width // 2

            self.text_game_over.sprite.y = self.window.height // 2 - self.text_game_over.sprite.height * 1.5
            self.text_game_over_1.sprite.y = self.window.height // 2 - self.text_game_over.sprite.height // 2
            self.text_game_over_2.sprite.y = self.window.height // 2 + self.text_game_over.sprite.height // 2

            self.text_game_over.sprite.draw()
            self.text_game_over_1.sprite.draw()
            self.text_game_over_2.sprite.draw()
            self.window.update()
            time.sleep(3)
            self.main_menu()
        if self.key[pg.K_ESCAPE]:
            self.clear()

    def draw(self):
        self.window.screen.fill(COLS["BLACK"])
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()

    def paddle_update(self, key_press):
        p1_newy = 0
        p2_newy = 0
        if key_press[pg.K_w]:
            p1_newy -= 13
        if key_press[pg.K_s]:
            p1_newy += 13
        if key_press[pg.K_UP]:
            p2_newy -= 13
        if key_press[pg.K_DOWN]:
            p2_newy += 13
        if key_press[pg.K_w] and key_press[pg.K_s]:
            p1_newy = 0
        if key_press[pg.K_UP] and key_press[pg.K_DOWN]:
            p2_newy = 0

        self.paddle_left.entity.move(0, p1_newy)
        self.paddle_right.entity.move(0, p2_newy)


    def update_ball(self):
        replace = False
        score = False
        if not self.ball.moving:
            return
        if self.ball.entity.rect.x + self.ball.radius * 2 > 1000 - self.paddle_right.width:
            self.lives_p2 -= 1
            replace = True
        elif self.ball.entity.rect.x < self.paddle_left.width:
            self.lives_p1 -= 1
            replace = True
        elif not self.ball.entity.move(round(self.ball.vx), round(self.ball.vy)):
            if self.ball.entity.collider.last_collider == self.border_top.collider:
                self.ball.vy = - self.ball.vy
            elif self.ball.entity.collider.last_collider == self.border_bottom.collider:
                self.ball.vy = - self.ball.vy
            elif self.ball.entity.collider.last_collider == self.paddle_right.entity.collider:
                self.score_p2 += 1
                score = True
            elif self.ball.entity.collider.last_collider == self.paddle_left.entity.collider:
                self.score_p1 += 1
                score = True

        if score:
            if abs(self.ball.vx) >= self.ball_speed_max:
                self.ball.v_increase_per_score = 0
            elif abs(self.ball.vx) == self.ball.half_speed:
                self.ball.v_increase_per_score /= 2
            if self.ball.vx < 0:
                self.ball.vx -= self.ball.v_increase_per_score
            elif self.ball.vx > 0:
                self.ball.vx += self.ball.v_increase_per_score
            if self.ball.vy < 0:
                self.ball.vy -= self.ball.v_increase_per_score
            elif self.ball.vy > 0:
                self.ball.vy += self.ball.v_increase_per_score
            self.ball.vx = - self.ball.vx
        if replace:
            self.ball.moving = False
            self.ball.vx = - self.ball.vx
            self.ball.vy = - self.ball.vy
            self.ball.entity.place(self.window.width // 2, self.window.height // 2)

    def main_menu(self):
        self.clear()
        levels.main_menu.MainMenu(self.window)

    def clear(self):
        self.open = False
        clear_lists()
