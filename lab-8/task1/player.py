import pygame
from clamp import clamp

class Player:


    def __init__(self,image,speed,screen):
        self.x = 0
        self.y = 0
        self.score = 0
        self.speed = speed
        self.imagepath = 'motorcycle.png'
        self.image = None
        self.rotation = 0 # rotation in degrees
        self.rect = pygame.Rect(-1000,-1000,0,0)
        self.mask = None
        self.screen = screen
    def check_collision(self,collider,collidermask): # checks pixel perfect collision, calculates offsets
        offset_x = collider.rect.x - self.rect.x
        offset_y = collider.rect.y  - self.rect.y 
        return self.mask.overlap(collidermask, (offset_x, offset_y))
    
    
    def update(self,screen:pygame.surface.Surface):
        self.image =  pygame.image.load(self.imagepath)
        self.image = pygame.transform.scale(self.image,((screen.get_width() // 8), (screen.get_height()//6)))
        self.image = pygame.transform.rotozoom(self.image,self.rotation,0.7) # rotates image,and scales it by 0.7 factor
        prect = self.image.get_rect()
        prect.center = (screen.get_width()//2,screen.get_height()//1.35)
        prect.x += self.x * self.speed
        self.rect = prect
        self.mask = pygame.mask.from_surface(self.image) # takes mask for pixelperfect collision
        screen.blit(self.image,prect)



    def rotate(self,angle): #changes rotation
        self.rotation += angle
        self.rotation = clamp(self.rotation,-60,60) # limits the rotation
        return self.rotation
    


    def move(self,speedx,speedy):
        self.x += speedx * 100 # simply increases x to move the rect of image
    
        


        


