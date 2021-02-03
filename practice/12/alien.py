import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.my_setting = ai_game.my_setting
        self.screen = ai_game.screen

    def check_edge(self):
        if self.x <= 0 or self.rect.right >= self.screen.get_rect().right:
            return True
        else:
            return False

    def update(self):
        self.x += self.my_setting.alien_speed_x * self.my_setting.alien_direction
        self.rect.x = self.x