class ServerGame:
    def __init__(self, id):
        self.p0Ready = False
        self.p1Ready = False
        self.ready = False
        self.id = id
        self.paddle_pos = [[0, 0], [0, 0]]
        self.scores = [0, 0]
        self.lives = [5, 5]

    def get_player_paddle_pos(self, player):
        return self.paddle_pos[player]

    def update(self, player, paddle_pos):
        self.paddle_pos[player] = paddle_pos

    def connected(self):
        return self.ready

