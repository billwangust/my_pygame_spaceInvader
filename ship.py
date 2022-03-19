import pygame

import os

from settings import Settings

class Ship():
       
    def __init__(self,screen):
        self.screen = screen
        
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        
        self.image = pygame.image.load(os.path.join("image","ship.bmp"))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blit_me(self):
        self.screen.blit(self.image,self.rect)
        
    def move_ship(self,setting):
        if self.move_left == True and self.rect.centerx >= 0 + self.rect.width / 2:
            self.rect.centerx -= Settings().SHIP_SPEED
        if self.move_right == True and self.rect.centerx <= setting.WIDTH - self.rect.width / 2:
            self.rect.centerx += Settings().SHIP_SPEED
        if self.move_up == True:
            self.rect.centery -= Settings().SHIP_SPEED
        if self.move_down == True and self.rect.centery <= setting.HEIGHT - self.rect.width / 2:
            self.rect.centery += Settings().SHIP_SPEED
            
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    