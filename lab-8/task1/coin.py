import pygame,random

class Coin:
    def __init__(self,screen:pygame.surface.Surface):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load("coin.png"),(screen.get_width()//15,screen.get_width()//15)).convert_alpha()
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(random.choice([x for x in range(60,screen.get_width()-60) if x % 50 == 0]),0-self.rect.height)
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
    def spawn(self,screen,delta_time):
        if self.active:
            self.rect = self.image.get_rect()
            self.position.y += 1200 * delta_time
            self.rect.y = self.position.y
            self.rect.x = self.position.x
            self.screen.blit(self.image,self.rect)
            if self.rect.y >= self.screen.get_height() + self.rect.height:
                self.active = False