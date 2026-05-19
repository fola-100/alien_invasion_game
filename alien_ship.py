from pygame.sprite import Sprite

class AlienCraft(Sprite):
    def __init__(self,image,screen,settings):
        super().__init__()
        self.image=image
        self.screen_size=screen.get_rect()
        self.settings=settings
        self.rect=image.get_rect()
        self.rect.centery=self.screen_size.centery
        self.rect.right=self.screen_size.right
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def update(self):
        self.y+= self.settings.speed * self.settings.vertical_direction
        self.rect.y=self.y


    def check_edge(self):
        return self.rect.top <= 0 or self.rect.bottom >= self.screen_size.bottom










        


