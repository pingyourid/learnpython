class Settings:
    def __init__(self):
        '''初始化设置'''
        self.bg_color = (230, 230, 230)
        self.screen_width = 800
        self.screen_height = 800

        '''ship'''        
        self.ship_counts = 3

        '''子弹'''        
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        '''外星人'''
        self.alien_spped_y = 20
        self.alien_direction = 1

        self.speed_scale = 1.1

        self._init_dynamic_setting()

    def _init_dynamic_setting(self):
        '''ship'''
        self.speed = 1.5
        '''子弹'''
        self.bullet_speed = 1.0
        '''外星人'''
        self.alien_speed_x = 0.3

    def _increase_speed(self):
        self.speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed_x *= self.speed_scale