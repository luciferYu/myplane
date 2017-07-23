# -*- coding:utf-8 -*-
#auth:zhiyi
import pygame
import time
import sys

def main():
    #整体流程控制
    #  创建一个窗口显示东西
    weight = 400
    height = 600
    screen = pygame.display.set_mode((weight,height),0,32)

    #  创建一个背景图片
    background = pygame.image.load('./resource/background.png')
    #  创建一个玩家飞机图片
    hero = pygame.image.load('./resource/hero1.png')

    #  3.将背景图片粘贴到窗口中
    screen.blit(background,(0,0))
    #  将飞机图片粘贴到窗口中
    screen.blit(hero,(weight/2-(100/2),height-150))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #  4.显示窗口中的内容
        pygame.display.update()

        time.sleep(0.05)


if __name__ == '__main__':
    main()