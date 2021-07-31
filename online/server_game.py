class ServerGame:
    def __init__(self, id):
        self.p0Ready = False
        self.p1Ready = False
        self.ready = False
        self.id = id
        self.paddle_pos = [[0, 0], [0, 0]]
        self.paddle_cols = [None, None]
        self.player_names = ["Not connected", "Not connected"]
        self.scores = [0, 0]
        self.lives = [5, 5]

    def get_player_paddle_pos(self, player):
        return self.paddle_pos[player]

    def update_x(self, player, paddle_pos_x):
        self.paddle_pos[player][0] = int(paddle_pos_x)

    def update_y(self, player, paddle_pos_y):
        self.paddle_pos[player][1] = int(paddle_pos_y)

    def update_name(self, player, name):
        self.player_names[player] = name

    def update_paddle_col(self, player, color):


    def connected(self):
        return self.ready
