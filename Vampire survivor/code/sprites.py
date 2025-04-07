from settings import *


class ColissionSprites(pygame.sprite.Sprite):
    def __init__(self,pos,size, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface(size)
        self.image.fill("#dddddd")
        self.rect = self.image.get_frect(center = pos)