import pygame

class Score:
    def __init__(self, win, setting):
        self.setting = setting
        self.win = win
        self.color = (60, 60, 60)
        self.size = 20
        self.pen = pygame.font.SysFont("comicsans", self.size)
        self.pre_score()
        
    def pre_score(self):
        
        
        self.text = self.pen.render(f"SCORE : {self.setting.init_score}", 1, self.color)
        self.rect = self.text.get_rect()
        self.rect.x = self.setting.WIDTH - self.size * 8
        self.rect.y = self.size 
        
        
    def write(self):
        self.win.blit(self.text, (self.rect))
        
        