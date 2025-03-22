import pygame

class Button: # simple button class,the code is fluffy, but it serves well
    def __init__(self,screen,position, width, height,text): 
        self.screen = screen
        self.w,self.h = width,height
        self.position = position
        self.text = text
        self.surface = pygame.surface.Surface((width,height)) #surface that contains both rect and text
        self.font = pygame.font.SysFont(None,36)
        self.fontsurface = self.font.render(text,True,'white') # next (12) line is centering the rect according to its position
        self.rect = pygame.Rect(self.position[0]-self.w//2,self.position[1]-self.h//2,width,height)
        self.active = True 
    def update(self):
        if self.active:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos): # hovering option
                self.surface.fill('green')
            else:
                self.surface.fill('black')
        self.surface.blit(self.fontsurface,((self.surface.get_width() - self.fontsurface.get_width())//2,self.surface.get_height()//2 - self.fontsurface.get_height()//2))
        self.screen.blit(self.surface, self.rect)
    def is_clicked(self, event): # checks if button was clicked
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.active = False
            self.surface.fill('green')
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
    def on_click(self,text): # returns preffered settings for the game
        if text == 'LVL 1':
            return 1
        elif text == 'LVL 2':
            return 2
        elif text == 'LVL 3':
            return 3
        elif text == 'Speed 1':
            return 1
        elif text == 'Speed 2':
            return 2
        elif text == 'Speed 3':
            return 3
        
