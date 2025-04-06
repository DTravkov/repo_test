import pygame,random
from clamp import *
class Coin:
    def __init__(self,screen:pygame.surface.Surface):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load("coin.png"),(screen.get_width()//15,screen.get_width()//15)).convert_alpha()
        self.rect = self.image.get_rect()
        self.y = 0-self.rect.height
        self.rect.x = random.choice([x for x in range(60,screen.get_width()-60) if x % 50 == 0])
        self.rect.y = 0-self.rect.height
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

        self.weight = random.randrange(1,4)
    def update(self,screen,delta_time):
        if self.active:
            self.rect.move_ip(0,int(710 * delta_time))
            self.screen.blit(self.image,self.rect)
        else:
            pass