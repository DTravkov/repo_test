import pygame,random
from clamp import clamp
class Enemy:
    def __init__(self,screen:pygame.Surface):
        self.x = random.choice(list([x for x in range(65,screen.get_width()-65) if x % 10 == 0])) # picks random spawnm coordinate
        self.y = 0
        self.speed = random.randint(9,14) # sets random speed to each car
        self.imagepath = 'car_red.png' 
        self.image =  pygame.image.load(self.imagepath)
        self.image = pygame.transform.scale(self.image,((screen.get_width() // 8), (screen.get_height()//6))).convert_alpha() # scales and renders png  
        self.active = True
        self.rect = self.image.get_rect()
        self.surface = self.image
        self.mask = None
        self.prect = self.image.get_rect()
        self.prect.width *= 0.7
        self.prect.height *= 0.7
        self.mask = pygame.mask.from_surface(self.image) # sets mask for perfect collision

    def update(self,screen,delta_time):
        if self.active:
            self.y += self.speed * delta_time * 175
            self.prect.center = (self.x,0-self.prect.height + self.y) # manipulates the rect of image to move car
            self.rect = self.prect
            self.surface = screen.blit(self.image,self.prect)
    
    
    
        
