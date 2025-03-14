import pygame,datetime
from classes import TimeClock


# This project uses relative paths for accessing images,make sure that you download this folder
#(where file is located) and opened it in VSCode,before running the main.py



pygame.init()
res = (600,600)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Clock")
enigneclock = pygame.time.Clock()
screen.fill("gray")
running = True
clock_object = TimeClock(screen)
font = pygame.font.SysFont(None,36)

def render_current_time(screen):
    timelabel = font.render(str(clock_object.current_time.time().replace(microsecond= 0)),True,"black")
    screen.blit(timelabel,(0,0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('gray')
    clock_object.update()
    render_current_time(screen)
    enigneclock.tick(10)
    pygame.display.flip()



    
    