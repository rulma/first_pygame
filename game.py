import pygame
import os

from pygame.constants import K_SPACE

#important var, screen size, title, fps and ship vel
WIDTH , HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SUPER BETA! v0.1")

#create border to seperate player sides
BORDER = pygame.Rect(WIDTH/2 - 20, 0, 10, HEIGHT)

#locked refresh rate
FPS = 60


#set velocity for ship movement
VEL = 5



BULLET_VEL = 7
MAX_BULLLETS = 3

#game bg color
BG = (250,150,200)
#BGPIC = pygame.image.load(os.path.join("Assets","Moon.png"))
BLACK = (0,0,0)
BLUE = (0, 0, 128)
RED = (200, 0, 0 )
#Set default ship size
SHIP_HEIGHT = 60
SHIP_WIDTH = 40


YELLOW_HIT =pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#get file path for yellow spaceship asset
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_blue.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH + 50, SHIP_HEIGHT + 50)), 90)

#get file path for red spaceship asset
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT )),90)

#updates and draw screen
def draw_window (red, yellow,RED_BULLETS,YELLOW_BULLETS):
    WIN.fill(BG)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    #WIN.draw.text("HI-SCORE", 20,20)
    

    for bullet in RED_BULLETS:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in YELLOW_BULLETS:
        pygame.draw.rect(WIN,BLUE,bullet)

    pygame.display.update()

    
#Handle User 1 input for ship
def red_handle_movement(keys_pressed, red): 
    if keys_pressed[pygame.K_a] and red.x - VEL > 0: #LEFT P1 
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x + VEL + red.width < BORDER.x: #RIGHT P1 
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > 0: #UP P1 
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y + VEL + red.height < HEIGHT:  #DOWN P1 
        red.y += VEL



#Handle User 2 input for ship
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x + VEL > BORDER.x: #LEFT P1 
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < WIDTH - 25: #RIGHT P1 
        yellow.x += VEL 
    if keys_pressed[pygame.K_UP]and yellow.y - VEL > -10: #UP P1 dd
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT : #DOWN P1 
         yellow.y += VEL


def handle_bullets(YELLOW_BULLETS, RED_BULLETS, yellow, red):
    for bullet in YELLOW_BULLETS:
        
        bullet.x -= BULLET_VEL
        
        if red.colliderect(bullet):
            YELLOW_BULLETS.remove(bullet)
            pygame.event.post(pygame.event.Event(RED_HIT))

        
        elif bullet.x < 0:
            YELLOW_BULLETS.remove(bullet)
    for bullet in RED_BULLETS:

        bullet.x += BULLET_VEL
        
        if yellow.colliderect(bullet):
            RED_BULLETS.remove(bullet)
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
        
        elif bullet.x > WIDTH:
            RED_BULLETS.remove(bullet)








        
#Main Program
def main():

    red = pygame.Rect(100,300,SHIP_WIDTH, SHIP_HEIGHT)
    yellow = pygame.Rect(700,300,SHIP_WIDTH, SHIP_HEIGHT)
    
    RED_BULLETS = []
    YELLOW_BULLETS = []

    run = True
    clock = pygame.time.Clock()

#while user is playing run through this 60 times per second
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            
            #check if user quit
            if event.type == pygame.QUIT:
                run = False

            
            #Check which keys are being presseed
            if event.type == pygame.KEYDOWN:

                #Check if user 1 has fired
                if event.key == pygame.K_RIGHTBRACKET and len(YELLOW_BULLETS) < MAX_BULLLETS:
                    
                    bullet = pygame.Rect(
                        yellow.x +  10, yellow.y + yellow.height//2 + 10, 10, 5)

                    YELLOW_BULLETS.append(bullet)
                    print(YELLOW_BULLETS)

                #check if user 2 has fired
                if event.key == pygame.K_SPACE and len(RED_BULLETS) < MAX_BULLLETS:

                    bullet = pygame.Rect(
                        red.x + red.width, red.y + red.height//2 - 12, 10, 5)

                    RED_BULLETS.append(bullet)
                    print(RED_BULLETS)
                
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(YELLOW_BULLETS,RED_BULLETS,yellow,red)
        draw_window(red, yellow,RED_BULLETS, YELLOW_BULLETS)
    pygame.quit()

if __name__ == "__main__":
    main()
