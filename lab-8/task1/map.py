import pygame


class Map:
    def __init__(self,resolution,imagepath): # creates map by size of screen
        self.width = resolution[0]
        self.height = resolution[1]
        self.imagepath = imagepath
        self.x = self.width // 2
        self.y = self.height//2
        self.scrollspeed = 1
        self.image = pygame.image.load(self.imagepath)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = self.image.get_rect()
    def update(self,screen:pygame.surface.Surface,delta_time): # updates the map,blits it on screen,and moves it repeatedly so that road seems to be infinite
        self.y += 1200 * delta_time * self.scrollspeed
        self.rect.center = (self.x, self.y)
        if self.rect.y <= self.height:
            screen.blit(self.image,pygame.Rect(self.rect.left,self.rect.top-self.height,self.rect.width,self.rect.height))
        else:
            self.y = self.height // 2
            screen.blit(self.image,pygame.Rect(self.rect.left,self.rect.top-self.height,self.rect.width,self.rect.height))
        screen.blit(self.image,self.rect)

    def get_h(self): # some misc (get) methods.not sure if they are neccessary,but let them be
        return self.height
    def get_w(self):
        return self.width
    def get_center(self):
        return self.width // 2, self.height // 2