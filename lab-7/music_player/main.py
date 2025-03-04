import pygame,random
from sound_player import sound_player as player
pygame.init()
res = (600,600)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

mixer = player("sfx/") # initializing mixer in sfx directory

running = True

font = pygame.font.SysFont(None,36)

def render_current_song(screen):
    label = font.render(str(mixer.current_song),True,"black")
    labelplaying = font.render("Is song playing :" + str(mixer.playing),True,"black")
    screen.blit(label,(screen.get_width() // 2 - label.get_rect().width // 2,screen.get_height() // 2))
    screen.blit(labelplaying,(screen.get_width() // 2 - labelplaying.get_rect().width // 2,screen.get_height() // 2 + 50))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                mixer.play_random_sound()
            elif event.key == pygame.K_SPACE: # to pause/resume player
                mixer.pause()
            elif event.key == pygame. K_RIGHT:
                mixer.play_next_song('right')
            elif event.key == pygame. K_LEFT:
                mixer.play_next_song('left')
    screen.fill('gray')
    render_current_song(screen)
    clock.tick(10)
    pygame.display.flip()



    
    