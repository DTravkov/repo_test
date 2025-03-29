import pygame
from clamp import clamp

class Player:


    def __init__(self,image,speed,screen):
        self.x = screen.get_width()//2
        self.y = screen.get_height() * 0.78
        self.score = 0
        self.speed = speed
        self.imagepath = 'motorcycle.png'
        self.image =  pygame.image.load(self.imagepath)
        self.image = pygame.transform.scale(self.image,((screen.get_width() // 8), (screen.get_height()//6)))
        self.rotation = 0 # rotation in degrees
        self.rect = pygame.Rect(screen.get_width()//2,screen.get_height()*0.85,0,0)
        self.mask = None
        self.screen = screen

    def check_collision(self,collider,collidermask): # checks pixel perfect collision, calculates offsets
        offset_x = collider.rect.x - self.rect.x
        offset_y = collider.rect.y  - self.rect.y 
        return self.mask.overlap(collidermask, (offset_x, offset_y))
    
    
    def update(self,screen:pygame.surface.Surface):
        self.copy = self.image
        self.copy = pygame.transform.rotozoom(self.copy,self.rotation,0.7) # rotates image,and scales it by 0.7 factor
        self.mask = pygame.mask.from_surface(self.copy) # takes mask for pixelperfect collision
        copyrect = self.copy.get_rect(center=(self.x, self.y))  # avoids jiggling when rotating img
        self.rect = copyrect
        screen.blit(self.copy,self.rect)



    def rotate(self,angle): #changes rotation
        self.rotation += angle
        self.rotation = clamp(self.rotation,-55,55) # limits the rotation
        return self.rotation
    def move(self,x,y):
        self.x += x * 40
        self.y += y * 15

        


