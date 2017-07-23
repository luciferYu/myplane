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
        self.size_x = size_x  # 物体的长
        self.size_y = size_y  # 物体的宽
        self.__image = pygame.image.load(image)  #加载物体的图片
        self.speed = speed
        self.position_x = 0
        self.position_y = 0

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y

    def get_image(self):
        return self.__image

    def get_speed(self):
        return self.speed

    def move(self):
        #物体的移动方法
        pass

    def is_top(self):
        #判断物体是否上越界
        if self.position_y <= 0:
            return True
        else:
            return False

    def is_bottom(self):
        #判断物体是否下越界
        if (self.position_y + self.size_y) >= m.get_height():
            return True
        else:
            return False

    def is_left(self):
        #判断物体是否左越界
        if self.position_x <= 0:
            return True
        else:
            return False

    def is_right(self):
        #判断物体是否右越界
        if (self.position_x + self.size_x) >= m.get_weight():
            return True
        else:
            return False

class Plane(Thing):
    pass

class Bullet(Thing):
    def __init__(self,main,hero):
        super().__init__(22,22,'./resource/bullet.png')
        self.position_x = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x()/2) + 1 # 物体的位置 横坐标
        self.position_y = hero.position_y - 20  # 物体的位置 纵坐标

    def auto_move(self):
        self.position_y -= self.speed

    def display(self,main):
        #  将飞机图片粘贴到窗口中
        main.screen.blit(self.get_image(),(self.position_x,self.position_y)) #显示子弹的位置

class Hero(Plane):
    def __init__(self,main):
        super().__init__(100,124,'./resource/hero1.png')
        self.position_x = (main.get_weight() / 2) - (self.get_size_x() / 2) # 物体的位置 横坐标
        self.position_y = main.get_height() - self.get_size_y() - 50  # 物体的位置 纵坐标
        self.bullets = []
        #self.bullet_type = Normal_Bullet
        self.bullet_type = Triple_Bullet

    def display(self,main):
        #  将飞机图片粘贴到窗口中
        main.screen.blit(self.get_image(),(int(self.position_x),int(self.position_y))) #显示飞机的位置

    def move(self):
        '''增加飞机移动方法'''
        key_pressed = pygame.key.get_pressed()  # 注意这种方式是能够检测到连续按下的，比之前的版本要新

        if key_pressed[K_w] or key_pressed[K_UP]:
            if not self.is_top():
                self.position_y -= self.get_speed()
            else:
                self.position_y = 0
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            if not self.is_bottom():
                self.position_y += self.get_speed()
            else:
                self.position_y = m.get_height() - self.size_y
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            if not self.is_left():
                self.position_x -= self.get_speed()
            else:
                self.position_x = 0
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            if not self.is_right():
                self.position_x += self.get_speed()
            else:
                self.position_x = m.get_weight() - self.size_x


    def shot(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_SPACE]:
            print('--space--')
            self.bullets.append(self.bullet_type(m,self))
        for bullet in self.bullets:
            bullet.auto_move()
            if not bullet.is_top() or not bullet.is_bottom or not bullet.is_right:
                bullet.display(m)
            else:
                del bullet

class Normal_Bullet(Bullet):
    pass


class Triple_Bullet(Bullet):
    def __init__(self,main,hero):
        super().__init__(main,hero)
        self.position_x1 = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x()/2) + 1 # 物体的位置 横坐标
        self.position_x2 = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x() / 2) + 1  # 物体的位置 横坐标
        self.position_x3 = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x() / 2) + 1  # 物体的位置 横坐标
        self.position_y = hero.position_y - 20  # 物体的位置 纵坐标

    def auto_move(self):
        self.position_x1 -= self.speed
        self.position_x3 += self.speed
        self.position_y -= self.speed

    def display(self,main):
        #  将飞机图片粘贴到窗口中
        main.screen.blit(self.get_image(),(self.position_x1,self.position_y)) #显示子弹的位置
        main.screen.blit(self.get_image(),(self.position_x2,self.position_y)) #显示子弹的位置
        main.screen.blit(self.get_image(),(self.position_x3,self.position_y)) #显示子弹的位置






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
            hero.shot()


            hero.display(m)



            #  4.显示窗口中的内容
            pygame.display.update()

            #  暂停0.05秒显示
            time.sleep(0.05)



if __name__ == '__main__':
    m = Main()
    m.main()