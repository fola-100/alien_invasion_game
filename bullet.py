from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, bullet_chars, space_craft,screen):
        super().__init__()
        self.color= bullet_chars.color
        self.screen=screen
        self.bullet_speed=bullet_chars.speed
        self.rect=pygame.Rect(0,0,bullet_chars.x,bullet_chars.y)
        self.rect.center=space_craft.rect.center
        self.x = float(self.rect.x)

    def update(self):
       self.x+=self.bullet_speed
       self.rect.x=self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

