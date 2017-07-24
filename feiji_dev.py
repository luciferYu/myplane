# -*- coding:utf-8 -*-
#auth:zhiyi

import pygame
import sys
import time
import math
from pygame.locals import *
from collections import deque
import random

class Thing(object):
    '''
    定义一个物体的基类
    '''
    def __init__(self,size_x,size_y,image,speed=10):
        self.size_x = size_x  # 物体的长
        self.size_y = size_y  # 物体的宽
        self.image = pygame.image.load(image)  #加载物体的图片
        self.speed = speed
        self.position_x = 0
        self.position_y = 0

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y

    def get_image(self):
        return self.image

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
    '''定义一个飞机基类'''
    pass


class Hero(Plane):
    '''定义英雄飞机类'''
    def __init__(self,main):
        '''初始化英雄飞机方法'''
        super().__init__(100,124,'./resource/hero1.png')
        self.position_x = (main.get_weight() / 2) - (self.get_size_x() / 2) # 物体的位置 横坐标
        self.position_y = main.get_height() - self.get_size_y() - 50  # 物体的位置 纵坐标
        self.bullets = []
        self.weapon_list = deque(maxlen=3)
        self.weapon_list.extend([Normal_Bullet,Double_Bullet,Triple_Bullet])
        self.bullet_type = Normal_Bullet
        self.missile = None
        self.main = main

    def display(self,main):
        #将导弹显示在飞机以下图层
        if self.missile and not self.missile.is_shot:
            self.missile.auto_move(self)
            self.missile.display()
        elif self.missile and self.missile.is_shot:
            self.missile.auto_shot_enemy_move(self.main.enemy)
            if (self.main.enemy.position_y  <= self.missile.position_y <= (self.main.enemy.position_y + self.main.enemy.get_size_y())) and (self.main.enemy.position_x <= self.missile.position_x <= (self.main.enemy.position_x+self.main.enemy.get_size_x())):
                # print(self.main.enemy,self.missile)  #  调试
                #print(self.missile.position_x, self.main.enemy.position_x)
                #print(self.missile.position_y, self.main.enemy.position_y)
                self.main.enemy = None
                self.missile = None
                # print(self.main.enemy,self.missile)  # 调试
            else:
                self.missile.display()


        #  将飞机图片粘贴到窗口中
        main.screen.blit(self.image,(int(self.position_x),int(self.position_y))) #显示飞机的位置

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
        '''飞机射击方法'''
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_SPACE]:
            #print('--space--')
            self.bullets.append(self.bullet_type(m,self))
        for bullet in self.bullets:
            bullet.auto_move()
            if not bullet.is_top() or not bullet.is_bottom or not bullet.is_right:
                bullet.display(m)
            else:
                #print(self.bullets)  # 调试子弹
                #在列表中删除子弹
                self.bullets.remove(bullet)
                #print(self.bullets)  调试子弹

    def change_weapon(self):
        '''飞机更换武器方法'''
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_j]:
            self.weapon_list.rotate(1)
            #print(self.weapon_list)
            self.bullet_type = self.weapon_list[0]

    def shot_missile(self):
        '''飞机发射方法'''
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_k] and not self.missile:
            self.missile = Missile(m,self)
            self.missile.display()
        if key_pressed[K_l] and self.missile:
            self.missile.is_shot = True


