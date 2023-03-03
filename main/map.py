
from objet import *
from monstres import *

from group import *
from maison import *

niveau=1
LIGNES=15
COLONNES=75
nb_tile=len(listdir("map/tiles"))


class Map():
    def __init__(self):
        self.decoration=[]


    def process_data(self,data,liste_image):
        liste_obs=[]
        for y,row in enumerate(data):
            for x , tile in enumerate(row):
                if tile>=0:
                    image=liste_image[tile]
                    image_rect=image.get_rect()
                    image_rect.width=image.get_width()
                    image_rect.height=image.get_height()

                    image_rect.x=x*50
                    image_rect.y=y*50

                    tile_data=(image,image_rect)

                    if tile >=0 and tile<=8:
                        image_rect.width -=11
                        image_rect.height -=5
                        liste_obs.append(tile_data)


                    if tile ==10 :
                        canon=Objet(image_rect.x+25,image_rect.y+70,"canon",60,450)#les images sont mal couper
                        canon_group.add(canon)

                    if tile==11:
                        coin=Objet(image_rect.x+25,image_rect.y+25,'coin',50,100)
                        coin_group.add(coin)

                    if tile==12:
                        image_rect.width =image.get_width()-30
                        image_rect.height -=27
                        blade=Objet(image_rect.x+35,image_rect.y,"blade",100,100)
                        blade_group.add(blade)
                    if tile==13:
                        image_rect.height = image.get_height()-30
                        image_rect.width = image.get_width()-30
                        eau=Objet(image_rect.x +25, image_rect.y+24, "eau", 50, 100)

                        eau_group.add(eau)
                    elif tile >=14 and tile <=23:
                        self.decoration.append(tile_data)

                    elif tile==24:
                        maison = Maison(image_rect.x, image_rect.y+60)
                        maison_group.add(maison)

                    if tile==25:
                        pic=Objet(image_rect.x+26,image_rect.y+26,"pic",45,200)
                        pic_group.add(pic)
                    if tile==26:
                        sun=Objet(image_rect.x,image_rect.y,"sun",100,100)
                        sun_group.add(sun)
                    if tile==27:
                        monstre=Monstre(image_rect.x,image_rect.y-10,"Blue")
                        monstre_group.add(monstre)
                    if tile==28:
                        monstre=Monstre(image_rect.x,image_rect.y-10,"Green")
                        monstre_group.add(monstre)
                    if tile==29:
                        monstre=Monstre(image_rect.x,image_rect.y-10,"Purple")
                        monstre_group.add(monstre)
        return liste_obs

    def draw(self,screen,scroll,liste_obs):

        for tile in self.decoration:

            tile[1][0]+=scroll
            screen.blit(tile[0],tile[1])
        for i in liste_obs:
            i[1][0] += scroll
            screen.blit(i[0],i[1])












