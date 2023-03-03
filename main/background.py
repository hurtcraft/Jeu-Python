
import pygame
class Background():
    def __init__(self,img,SCREEN_WIDTH,SCREEN_HEIGHT):

        self.image=pygame.transform.scale(img,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.rect=self.image.get_rect()

    def draw(self,screen,scroll):
        for x in range(0, 4):
            screen.blit(self.image, ((x * screen.get_width()) - scroll, 0))