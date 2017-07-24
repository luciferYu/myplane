# -*- coding:utf-8 -*-
#auth:zhiyi

import pygame
import sys
import math
from pygame.locals import *

class Target(object):
    def __init__(self,x,y,image,speed,screen):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.speed = speed
        self.screen = screen
        self.director = 1
    def move(self):
        if self.y >= 400:
            self.director = -1
        if self.y <= 30:
            self.director = 1

        self.y = self.y + (self.speed * self.director)

    def display(self):
       self.screen.blit(self.image, (self.x, self.y))


class Bomb(object):
    def __init__(self,x,y,image,speed,screen,target):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.speed = speed
        self.screen = screen
        self.angle = 60
        self.target =target


    def move(self):
        self.angle = int(math.atan2((self.y - self.target.y),(self.target.x - self.x)) * 180 / math.pi)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_SPACE]:
            if self.x > self.target.x:
                self.x -= self.speed
            else:
                self.x += self.speed
            if self.y > self.target.y:
                self.y -= self.speed
            else:
                self.y += self.speed

    def display(self):
        print(self.angle)
        self.new_image = self.image
        #self.new_image = pygame.transform.rotate(self.new_image,-(self.angle + 45))
        self.new_image = pygame.transform.rotate(self.new_image,(self.angle + 270))
        self.screen.blit(self.new_image, (self.x, self.y))






def main():
    #整体流程控制
    #  创建一个窗口显示东西
    size = weight,height = 700,500  #  屏幕的宽度
    screen = pygame.display.set_mode(size)
    bg = (255, 255, 255)

    screen.fill(bg)

    target = Target(350, 49, 'target.png', 10, screen)

    bomb = Bomb(500,400,'bomb1.png',10,screen,target)





    while True:  # 进入游戏主循环
        #  添加退出事件循环
        for event in pygame.event.get():
            # 判断退出条件
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg)


        target.move()

        bomb.move()

        bomb.display()

        target.display()



        pygame.display.update()  # 4.显示窗口中的内容

        pygame.time.delay(50)  # 暂停0.05秒显示





if __name__ == '__main__':
    m = main()