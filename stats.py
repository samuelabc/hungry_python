class Stats:
    def __init__(self, snake_game):
        self.settings = snake_game.settings
        self.game_active = True
        self.highscore = 0

    def update_highscore(self, score):
        if score > self.highscore:
            self.highscore = score
