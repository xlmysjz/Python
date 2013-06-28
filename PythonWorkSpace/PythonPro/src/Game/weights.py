#-*-coding:utf-8-*-
'''
Created on 2013-5-22

@author: Administrator
'''
import sys,pygame
from pygame.locals import *
from random import randrange
class Weight(pygame.sprite.Sprite):

    def __init__(self):
        weight_image = pygame.image.load("weight.png")
        #weight_image = weight_image.convert()
        pygame.sprite.Sprite.__init__(self)
        #在画sprite时使用的图像和矩形
        self.image=weight_image
        self.rect=self.image.get_rect()
        self.reset()
    def reset(self):
        #将秤砣移动到屏幕顶端的随机位置
        screen_size=800,600
        self.rect.top=-self.rect.height
        self.rect.centerx=randrange(screen_size[0])
    def update(self):
        #更新秤砣，显示下一帧
        self.rect.top +=1
        if self.rect.top>screen_size[1]:
            self.reset()

if __name__=="__main__":
    Weight().__init__()
    screen_size=800,600
    pygame.display.set_mode(screen_size,FULLSCREEN)
    pygame.mouse.set_visible(0)
    #载入秤砣的图像
    weight_image = pygame.image.load("weight.png")
    weight_image = weight_image.convert()
    #创建一个字图形组（sprite group）,增加weight
    sprites=pygame.sprite.RenderUpdates()
    sprites.add(Weight())
    
    #获取屏幕表明，并填充
    screen=pygame.display.get_surface()
    bg=(255,255,255)#white
    screen.fill(bg)
    pygame.display.flip()
    #用于清除子图形
    def clear_callback(surf,rect):
       surf.fill(bg,rect)
    while True:
        #检查退出事件
        for even in pygame.event.get():
            if even.type==QUIT:
                sys.exit()
            if even.type==KEYDOWN and even.key==K_ESCAPE:
                sys.exit
    #清除前面的位置
    sprites.clear(screen,clear_callback)
    #更新所有子图形
    sprites.update()
    #绘制所有子图形
    updates=sprites.draw(screen)
    #更新所需的显示部分
    pygame.display.update(updates)
    