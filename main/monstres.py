# Créé par suyil, le 13/03/2022 en Python 3.7
import pygame
from os import listdir
class Monstre(pygame.sprite.Sprite):


    def __init__(self,x,y,color):
        """
        x0, y0: position initiale
        xmin, xmax: valeurs à ne pas dépasser
        """
        super().__init__()

        self.animation_list=[]
        self.frame=0
        self.update_time=pygame.time.get_ticks()
#ajout animation pour le monstre

#____________________________________________________________________________
        nb_sprite=len(listdir(f"monstre/big slime/{color}/idle"))
        for i in range(1,nb_sprite):


            image=pygame.image.load(f"monstre/big slime/{color}/idle/Slime_Big_{color}_{i}.png").convert_alpha()
            image =pygame.transform.scale(image,(53,53))


            self.animation_list.append(image)

#_______________________________________________________________

        self.jump=False
        self.en_air=True
        self.image=self.animation_list[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width=self.image.get_width()
        self.height=self.image.get_height()

        self.speed=2
        self.velocity_y=0
        self.flip=False

        self.move_right=True




    def update_animation(self):
        """
        fait defiler les sprites contenu dans self.animation_list->(liste en 2d contenant les differente animation)
         qu'on a charger auparavant
        :return:
        """
        animation_cd=85#on change de sprite tt les 85 ms

        self.image=self.animation_list[self.frame]
        if pygame.time.get_ticks()-self.update_time>animation_cd:
            self.update_time=pygame.time.get_ticks()
            self.frame+=1
        if self.frame>=len(self.animation_list):

            self.frame=0


    def update(self,scroll_screen,liste_obs,screen):
        self.move(liste_obs)
        self.rect.x+=scroll_screen
        self.update_animation()
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)



    def move(self,liste_obs):

        """
        fait avancer ou reculer le joueur
        :param move_left:
        :param move_right:
        :return:
        """

        dx=0
        dy=0


        if self.jump==True and self.en_air==False:
            self.velocity_y=-18
            self.jump=False
            self.en_air=True


        self.velocity_y+=0.98

        if self.velocity_y>15:
            self.velocity_y=15
        dy+=self.velocity_y

        dx+=self.speed



        for tile in liste_obs:
            if tile[1].colliderect(self.rect.x+dx,self.rect.y,self.width,self.height):
                if self.move_right==True:
                    self.move_right=False
                    self.flip = True
                    self.direction = 1
                    self.speed=-2

                else:
                    self.direction = 1
                    self.move_right=True
                    self.flip = False
                    self.speed=2

            if tile[1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                if self.velocity_y<0:
                    self.velocity_y=0
                    dy= int(tile[1].bottom-self.rect.top)

                elif self.velocity_y>=0:
                    self.velocity_y=0
                    self.en_air = False
                    dy = 0

        self.rect.y += dy
        self.rect.x += dx


