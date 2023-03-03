import pygame
from os import listdir
class Maison(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.animation_liste=[]
        for i in range(len(listdir(f"map/maison"))):
            image=pygame.image.load(f"map/maison/maison{i}.png")
            image=pygame.transform.scale(image,(200,180))
            self.animation_liste.append(image)

        self.image=self.animation_liste[0]
        self.x=x
        self.y=y
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)


    def update(self,scroll_screen,reached):
        if reached==True:
            self.image = self.animation_liste[1]
        else:
            self.rect.x+=scroll_screen
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
