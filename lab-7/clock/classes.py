import pygame,datetime

class TimeClock:
    def __init__(self,screen:pygame.surface.Surface):
        self.screen = screen
        self.rotationx = 0
        self.rotationy = 0
        self.has_sprite = False
        self.sprites = []
        self.current_time = datetime.datetime.today()
    def get_sprites(self):
        self.sprites += [pygame.transform.scale(pygame.image.load("sprites/clock_base.png"),self.screen.get_size()),pygame.transform.scale(pygame.image.load("sprites/minute_arrow2.png"),self.screen.get_size()),pygame.transform.scale(pygame.image.load("sprites/hour_arrow2.png"),self.screen.get_size())]
        self.has_sprite = True
    def apply_rotation(self):
        rotated_image = pygame.transform.rotate(self.sprites[1], self.rotationx)# for minute arrows
        prect = rotated_image.get_rect()
        prect.center = (int(self.screen.get_width()/2),int(self.screen.get_height()/2))
        self.screen.blit(rotated_image,prect)
        rotated_image = pygame.transform.rotate(self.sprites[2], self.rotationy) # for hour arrows
        prect = rotated_image.get_rect()
        prect.center = (int(self.screen.get_width()/2),int(self.screen.get_height()/2))
        self.screen.blit(rotated_image,prect)
    def update(self):
        if self.has_sprite == False:
            self.get_sprites()
        else:
            self.current_time = datetime.datetime.today()
            self.rotationx = -self.current_time.minute * 6 #following 2 lines convert time into angles
            self.rotationy = (-(self.current_time.hour % 12) * 30) + (-self.current_time.minute * 1/2)
            self.screen.blit(self.sprites[0],(0,0))
            self.apply_rotation() # applies rotation to arrows,while keeping arrows aligned
            


        

        
        