class Small_Enemy(Plane):
    '''定义一个敌人的小飞机类'''
    def __init__(self,main):
        super().__init__(51, 39, './resource/enemy0.png', speed=3)  # 初始化敌人小飞机类
        self.position_x = random.randint(0,m.get_weight() - self.size_x)
        self.position_y = 0
        self.bullets = []
        self.main = main

    def move(self):
        self.position_y += self.get_speed()  # 小飞机向下移动
        if self.is_left():
            self.position_x += self.get_speed()
        elif self.is_right():
            self.position_x -= self.get_speed()
        else:
            self.position_x += random.randint(-1,1) * self.get_speed()*3

    def bullet_move(self,bullet_temp):
        #print(self.position_x,self.position_y)
        bullet_temp.position_y += (self.speed + 5)

    def auto_file(self):
        rand_num = random.randint(1,50)
        if rand_num in (10,20,30,40):
            self.bullet = Bullet(m,self.main.enemy)
            self.bullet.speed = (- self.bullet.speed)
            self.bullet.position_x = self.position_x + 23
            self.bullet.position_y = self.position_y + 20
            self.bullets.append(self.bullet)

    def display(self,main):
        #  将飞机图片粘贴到窗口中
        for bullet in self.bullets:
            if  not bullet.is_bottom():
                self.bullet_move(bullet)
                main.screen.blit(bullet.image,(int(bullet.position_x),int(bullet.position_y)))
            else:
                #print(self.bullets)
                self.bullets.remove(bullet)

        main.screen.blit(self.image, (int(self.position_x), int(self.position_y))) # 显示飞机的位置


class Bullet(Thing):
    '''定义了一个子弹基类'''
    def __init__(self,main,hero):
        super().__init__(22,22,'./resource/bullet.png')
        self.position_x = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x()/2) + 1 # 物体的位置 横坐标
        self.position_y = hero.position_y - 20  # 物体的位置 纵坐标

    def auto_move(self):
        '''子弹的移动方法'''
        self.position_y -= self.speed

    def display(self,main):
        #  将飞机图片粘贴到窗口中
        main.screen.blit(self.image,(self.position_x,self.position_y)) #显示子弹的位置


class Normal_Bullet(Bullet):
    '''定义了一个普通子弹类'''
    pass


class Double_Bullet(Bullet):
    '''定义了一个双重子弹类'''
    def __init__(self,main,hero):
        super().__init__(main,hero)
        self.position_x1 = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x()/2) + 35 # 物体的位置 横坐标
        self.position_x2 = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x() / 2) - 35  # 物体的位置 横坐标
        self.position_y = hero.position_y + 22  # 物体的位置 纵坐标


    def auto_move(self):
        self.position_y -= self.speed

    def display(self,main):
        #  将飞机图片粘贴到窗口中
        main.screen.blit(self.image,(self.position_x1,self.position_y)) #显示子弹的位置
        main.screen.blit(self.image,(self.position_x2,self.position_y)) #显示子弹的位置


class Triple_Bullet(Bullet):
    '''定义了一个三重子弹类'''
    def __init__(self,main,hero):
        super().__init__(main,hero)
        self.position_x1 = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x()/2) + 1 # 物体的位置 横坐标
        self.position_x2 = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x() / 2) + 1  # 物体的位置 横坐标
        self.position_x3 = hero.position_x + (hero.get_size_x() / 2) - (self.get_size_x() / 2) + 1  # 物体的位置 横坐标
        self.position_y = hero.position_y - 20  # 物体的位置 纵坐标


    def auto_move(self):
        '''子弹移动'''
        self.position_x1 -= (self.speed - 8)
        self.position_x3 += (self.speed - 8)
        self.position_y -= self.speed

    def display(self,main):
        #  将飞机图片粘贴到窗口中
        main.screen.blit(self.image,(self.position_x1,self.position_y)) #显示子弹的位置
        main.screen.blit(self.image,(self.position_x2,self.position_y)) #显示子弹的位置
        main.screen.blit(self.image,(self.position_x3,self.position_y)) #显示子弹的位置


