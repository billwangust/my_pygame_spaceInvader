import sys

import os

import pygame

from bullet import Bullet

from alien import Alien




def check_key_down(event,setting,win,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
            ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting,win,ship,bullets)
    
def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False    
    elif event.key == pygame.K_UP:
            ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False

            
def check_event(setting,win,ship,bullets):
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_key_down(event, setting, win, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_key_up(event, ship)
                
def update_screen(setting,win,ship,aliens,bullets,score):
    win.fill(setting.BG_COLOR)
    ship.blit_me()
    
    aliens.draw(win)
    score.write()
    for bullet in bullets.sprites():
        bullet.draw_bullet() 
    for alien in aliens:
        if alien.rect.bottom >= setting.HEIGHT:
            ship_hit(setting, win, ship, aliens, bullets)
    game_end(setting,win)
         
    
 
def update_bullet(setting,win,aliens,bullets,score):
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collision:
        setting.init_score += 1
        score.pre_score()
    if len(aliens) == 0:
        bullets.empty()
        alien_fleet(setting, win, aliens)
            
def fire_bullet(setting,win,ship,bullets):
    if len(bullets) < setting.BULLET_MAX:
            shoot_spund()
            new_bullet = Bullet(setting, win, ship)
            bullets.add(new_bullet)
    
            
def num_aliens(setting,alien_width):
    available_x_width = setting.WIDTH - 2 * alien_width
    number_x = int(available_x_width / (2 * alien_width))
    return number_x

def create_alien(setting,win,aliens,alien_num):
    alien = Alien(setting, win)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    aliens.add(alien)
    
def alien_fleet(setting,win,aliens):
    alien = Alien(setting, win)
    number_x = num_aliens(setting,alien.rect.width)
    for alien_num in range(number_x):
        create_alien(setting, win, aliens, alien_num)
        
def ship_hit(setting,win,ship,aliens,bullets):
    
        setting.ship_life -= 1  
        aliens.empty()
        bullets.empty()
        crash_sound()
        pygame.time.delay(1000) 
        alien_fleet(setting, win, aliens)
        ship.center_ship()
          
def shoot_spund():
    shoot = pygame.mixer.Sound(os.path.join("sound","shooting.mp3"))
    pygame.mixer.Sound.play(shoot)
    
def crash_sound():
    crash = pygame.mixer.Sound(os.path.join("sound","crash.mp3"))
    pygame.mixer.Sound.play(crash)


def prep_ship(setting,ship,win):
    ship_list = list(range(setting.ship_life))
    for i,j in enumerate(ship_list):
        j = pygame.image.load(os.path.join("image","ship.bmp"))
        # j_rect = j.get_rect()
        #j_rect.center = ( )
        win.blit(j, (i*50+10,10))

def game_end(setting,win):
    if setting.ship_life <= 0:
        pen = pygame.font.SysFont("comicsans", 100)
        lose_text = pen.render("YOU LOSE", 1, (255,0,0))
        rect = lose_text.get_rect()
        rect.centerx, rect.centery = setting.WIDTH//2, setting.HEIGHT//2
        win.blit(lose_text, (rect))
        pygame.display.flip()
        pygame.time.delay(5000)
        sys.exit()
    
def bgm():
    pygame.mixer.music.load(os.path.join("sound","bgm.mp3"))
    pygame.mixer.music.set_volume(7)
    pygame.mixer.music.play(-1)
        
        
        
        