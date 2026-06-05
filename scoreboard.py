import pygame

class Scoreboard:
    def __init__(self, screen, game_stat):
        self.display_score= "SCORE:"
        self.display_highest_score= "TOP-SCORE:"
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.game_stat=game_stat
        self.width=170
        self.height=40
        self.top_score_width=250
        self.top_score_height=40
        self.text_color=(253,253,253)
        self.back_ground_color=(0,0,255)
        self.font=pygame.font.SysFont(None, 39)
        #self.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top=self.screen_rect.top+10
        self.rect.left=self.screen_rect.left
        self.top_score_rect=pygame.Rect(0, 0, self.top_score_width, self.top_score_height)
        self.top_score_rect.top=self.screen_rect.top+10
        self.top_score_rect.right=self.screen_rect.right-20
        self.score_display()
        self.pre_score()
        self.display_top_score()
        self.pre_high_score()

    def score_display(self):
        self.display_image = self.font.render(self.display_score, True, self.text_color)
        self.display_image_rect= self.display_image.get_rect()
        self.display_image_rect.left=self.rect.left
        self.display_image_rect.top=self.rect.top

    def pre_score(self):
        self.score_color=(0,0,0)
        rounded_score=round(self.game_stat.score,-1)
        "{:,}".format(rounded_score)
        str_rounded_score=str(rounded_score)
        self.score_image=self.font.render(str_rounded_score, True, self.score_color)
        self.score_image_rect=self.score_image.get_rect()
        self.score_image_rect.right=self.rect.right
        self.score_image_rect.top = self.rect.top

    def display_top_score(self):
       self.top_score_image= self.font.render(self.display_highest_score, True, self.text_color)
       self.top_score_image_rect=self.top_score_image.get_rect()
       self.top_score_image_rect.left =self.top_score_rect.left
       self.top_score_image_rect.top=self.top_score_rect.top

    def  pre_high_score(self):
        self.high_score_color=(0,0,0)
        roundup_score_high= round(self.game_stat.high_score,-1)
        "{:,}".format(roundup_score_high)
        roundup_score_high_str=str(roundup_score_high)
        self.high_score_image= self.font.render(roundup_score_high_str, True, self.score_color)
        self.high_score_image_rect= self.high_score_image.get_rect()
        self.high_score_image_rect.right= self.top_score_rect.right
        self.high_score_image_rect.top=self.top_score_rect.top

    def show_score(self):
        self.screen.fill(self.back_ground_color,self.rect)
        #Text-Image
        self.screen.blit(self.display_image,self.display_image_rect)
        #Score_value
        self.screen.blit(self.score_image,self.score_image_rect)
        #Top_score_display
        self.screen.fill(self.back_ground_color, self.top_score_rect)
        #Text-Image
        self.screen.blit(self.top_score_image,self.top_score_image_rect)
        #Score_value
        self.screen.blit(self.high_score_image,self.high_score_image_rect)
        
