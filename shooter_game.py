#Create your own shooter

from pygame import *

w_width = 700
w_height = 500

img_back = 'C:/Users/LENOVO/.vscode/extensions/algoritmika.algopython-20241210.135312.0/data/student/100067267/1414727/galaxy.jpg'


display.set_caption('Shooter')
win = display.set_mode((700, 500))
background = transform.scale(image.load(img_back), (w_width, w_height))


class Base(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def bleet(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Pleyer(Base):
    def movemnt(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < w_width - 10:
            self.rect.x += self.speed    


img_player = 'C:/Users/LENOVO/.vscode/extensions/algoritmika.algopython-20241210.135312.0/data/student/100067267/1414727/rocket.png'
hero = Pleyer(img_player, w_width/2, w_height/2, 80, 100, 10)

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        win.blit(background, (0,0))
        hero.movemnt()
        hero.bleet()    

        display.update()
    time.delay(50)
     



