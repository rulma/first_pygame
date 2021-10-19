import pygame
import os
pygame.font.init()

#important var, screen size, title, fps and ship vel
WIDTH , HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SUPER BETA! v0.1")

#create border to seperate player sides
BORDER = pygame.Rect(WIDTH//2 - 2, 0, 5, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)


#locked refresh rate
FPS = 60
#arrays to store player lives(deaths) when the array has N indexs the other player wins


#set velocity for ship movement
VEL = 5
#set bullet vel
BULLET_VEL = 7
#set max bhullets on screenm respective to plaery
MAX_BULLLETS = 3



#game bg color, and other color variables
BG = (250,150,200)
BLACK = (0,0,0)  
WHITE = (255, 255, 255)
RED = (255, 0, 100 )

#Set default ship size
SHIP_HEIGHT = 60
SHIP_WIDTH = 40

#create unique events for when yellow or red is hit by a bullet
YELLOW_HIT =pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#get file path for yellow spaceship asset
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_blue.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH + 50, SHIP_HEIGHT + 50)), 90)
Y_LIVES_1 = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH - 10, SHIP_HEIGHT - 10)), 0)
Y_LIVES_2 = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH - 10, SHIP_HEIGHT - 10)), 0)
Y_LIVES_3 = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH - 10, SHIP_HEIGHT - 10)), 0)
#get file path for red spaceship asset
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT )),90)
R_LIVES_1 = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SHIP_WIDTH - 20, SHIP_HEIGHT - 20)), 180)
R_LIVES_2 = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SHIP_WIDTH - 20, SHIP_HEIGHT - 20)), 180)
R_LIVES_3 = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SHIP_WIDTH - 20, SHIP_HEIGHT - 20)), 180)
SPACE = pygame.transform.scale(pygame.image.load
    (os.path.join("Assets", "space.png")),(WIDTH, HEIGHT))




#updates and draw screen
def draw_window (red, yellow,RED_BULLETS,YELLOW_BULLETS, red_health, yellow_health, RED_LIVES, YELLOW_LIVES):
    WIN.blit(SPACE, [0,0])
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health = " + str(red_health), 1 , WHITE)
    yellow_health_text = HEALTH_FONT.render("Health = " + str(yellow_health), 1 , WHITE)

    WIN.blit(red_health_text,( 10, 10))
    WIN.blit(yellow_health_text, (WIDTH - yellow_health_text.get_width() - 10, 10))



    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    if len(YELLOW_LIVES) == 0:
        WIN.blit(Y_LIVES_1,(WIDTH//2,10))
        WIN.blit(Y_LIVES_2,(WIDTH//2 + 20,0))
        WIN.blit(Y_LIVES_3,(WIDTH//2 + 40,10))
    elif len(YELLOW_LIVES) == 1:
        WIN.blit(Y_LIVES_2,(WIDTH//2 + 20,0))
        WIN.blit(Y_LIVES_3, (WIDTH//2 + 40,10))
    elif len(YELLOW_LIVES) == 2:
        WIN.blits(Y_LIVES_3, (WIDTH//2 + 40,10)) 
   
    WIN.blit(R_LIVES_1,(WIDTH//2 - 40,10))
    WIN.blit(R_LIVES_2,(WIDTH//2 - 60,0))
    WIN.blit(R_LIVES_3,(WIDTH//2- 80,10))

    #WIN.draw.text("HI-SCORE", 20,20)
    
    #draw a bullet on screen with its respect vel, position measurements
    for bullet in RED_BULLETS:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in YELLOW_BULLETS:
        pygame.draw.rect(WIN,WHITE,bullet)

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



#counts bullets on screen and detect if the bullet has hit other platyer or travel off screen, assign velocity variable to bullet 
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


#####################TO DO##################

# number of "#" indicate difficulty/ priority of task # = most pressing, #### = reach/far off idea

           # need to add draw animation for explosion of ship and some kind of reset timer in between deaths.
           # would be cool to figure out aniumations wit sprites as well inststead of just overlaying PNGS over rect generated in oygame
           
           ## Work on title page?
           ## User button interface (RESET, HOME, START)

           ### basic AI to play against cpu......(Adjustable dificulty w hi score tracker)
           ### Item/ability spawns, maybe change shot angle or bullet size/speed
           ### track score based off accuracy and shots takem, maybe a grading scale?

           #### ship editor? maybe give template for ship look and have user be able to color and save their ships SUPER REACH GOAL    






        
#Main Program
def main():

    red = pygame.Rect(100,300,SHIP_WIDTH, SHIP_HEIGHT)
    yellow = pygame.Rect(700,300,SHIP_WIDTH, SHIP_HEIGHT)

    red_health = 10 
    yellow_health = 10


    RED_BULLETS = []
    YELLOW_BULLETS = []
    
    RED_LIVES = []
    YELLOW_LIVES = []

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
                    

                #check if user 2 has fired
                if event.key == pygame.K_SPACE and len(RED_BULLETS) < MAX_BULLLETS:

                    bullet = pygame.Rect(
                        red.x + red.width, red.y + red.height//2 - 12, 10, 5)

                    RED_BULLETS.append(bullet)
            
            if event.type == RED_HIT:
                red_health = red_health - 1
    
            if event.type == YELLOW_HIT:
                yellow_health -= 1
    
            if red_health <= 0 and len(RED_LIVES) < 1:
                lives = 1
                RED_LIVES.append(lives)
                red_health = 10
                #Want to have a smaller version of the ships drawn in top corner, when they die remove or grey out ship
                #if len(RED_LIVES) == 3:
                    #winner_txt = "BLUE WINS"
            elif red_health <= 0 and len(RED_LIVES) < 2:
                lives = 1
                RED_LIVES.append(lives)
                red_health = 10

            elif red_health <= 0 and len(RED_LIVES) < 3:
                lives = 1
                RED_LIVES.append(lives)
                red_health = 10
    
            # if yellow_health <= 0:
            #     lives = 1
            #     YELLOW_LIVES.append(lives)
            #     if len(YELLOW_LIVES) == 3:    
            #         winner_txt = "RED WINS!"

                
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(YELLOW_BULLETS,RED_BULLETS,yellow,red)
        draw_window(red, yellow,RED_BULLETS, YELLOW_BULLETS, red_health, yellow_health, RED_LIVES, YELLOW_LIVES)
    pygame.quit()

if __name__ == "__main__":
    main()
