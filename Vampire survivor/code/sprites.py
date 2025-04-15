from settings import * 

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
    def __init__(self,palayer ,*groups):
        super().__init__(*groups)
        self.surf = pygame.image.load(join("Vampire survivor","images","gun","gun.png"))
        self.image = self.surf
        self.direction = pygame.math.Vector2(1,0)
        self.player_distance = 150
        self.rect = self.image.get_frect(center = (palayer.rect.center + self.direction * self.player_distance))

    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs) 