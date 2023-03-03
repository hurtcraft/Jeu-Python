import pygame


from image import image_bullet
class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image=image_bullet
        self.vitesse=5
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.alive=True


    def update(self,screen_scroll):

        self.rect.x-=self.vitesse-screen_scroll
        if self.rect.right<0 or self.rect.left>1000:
            self.kill()