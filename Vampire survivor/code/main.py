from settings import *
from player import Player
from sprites import *

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
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        # spriters
        self.player = Player((100,100),self.collision_sprites,self.all_sprites) 
        for _ in range(6):
            x, y = randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)
            w, h = randint(0,100), randint(0,100)
            ColissionSprites((x,y),(w,h),(self.all_sprites,self.collision_sprites))
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
            # update
            self.all_sprites.update(dt)
            # draw
            self.display.fill("#fafafa")
            self.all_sprites.draw(self.display)
            pygame.display.update()
        pygame.quit()
        
if __name__ == "__main__":
    game = Game()
    game.run()