#import this
#import antigravity
import os

import pygame

from pygame.sprite import Group

import game_func as gf

from bullet import Bullet

from settings import Settings

from ship import Ship

from alien import Alien

from game_stats import Score



def run_game():
    
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    set = Settings()
    win = pygame.display.set_mode((set.WIDTH,set.HEIGHT))
    space_ship = Ship(win)
    score = Score(win,set)
    bullets = Group()
    aliens = Group()
    gf.alien_fleet(set, win, aliens)
    pygame.display.set_caption(set.GAME_NAME)
    gf.bgm()
    while 1:
        pygame.mouse.set_visible(0)
        clock.tick(set.FPS)
        gf.check_event(set,win,space_ship,bullets)
        
        space_ship.move_ship(set)
        aliens.update()
        gf.update_screen(set,win,space_ship,aliens,bullets,score)
        gf.prep_ship(set, space_ship, win)
        gf.update_bullet(set,win,aliens,bullets,score)
        if pygame.sprite.spritecollideany(space_ship, aliens):
            gf.ship_hit(set, win, space_ship, aliens, bullets)
        pygame.display.flip()     
        
    
if __name__ == '__main__':
    run_game()
