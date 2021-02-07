import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.my_setting = ai_game.my_setting
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        '''移动标识'''
        self.right_moving = False
        self.left_moving = False

        self.speed = self.my_setting.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x = float(self.rect.x)

        if self.right_moving and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.left_moving and self.x > 0:
            self.x -= self.speed
        self.rect.x = self.x

    def center_place(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)