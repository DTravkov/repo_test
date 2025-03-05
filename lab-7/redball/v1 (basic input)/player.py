import pygame

class Player:
    def __init__(self,position,screen):
        self.screen = screen
        self.position = pygame.Vector2(position)
        self.surface = pygame.surface.Surface((50,50),pygame.SRCALPHA).convert_alpha()
        self.radius = 25
        self.circle = pygame.draw.circle(self.surface,'red',(self.surface.get_width()//2,self.surface.get_height()//2),self.radius)
    def render(self):
        self.screen.blit(self.surface,self.position)
    def move(self,direction):
        if direction == 'a' and self.position.x - 20 > 0:
            self.position.x -= 20
        if direction == 'd' and self.position.x + 20 < self.screen.get_width() - self.radius * 2:
            print(self.position.x + 20 < self.screen.get_width())
            self.position.x += 20
        if direction == 'w' and self.position.y - 20 > 0:
            self.position.y -= 20
        if direction == 's' and self.position.y + 20 < self.screen.get_height() - self.radius * 2:
            self.position.y += 20
    
    