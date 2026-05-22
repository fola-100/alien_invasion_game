class SpaceShip:

    def __init__(self, ship_image,screen):
        self.ship_image = ship_image
        self.screen=screen.get_rect()
        # rect stores position
        self.rect = self.ship_image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.centery= self.screen.centery
        self.rect.left=self.screen.left

    def move_right(self):
        self.rect.x += 5

    def move_left(self):
        self.rect.x -= 5

    def move_up(self):
        self.rect.y -= 5

    def move_down(self):
        self.rect.y += 5




















