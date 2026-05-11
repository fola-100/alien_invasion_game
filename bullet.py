from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,speed,bullet_image,space_craft):
        super().__init__()
        self.image= bullet_image
        self.bullet_speed=speed
        self.rect=bullet_image.get_rect()
        self.rect.center=space_craft.rect.center
        self.x = float(self.rect.x)


    def update(self):
       self.x+=self.bullet_speed
       self.rect.x=self.x

