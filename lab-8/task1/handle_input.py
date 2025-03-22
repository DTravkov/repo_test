import pygame
from clamp import clamp
velocity = pygame.math.Vector2(0.0,0.0) # velocity in Vectors,handy thing
velocity_limit = 15 # limits the x speed of movement
def handle_input(delta_time,player,map):
    input = pygame.key.get_pressed()
    if input[pygame.K_a]: # rotates the player sprite and increases velocity
        player.rotate(1000 * delta_time)
        velocity.x = pygame.math.lerp(velocity.x,velocity.x - 5, 5 * delta_time * 9)
    if input[pygame.K_d]: # rotates the player sprite and increases velocity
        player.rotate(-1000 * delta_time)
        velocity.x = pygame.math.lerp(velocity.x,velocity.x + 5, 5 * delta_time * 9)
    if not(input[pygame.K_d] or input[pygame.K_a]): # rotation damping
        player.rotation = player.rotation * 0.9 # pygame.math.lerp(player.rotation,0, 5*delta_time*9)
    player.move(velocity.x * delta_time,velocity.y * delta_time)
    if not (input[pygame.K_d] or input[pygame.K_a]): # velocity damping
        velocity.x = velocity.x * 0.9# pygame.math.lerp(velocity.x,0, 5*delta_time*4)
    velocity.x = clamp(velocity.x,-velocity_limit,velocity_limit)