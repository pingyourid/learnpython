import sys
import pygame
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_status import GameStatus
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.my_setting = Settings()        

        self.screen = pygame.display.set_mode((self.my_setting.screen_width, self.my_setting.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.color = self.my_setting.bg_color

        '''放在初始化完成下面'''
        self.ship = Ship(self)

        '''子弹'''
        self.bullets = pygame.sprite.Group()
        self.is_bulleting = False

        '''外星人'''
        self.aliens = pygame.sprite.Group()
        self._build_aliens()

        '''游戏状态'''
        self.status = GameStatus(self)

        '''play按钮'''
        self.play_button = Button(self, 'Play')

    def run_game(self):    
        self._auto_fire()   
        while True:
            self._check_event()
            if self.status.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()            
            self._update_screen()  

    '''--------------------------'''
    def _build_aliens(self):
        alien_sample = Alien(self)

        alien_width = alien_sample.rect.width
        alien_height = alien_sample.rect.height
        '''可用宽度'''
        available_space_x = self.screen.get_rect().width - 2 * alien_width
        available_number_x = available_space_x // (2 * alien_width)
        '''可用高度'''
        available_space_y = self.screen.get_rect().height - 3 * alien_width
        available_number_y = available_space_y // (2 * alien_height)

        for num_y in range(available_number_y):
            for num_x in range(available_number_x):
                alien = self._create_alien(num_x, num_y)
                self.aliens.add(alien)

        

    def _create_alien(self, num_x, num_y):
        alien = Alien(self)
        alien.x = alien.rect.width + num_x * (2 * alien.rect.width)
        alien.rect.x = alien.x

        alien.y = alien.rect.height + num_y * (2 * alien.rect.width)
        alien.rect.y = alien.y
        return alien

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collide()

    def _check_bullet_alien_collide(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self.my_setting._increase_speed()
            self._build_aliens()

    def _update_aliens(self):
        self._check_alien_edge()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alien_bottom()

    def _ship_hit(self):
        self._reset_scene_status()
        self.status.minus_ship()
        sleep(1)

    def _check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break;
            

    def _check_alien_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_alien_direction(alien)
                break;

    def _change_alien_direction(self, alien):
        self.my_setting.alien_direction = self.my_setting.alien_direction * (-1)
        for alien in self.aliens.sprites():
            alien.y += self.my_setting.alien_spped_y
            alien.rect.y = alien.y


    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.timer.cancel()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_key_down(event)
                elif event.type == pygame.KEYUP:
                    self._check_key_up(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_mouse_down(mouse_pos)

    def _check_key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.right_moving = True
        elif event.key == pygame.K_LEFT:
            self.ship.left_moving = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # self._fire_bullet()
            self.fire_job.resume()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.right_moving = False
        elif event.key == pygame.K_LEFT:
            self.ship.left_moving = False
        elif event.key == pygame.K_SPACE:
            # self._fire_bullet()
            self.fire_job.pause()

    def _check_mouse_down(self, pos):
        if self.play_button.rect.collidepoint(pos):
            self._start_game()


    def _start_game(self):
         if not self.status.game_active:
            self.status.reset()
            self.status.game_active = True
            self._reset_scene_status()  
            self.my_setting._init_dynamic_setting()
            pygame.mouse.set_visible(False) 

    def _reset_scene_status(self):
        self.aliens.empty()
        self.bullets.empty()
        self._build_aliens()
        self.ship.center_place()

    def _auto_fire(self):
        scheduler = BackgroundScheduler()
        self.fire_job = scheduler.add_job(self._fire_bullet, 'interval', seconds=0.1)
        scheduler.start()
        self.fire_job.pause()           
        
    def _update_screen(self):
        self.screen.fill(self.color)        

        self.ship.blitme()
        '''绘制子弹'''
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        if not self.status.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
