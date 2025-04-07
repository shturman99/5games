from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,colission_sprites, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join("Vampire survivor","images","player","down","0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = pos)

        #movment
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 300
        self.colission_sprites = colission_sprites 
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_l]-keys[pygame.K_h])
        self.direction.y = int(keys[pygame.K_j]-keys[pygame.K_k])
        self.direction = self.direction.normalize() if self.direction else self.direction
    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def collisions(self,direction):
        pass

    def update(self,dt, *args, **kwargs):
        self.input()
        self.move(dt)