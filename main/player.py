# Créé par julien.weng, le 17/02/2022 en Python 3.7

from os import listdir
from variable import *
from fonction import *
from music import *

class Player(pygame.sprite.Sprite):


    def __init__(self,x,y):
        """
        x0, y0: position initiale
        xmin, xmax: valeurs à ne pas dépasser
        """
        super().__init__()

        self.animation_list=[]#liste en 2d contenant les differente animation
        self.frame=0
        self.action=0
        self.update_time=pygame.time.get_ticks()
#ajout animation pour le joueur
#____________________________________________________________________________
        animation_types=["idle","run","death","jump","hurt"]
        for animation in animation_types:

            temp_list=[]
            nb_sprite=len(listdir(f"assets_joueur/{animation}"))

            for i in range(nb_sprite):
                image=pygame.image.load(f"assets_joueur/{animation}/{animation}{i}.png").convert_alpha()
                image =pygame.transform.scale(image,(53,53))
                temp_list.append(image)

            self.animation_list.append(temp_list)

#_______________________________________________________________

        self.jump=False
        self.en_air=True
        self.image=self.animation_list[self.action][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width=self.image.get_width()-10
        self.height=self.image.get_height()

        self.vie = 3

        self.speed=5
        self.velocity_y=0
        self.direction=1
        self.flip=False
        self.pos = 300

    def update_animation(self):
        """
        fait defiler les sprites contenu dans self.animation_list->(liste en 2d contenant les differente animation)
         qu'on a charger auparavant
        :return:
        """
        animation_cd=85#on change de sprite tt les 85 ms

        self.image=self.animation_list[self.action][self.frame]
        if pygame.time.get_ticks()-self.update_time>animation_cd:
            self.update_time=pygame.time.get_ticks()
            self.frame+=1
        if self.frame>=len(self.animation_list[self.action]):
            if self.action==2:
                self.frame=len(self.animation_list[self.action])-1

            else:
                self.frame=0

    def update_action(self,new_action):
        """

        :param new_action:L'action qu'on veut faire
        0:idle
        1:run
        2:die
        :return:
        """
        if new_action!=self.action:
            self.action=new_action
            #reset des parametres d'animation
            self.frame=0
            self.update_time=pygame.time.get_ticks()

    def update(self,Objet,SCREEN_WIDTH):
        if len(coeur_group)==0:
            self.draw_coeur(Objet,SCREEN_WIDTH)

        self.update_animation()
        self.is_alive()




    def move(self,move_left,move_right,liste_obs):

        """
        fait avancer ou reculer le joueur
        :param move_left:
        :param move_right:
        :return:
        """
        scroll=0
        dx=0
        dy=0


        if move_left==True :
            dx=dx-self.speed
            self.flip=True
            self.direction=-1


        if move_right==True :
            dx=dx+self.speed
            self.flip=False
            self.direction=1

        if self.jump==True and self.en_air==False:
            jump_son.play()
            self.velocity_y=-18
            self.jump=False
            self.en_air=True


        self.velocity_y+=GRAVITY

        if self.velocity_y>15:
            self.velocity_y=15
        dy+=self.velocity_y

        for tile in liste_obs:
            if tile[1].colliderect(self.rect.x+dx,self.rect.y,self.width,self.height):
                dx=0
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


        if self.rect.x>SCREEN_WIDTH-270 or self.rect.left<170:

            self.rect.x=self.rect.x-dx

            scroll= -dx


        return scroll


    def is_alive(self):
        if self.vie<0:
            self.speed=0
            self.update_action(2)

    def draw(self,screen):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)

    def hurt(self,kb):
        self.vie-=1
        if kb==True:

            self.rect.x-=20
            self.velocity_y+=10
            self.rect.y-=20

        coeur_group.sprites()[0].kill()

    def set_default(self):

        self.rect.x=310
        self.rect.y=10
        self.vie=3


    def draw_coeur(self,Objet,SCREEN_WIDTH):
        for i in range (self.vie):
            vie = Objet((SCREEN_WIDTH * 0.85) + (i * 50), 60, "heart", 50, 150)
            coeur_group.add(vie)


