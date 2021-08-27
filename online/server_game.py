class ServerGame:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.player_ready = [False, False]
        self.paddle_pos = [[0, 0], [0, 0]]
        self.paddle_dir = [0, 0]
        self.paddle_cols = [(0, 0, 0), (0, 0, 0)]
        self.player_names = ["Not connected", "Not connected"]
        self.scores = [0, 0]
        self.lives = [5, 5]

    def get_player_paddle_pos(self, player):
        return self.paddle_pos[player]

    def update_x(self, player, paddle_pos_x):
        self.paddle_pos[player][0] = int(paddle_pos_x)

    def update_y(self, player, paddle_pos_y):
        old_y = self.paddle_pos[player][1]
        if old_y > int(paddle_pos_y):
            self.paddle_dir[player] = -1
        elif old_y < int(paddle_pos_y):
            self.paddle_dir[player] = 1
        else:
            self.paddle_dir[player] = 0
        self.paddle_pos[player][1] = int(paddle_pos_y)

    def update_name(self, player, name):
        self.player_names[player] = name

    def update_paddle_col(self, player, color):
        self.paddle_cols[player] = eval(color)

    def update_ready(self, player):
        self.player_ready[player] = not self.player_ready[player]

    def connected(self):
        return self.ready

