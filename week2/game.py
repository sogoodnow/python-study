import pygame
from pygame.locals import *
import time

HERO_SPEED = 10  # 英雄飞机速度

class Plane:
    def __init__(self,screen_plane):
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
        print("fire")

def main():
    # 定义窗体
    screen_main = pygame.display.set_mode((512, 568), 0, 0)
    # 定义背景
    backround = pygame.image.load("./images/bg2.jpg")
    # 创建玩家飞机
    hero = Plane(screen_main)

    m = -968
    while True:
        # 绘制画面,blit:draw one image onto another 理解为将源图片刷入某一区域或另一图片
        screen_main.blit(backround, (0, m))
        # 显示英雄飞机
        hero.display()
        # 飞机控制，传入英雄飞机对象
        key_control(hero)

        m += 2
        if m >= -100:
            m == -968
        pygame.display.update()
        # 定时显示
        time.sleep(0.04)


if __name__ == '__main__':
    main()
