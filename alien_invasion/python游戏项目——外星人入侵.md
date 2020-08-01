# python游戏项目——外星人入侵

## 1.应用pygame模块

pygame模块是此游戏开发核心模块，应用各类函数优化游戏：

`pygame.init()`  初始化游戏

`pygame.display.set_mode(width, height)`  设置屏幕尺寸

`pygame.display.set_caption(title)`  设置屏幕标题

`self.font.render(str, bool, text_color, background_color)`  将字符串渲染成图像，bool为是否开抗锯齿

`pygame.font.SysFont(font, number)`  返回字体和字号

`pygame.Rect(x, y, width, height)`  返回rect值，参数为坐标和宽高

`screen.get_rect()`  获取屏幕rect属性

`rect.collidepoint(mouse_x, mouse_y)`  检查坐标是否在rect内

`pygame.K_LEFT`  左键

`pygame.K_RIGHT`  右键

`pygame.K_SPACE`  空格键

`pygame.K_q`  Q键

`pygame.QUIT`  动作类型为退出

`pygame.KEYDOWN`  动作类型为按下按键

`pygame.KEYUP`  动作类型为松开按键

`pygame.MOUSEBUTTONDOWN`  动作类型为按下鼠标

`mouse_x, mouse_y = pygame.mouse.get_pos()`  返回一个包含鼠标x, y坐标的元组

`pygame.event.get()`  获取用户当前动作的事件列表，列表中的event

`event.type`  动作类型

`event.key`  动作按键种类

`pygame.mouse.set_visible(False)`  隐藏鼠标光标

`pygame.draw.rect(screen, color, rect)`  绘制子弹

`pygame.image.load('')`  返回项目文件夹下的图像

`from pygame.sprite import Sprite`  导入精灵类，通过继承来管理创造的元素编组

`from pygame.sprite import Group`  导入编组，类似列表，存储精灵或实例对象



## 2.游戏编写流程

确定游戏各种功能，分别写为函数和类添加到主函数中运行

1. 建立一个settings类，存储游戏各类设置值及初始化设置函数
2. 建立个functions模块，存储游戏各项功能的函数
3. 建立个ship类，存储飞船属性、更新飞船位置、绘制飞船
4. 建立个bullet类，存储子弹属性、更新子弹位置、绘制子弹
5. 建立个alien类，存储外星人属性，更新外星人位置、绘制外星人、检查外星人是否到达屏幕边缘
6. 建立个GameStats类，存储游戏统计信息，如游戏状态、得分、等级及重置信息函数
7. 建立个button类，建立个按钮来决定是否开始游戏，将字符渲染成图像并绘制
8. 建立个scoreboard类，将当前比分与最高得分及剩余飞船绘制成图像
9. 在主函数alien_invasion中运行