class Missile(Thing):
    def __init__(self,main,hero):
        super().__init__(63,53,'./resource/bomb1.png')
        self.position_x = hero.position_x + hero.size_x/2 + 3 # 物体的位置 横坐标
        self.position_y = hero.position_y + 30  # 物体的位置 纵坐标
        self.main = main
        self.is_shot = False
        self.speed = 20
        self.y_flag = False  #用来识别自己的飞机是否超过了对方飞机 调整导弹方向

    def auto_move(self,hero):
        if not self.is_shot:
            self.position_x = hero.position_x + hero.size_x / 2 + 3  # 物体的位置 横坐标
            self.position_y = hero.position_y + 30  # 物体的位置 纵坐标

    def auto_shot_enemy_move(self,enemy):
        if self.is_shot:
            #增加导弹变速更能
            if math.sqrt(((self.position_x - self.main.enemy.position_x) ** 2) + ((self.position_y - self.main.enemy.position_x) ** 2)) > 500:
                self.speed = 100
            elif math.sqrt(((self.position_x - self.main.enemy.position_x) ** 2) + ((self.position_y - self.main.enemy.position_x) ** 2)) > 150:
                self.speed = 50
            elif math.sqrt(((self.position_x - self.main.enemy.position_x) ** 2) + ((self.position_y - self.main.enemy.position_x) ** 2))  > 100:
                self.speed = 30
            elif math.sqrt(((self.position_x - self.main.enemy.position_x) ** 2) + ((self.position_y - self.main.enemy.position_x) ** 2))  > 20:
                self.speed = 5
            else:
                self.speed = 1
            #导弹跟踪功能
            if self.position_x > enemy.position_x:
                self.position_x -= self.speed
            else:
                self.position_x += self.speed
            if self.position_y > enemy.position_y:
                self.position_y -= self.speed
            else:
                self.position_y += self.speed

    def display(self):
        '''显示导弹位置'''
        if self.position_y < self.main.enemy.position_y and not self.y_flag:
            self.image = pygame.transform.flip(self.image,False,True)
            self.y_flag = True
        elif self.position_y > self.main.enemy.position_y and self.y_flag:
            self.image = pygame.transform.flip(self.image, False, True)
            self.y_flag = False
        self.main.screen.blit(self.image, (self.position_x, self.position_y))  # 显示子弹的位置


class Main(object):
    '''游戏主界面类'''
    def __init__(self,weight=400,height=600):
        self.__weight = weight #  屏幕的宽度
        self.__height = height  # 屏幕的高度
        self.background = pygame.image.load('./resource/background.png') #  背景图片
        self.screen = pygame.display.set_mode((self.__weight, self.__height), 0, 32)
        self.enemy = None
        self.screen_y1 = 0
        self.screen_y2 = -600
        self.screen_speed = 5

    def get_weight(self):  # 获得主窗口的宽度
        return self.__weight

    def get_height(self):  # 获得主窗口的高度
        return self.__height

    def rorate_screen(self):
        #print(self.screen_y)
        self.screen_y1 += self.screen_speed
        self.screen_y2 += self.screen_speed
        self.screen.blit(self.background, (0, self.screen_y1))
        self.screen.blit(self.background,(0,self.screen_y2))
        if self.screen_y1 >= 600:
            self.screen_y1 = -600
        if self.screen_y2 >= 600:
            self.screen_y2 = -600

    def main(self):
        '''游戏的主界面函数'''
        hero = Hero(m)  # 创建自己的英雄飞机
        self.enemy = Small_Enemy(m)  # 创建敌人的小飞机

        #ms = Missile(m,hero) ##测试功能
        while True:  # 进入游戏主循环
            #  添加退出事件循环
            for event in pygame.event.get():
                # 判断退出条件
                if event.type == pygame.QUIT:
                    sys.exit()

            self.rorate_screen()# 添加背景信息

            #ms.display()  ## 测试功能

            hero.move()  # 英雄飞机的移动
            hero.shot()  # 英雄飞机的射击
            hero.change_weapon()  # 英雄飞机更换武器
            hero.shot_missile()
            hero.display(m)  # 英雄飞机显示

            if self.enemy:
                self.enemy.move()
                self.enemy.auto_file()
                self.enemy.display(m)
            else:
                self.enemy = Small_Enemy(m)



            #pygame.display.update()  # 4.显示窗口中的内容
            pygame.display.flip()  # 4.显示窗口中的内容

            pygame.time.delay(50)  # 暂停0.05秒显示


if __name__ == '__main__':  # 游戏主函数
    m = Main()  # 实例化主函数类
    m.main()  # 启动主函数