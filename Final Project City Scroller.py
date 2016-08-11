import random
import pygame
import NEWOMG 
from NEWOMG import Scroller
from NEWOMG import Building
from NEWOMG import Sidewalk
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("Mom Code")

clock = pygame.time.Clock()
totalscreen = (SCREEN_WIDTH, SCREEN_HEIGHT)
done = False
screen = pygame.display.set_mode(totalscreen)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 225)
GREY = (129, 129, 129)
PINK = (225, 0, 128)
colors = [BLACK, GREEN, BLUE, RED, PINK]   
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

sidewalk = Sidewalk(0, 475, SCREEN_WIDTH,200, GREY) 
front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 1)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
backgroundim = pygame.image.load("bg3.png").convert()

xPosition = 400
yPosition = 15

all_sprites_list = pygame.sprite.Group()
bad_sprites_list = pygame.sprite.Group()
good_sprites_list = pygame.sprite.Group()

class girlSprite(pygame.sprite.Sprite):

    def __init__(self, file_name, file_name2):
        super().__init__()
        self.images = []
        for i in range(20):
            self.images.append(file_name)
        for i in range(20):
            self.images.append(file_name2)
        self.index = 0
        self.image = pygame.image.load(self.images[self.index]).convert_alpha()
        self.rect = self.image.get_rect()

    def playerjump(self):
        if (pygame.key.get_pressed()[pygame.K_SPACE] == 1):
            self.rect.y = 350
        if (pygame.key.get_pressed()[pygame.K_SPACE] == 0 and self.rect.y != 500):
            self.rect.y = 450
            
    def update(self):
        self.rect.x -= 3
        if self.rect.center[0] < -15:
            self.rect.x = SCREEN_WIDTH + 10
            #self.kill
    
    def animate(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = pygame.image.load(self.images[self.index]).convert_alpha()
 

def makeup():
    for i in range(1):
        germ_sprite = girlSprite("germ.png", "germ.png")
        troll_sprite = girlSprite("evillegs.png", "evillegs.png")
        honey_sprite = girlSprite("honey.png", "honey.png")       
        envelope_sprite = girlSprite("envelope.png", "envelope.png")
        diaper_sprite = girlSprite("diaper.png", "diaper.png")
        pacifier_sprite = girlSprite("pacifier.png", "pacifier.png")

        germ_sprite.rect.x = random.randrange(800, 1500)
        germ_sprite.rect.y = 450
    
        troll_sprite.rect.x = random.randrange(800, 1500)
        troll_sprite.rect.y = 450

        honey_sprite.rect.x = random.randrange(800, 1500)
        honey_sprite.rect.y = 450

        envelope_sprite.rect.x = random.randrange(800, 1500)
        envelope_sprite.rect.y = random.randrange(100, 450)

        diaper_sprite.rect.x = random.randrange(800, 1500)
        diaper_sprite.rect.y = random.randrange(100, 500)

        pacifier_sprite.rect.x = random.randrange(800, 1500)
        pacifier_sprite.rect.y = random.randrange(100, 450)


        good_sprites_list.add(envelope_sprite)
        good_sprites_list.add(diaper_sprite)
        good_sprites_list.add(pacifier_sprite)
        bad_sprites_list.add(honey_sprite)
        bad_sprites_list.add(germ_sprite)
        bad_sprites_list.add(troll_sprite)
        all_sprites_list.add(germ_sprite)
        all_sprites_list.add(troll_sprite)
        all_sprites_list.add(honey_sprite)
        all_sprites_list.add(envelope_sprite)
        all_sprites_list.add(diaper_sprite)
        all_sprites_list.add(pacifier_sprite)


'''
    def make_sprites(self, level):
        all_sprites_list.add(player)

        for i in range(50):
            good_sprite = Block(".png")


            good_sprite.rect.x = random.randrange(screen_width, screen_width *2)
            good_sprite.rect.y = random.randrange(screen_height)

            good_sprites_list.add(good_sprite)
            all_sprites_list.add(good_sprite)

        for i in rande(10 *level):
            bad_sprite = Block(".png")

            bad_sprite.rect.x = random randrange(screen_width, screen_width *2)
            bad_sprite.rect.y = random.randrange(screen_height)

            bad_sprites_list.add(good_sprite)
            all_sprites_list.add(good_sprite)
'''
sprite1 = girlSprite("girlstop.png", "rungirl.png")
baby_sprite = girlSprite("baby1.png", "baby1.png")


all_sprites_list.add(sprite1)
all_sprites_list.add(baby_sprite)




sprite1.rect.x = 30
sprite1.rect.y = 450

baby_sprite.rect.x = 700
baby_sprite.rect.y = 450


while not done:   
   # --- Main event loop
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
    sprite1.playerjump()    
    bad_sprites_list.update()
    sprite1.animate()
    good_sprites_list.update()
    
    # --- Game logic should go here
    badguy = len(bad_sprites_list)
    if badguy <= 2:
        makeup()
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    #all_sprites_list.update(self)
    screen.blit(backgroundim, (0,0))

    # --- Drawing code should go here

    back_scroller.draw_buildings(screen)
    back_scroller.move_buildings()
    middle_scroller.draw_buildings(screen)
    middle_scroller.move_buildings()
    front_scroller.draw_buildings(screen)
    front_scroller.move_buildings()
    sidewalk.draw(screen)
    
    all_sprites_list.draw(screen)


    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE

