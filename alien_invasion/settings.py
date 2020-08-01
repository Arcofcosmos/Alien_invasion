class Settings():
    """存储《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1300
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        #飞船设置
        #self.ship_speed_factor = 1.5   #飞船移动速度设置
        self.ship_limit = 3  #拥有的飞船数量

        #子弹设置属性
        #self.bullet_speed_factor = 1  #子弹速度1像素
        self.bullet_width = 3  #子弹宽度3像素
        self.bullet_height = 15  #子弹高度15像素
        self.bullet_color = 60, 60, 60  #子弹颜色深灰色
        self.bullets_allowed = 3  #屏幕上未消失的子弹数量限制

        #外星人设置
       # self.alien_speed_factor = 1  #外星人移动速度
        self.fleet_drop_speed = 10  #外星人群向下移动速度
        #fleet_direction为1表示向右移，-1表示向左移
        #self.fleet_direction = 1

        #加快游戏节奏设置
        self.speedup_scale = 1.5

        #每消灭一批外星人点数提高的速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        #fleet_direction为1表示右，为-1表示左
        self.fleet_direction = 1

        #记分
        self.alien_points = 50


    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale) 
        



