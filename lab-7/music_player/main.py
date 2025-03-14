import pygame,random
from sound_player import sound_player as player


# This project uses relative paths for accessing sounds,make sure that you download this folder separately
#(where file is located) and open it in VSCode,before running the main.py


pygame.init()
res = (600,600)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

mixer = player("sfx/") # initializing mixer in sfx directory
mixer.play_sound('sfx/track.mp3')
running = True

font = pygame.font.SysFont(None,36)

def render_info(screen):
    label = font.render(str(mixer.current_song),True,"black")
    labelplaying = font.render("Is song playing :" + str(mixer.playing),True,"black")
    labellen = font.render("There are " + str(len(mixer.queue)) + f' songs in {mixer.mainpath} directory',True,"black")
    screen.blit(label,(screen.get_width() // 2 - label.get_rect().width // 2,screen.get_height() // 2))
    screen.blit(labelplaying,(screen.get_width() // 2 - labelplaying.get_rect().width // 2,screen.get_height() // 2 + 50))
    screen.blit(labellen,(screen.get_width() // 2 - labellen.get_rect().width // 2,screen.get_height() // 2 + 100))

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
    render_info(screen)
    clock.tick(60)
    pygame.display.flip()



    
    
