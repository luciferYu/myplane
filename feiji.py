# -*- coding:utf-8 -*-
#auth:zhiyi
import pygame
import time
import sys
from pygame.locals import *
import math

class Hero(object):
    def __init__(self,weight,height):
        '''初始化飞机'''
        self.image = pygame.image.load('./resource/hero1.png')
        self.position = self.x,self.y = weight / 2 - (100 / 2),height - 150
        self.speed = 5

    def move(self):
        '''增加飞机移动方法'''
        key_pressed = pygame.key.get_pressed()  # 注意这种方式是能够检测到连续按下的，比之前的版本要新

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed

    def display(self,screen):
        #  将飞机图片粘贴到窗口中
        screen.blit(self.image,(self.x,self.y))



def main():
    #整体流程控制
    #  创建一个窗口显示东西
    weight = 400  #  屏幕的宽度
    height = 600  #  屏幕的高度
    #  设置屏幕的大小
    screen = pygame.display.set_mode((weight,height),0,32)

    #  创建一个背景图片
    background = pygame.image.load('./resource/background.png')
    #   创建一个英雄飞机
    hero = Hero(weight, height)
    while True:
        #  添加事件循环
        for event in pygame.event.get():
            #判断退出条件
            if event.type == pygame.QUIT:
                sys.exit()


        #  3.将背景图片粘贴到窗口中
        screen.blit(background, (0, 0))

        hero.move()

        hero.display(screen)

        #  4.显示窗口中的内容
        pygame.display.update()

        #  暂停0.05秒显示
        time.sleep(0.05)


if __name__ == '__main__':
    main()