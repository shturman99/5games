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

clock = pygame.time.Clock()

# import images
player_im= join("space shooter", "images", "player.png")
player_surf = pygame.image.load(player_im).convert_alpha()
player_rect = player_surf.get_frect(center=(W//2, H//2))
player_speed = 200
player_direction = pygame.math.Vector2(1, 1)
star_im = join("space shooter", "images", "star.png")
star_surf = pygame.image.load(star_im).convert_alpha()
star_postion = [(rd.randint(0, W), rd.randint(0, H)) for _ in range(20)]
meteor_im = join("space shooter", "images", "meteor.png")
meteor_surf= pygame.image.load(meteor_im).convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(W//2+100, H//2+100))
laser_im = join("space shooter", "images", "laser.png")
laser_surf = pygame.image.load(laser_im).convert_alpha()
running = True

while running:
    dt = clock.tick(60)/1000
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    #input handler

    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
    player_direction = player_direction.normalize() if player_direction.length() > 0 else player_direction
    player_rect.center += player_direction * player_speed * dt
    # shooting laser
    recent_key = pygame.key.get_just_pressed()
    if recent_key[pygame.K_SPACE]:
        print("shoot") 
        laser_rect = laser_surf.get_frect(center=(W//2, H//2))
        display_surface.blit(laser_surf, laser_rect)
        laser_rect.centerx -= 100 * dt
    # drawing code
    display_surface.fill(("darkgray"))
    for star in star_postion:
        display_surface.blit(star_surf, star) 
    surface.fill((255, 0, 0))
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(player_surf, player_rect)
    # update the display
    pygame.display.update()