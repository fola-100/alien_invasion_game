import pygame

class Scoreboard:
    def __init__(self, screen, game_stat):
        self.display="SCORE:"
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.game_stat=game_stat
        self.width=170
        self.height=35
        self.text_color=(253,253,253)
        self.back_ground_color=(0,0,255)
        self.font=pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.top=self.screen_rect.top+10
        self.rect.left=self.screen_rect.left
        self.score_display()
        self.pre_score()

    def score_display(self):
        self.display_image = self.font.render(self.display, True, self.text_color)
        self.display_image_rect= self.display_image.get_rect()
        self.display_image_rect.left=self.rect.left
        self.display_image_rect.top=self.rect.top
    def pre_score(self):
        self.score_color=(0,0,0)
        self.score_str=str(self.game_stat.score)
        self.score_image=self.font.render(self.score_str,True,self.score_color)
        self.score_image_rect=self.score_image.get_rect()
        self.score_image_rect.right=self.rect.right
        self.score_image_rect.top = self.rect.top
    def show_score(self):
        self.screen.fill(self.back_ground_color,self.rect)
        #Text-Image
        self.screen.blit(self.display_image,self.display_image_rect)
        #Score_value
        self.screen.blit(self.score_image,self.score_image_rect)
