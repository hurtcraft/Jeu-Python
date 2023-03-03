import pygame.mixer
from pygame import mixer

def son_bg():
    mixer.music.load("music/music_fond.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1,0,1000)

jump_son=pygame.mixer.Sound("music/chui_un_avion.mp3")
jump_son.set_volume(0.2)

coin_son=pygame.mixer.Sound('music/coin_son.wav')
coin_son.set_volume(0.1)

fall_water=pygame.mixer.Sound("music/fall_water.wav")
fall_water.set_volume(0.1)

