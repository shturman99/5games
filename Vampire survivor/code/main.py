from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from groups import *
from random import randint

class Game():
    def __init__(self):
        #setup
        pygame.init()
        self.display= pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Shooter")
        self.running = True
        self.clock = pygame.time.Clock()
        # Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites= pygame.sprite.Group()
        self.setup()
        # Shooting
        self.can_shoot = True
        self.timer =0
        self.reload_time = 100
        self.load_imagers()
    def reload(self):
        if not self.can_shoot:
            if pygame.time.get_ticks() - self.timer > self.reload_time:
                self.can_shoot = True

    def load_imagers(self):
        self.bullet_surf = pygame.image.load(join("Vampire survivor","images","gun","bullet.png"))

    def input(self):
            if pygame.mouse.get_just_pressed()[0] and self.can_shoot:
                print(list(pygame.mouse.get_just_pressed()))
                self.bullet = Bulet(self.bullet_surf,self.gun,(self.all_sprites,self.bullet_sprites))
                self.can_shoot =False
                self.timer = pygame.time.get_ticks()

    def setup(self):
        map = load_pygame(join("Vampire survivor","data","maps","world.tmx"))
        for x, y, image in map.get_layer_by_name("Ground").tiles():
            Sprite((x * TILE_SIZE,y* TILE_SIZE),image,(self.all_sprites))

        for obj in map.get_layer_by_name("Objects"):
            CollisionSprite((obj.x,obj.y),obj.image,(self.all_sprites,self.collision_sprites))

        for obj in map.get_layer_by_name("Collisions"):
            invis_surf = pygame.Surface((obj.width,obj.height))
            CollisionSprite((obj.x,obj.y),pygame.Surface((obj.width,obj.height)),self.collision_sprites)

        for obj in map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                self.player = Player((obj.x,obj.y),self.collision_sprites,self.all_sprites) 
                self.gun = Gun(self.player,self.all_sprites)

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick()/1000
            # event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.input()
            self.reload()
            # update
            self.all_sprites.update(dt)
            # draw
            self.display.fill("#fafafa")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()