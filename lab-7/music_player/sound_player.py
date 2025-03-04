import pygame,os,random
class sound_player:
    def __init__(self,songspath):
        self._sound_library = {}
        self.add_all_sounds(songspath)
        self.get_songs_list()
        self.current_song = ''
        self.playing = False
        self.queue = []


    def canonicalize_path(self,path):
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        return canonicalized_path
    

    def play_random_sound(self):
        pygame.mixer.stop()
        song = random.choice(self.get_songs_list())
        self.current_song = song
        pygame.mixer.Sound(song).play()

    def play_next_song(self,direction:str):
            self.stop()
            self.get_songs_list()
            newidx = 0
            if direction == 'right':
                curidx = self.queue.index(self.current_song)
                if curidx + 1 < len(self.queue):
                    newidx = curidx + 1
                    self.play_sound(self.queue[curidx + 1])
                else:
                    self.play_sound(self.queue[0])
                    newidx = 0
            elif direction == 'left':
                curidx = self.queue.index(self.current_song)
                if curidx - 1 >= 0:
                    self.play_sound(self.queue[curidx - 1])
                    newidx = curidx - 1
                
                elif curidx - 1 == 0:
                    self.play_sound(self.queue[0])
                    newidx = 0
                elif curidx - 1 < 0:
                    self.play_sound(self.queue[-1])
                    newidx = len(self.queue) - 1
            self.current_song = self.queue[newidx]

            


    def stop(self):
        pygame.mixer.stop()
        self.playing = False
    
    def add_all_sounds(self,path):
        path = self.canonicalize_path(path)
        for i in os.listdir(path):
            sound = self._sound_library.get(i)
            if sound == None:
                sound = pygame.mixer.Sound(path + i)
                self._sound_library[path + i] = sound
            else:
                pass

    def pause(self):
        if self.playing:
            pygame.mixer.pause()
            self.playing = False
        elif self.playing == False:
            pygame.mixer.unpause()
            self.playing = True
    def play_sound(self,path):
        sound = self._sound_library.get(self.canonicalize_path(path))
        if sound == None:
            canon_path = self.canonicalize_path(path)
            sound = pygame.mixer.Sound(canon_path)
            self._sound_library[canon_path] = sound
        self.current_song = path.replace('\\','/')
        sound.play()
        self.playing = True

    def get_songs_list(self):
        self.queue = lst = list(self._sound_library.keys())
        for i in lst:
            lst[lst.index(i)] = str(i).replace('\\','/')
        return lst