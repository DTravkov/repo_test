import pygame
import random

class WallMap: # This class takes chosen level,and draws walls using the array coordinates
    def __init__(self,screen=pygame.surface.Surface((600,600)),level=1): 
        self.level = level
        self.screen = screen
        self.walls_position = []
        if level == 1: # I couldnt come up with simple level creation system,so each wall is a coordinate in an array
            center = [self.screen.get_width()//2-20,self.screen.get_height()//2-20]
            self.walls_position = [
                center,
            [center[0]-20,center[1]],
            [center[0]+20,center[1]],
            [center[0]-40,center[1]],
            [center[0]+40,center[1]],
            [center[0],center[1]+20],
            [center[0],center[1]-20],
            [center[0],center[1]+40],
            [center[0],center[1]-40]]
        elif level == 2:
            self.walls_position = [
            [20, 20], [40, 20],  
            [540, 20], [560, 20],  
            [20, 560], [40, 560],  
            [540, 560], [560, 560],  
            [160, 160], [180, 160],  
            [420, 160], [440, 160],  
            [160, 420], [180, 420],  
            [420, 420], [440, 420]  
]
        else:
            self.walls_position = []
        self.draw_level() # draws level in init stage,so that apple and snake receives coordinates of the walls
    def draw_level(self):
        for wall in self.walls_position: #draws each gray wall
            pygame.draw.rect(self.screen,'gray',pygame.Rect(wall[0],wall[1],20,20))
    def get_walls_position(self):
        return self.walls_position # just to get the coordinates for snake and apples