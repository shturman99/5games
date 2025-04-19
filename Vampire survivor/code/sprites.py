from settings import * 
from math import degrees,atan2

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Gun(pygame.sprite.Sprite):
    def __init__(self,player ,*groups):
        super().__init__(*groups)
        self.surf = pygame.image.load(join("Vampire survivor","images","gun","gun.png"))
        self.image = self.surf
        self.player = player
        self.direction = pygame.math.Vector2(1,0)
        self.player_distance = 150
        self.rect = self.image.get_frect(center = (player.rect.center + self.direction * self.player_distance))

    def get_direction(self):
        mous_location = pygame.math.Vector2(pygame.mouse.get_pos())
        player_postion = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
        self.direction = (mous_location - player_postion).normalize() if (mous_location -player_postion) else pygame.Vector2(1,0)
        return self.direction
        
    def rotate_gun(self):
        angle = degrees(atan2(self.direction.x,self.direction.y))-90
        if self.direction.x > 0:
            self.image =pygame.transform.rotozoom(self.surf,angle,1)
        else:
            self.image =pygame.transform.rotozoom(self.surf,abs(angle),1)
            self.image = pygame.transform.flip(self.image,False,True)

    def update(self, *args, **kwargs):
        self.direction =self.get_direction()
        self.rotate_gun()
        self.rect.center = self.player.rect.center + self.direction * self.player_distance

class Bulet(pygame.sprite.Sprite):
    def __init__(self,surf,Gun, *groups):
        super().__init__(*groups)
        #Prams
        self.gun_length = 60
        self.speed =400
        self.gun = Gun
        self.direction = self.gun.get_direction() 

        self.image = surf
        self.rect = self.image.get_frect(center = self.gun.rect.center + self.direction * self.gun_length)
    
        self.life_time = 1000 
        self.spawn_time = pygame.time.get_ticks()
    def update(self,dt, *args, **kwargs):
        self.rect.center += self.direction * self.speed * dt

        if pygame.time.get_ticks() - self.spawn_time >= self.life_time:
            self.kill()