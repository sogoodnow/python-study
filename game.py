import pygame
from pygame.locals import *
import time


def key_control():
    for ev in pygame.event.get():
        if ev.type == QUIT:
            exit()

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_LEFT]:
        print("left")

def main():
    # 定义窗体
    screen = pygame.display.set_mode((512, 568), 0, 0)
    # 定义背景
    backround = pygame.image.load("./1.jpg")
    m = -968
    while True:
        # 绘制画面
        screen.blit(backround, (0, m))
        key_control()
        m += 2
        if m >= -200:
            m == -968
        pygame.display.update()
        time.sleep(0.04)


if __name__ == '__main__':
    main()
