import sys

import pygame

from time import sleep  #sleep()暂停游戏

from bullet import Bullet
from alien import Alien

#按键按下判断
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:  #按右键
        #向右移动飞船
        ship.moving_right = True  #开始移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
         

#按键松开判断
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False  #停止移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def  check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():  #该方法获得用户当前所做动作的事件列表
        if event.type == pygame.QUIT:  #判断事件类型是否为退出
            sys.exit()  #退出游戏

        elif event.type == pygame.KEYDOWN:  #按键事件响应
            check_keydown_events(event, ai_settings, screen, ship, bullets)
                    
        elif event.type == pygame.KEYUP:  #检测到按键松开
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()  #返回一个包含鼠标x,y坐标的元组
            check_play_button(ai_settings, screen, stats, sb,  play_button, ship, aliens,
                        bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                        bullets, mouse_x, mouse_y):
    """玩家单击Play时开始新游戏"""
    #collidepoint()检查参数坐标是否在Play的rect内
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    #游戏非活动状态时才可启动，避免游戏开始也可重置
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()

        #隐藏光标
        pygame.mouse.set_visible(False)

        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        #重置记分的图像
        sb.prep_level()
        sb.prep_score()
        sb.prep_ships()

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets):
    """若子弹数量未达到限制，就发射一颗"""
    if len(bullets) < ai_settings.bullets_allowed:
        #创建一颗子弹，并将其加入编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def  update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹位置，并删除已消失的子弹"""
    #更新子弹位置
    bullets.update()
    #删除已经消失的子弹
    for bullet in bullets.copy():   #copy()复制编组元素
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  #删除到屏幕顶端的子弹
    #print(len(bullets))  #显示剩余子弹

    #子弹和外星人碰撞措施
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #检查是否有子弹击中了外星人
    #如果是这样，就删除对应的子弹和外星人
    """sprite.groupcollide()返回一个字典，子弹为键，外星人为值，
        后面两个布尔实参表示两个精灵碰撞后消失有效，若为False表示不消失"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        #确保每个被消灭的外星人都可以加分
        for aliens in collisions.values():  #每个值都是个列表
            stats.score += ai_settings.alien_points * len(aliens) 
            sb.prep_score()
        check_high_score(stats, sb)

    #检查外星人是否被全部消灭，若是就再创造一批外星人
    if len(aliens) == 0:
        bullets.empty()  #删除屏幕剩余所有子弹
        ai_settings.increase_speed()

        #提高游戏等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)



def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移并且改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed  #向下移动
    ai_settings.fleet_direction *= -1  #移动方向改变

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达屏幕边缘时实施措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        #碰撞后飞船数量减1
        stats.ships_left -= 1

        #更新记分牌
        sb.prep_ships()

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新外星人，并将飞船放在屏幕低端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #暂停一下
        sleep(0.5)

    else:
        stats.game_active = False

        #游戏结束，显示光标
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞到一样地处理
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break


def  update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #检测外星人与飞船之间的碰撞
    ""#检查编组中是否有成员与精灵ship发生碰撞,若无则返回None"""
    if pygame.sprite.spritecollideany(ship, aliens):  
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    #检查是否有外星人撞到了屏幕底端，并做处理
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def get_number_aliens_x(ai_settings, alien_width):
    #计算每行可以容纳多少个外星人
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return  number_alien_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return  number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #创建一个外星人并将其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可以容纳多少个外星人
    #外星人间距为外星人宽度，两边的外星人与屏幕间距宽度为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


def check_high_score(stats, sb):
    """检查是否产生新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()



def  update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)  #每次循环填充背景色

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():  #bullets.sprites()返回一个精灵列表
        bullet.draw_bullet()   #绘制子弹
    ship.blitme()  #绘制飞船
    aliens.draw(screen)  #绘制外星人,对每个精灵依次调用blit()
    sb.show_score()  #显示得分

    #如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    #更新屏幕
    pygame.display.flip()