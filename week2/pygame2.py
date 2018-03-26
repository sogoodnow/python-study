import pygame
from pygame.locals import *
import time
import random

HERO_SPEED = 10  # 英雄飞机速度
BULLET_SPEED = 10 # 子弹速度
ENEMY_SPEED = 4 # 敌机速度
ENEMY_IMG1 = "./images/e0.png"   # 敌机图片1
ENEMY_IMG2 = "./images/e1.png"   # 敌机图片2
HERO_IMG = "./images/me.png"    # 英雄图片
BULLET_IMG1 = "./images/pd.png"  # 英雄子弹图片
BULLET_IMG2 = "./images/epd.png"  # 敌机子弹图片
MAIN_IMG = "./images/bg2.jpg"   # 背景图片
MAIN_BOMB = "./images/aa.jpg"  # 爆炸图片
BULLET_ENEMY = 8            # 敌机子弹速度

class Game:
    """
    定义游戏元素父类
    """
    def __init__(self,screen_temp, img_path):
        self.screen_plane = screen_temp  # 窗口对象
        self.image = pygame.image.load(img_path)  # 飞机的图片
        self.size = self.image.get_size()
        # 显示飞机
    def display(self):
        self.screen_plane.blit(self.image, (self.x, self.y))  # 填充画布

class Bullet(Game):
    """
    子弹
    """
    def __init__(self,screen_bullet, posX ,posY, flag):
        self.x = posX
        self.y = posY
        self.flag = flag
        if flag=="hero":
            Game.__init__(self, screen_bullet, BULLET_IMG1)
        else:
            Game.__init__(self, screen_bullet, BULLET_IMG2)
    def __del__(self):
        print("销毁对象")
    # 显示英雄子弹
    def display(self):
        self.screen_plane.blit(self.image,(self.x ,self.y)) # 填充画布

    # 显示敌人子弹
    def display_enbu(self):
        self.screen_plane.blit(self.image,(self.x+25 ,self.y+80)) # 填充画布

class Enemy(Game):
    """
    敌机
    """
    def __init__(self,screen_enemy):
        self.bullets = []  # 敌发射的子弹
        self.x = random.choice(range(450))  # 随机在屏幕中显示
        self.y = -100  # 初始y坐标为-100
        # 随机选择敌机种类
        if random.choice(range(8))==5:
            Game.__init__(self, screen_enemy, ENEMY_IMG1) # 调用父类初始化 红色机
        else:
            Game.__init__(self, screen_enemy, ENEMY_IMG2)  # 调用父类初始化 普通机
    # 移动
    def move(self):
        self.y += 5
        if random.choice(range(150)) == 25:
            self.x += random.randrange(65)
        if random.choice(range(50))==10 :
            self.x -= random.randrange(65)
    # 开火
    def fire(self):
        if self.y > 10:  # 敌机在屏幕上显示后，添加子弹对象
            bu = Bullet(self.screen_plane, self.x +25, self.y - 25,"enmey")
            self.bullets.append(bu)

class HeroPlane(Game):
    x = 220  # 初始位置
    y = 450
    def __init__(self,screen_plane):
        self.bullets = []   # 英雄发射的子弹啊
        Game.__init__(self, screen_plane, HERO_IMG)
    # 动作
    def mv_left(self):
        """
        # 左移动
        :return:
        """
        if self.x > 0:  # 出界判定
            self.x -= HERO_SPEED
            print("已经向左")
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
        bu = Bullet(self.screen_plane, self.x + 75, self.y - 25, "hero")
        self.bullets.append(bu)


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

