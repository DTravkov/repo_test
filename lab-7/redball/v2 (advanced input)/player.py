import pygame

class Player:
    def __init__(self,position,screen:pygame.surface.Surface):
        self.screen = screen
        self.speed = 15
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(0,0)
        self.movement_vector = pygame.Vector2(0,0)
        self.surface = pygame.surface.Surface((50,50),pygame.SRCALPHA).convert_alpha()
        self.radius = 25
        self.circle = pygame.draw.circle(self.surface,'red',(self.surface.get_width()//2,self.surface.get_height()//2),self.radius)
    def render(self):
        self.velocity += self.movement_vector * self.speed
        self.velocity *= 0.95
        self.position += self.velocity * pygame.time.Clock().tick(60) / 1000
        
        self.screen.blit(self.surface,self.position)
        
    