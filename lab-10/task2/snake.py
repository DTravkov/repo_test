import pygame
import random
class Snake:
    def __init__(self,screen,map,speed):
        self.head = [100,100]
        self.body = [[40,100],[60,100],[80,100],[100,100]]
        self.direction = 'right'
        self.screen = screen
        self.speed = speed
        self.rect = pygame.Rect(self.head[0],self.head[1],20,20)
        self.grow = False
        if speed != -1: # freeplay adjustment,else statement start freeplay with speed = 1 
            self.difficulty = (self.speed * 2) + 7
        else:
            self.difficulty = 7 
        self.score = 0
        self.map = map
    def move(self):
        newhead = list(self.body[-1])
        if self.direction == 'right':
            newhead[0] += 20
        elif self.direction == 'left':
            newhead[0] -= 20 
        elif self.direction == 'up':
            newhead[1] -= 20 
        elif self.direction == 'down':
            newhead[1] += 20 
        self.head = newhead
        self.body.append(newhead)
        if not self.grow:
            self.body.remove(self.body[0])
        else:
            self.grow = False
    def update(self):
        self.rect = pygame.Rect(self.body[-1][0],self.body[-1][1],20,20) # snake head rect
        self.move()
        for block in self.body:
            color = random.choice([(0,255,113),(30,237,0)])
            pygame.draw.rect(self.screen,color,pygame.Rect(block[0],block[1],20,20))
    def is_game_over(self):
        gameIsOver = False
        if self.body.count(self.head) > 1:
            gameIsOver = True
        if self.head[0] >= self.screen.get_width() or self.head[0] < 0: # gameover conditions
            gameIsOver = True
        elif self.head[1] >= self.screen.get_width() or self.head[1] < 0:
            gameIsOver = True
        elif self.head in self.map.get_walls_position():
            gameIsOver = True
        return gameIsOver
        
    def check_collision(self,rect):
        if self.rect.colliderect(rect):
            self.grow = True
            self.add_speed()
        self.is_game_over()
        return self.rect.colliderect(rect)
    def add_speed(self):
        if self.speed == -1:
            self.difficulty = (self.score//4) * 2 + 7