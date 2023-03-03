from map import *
from image import *
import pygame


SCREEN_WIDTH=1000
SCREEN_HEIGHT=int(SCREEN_WIDTH*0.7)
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

FPS=200

GRAVITY=0.98
move_left=False
move_right=False

LIGNES=15
COLONNES=75
idle=0
run=1
die=2
jump=3
hurt=4

shoot_cd=1350

map=Map()

scroll_depart=250
scroll_screen=0
scroll_background=0

tile_size=50


hitted=False
scrolling=False
shoot=False
next=False
pos=0


nb_piece=0
nb_mort=0

time_start=pygame.time.get_ticks()

running=True
shoot_update_time=pygame.time.get_ticks()
esc=False
rejouer=False

start_game=False

