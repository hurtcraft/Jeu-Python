import pygame
from variable import *
from player import *

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y,image):
        super().__init__()
        self.x=x
        self.y=y
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)


    def update(self,scroll_screen):
        self.rect.x+=scroll_screen
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))