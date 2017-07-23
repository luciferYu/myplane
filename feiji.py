# -*- coding:utf-8 -*-
#auth:zhiyi
import pygame
import time

def main():
    #整体流程控制
    #  创建一个窗口显示东西
    screen = pygame.display.set_mode((488,852),0,32)

    #  创建一个背景图片
    background = pygame.image.load('./resource/background.png')

    #  3.将北京图片粘贴到窗口中
    screen.blit(background,(0,0))

    while True:
        #  4.显示窗口中的内容
        pygame.display.update()

        time.sleep(0.04)


if __name__ == '__main__':
    main()