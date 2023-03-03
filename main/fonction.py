
from variable import *
import csv
from group import *





def get_map_data(LIGNES,COLONNES,niveau):
    data = []
    for i in range(LIGNES):
        ligne=[-1]*COLONNES
        data.append(ligne)

    with open(f"lvl{niveau}_data.csv","r",newline='') as csvfile:
        reader=csv.reader(csvfile,delimiter=",")
        for x,row in enumerate(reader):
            for y,tile in enumerate(row) :
                data[x][y]=int(tile)
    return data


def get_liste_img(nb_tile):
    liste_image=[]
    for i in range(nb_tile):
        image=pygame.image.load(f"map/tiles/{i}.png").convert_alpha()
        image_width = image.get_width()
        image_height = image.get_height()
        if i == 24:
            image = pygame.transform.scale(image, (150, 150))

        else:
            image = pygame.transform.scale(image, (image_width * 3, image_height * 3))
        liste_image.append(image)
    return liste_image

def put_elt(screen,scroll_screen,liste_obs):
    sun_group.update(scroll_screen)
    sun_group.draw(screen)

    bullet_groupe.update(scroll_screen)
    bullet_groupe.draw(screen)

    canon_group.update(scroll_screen)
    canon_group.draw(screen)

    blade_group.update(scroll_screen)
    blade_group.draw(screen)

    eau_group.update(scroll_screen)
    eau_group.draw(screen)

    pic_group.update(scroll_screen)
    pic_group.draw(screen)

    maison_group.update(scroll_screen,False)
    maison_group.draw(screen)

    coeur_group.update(scroll_screen)
    coeur_group.draw(screen)

    coin_group.update(scroll_screen)
    coin_group.draw(screen)

    monstre_group.update(scroll_screen,liste_obs,screen)

def remove_elt():
    sun_group.empty()
    canon_group.empty()
    blade_group.empty()
    eau_group.empty()
    pic_group.empty()
    maison_group.empty()
    coeur_group.empty()
    monstre_group.empty()
    eau_group.empty()
    coin_group.empty()



def draw_text(screen,text,font,text_color,x,y):
    img=font.render(text,True,text_color)
    screen.blit(img,(x,y))

def timer(screen, font_pixel, font_color, SCREEN_WIDTH, time):
    m = time // 60000
    s = (time % 60000) // 1000
    m = formatage(m)
    s = formatage(s)
    draw_text(screen, f"timer: {m}:{s}", font_pixel, font_color, SCREEN_WIDTH*0.775, 10)

def formatage(time):
    """
    time: int
    renvoie: str
    """
    if len(str(time)) < 2:
        time = "0"+ str(time)
    return time



def draw_counter(screen,nb,font_pixel,color,img,x,y):
    screen.blit(img,(x,y))
    draw_text(screen, f'x{nb}',font_pixel,color,x+50,y+10)



def draw_menu(screen,player,accueil_bg,menu_tile,x,y,Objet):

    screen.blit(accueil_bg, (0, 0))
    screen.blit(menu_tile,(x*0.91,y-100))

    player.rect.y=550

    if player.rect.x<screen.get_width():
        player.rect.x+=5
        player.action=1

    else:
        player.rect.x=-150

    player.update(Objet,screen.get_size()[0])
    player.draw(screen)

def load_menu_btn(screen,btn_start_img,btn_leave_img,x,y,Bouton):
    start_btn = Bouton(x + 20, y, btn_start_img)
    leave_btn = Bouton(x + 20, y * 1.4, btn_leave_img)
    if start_btn.draw(screen)== True:
        return True
    if leave_btn.draw(screen)==True:
        return False
