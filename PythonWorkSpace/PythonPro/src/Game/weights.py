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
        #�ڻ�spriteʱʹ�õ�ͼ��;���
        self.image=weight_image
        self.rect=self.image.get_rect()
        self.reset()
    def reset(self):
        #�������ƶ�����Ļ���˵����λ��
        screen_size=800,600
        self.rect.top=-self.rect.height
        self.rect.centerx=randrange(screen_size[0])
    def update(self):
        #���³��ȣ���ʾ��һ֡
        self.rect.top +=1
        if self.rect.top>screen_size[1]:
            self.reset()

if __name__=="__main__":
    Weight().__init__()
    screen_size=800,600
    pygame.display.set_mode(screen_size,FULLSCREEN)
    pygame.mouse.set_visible(0)
    #������ȵ�ͼ��
    weight_image = pygame.image.load("weight.png")
    weight_image = weight_image.convert()
    #����һ����ͼ���飨sprite group��,����weight
    sprites=pygame.sprite.RenderUpdates()
    sprites.add(Weight())
    
    #��ȡ��Ļ�����������
    screen=pygame.display.get_surface()
    bg=(255,255,255)#white
    screen.fill(bg)
    pygame.display.flip()
    #���������ͼ��
    def clear_callback(surf,rect):
       surf.fill(bg,rect)
    while True:
        #����˳��¼�
        for even in pygame.event.get():
            if even.type==QUIT:
                sys.exit()
            if even.type==KEYDOWN and even.key==K_ESCAPE:
                sys.exit
    #���ǰ���λ��
    sprites.clear(screen,clear_callback)
    #����������ͼ��
    sprites.update()
    #����������ͼ��
    updates=sprites.draw(screen)
    #�����������ʾ����
    pygame.display.update(updates)
    