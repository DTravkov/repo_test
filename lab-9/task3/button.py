import pygame



class Button: #thick buttons code
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.surface = pygame.surface.Surface((width,height))
        self.surface.fill(color)
        self.font = pygame.font.Font(None, 26)
        self.text = text
        self.shadow_surface = self.font.render(self.text, True, (60,60,60)) #gray shadow
        self.text_surface = self.font.render(self.text, True,'white')
        self.action = action
    def draw(self, screen):
        screen.blit(self.surface, (self.rect.x, self.rect.y))
    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.action()
    def check_hover(self,mousepos):
        if self.rect.collidepoint(mousepos):
            self.text_surface = self.font.render(self.text, True,'green') # the next 2 lines are long,but all they do is blitting cenetered text and its shadow
            self.surface.blit(self.shadow_surface,((self.surface.get_width()//2 - self.text_surface.get_width()//2) + 2 , (self.surface.get_height()//2 - self.text_surface.get_height()//2) + 2))
            self.surface.blit(self.text_surface,(self.surface.get_width()//2 - self.text_surface.get_width()//2,self.surface.get_height()//2 - self.text_surface.get_height()//2))
        else:
            self.text_surface = self.font.render(self.text, True,'white')
            self.surface.blit(self.shadow_surface,((self.surface.get_width()//2 - self.text_surface.get_width()//2) + 2 , (self.surface.get_height()//2 - self.text_surface.get_height()//2) + 2))
            self.surface.blit(self.text_surface,(self.surface.get_width()//2 - self.text_surface.get_width()//2,self.surface.get_height()//2 - self.text_surface.get_height()//2))
 
 
class SwitcherButton(Button): # button with switching hover setting,so that user knows he's erasing stuff
    def __init__(self, x, y, width, height, text, color, action):
        super().__init__(x, y, width, height, text, color, action)
        self.state = False
    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.action()
                self.state = not self.state
    def draw(self,screen):
        self.text_surface = self.font.render(self.text, True,'green' if self.state == True else 'white')
        self.surface.blit(self.shadow_surface,((self.surface.get_width()//2 - self.text_surface.get_width()//2) + 2 , (self.surface.get_height()//2 - self.text_surface.get_height()//2) + 2))
        self.surface.blit(self.text_surface,(self.surface.get_width()//2 - self.text_surface.get_width()//2,self.surface.get_height()//2 - self.text_surface.get_height()//2))

        screen.blit(self.surface,(self.rect.x,self.rect.y))

          
        