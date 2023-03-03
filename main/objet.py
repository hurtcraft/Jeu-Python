import pygame

from os import listdir
from bullet import *
from group import bullet_groupe

class Objet(pygame.sprite.Sprite):
    def __init__(self,x,y,objet,scale,cd):
        super().__init__()
        self.objet=objet
        self.shoot_update_time = pygame.time.get_ticks()
        self.scale=scale
        self.cd=cd
        self.frame=0
        self.x=x
        self.y=y
        self.update_time=pygame.time.get_ticks()
        self.animation_list=[]

        for i in range(len(listdir(f"map/{self.objet}"))):
                image=pygame.image.load(f"map/{self.objet}/{self.objet}{i}.png")
                image = pygame.transform.scale(image, (self.scale, self.scale))
                self.animation_list.append(image)

        self.image=self.animation_list[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update_animation(self):

        self.image=self.animation_list[self.frame]
        animation_cd=self.cd
        if pygame.time.get_ticks()-self.update_time>animation_cd:
            self.frame+=1
            self.update_time=pygame.time.get_ticks()
        if self.frame==len(self.animation_list):
            self.frame=0

    def update(self,scroll_screen):


        if self.objet!="sun":
            self.rect.x += scroll_screen
        if self.objet=="heart":
            self.rect.x-=scroll_screen

        self.update_animation()

        if self.objet=="canon":
            self.shoot(scroll_screen)


    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))

    def shoot(self,scroll_screen):
        ## a utiliser que pour un canon
        shoot=False

        shoot_cd=1350
        if pygame.time.get_ticks()-self.shoot_update_time>shoot_cd:
            shoot=True
            self.shoot_update_time=pygame.time.get_ticks()


        if shoot==True:


            bullet=Bullet(self.rect.x-10,self.rect.y+33)
            bullet_groupe.add(bullet)
            bullet.update(scroll_screen)





