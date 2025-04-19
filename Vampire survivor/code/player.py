from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,collision_sprites, *groups):
        super().__init__(*groups)
        self.load_image()
        self.state, self.frame_index = "up", 0
        self.image = self.frames[self.state][self.frame_index]
        self.rect = self.image.get_frect(center = pos)
        self.hit_box = self.rect.inflate(-60,-60)

        #movment
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 300
        self.collision_sprites = collision_sprites 
    
    def load_image(self):
        self.frames = {"left":[],"up":[],"down":[],"right":[]}
        for state in self.frames.keys():
            for start_folder,sub_folder,file_names in list(walk(join("Vampire survivor","images","player",state))):
                if file_names:
                    for file in sorted(file_names,key= lambda name: int(name.split(".")[0]) ):
                        image = pygame.image.load(join(start_folder,file)).convert_alpha() 
                        self.frames[state].append(image)

    def input(self): 
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_l]-keys[pygame.K_h])
        self.direction.y = int(keys[pygame.K_j]-keys[pygame.K_k])
        self.direction = self.direction.normalize() if self.direction else self.direction
    def move(self, dt):
        self.hit_box.x+= self.direction.x * self.speed * dt
        self.rect.center = self.hit_box.center
        self.collisions("horizontal")
        self.hit_box.y+= self.direction.y * self.speed * dt
        self.rect.center = self.hit_box.center
        self.collisions("vertical")

    def animate(self,dt):
        # get direction 
        if self.direction.x ==0 and self.direction.y ==0:
            self.animation_speed = 0
            self.frame_index = 0
        else:
            self.animation_speed =2 
        if self.direction.x != 0:
            self.state = "right" if self.direction.x > 0 else  "left"
        if self.direction.y != 0:
            self.state = "down" if self.direction.y > 0 else  "up"
        # animation

        self.frame_index += self.animation_speed * dt
        self.image = self.frames[self.state][(int(self.frame_index%len(self.frames[self.state])))]

    def collisions(self,direction):
        for sprite  in self.collision_sprites:
            if sprite.rect.colliderect(self.hit_box):
                if direction == "horizontal":
                    if self.direction.x > 0: self.hit_box.right = sprite.rect.left
                    if self.direction.x < 0: self.hit_box.left = sprite.rect.right

                if direction == "vertical":
                    if self.direction.y > 0: self.hit_box.bottom= sprite.rect.top
                    if self.direction.y < 0: self.hit_box.top= sprite.rect.bottom

    def update(self,dt, *args, **kwargs):
        self.input()
        self.move(dt)
        self.animate(dt)