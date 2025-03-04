import pygame,random
from player import Player
from input_handler import input_handler as input
pygame.init()
res = (800,800)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Red ball")
clock = pygame.time.Clock()
player = Player((random.randint(50,res[0]-50),random.randint(50,res[1]-50)),screen)
running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('white')
    input(pygame.key.get_pressed(),player)
    player.render()
    clock.tick(60)
    pygame.display.flip()



    
    