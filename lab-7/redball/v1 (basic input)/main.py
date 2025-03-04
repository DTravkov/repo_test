import pygame,random
from player import Player
pygame.init()
res = (200,200)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Red ball")
clock = pygame.time.Clock()
player = Player((random.randint(50,res[0]-50),random.randint(50,res[1]-50)),screen)
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move('w')
            elif event.key == pygame.K_a: 
                player.move('a')
            elif event.key == pygame. K_s:
                player.move('s')
            elif event.key == pygame. K_d:
                player.move('d')
    screen.fill('white')
    player.render()
    clock.tick(60)
    pygame.display.flip()



    
    