import pygame
from fighter import Fighter

pygame.init()

#create game window 
SCREEN_WIDTH = 1000
SCREEM_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEM_HEIGHT))
pygame.display.set_caption("Brawler")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [122, 105]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#load background image
bg_image = pygame.image.load("Assets/images/background/background.jpg").convert_alpha()

#load health bar icon
hb_icon = pygame.image.load("Assets/images/icons/health_bar.png").convert_alpha()

#load spritesheets
warrior_sheet = pygame.image.load("Assets/images/warrior/sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("Assets/images/wizard/sprites/wizard.png").convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

#function for drawing backround
def draw_bg():
    scale_bg = pygame.transform.scale(bg_image, (1000, 600))
    screen.blit(scale_bg, (0, 0))

#function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, RED, (x, y, 290, 40))
    pygame.draw.rect(screen, YELLOW, (x, y, 290 * ratio, 40))

#sunction for drawing health bar icons
def draw_hb():
    scale_hb = pygame.transform.scale(hb_icon, (400, 300))
    screen.blit(scale_hb, (30, -85))
    screen.blit(scale_hb, (570, -85))

#create two instances of fighters
fighter_1 = Fighter(200, 370, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS)
fighter_2 = Fighter(700, 370, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)

#game loop
run = True
while run:
    
    clock.tick(FPS)
    
    #draw backround
    draw_bg()
    
    
    #show player stats
    draw_health_bar(fighter_1.health, 100, 31)
    draw_health_bar(fighter_2.health, 640, 31)
    draw_hb()
    
    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEM_HEIGHT, screen, fighter_2)
    
    #update fighters
    fighter_1.update()
    fighter_2.update()
    
    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
   
   
    #update display
    pygame.display.update()
            
            
#exit pygame
pygame.quit()