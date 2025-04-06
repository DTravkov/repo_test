import pygame,random
from clamp import clamp

class Enemy:
    def __init__(self,screen:pygame.Surface,player_score):
        self.imagepath = 'car_red.png' 
        self.image = pygame.transform.scale(pygame.image.load(self.imagepath),((screen.get_width() // 8), (screen.get_height()//6))).convert_alpha() # scales and renders png  
        self.active = True
        self.rect = self.image.get_rect()
        self.x = random.randint(60,screen.get_width()-60)
        self.y = 0-self.rect.height
        self.speed = random.randint(9,10+(player_score//10)) # sets random speed to each car,increases maximum car speed when 10 coins are ontained
        self.rect.x = self.x
        self.rect.y = self.y
        self.surface = self.image
        self.mask = None
        self.mask = pygame.mask.from_surface(self.image) # sets mask for perfect collision
    def update(self,screen,delta_time):
        if self.active:
            self.rect.move_ip(0,int(90* self.speed *delta_time))
            self.surface = screen.blit(self.image,self.rect)
    
    
    
        