import pygame.font

class ScoreBoard():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.status = ai_game.status

        self.text_color = (30, 30, 30)
        self.bg_color = ai_game.my_setting.bg_color
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        score_str = str(self.status.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)