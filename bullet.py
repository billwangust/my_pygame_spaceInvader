import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,setting,win,ship):
        super().__init__()
        self.win = win
        self.rect = pygame.Rect(0,0,setting.BULLET_WIDTH,setting.BULLET_HEIGHT)
        self.color = setting.BULLET_COLOR
        self.speed = setting.BULLET_SPEED
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        
    def draw_bullet(self):
        pygame.draw.rect(self.win,self.color,self.rect)
        
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y