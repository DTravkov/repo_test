import pygame


class Label: # simple class for rendering text
    def __init__(self,screen,size=36,color=(255,255,255),centered=True):
        self.font = pygame.font.SysFont(None,size)
        self.screen = screen
        self.color = color
        self.centered = centered
        self.prev_color = self.color
    def update(self,text,position):
        self.surface = self.font.render(f'{text}',True,self.color)
        if self.centered:
            self.screen.blit(self.surface,((int(position[0]) - self.surface.get_width() // 2), position[1]))
        else:
            self.screen.blit(self.surface,position)
    def recolor(self,color=None):
        if color == None:
            self.color = self.prev_color
        else:
            self.prev_color = self.color
            new_color = color
            self.color = color