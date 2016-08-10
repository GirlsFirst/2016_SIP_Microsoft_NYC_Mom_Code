import random
import pygame
 
from NEWOMG import Scroller
from NEWOMG import Building
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("FinalProjectCityScroller")

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
front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
backgroundim = pygame.image.load("galaxy.jpg").convert()

xPosition = 400
yPosition = 15


class girlSprite(pygame.sprite.Sprite):

    def __init__(self, file_name):
        super().__init__()
        self.image = pygame.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect()
        
    def playermove(self):
        pygame.event.pumped()
        key = pygame.key.get_pressed()
        if key[pygame.K_Space]()
            



    def update(self):
        for germ_sprite in girlSprite:
            self.rect.x -=5 

		
sprite1 = girlSprite("girlstop.png")
sprite2 = girlSprite("rungirl.png")
sun_sprite = girlSprite("sun.png")
baby_sprite = girlSprite("baby1.png")
germ_sprite = girlSprite("germ.png")
troll_sprite = girlSprite("evillegs.png")
all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(sprite2)
all_sprites_list.add(sun_sprite)
all_sprites_list.add(baby_sprite)
all_sprites_list.add(germ_sprite)
all_sprites_list.add(troll_sprite)

        
while not done:   
   # --- Main event loop
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
        
     
    # --- Game logic should go here

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
    front_scroller.draw_sidewalk(screen)
    front_scroller.move_sidewalk()
    
    all_sprites_list.draw(screen)

    #sprite1.rect.x = 50
    #sprite1.rect.y = 500

    sprite2.rect.x = 30
    sprite2.rect.y = 500

    sun_sprite.rect.x = 30
    sun_sprite.rect.y = 600

    baby_sprite.rect.x = 700
    baby_sprite.rect.y = 500

    germ_sprite.rect.x = 220
    germ_sprite.rect.y = 500

    troll_sprite.rect.x =500
    troll_sprite.rect.y = 500

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE

