import pygame
def input_handler(input,player):

    if input[pygame.K_w]:
        player.movement_vector.y = -1
    elif input[pygame.K_s]:
        player.movement_vector.y = 1
    else:
        player.movement_vector.y = 0
    
    if input[pygame.K_a]:
        player.movement_vector.x = -1
    elif input[pygame.K_d]:
        player.movement_vector.x = 1
    else:
        player.movement_vector.x = 0
    if player.movement_vector.x != 0 or player.movement_vector.y != 0:
        player.movement_vector.normalize()
    