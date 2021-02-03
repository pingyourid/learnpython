import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理子弹'''

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.my_setting = ai_game.my_setting
        self.color = self.my_setting.bullet_color

        self.rect = pygame.Rect(0, 0, self.my_setting.bullet_width, self.my_setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.my_setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)