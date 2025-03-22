import pygame
from math import *

# Controls : 
# [q] - start to draw, [space] - start to erase
# [r,g,b] - changing colors
# [c] - draw circles, [s] = draw squares
#

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    erase = False
    drawmode = 'square'
    while True:
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            erase = True
        else:
            erase = False
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_s:
                    drawmode = 'square'
                elif event.key == pygame.K_c:
                    drawmode = 'circle'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and (pressed[pygame.K_q] or pressed[pygame.K_SPACE]):
                # if mouse moved, add point to list
                position = event.pos
                points = points + [[position,erase]]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            if drawmode == 'circle':
                if points[i][1] == False:
                    if points[i][1] == points[i+1][1]:
                        drawLineBetween(screen, i, points[i][0], points[i + 1][0], radius, mode)
                else:
                    if points[i][1] == points[i+1][1]:
                        drawErase(screen, points[i][0], points[i + 1][0], radius)
                    #pygame.draw.circle(screen,'black',points[i][0],radius)
            elif drawmode == 'square':
                if points[i][1] == False:
                    if points[i][1] == points[i+1][1]:
                        drawRectBetween(screen, i, points[i][0], points[i + 1][0], radius, mode)
                else:
                    if points[i][1] == points[i+1][1]:
                        drawErase(screen, points[i][0], points[i + 1][0], radius)
                    #pygame.draw.circle(screen,'black',points[i][0],radius)

        
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
def drawRectBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.rect(screen, color,pygame.Rect(x,y,width,width))
def coloring(color_mode,i):
    c1 = max(0, min(255, 2 * i - 256))
    c2 = max(0, min(255, 2 * i))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    return color
def drawErase(screen, start, end, width):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, 'black', (x, y), width)

main()