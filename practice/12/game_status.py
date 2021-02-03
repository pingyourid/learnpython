import pygame

class GameStatus:
    def __init__(self, ai_game):
        self.my_setting = ai_game.my_setting
        self.reset()
        self.game_active = False

    def reset(self):
        self.ship_left = self.my_setting.ship_counts
        self.score = 0

    def minus_ship(self):
        if self.ship_left > 0:
            self.ship_left -= 1;
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)