import pygame

class GameStatus:
    def __init__(self, ai_game):
        self.my_setting = ai_game.my_setting
        self.read_high_score()
        self.reset()
        self.game_active = False

    def reset(self):
        self.ship_left = self.my_setting.ship_counts
        self.score = 0
        self.level = 1

    def minus_ship(self):
        if self.ship_left > 0:
            self.ship_left -= 1;
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def save_high_score(self):
        finename = 'high_score.txt'
        high_score = str(self.high_score)

        with open(finename, 'w') as f:
            f.write(high_score)

    def read_high_score(self):
        self.high_score = 0

        filename = 'high_score.txt'
        try:
            with open(filename) as f:
                num_str = f.read()
                if num_str:
                    self.high_score = int(num_str)
        except Exception as e:
            print('未找到最高分文件')