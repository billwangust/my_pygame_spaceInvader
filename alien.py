import pygame

import os 

from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self,setting,win):
        super().__init__()
        self.setting = setting
        self.win = win
        
        self.image = pygame.image.load(os.path.join("image","alien.bmp"))
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.y = float(self.rect.y)
        
    
        
    def update(self):
        self.y += (self.setting.ALIEN_SPEED)
        self.rect.y = self.y
        
    def blit_me(self):
        self.win.blit(self.image,self.rect)