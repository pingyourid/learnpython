import pygame.font
from pygame.sprite import Group

from ship import Ship

class ScoreBoard():
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.status = ai_game.status

        self.text_color = (30, 30, 30)
        self.bg_color = ai_game.my_setting.bg_color
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        self.status.score = round(self.status.score, -1)
        score_str = "{:,}".format(self.status.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prep_high_score(self):
        self.status.high_score = round(self.status.high_score, -1)
        high_score_str = "{:,}".format(self.status.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.bg_color)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.center = self.screen_rect.center
        self.high_score_image_rect.top = 20

    def prep_level(self):
        level_str = str(self.status.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom + 20

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.status.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.status.score > self.status.high_score:
            self.status.high_score = self.status.score
            self.prep_high_score()          
        