class Crash(Game):
    """
    碰撞判断：传递2个对象，判断x范围 与 子弹头范围重叠，如果重叠则视为碰撞，消除对象，产生爆炸效果
    可能会有飞机撞飞机
    :param:   obj1 被碰撞物体1（子弹）
    :param:   obj2 被碰撞物体2
    """
    def __init__(self, obj1 ,obj2,screen_plane):
        Game.__init__(self, screen_plane, MAIN_BOMB)
        # 在Game类中已经通过get_size()方法取得了图片的大小，通过大小加上x、y轴的坐标算出是否进入碰撞区域
        self.x = obj2.x
        self.y = obj2.y
        self.obj1 = obj1
        self.obj2 = obj2
        self.x1 = obj1.x
        self.x2 = obj2.x
        self.y1 = obj1.y
        self.y2 = obj2.y
        self.width1, self.height1 = obj1.size
        self.width2, self.height2 = obj2.size
    def display(self):
        self.screen_plane.blit(self.image, (self.x+25, self.y+25))  # 填充画布

    def crashed_enmey(self):
        return (self.x1 >= self.x2) and (self.x1 <= self.x2+self.width2) and \
               ((self.y1 >= self.y2) and (self.y1 <= self.y2 + self.height2))


    def crashed_hero(self):
        return (self.x1 >= self.x2) and (self.x1 <= self.x2+self.width2) and \
               ((self.y1 >= self.y2) and (self.y1 <= self.y2 + self.height2))

def main():
    # 定义窗体
    screen_main = pygame.display.set_mode((512, 568), 0, 0)
    # 定义背景
    backround = pygame.image.load(MAIN_IMG)
    # # 子弹列表
    # hero_bullet_list = []
    # 创建玩家飞机
    hero = HeroPlane(screen_main)
    enemy_lis = []
    m = -968
    while True:
        # 绘制画面,blit:draw one image onto another 理解为将源图片刷入某一区域或另一图片
        screen_main.blit(backround, (0, m))
        # 生成英雄飞机，接受键盘操作
        hero.display()
        key_control(hero)
        # 在英雄对象按下SPACE键后，生成子弹对象，并添加至列表
        hero_bullet_list = hero.bullets

        # 随机生成放置敌机
        if random.choice(range(20)) == 10:   # 随机数等于某一数值后，产生敌机
            en = Enemy(screen_main)
            enemy_lis.append(en)             # 加入敌机列表

        # 已生成的敌机，每次while循环理解为每一帧，调用移动方法，进行移动
        for en in enemy_lis:
            en.move()               # 移动敌机
            if random.choice(range(20)) == 3:  # 20分之3的概率发射子弹
                en.fire()
            en.display()
            # 在敌机移动过程中，随机产生子弹
            for i in en.bullets:
                i.y += BULLET_ENEMY     # 敌机子弹速度
                i.display_enbu()
                if i.y > 600:  # 已经出界的子弹，销毁对象
                    en.bullets.remove(i)
                crs = Crash(hero, i, screen_main)  # 传入检测对象
                if crs.crashed_hero():  # 如果碰撞则销毁子弹和敌机对象
                    # time.sleep(60)
                    print("中弹了")
                    crs.display()
                    print("game over")


        # 对子弹队列进行位置判断，对已经出界的子弹，销毁对象
        for i in hero_bullet_list:
            if i.y < 0:  # 已经出界的子弹，销毁对象
                hero_bullet_list.remove(i)
                del i
            else:
                i.display()  # 没有出界的则进行移动
                i.y -= BULLET_SPEED


        # 遍历敌机与子弹，判断是否碰撞
        for bu in hero_bullet_list:
            for en in enemy_lis:
                # 进行碰撞检测
                crs = Crash(bu ,en,screen_main)  # 传入检测对象
                if crs.crashed_enmey():    # 如果碰撞则销毁子弹和敌机对象
                    print("碰到了")
                    crs.display()
                    enemy_lis.remove(en)
                    hero_bullet_list.remove(bu)
                    continue


        # 遍历敌机与我及，判断是否碰撞,没有碰撞且出界的则销毁敌机对象
        for en in enemy_lis:
            # 进行碰撞检测
            crs = Crash(hero ,en,screen_main)  # 传入检测对象
            if crs.crashed_enmey():    # 如果碰撞则销毁子弹和敌机对象
                # time.sleep(60)
                print("碰到了")
                crs.display()
                enemy_lis.remove(en)
            if en.y > 570 :
                enemy_lis.remove(en)
                print("销毁敌机对象")





        #  画布控制，每次向+Y反向移动2，当到达一定位置后，重置位置
        m += 2
        if m >= -100:
            m == -968
        pygame.display.update()
        # 定时显示
        time.sleep(0.04)


if __name__ == '__main__':
    main()
