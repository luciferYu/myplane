# -*- coding:utf-8 -*-
#auth:zhiyi

import pygame
import sys
import time
from pygame.locals import *

class Thing(object):
    '''
    定义一个物体的基类
    '''
    def __init__(self,size_x,size_y,image,speed=10):
        self.__size_x = size_x  # 物体的长
        self.__size_y = size_y  # 物体的宽
        self.__image = pygame.image.load(image)  #加载物体的图片
        self.__speed = speed

    def get_size_x(self):
        return self.__size_x

    def get_size_y(self):
        return self.__size_y

    def get_image(self):
        return self.__image

    def get_speed(self):
        return self.__speed

    def move(self):
        #物体的移动方法
        pass

    def is_top(self):
        #判断物体是否上越界
        pass

    def is_bottom(self):
        #判断物体是否下越界
        pass

    def is_left(self):
        #判断物体是否左越界
        pass

    def is_right(self):
        #判断物体是否右越界
        pass

class Plane(Thing):
    pass

class Hero(Plane):
    def __init__(self,main):
        super().__init__(100,124,'./resource/hero1.png')
        self.__position_x = (main.get_weight() / 2) - (self.get_size_x() / 2) # 物体的位置 横坐标
        self.__position_y = main.get_height() - self.get_size_y() - 50  # 物体的位置 纵坐标

    def display(self,main):
        #  将飞机图片粘贴到窗口中
        main.screen.blit(self.get_image(),(int(self.__position_x),int(self.__position_y))) #显示飞机的位置

    def move(self):
        '''增加飞机移动方法'''
        key_pressed = pygame.key.get_pressed()  # 注意这种方式是能够检测到连续按下的，比之前的版本要新

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.__position_y -= self.get_speed()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.__position_y += self.get_speed()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.__position_x -= self.get_speed()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.__position_x += self.get_speed()



class Main(object):
    def __init__(self,weight=400,height=600):
        self.__weight = weight #  屏幕的宽度
        self.__height = height  # 屏幕的高度
        self.background = pygame.image.load('./resource/background.png') #  背景图片
        self.screen = pygame.display.set_mode((self.__weight, self.__height), 0, 32)

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height


    def main(self):
        hero = Hero(m)
        while True:
            #  添加事件循环
            for event in pygame.event.get():
                # 判断退出条件
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.blit(self.background, (0, 0))

            hero.move()


            hero.display(m)



            #  4.显示窗口中的内容
            pygame.display.update()

            #  暂停0.05秒显示
            time.sleep(0.05)



if __name__ == '__main__':
    m = Main()
    m.main()