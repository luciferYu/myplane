# -*- coding:utf-8 -*-
#auth:zhiyi
import pygame
import time
import sys
from pygame.locals import *
import math

def main():
    #整体流程控制
    #  创建一个窗口显示东西
    weight = 400  #  屏幕的宽度
    height = 600  #  屏幕的高度
    #  设置屏幕的大小
    screen = pygame.display.set_mode((weight,height),0,32)

    #  创建一个背景图片
    background = pygame.image.load('./resource/background.png')
    #  创建一个玩家飞机图片
    hero = pygame.image.load('./resource/hero1.png')

    # 创建一个敌机
    enemy = pygame.image.load('./resource/enemy-3.gif')




    #screen.blit(enemy, (weight / 2 - (140 / 2), height - 580))

    x =  weight / 2 - (100 / 2)
    y =  height - 150
    z = 1

    while True:
        #  添加事件循环
        for event in pygame.event.get():
            #判断退出条件
            if event.type == pygame.QUIT:
                sys.exit()
            #判断键盘是否是按下了键
            elif event.type == KEYDOWN:
                #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    x -= 5
                elif event.key == K_s or event.key == K_DOWN:
                    y += 5
                elif event.key == K_d or event.key == K_RIGHT:
                    x += 5
                elif event.key == K_w or event.key == K_UP:
                    y -= 5


        #  3.将背景图片粘贴到窗口中
        screen.blit(background, (0, 0))
        z += 1
        x += math.sin(z)* 60
        y = math.sin(z)* 60 + 200
        #  将飞机图片粘贴到窗口中
        screen.blit(hero, (x,y))
        #screen.blit(hero, (x,y))


        #  4.显示窗口中的内容
        pygame.display.update()

        #  暂停0.05秒显示
        time.sleep(0.1)


if __name__ == '__main__':
    main()