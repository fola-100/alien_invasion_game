class SpaceShip:

    def __init__(self, x, y, ship_image):
        self.ship_image = ship_image

        # rect stores position
        self.rect = self.ship_image.get_rect(center=(x, y))

    def move_right(self):
        self.rect.x += 5

    def move_left(self):
        self.rect.x -= 5

    def move_up(self):
        self.rect.y -= 5

    def move_down(self):
        self.rect.y += 5




















