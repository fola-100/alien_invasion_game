import high_score
class GameStats:
    def __init__(self, rocket_settings):
        self.rockets=rocket_settings
        self.game_active=False
        self.pre_high_score()
        self.reset()

    def reset(self):
        self.ship_left=self.rockets.ship_left
        self.score = 0
        self.pre_high_score()

    def pre_high_score(self):
        value=high_score.get_high_score()
        value=int(value)
        self.high_score =value

    def update_high_score(self):
        if self.score> self.high_score:
            self.high_score=self.score
            high_score.store_score(self.high_score)








