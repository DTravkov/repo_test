import pygame
from map import Map
from player import Player
from clamp import clamp
from enemy import Enemy
from handle_input import handle_input
from coin import Coin



# 
# 
# This project uses relative paths.Make sure to download the folder with this game and open it in VSCode before running it,because otherwise sprites used in the game may not be found by pygame.
#
#


pygame.init()
FPS = 60
res = (600,800)
map = Map(res,"road.png")
screen = pygame.display.set_mode((map.get_w(),map.get_h()))
running = True
clock = pygame.time.Clock()
player = Player(1,1.3,screen)
enemylist = []
coinlist = []
timer_interval = 500 
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event , timer_interval)
font = pygame.font.SysFont(None,48)

def render_info(screen): # Renders amount of picked coins
    label = font.render(str(player.score) + "$",True,"white")
    screen.blit(label,(screen.get_width() // 2 - label.get_rect().width // 2,screen.get_height() // 12))
delta_time = 0.005 #inital deltatime so that first game loop wont crash, becausre of missing delta_time value
while running:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame = False
            running = False
        elif event.type == timer_event: # spawns enemy and coins using event-based timer

            enemy = Enemy(screen,player.score)
            enemylist.append(enemy)

            coin = Coin(screen)
            coinlist.append(coin)

    handle_input(delta_time,player,map) # takes input from keyboard,translates it into player's velocity

    map.update(screen,delta_time) #updates and moves the map

    for coin in coinlist: # coin managera
        coin.update(screen,delta_time)
        if player.check_collision(coin,coin.mask) and coin.active: # checks collision with coins
            player.score += coin.weight
            coin.active = False
    for enemy in enemylist: # enemy manager
        enemy.update(screen,delta_time)
        if player.check_collision(enemy,enemy.mask): # checks pixel perfect collision with ebemies
            pygame.quit()
        if enemy.rect.y > screen.get_height()+80:
            enemy.active = False
    player.update(screen) # renders player
    render_info(screen) # renders amount of money
    pygame.display.flip()
    delta_time = clock.tick(FPS) / 1000 # difference between last and current frame to cut dependence on framerate, and use some smooth features (like lerp,velocity damping in unity or godot game enignes)
    clock.tick(FPS)
    


    
