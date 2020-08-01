import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并初始化其位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  #获取飞船图像的rect属性
        self.screen_rect = screen.get_rect()  #获取屏幕的rect属性

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  #飞船图像的中心x坐标与屏幕相同
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        #rect的centerx等属性只能存储整数值，因此要用变量center
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect属性
        self.rect.centerx = self.center  #此时rect.centerx扔存储整数部分，但整体问题不大

    def blitme(self):
        """在指定地方绘制飞船"""
        self.screen.blit(self.image, self.rect)  #在screen中将image放在位置position上，blit(image, position)


    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.rect.x = self.screen_rect.centerx

