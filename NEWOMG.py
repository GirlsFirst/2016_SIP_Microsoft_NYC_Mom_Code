import pygame
import random

class Building():

    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color



    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height), 0)

    def move(self, speed):
        self.x_point = self.x_point-speed
        
        
class Scroller(object):

    def __init__(self, width, height, base, color, speed):
        
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.buildings = []
        #SCREEN_WIDTH = 800
        #SCREEN_HEIGHT = 600
        #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fill_scroller()
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 225)
        GREY = (129, 129, 129)
        PINK = (225, 0, 128)
        colors = [BLACK, GREEN, BLUE, RED, PINK]   
class girlSprite(pygame.sprite.Sprite):
    def __init__(self, file_name):
        super().__init__()
        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect()
    def make_sprites(level):
        all_sprites_list.add(player)

        for i in range(50):
            good_sprite = Block("baby.png")


            good_sprite.rect.x = random.randrange(screen_width, screen_width *2)
            good_sprite.rect.y = random.randrange(screen_height)

            good_sprites_list.add(good_sprite)
            all_sprites_list.add(good_sprite)

        for i in rande(10 *level):
            bad_sprite = Block("sun.png")

            bad_sprite.rect.x = random.randrange(screen_width, screen_width *2)
            bad_sprite.rect.y = random.randrange(screen_height)

            bad_sprites_list.add(good_sprite)
            all_sprites_list.add(good_sprite)
            

sprite1 = girlSprite("girlstill.png")
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(sprite1)

      

def fill_scroller(self):
    currentwidth = 0
    while currentwidth <= self.width:
        self.add_building(currentwidth)
        recent = self.buildings[-1].width
        currentwidth += recent

    def add_building(self, x_point):

        self.x_point= x_point
        
        max_height = self.base - self.height
        height2 = random.randint((max_height // 4), (max_height -1))
        width2 = random.randint((self.width // 20) ,(self.width //4))
        y_location = self.base - height2

        b1 = Building(x_point, y_location, width2, height2, self.color)

        self.buildings.append(b1)

    def draw_buildings(self,screen):

        for x in self.buildings:
            x.draw(screen)

    def move_buildings(self):

        prevx = self.buildings[-1].x_point
        actualw = self.buildings[-1].width
        newpoint = actualw + prevx
        for x in self.buildings:
            x.move(self.speed)
        self.add_building(newpoint)



