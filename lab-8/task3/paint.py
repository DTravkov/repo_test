import pygame
from button import *
pygame.init()
res = (800,600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(res)
pygame.display.set_caption('Paint')

white = (255, 255, 255) #predefined colors,but i mostly use 'colorX' style
black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)



drawing = False #settings
brush_color = black
last_color = black
brush_radius = 5
brush_mode = 'draw' # ['draw','erase']
points = []
radius = 0

def set_draw(): # some functions  to keep things organized
    global brush_mode
    brush_mode = 'draw'

def set_erase():
    global brush_mode
    global brush_color
    brush_color = 'white' if brush_mode != 'erase' else last_color
    brush_mode = 'erase' if brush_mode != 'erase' else 'draw'


def set_black():
    if brush_mode != 'erase':
        global brush_color
        global last_color
        brush_color = black
        last_color = black
        set_draw()
def set_green():
    if brush_mode != 'erase':
        global brush_color
        global last_color
        brush_color = green
        last_color = green
        set_draw()
def set_red():
    if brush_mode != 'erase':
        global brush_color
        global last_color
        brush_color = red
        last_color = red
        set_draw()
def set_blue():
    if brush_mode != 'erase':
        global brush_color
        global last_color
        brush_color = blue
        last_color = blue
        set_draw()
def set_thin():
    global brush_radius
    brush_radius = 5
def set_medium():
    global brush_radius
    brush_radius = 10
def set_thick():
    global brush_radius
    brush_radius = 15




def clear_screen():
    points.clear()
    screen.fill(white)
def exit_app():
    pygame.quit()


uikit = [
    Button(8, 10, 64, 30, 'Black', black, set_black),
    Button(8, 50, 64, 30, 'Green', green, set_green),
    Button(8, 90, 64, 30, 'Red', red, set_red),
    Button(8, 130, 64, 30, 'Blue', blue, set_blue),
    SwitcherButton(8, 180, 64, 30, 'Erase', gray, set_erase),
    Button(8, 230, 64, 30, 'Thin', (40,40,40), set_thin),
    Button(8, 280, 64, 30, 'Med.', (40,40,40), set_medium),
    Button(8, 330, 64, 30, 'Thick', (40,40,40), set_thick),
    Button(8, 380, 64, 30, 'Clear', gray, clear_screen),
    Button(8, 430, 64, 30, 'Exit', gray, exit_app)
]

slide = None
clear_screen()
while pygame:
    mouse_x , mouse_y = pygame.mouse.get_pos() #updates mosue position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in uikit:
                button.check_action(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z: # circle drawing
            pygame.draw.circle(screen,brush_color,pygame.mouse.get_pos(),10*brush_radius,3)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:# rect drawing
            w,h = 16*brush_radius,16*brush_radius
            pygame.draw.rect(screen,brush_color,pygame.Rect(pygame.mouse.get_pos()[0] - w // 2,pygame.mouse.get_pos()[1] - h//2,w,h),3)

    
    last = None if len(points) == 0 else points[-1] # last point

    if drawing: # draws a smooth lines using array,when lmb is not held erases the points array,blitting the image drawn only
        if mouse_x > 50:
            point = [mouse_x,mouse_y,False,brush_radius,brush_color]
            points.append(point)
    elif not drawing and last:
        points.append([mouse_x,mouse_y,True,brush_radius,brush_color])
        slide = screen.copy()
        points.clear()
        screen.blit(slide,(0,0))

    n = 0 
    while n+1 < len(points): #while loop which handles the smooth lines
        if points[n][2] == False:
            pygame.draw.circle(screen, points[n][4], (points[n][0], points[n][1]), points[n][3] // 2 - 0.4)
            pygame.draw.line(screen, points[n][4], [points[n][0], points[n][1]], [points[n+1][0], points[n+1][1]], points[n][3])
        n += 1
    pygame.draw.rect(screen, black, (0, 0, 82, res[1]))#instrument pad background
    pygame.draw.rect(screen, gray, (0, 0, 80, res[1]))
    pygame.draw.rect(screen, brush_color, (8, 510, 64, 40)) #color info
    for button in uikit: # resposnible for buttons
        button.draw(screen)
        button.check_hover((mouse_x,mouse_y))
    clock.tick(60)
    pygame.display.flip()



    






