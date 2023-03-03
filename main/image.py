import pygame


convert_surface=pygame.display.set_mode((1000,700))

image_bullet=pygame.image.load("map/bullet.png").convert_alpha()
image_bullet=pygame.transform.scale(image_bullet,(45,45))

coin_img=pygame.image.load("map/coin/coin0.png").convert_alpha()
coin_img=pygame.transform.scale(coin_img,(50,50))

death_png=pygame.image.load("pp_the_frog/death_img2.png").convert_alpha()
death_png=pygame.transform.scale(death_png,(47,47))


bg=pygame.image.load("map/background ete/_Complete_static_BG_(288 x 208).png").convert_alpha()
bg=pygame.transform.scale(bg,(1000,700))

icone=pygame.image.load("pp_the_frog/icone_jeu.jpg").convert_alpha()

menu_tile = pygame.image.load("menu/menu_bg.png").convert_alpha()
menu_tile = pygame.transform.scale(menu_tile, (250, 300))
menu_tile = pygame.transform.rotate(menu_tile, 0)

btn_start_img = pygame.image.load("menu/jouer.png").convert_alpha()
btn_start_img = pygame.transform.scale(btn_start_img, (150, 50))

btn_leave_img = pygame.image.load("menu/quitter.png").convert_alpha()
btn_leave_img = pygame.transform.scale(btn_leave_img, (150, 50))

btn_restart_img=pygame.image.load("menu/rejouer.png").convert_alpha()
btn_restart_img=pygame.transform.scale(btn_restart_img,(150,50))

accueil_bg=pygame.image.load("menu/start_bg.png").convert_alpha()

