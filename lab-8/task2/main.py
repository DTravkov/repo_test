import pygame
from snake import *
from spawn_food import *
from text_manager import Label
from wall_generation import WallMap
from button import *
pygame.init()
res = (600,600)
screen = pygame.display.set_mode(res)

running = True
clock = pygame.time.Clock()
welcome = Label(screen,52,'darkgreen',True) # UI elements defined with classes
welcome2 = Label(screen,36,'darkgreen',True)
button_1 = Button(screen,(250,360),80,40,'LVL 1')
button_2 = Button(screen,(340,360),80,40,'LVL 2')
difficulty_1 = Button(screen,(170,300),120,40,'Speed 1')
difficulty_2 = Button(screen,(300,300),120,40,'Speed 2')
difficulty_3 = Button(screen,(430,300),120,40,'Speed 3')
freeplay = Button(screen,(300,460),125,50,'Freeplay')
ui = [button_1,button_2,difficulty_1,difficulty_2,difficulty_3,freeplay]



level = None
speed = None

while running: # First menu loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame = False
            running = False
        for element in ui: # looping through events with buttons,untill all the settings are correctly chosen
            if element.is_clicked(event) and "LVL" in element.text:
                level = int(element.text[-1])
                for button in ui:
                    if button != element and "LVL" in element.text:
                        button.active = True
            elif element.is_clicked(event) and "Speed" in element.text:
                speed = int(element.text[-1])
                for button in ui:
                    if button != element and "Speed" in element.text:
                        button.active = True
            elif element.is_clicked(event) and "Free" in element.text:
                level = 3
                speed = int(-1)
                running = False
            if (level and speed):
                running = False
    screen.fill((243, 243, 243))
    welcome.update("Welcome to the Snake Game!",(300,150))
    welcome2.update("Choose a difficulty and a level that you'd like",(300,200))
    button_1.update()
    button_2.update()
    difficulty_1.update()
    difficulty_2.update()
    difficulty_3.update()
    freeplay.update()
    
    clock.tick(60)
    pygame.display.flip()

        
map = WallMap(screen,level) # class that builds walls
running = True
clock = pygame.time.Clock()
snake = Snake(screen,map,speed) # player

score = Label(screen,36,(255,255,255)) # score handler
food_spawn_exclusions = map.get_walls_position() + snake.body # positions that food cant spawn on
food = Apple(screen,snake,food_spawn_exclusions)
newdir = False # variable to fix 2 inputs in 1 frame
            
while running: #Main game loop
    food_spawn_exclusions = map.get_walls_position() + snake.body # updating the food exclusions with respect to snake position
    score.recolor()
    newdir = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame = False
            running = False
        if event.type == pygame.KEYDOWN and not newdir: # Input handling
            if event.key == pygame.K_w and snake.direction != 'down':
                snake.direction = 'up'
                newdir = True
            elif event.key == pygame.K_s and snake.direction != 'up' :
                snake.direction = 'down'
                newdir = True
            elif event.key == pygame.K_a and snake.direction != 'right':
                snake.direction = 'left'
                newdir = True
            elif event.key == pygame.K_d and snake.direction != 'left':
                snake.direction = 'right'
                newdir = True
    screen.fill('black')
    map.draw_level()
    if snake.check_collision(food.rect):
        food.respawn()
        score.recolor('green')
    food.update()
    snake.update()
    score.update('score : ' + str(snake.score),(100,40))
    pygame.display.flip()
    clock.tick(snake.difficulty) # framerate = 7 + (speed * 2) for normal mode, and 7 + (score * 2) for freeplay
