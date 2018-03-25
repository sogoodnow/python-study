import pygame
from pygame.locals import *
import time
import random

HERO_SPEED = 10  # 英雄飞机速度
BULLET_SPEED = 10 # 子弹速度
ENEMY_SPEED = 10 # 敌机速度
class Enemy:
    def __init__(self,screen_enemy):
        self.bullets = []
        self.x = random.choice(range(450))
        self.y = -100
        self.screen_plane = screen_enemy  # 窗口对象
        self.image = pygame.image.load("./images/e0.png")  # 飞机的图片
    # 显示飞机
    def display(self):
        self.screen_plane.blit(self.image,(self.x ,self.y)) # 填充画布
    # 移动
    def move(self):
        self.y += 5


class Bullet:
    def __init__(self,screen_bullet, posX ,posY):
        self.x = posX
        self.y = posY
        self.screen_plane = screen_bullet  # 窗口对象
        self.image = pygame.image.load("./images/pd.png")  # 子弹的图片
    def __del__(self):
        print("销毁对象")
    # 显示子弹
    def display(self):
        self.screen_plane.blit(self.image,(self.x ,self.y)) # 填充画布


class HeroPlane:
    def __init__(self,screen_plane):
        self.bullets = []
        self.x = 220
        self.y = 450
        self.screen_plane = screen_plane  # 窗口对象
        self.image = pygame.image.load("./images/me.png")  # 飞机的图片
    # 显示飞机
    def display(self):
        self.screen_plane.blit(self.image,(self.x ,self.y)) # 填充画布
    # 动作
    def mv_left(self):
        """
        # 左移动
        :return:
        """
        if self.x > 0:  # 出界判定
            self.x -= HERO_SPEED
        else:
            self.x == 0
    def mv_right(self):
        """
        # 右移动
        :return:
        """
        if self.x < 400:
            self.x += HERO_SPEED
        else:
            self.x == 400
    def mv_up(self):
        """
        # 上移动
        :return:
        """
        if self.y > 0:   # 出界判定
            self.y -= HERO_SPEED
        else:
            self.y ==0
    def mv_down(self):
        """
        # 下移动
        :return:
        """
        if self.y < 500:   # 出界判定
            self.y += HERO_SPEED
        else:
            self.y == 500

    def mv_fire(self):
        """
        # 空格键开火,开火时新建子弹对象
        :return:
        """
        # 创建子弹
        bu = Bullet(self.screen_plane, self.x + 75, self.y - 25)
        self.bullets.append(bu)

        print("fire")

def key_control(hero):
    """
    用于获取键盘控制操作,并进行对应处理
    :return:
    """
    # 退出操作
    for ev in pygame.event.get():
        if ev.type == QUIT:
            print("exit")
            exit()
    # 按键接收
    key_pressed = pygame.key.get_pressed()
    # A或左键
    if key_pressed[K_LEFT] or key_pressed[K_a]:
        hero.mv_left()
        print("left")
    # d或右键
    if key_pressed[K_RIGHT] or key_pressed[K_d]:
        hero.mv_right()
        print("right")

    # w或上键
    if key_pressed[K_UP] or key_pressed[K_w]:
        hero.mv_up()
        print("up")
    # s或下键
    if key_pressed[K_DOWN] or key_pressed[K_s]:
        hero.mv_down()
        print("down")
    # SPACE键
    if key_pressed[K_SPACE]:
        hero.mv_fire()
        print("fire")

def main():
    # 定义窗体
    screen_main = pygame.display.set_mode((512, 568), 0, 0)
    # 定义背景
    backround = pygame.image.load("./images/bg2.jpg")
    # 显示子弹

    # 创建玩家飞机
    hero = HeroPlane(screen_main)
    enemy_lis = []

    m = -968
    while True:
        # 绘制画面,blit:draw one image onto another 理解为将源图片刷入某一区域或另一图片
        screen_main.blit(backround, (0, m))

        if random.choice(range(50)) == 10:
            en = Enemy(screen_main)
            enemy_lis.append(en)
        for en in enemy_lis:
            en.move()
            en.display()
        hero.display()

        # 飞机控制，传入英雄飞机对象
        key_control(hero)
        buli = hero.bullets
        # print(len(buli))
        for i in buli:

            if i.y < 0:  # 已经出界的子弹，销毁对象
                buli.remove(i)
                del i
            else:
                i.display()
                i.y -= BULLET_SPEED
        m += 2
        if m >= -100:
            m == -968
        pygame.display.update()
        # 定时显示
        time.sleep(0.04)


if __name__ == '__main__':
    main()
