# -*- coding:utf-8 -*-
#auth:zhiyi

import pygame
import sys
import time
from pygame.locals import *

class Thing(object):
    pass



class Main(object):
    def __init__(self,weight=400,height=600):
        self.weight = weight #  屏幕的宽度
        self.height = height  # 屏幕的高度
        self.background = pygame.image.load('./resource/background.png') #  背景图片
        self.screen = pygame.display.set_mode((self.weight, self.height), 0, 32)
    def main(self):
        while True:
            #  添加事件循环
            for event in pygame.event.get():
                # 判断退出条件
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.blit(self.background, (0, 0))

            #  4.显示窗口中的内容
            pygame.display.update()

            #  暂停0.05秒显示
            time.sleep(0.05)



if __name__ == '__main__':
    m = Main()
    m.main()