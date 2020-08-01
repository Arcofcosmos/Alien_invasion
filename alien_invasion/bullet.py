import pygame
"""导入精灵类,即可移动的小图像可与其它图像交互"""
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对子弹进行管理的类，继承精灵类"""
    
    def  __init__(self, ai_settings, screen, ship):
        super().__init__()  #关联父类子类，等同于super(Bullet, self).__init__()
        self.screen = screen

        #在（0,0）处创建表示子弹的矩形，再设置其正确位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
             ai_settings.bullet_height)  #设置子弹rect属性
        #设置子弹位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color  #子弹颜色
        self.speed_factor = ai_settings.bullet_speed_factor  #子弹速度

    def  update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect位置
        self.rect.centery = self.y

    def  draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect) #(屏幕，颜色，子弹rect)  