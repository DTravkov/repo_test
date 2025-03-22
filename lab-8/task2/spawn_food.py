import pygame
from random import *
class Apple:
    def __init__(self,screen,snake,food_spawn_exclusions):
        self.screen = screen
        self.food_spawn_exclusions = food_spawn_exclusions
        self.surface = pygame.surface.Surface((20,20))
        self.surface.fill('red')
        self.rect = self.surface.get_rect()
        self.posx = [x for x in range(40,screen.get_width()-40) if x % 20 == 0] 
        self.posy = [x for x in range(40,screen.get_height()-40) if x % 20 == 0]
        self.rect.x,self.rect.y = (choice(self.posx),choice(self.posy))
        self.pos = [self.rect.x,self.rect.y]
        while self.pos in food_spawn_exclusions: # chooses the right position to spawn
            self.rect.x,self.rect.y = (choice(self.posx),choice(self.posy))
            self.pos = [self.rect.x,self.rect.y]
        self.rect = pygame.Rect(self.pos[0],self.pos[1],20,20)
    def update(self):
        self.screen.blit(self.surface,self.rect)
    def respawn(self): # respawns apple after eaten
        self.rect.x,self.rect.y = (choice(self.posx),choice(self.posy))
        self.pos = [self.rect.x,self.rect.y]
        while self.pos in self.food_spawn_exclusions:
            self.rect.x,self.rect.y = (choice(self.posx),choice(self.posy))
            self.pos = [self.rect.x,self.rect.y]
        self.screen.blit(self.surface,self.rect)

        
    
    
