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
envelope_sprite_list = pygame.sprite.Group()
sb_list = pygame.sprite.Group()

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


    def changesize(self, width, height):
        center = self.rect.center
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = center

    def playerjump(self):
        if (pygame.key.get_pressed()[pygame.K_SPACE] == 1):
            self.rect.y = 250
        if (pygame.key.get_pressed()[pygame.K_SPACE] == 0 and self.rect.y != 450):
            self.rect.y = 400
            
    def update(self):
        self.rect.x -= 3
        if self.rect.center[0] < -15:
            self.rect.x = SCREEN_WIDTH + 10
            self.kill()
    
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
        envelope_sprite_list.add(envelope_sprite)

def end():
    good_sprites_list.empty()
    all_sprites_list.empty()
    bad_sprites_list.empty()
    envelope_sprite_list.empty()


lives = 3
points = 0
tipnumber = 0

sprite1 = girlSprite("girlstop.png", "rungirl.png")
baby_sprite = girlSprite("baby1.png", "baby1.png")
scoreboard_sprite = girlSprite("scoreboard.png", "scoreflash.png")

all_sprites_list.add(sprite1)
all_sprites_list.add(baby_sprite)
sb_list.add(scoreboard_sprite)

scoreboard_sprite.rect.x = 600
scoreboard_sprite.rect.y = 150

sprite1.rect.x = 30
sprite1.rect.y = 450

baby_sprite.rect.x = 700
baby_sprite.rect.y = 450


while not done:   
   # --- Main event loop
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and restart:
                lives = 3
                points = 0
                makeup()
                restart = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g and over:
                pygame.quit()
                exit() 
                
    sprite1.playerjump()    
    bad_sprites_list.update()
    sprite1.animate()
    scoreboard_sprite.animate()
    good_sprites_list.update()
    sprite1.changesize(150, 150)
    scoreboard_sprite.changesize(300, 300)
    baby_sprite.changesize(150, 150)
    envelope_sprite_list.update()


    bad_sprites_hit_list = pygame.sprite.spritecollide(sprite1, bad_sprites_list, True)
    good_sprites_hit_list = pygame.sprite.spritecollide(sprite1, good_sprites_list, True)
    envelope_sprites_hit_list = pygame.sprite.spritecollide(sprite1, envelope_sprite_list, True)

    
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
    sb_list.draw(screen)

    mom_code_tips = ["Figuring out what your baby is upset about is major guessing game(no pun intended).",
     "After having to guess if they are hunger,messy, or just want some attention another factor could be that your baby is gassy.",
     "When coming out of the womb babies are born with the Moro, or startle,reflex.",
     "If your baby's private parts are a bit bigger than usual it might be due to swelling caused by pressure exerted on your baby during birth.",
     "If your baby seems hungry all the time it’s due to your baby’s growing appetite.",
     "Babies who are breastfed tend to be more hungry than babies who are not.",
     "Breast milk is more quickly digested and more completely absorbed than formula.",
     "Skin-to-skin contact with your baby allows you and your baby to build a stronger bond.",
     "When making eye contact with your baby it will allow your baby to recognize your face and starts to build their memory.",
     "While many may think honey would be a good thing to feed to your newborn it is actually contains a bacteria that can germinate in a baby’s developing digestive system.",
     "Save yourself from the despair of buying a changing table it becomes virtually useless when your baby has to be changed outside the house.",
     "Changing pads are more efficient than changing tables because you can take them everywhere.", 
     "Wipe warmers are also something you can refrain from buying because they tend to dry out wipes faster.",
     "Stay away from expensive diaper bags because most bags don’t have baby friendly features.",
     "Your baby’s flaky skin could be caused by its layer of vernix being rubbed away and drying out when they are exposed to air.",
     "If your baby experiences excessive sneezing it’s due to your baby clearing their nasal and respiratory passages of congestion and airborne particles.",
     "If you seen your newborn has irregular breathing it’s because they are it normal for them to take slight pauses and then go through periods of rapid breathing.",
     "Touching your baby’s soft spot is not a big deal you’re not touching their brain but a thick protective  membrane.",
     "Babies  who are fed formula have less-frequent bowel movements which causes them to poop less."]

    length = len(mom_code_tips)
    random_number = random.randint(0, length -1)
    #(mom_code_tip0 [random_number])

    font1 = mom_code_tips.pygame.font.Font(None, 50)

    score = font.render("Lives: "+ str(lives), True, BLACK)
    screen.blit(score, [600, 150])

    tips = font.render( "Score: " + str(points), True, BLACK)
    screen.blit(tips, [600, 200])  
    
    ln_ = mom_code_tips[tipnumber]
    

    if bad_sprites_hit_list:
        lives -= 1
        
    if lives < 1:
        end()
        game_over = font.render("Game Over", True, RED)
        screen.blit(game_over, [300, 200])
        try_again = font.render("Play Again and Press A", True, RED)
        screen.blit(try_again, [200, 300])
        restart = True
        endit = font.render("End Game and Press G", True, RED)
        screen.blit(endit, [200, 400])
        over = True 
        tip_it = font.render(ln_, True, BLACK)
        screen.blit(tip_it, [100, 500])
        
        
        
    if envelope_sprites_hit_list:
        points += 1
        tipnumber += 1


        



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE

