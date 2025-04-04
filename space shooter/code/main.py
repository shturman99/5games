import pygame
from os.path import join
import random as rd
# genreal setup

pygame.init()
W, H = 800, 600
display_surface = pygame.display.set_mode((W, H))
pygame.display.set_caption("Space Shooter") 


# surface setup
w, h = 200, 100
surface = pygame.Surface((w, h))


# import images
player_im= join("space shooter", "images", "player.png")
player_surf = pygame.image.load(player_im).convert_alpha()
player_rect = player_surf.get_frect(center=(W//2, H//2))
star_im = join("space shooter", "images", "star.png")
star_surf = pygame.image.load(star_im).convert_alpha()
star_postion = [(rd.randint(0, W), rd.randint(0, H)) for _ in range(20)]
meter_im = join("space shooter", "images", "meter.png")
meter_surf = pygame.image.load(meter_im).convert_alpha()
meter_rect = meter_surf.get_frect(center=(W//2, H//2))

running = True

while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawing code
    display_surface.fill((0, 0, 0))
    display_surface.blit(player_surf, player_rect)
    for star in star_postion:
        display_surface.blit(star_surf, star) 
    surface.fill((255, 0, 0))
    # update the display
    pygame.display.update()