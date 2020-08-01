import  pygame
#导入Group类,创建编组类似于列表
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
#from bullet import Bullet
import game_functions as gf

def  run_game():
    #初始化游戏
    pygame.init()  
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  #定义屏幕尺寸
    pygame.display.set_caption("Alien Invasion")  #设置屏幕标题

    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建一个存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #bullet_fu = Bullet(ai_settings, screen, ship)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建外星人编组
    aliens = Group()

    #创建一个外星人
    alien = Alien(ai_settings, screen)

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)


    #开始游戏主循环
    while  True:

        #监听用户行为
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()  #更新飞船位置
            # bullet_fu.update()  #调用update(),
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                            bullets, play_button)  #更新屏幕图像

run_game()