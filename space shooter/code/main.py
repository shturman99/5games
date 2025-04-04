import pygame
from os.path import join
import random as rd
# genreal setup

class Star(pygame.sprite.Sprite):
    def __init__(self, surf,*groups):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(rd.randint(0, W), rd.randint(0, H)))

class Meteor(pygame.sprite.Sprite):
    def __init__(self,surf,pos, *gorups):
        super().__init__(*gorups)
        self.image = surf
        self.rect = self.image.get_frect(center = (pos))
        self.speed = rd.randint(100, 200)
        self.direction = pygame.math.Vector2(rd.uniform(-0.5,0.5), 1)
        self.direction = self.direction.normalize() if self.direction.length() > 0 else self.direction
        # cooldown setup
        self.time = pygame.time.get_ticks()
        self.cooldown = 5000
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if self.rect.top > H:
            self.rect.center = (rd.randint(0, W), rd.randint(-200, 0))
            self.speed = rd.randint(100, 200)
        # cooldown
        if pygame.time.get_ticks() - self.time > self.cooldown:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join("space shooter", "images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center=(W//2, H//2))
        self.speed = 200
        self.direction = pygame.math.Vector2()
        # cooldown setup
        self.can_shoot = True
        self.shot_time = 0
        self.cooldown = 400

    def laser_cooldown(self):
        if not self.can_shoot:
            if pygame.time.get_ticks() - self.shot_time > self.cooldown:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_l]) - int(keys[pygame.K_h])
        self.direction.y = int(keys[pygame.K_j]) - int(keys[pygame.K_k])
        self.direction = self.direction.normalize() if self.direction.length() > 0 else self.direction
        self.rect.center += self.direction * self.speed * dt

        # fiering 
        recent_key = pygame.key.get_just_pressed()
        if recent_key[pygame.K_SPACE] and self.can_shoot:
            if self.can_shoot:
                laser = Laser(laser_surf, self.rect.center, (all_sprites, laser_sprite))
                laser.rect.center = self.rect.midtop
                self.can_shoot = False
                self.shot_time = pygame.time.get_ticks()
        
        self.laser_cooldown()

class Laser(pygame.sprite.Sprite):
    def __init__(self,surf,pos, *groups):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
        self.speed = 200
    
    def update(self, dt):
        self.rect.center += pygame.math.Vector2(0, -1) * self.speed * dt
        if self.rect.bottom < 0:
            self.kill()

def collision_check():
    for laser in laser_sprite:
        if pygame.sprite.spritecollide(laser , meteor_sprite, True):
            laser.kill()
    player_collide = pygame.sprite.spritecollide(player, meteor_sprite, True)
    if player_collide:
        player.kill()
        return False
    return True

# pygame setup
pygame.init()
W, H = 800, 600
display_surface = pygame.display.set_mode((W, H))
pygame.display.set_caption("Space Shooter") 

clock = pygame.time.Clock()

# sprite setup
all_sprites = pygame.sprite.Group()
meteor_sprite = pygame.sprite.Group()
laser_sprite = pygame.sprite.Group()
laser_surf = pygame.image.load(join("space shooter", "images", "laser.png")).convert_alpha()
star_surf = pygame.image.load(join("space shooter", "images", "star.png")).convert_alpha()
meteor_surf = pygame.image.load(join("space shooter", "images", "meteor.png")).convert_alpha()
for _ in range(20):
    Star(star_surf, all_sprites)
player = Player(all_sprites)
running = True

# custom event setup
meteror_event = pygame.event.custom_type()
pygame.time.set_timer(meteror_event, 200) 

while running:
    dt = clock.tick(60)/1000
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == meteror_event:
            Meteor(meteor_surf, (rd.randint(0, W), rd.randint(-200, 0)),(all_sprites, meteor_sprite))

    # collision check
    if not collision_check():
        running = False
    # drawing code
    display_surface.fill(("darkgray"))
    all_sprites.draw(display_surface)
    all_sprites.update(dt)
    # update the display
    pygame.display.update()

pygame.quit()