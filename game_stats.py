class GameStats:
    def __init__(self,game_settings):
        self.game_controls=game_settings
        self.game_active=True
        self.reset()

    def reset(self):
        self.ship_left=self.game_controls.ship_left


