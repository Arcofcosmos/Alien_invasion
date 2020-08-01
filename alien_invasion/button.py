#pygame.font模块可将文本渲染到屏幕
import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  #设置按钮rect对象为绿色
        self.text_color = (255, 255, 255)  #设置文本颜色为白色
        self.font = pygame.font.SysFont(None, 48)  #设置字体，None为默认字体，48为字号

        #创建按钮的rect对象，使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #按钮的标签只需创建一次
        self.prep_msg(msg)


    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        #msg表示文本,True为是否开启反锯齿，得到msg_image文本图像
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center  #文本居中


    def draw_button(self):
        #prep_msg(msg)
        #绘制一个颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)  #在屏幕上绘制文本图像