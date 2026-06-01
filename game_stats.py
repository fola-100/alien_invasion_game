class GameStats:
    def __init__(self, rocket_settings):
        self.rockets=rocket_settings
        self.game_active=False
        self.reset()

    def reset(self):
        self.ship_left=self.rockets.ship_left


