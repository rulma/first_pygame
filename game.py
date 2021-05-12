import pygame
import os

#important var, screen size, title, fps and ship vel
WIDTH , HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SUPER BETA!")

#create border to seperate player sides
BORDER = pygame.Rect(WIDTH/2 - 20, 0, 10, HEIGHT)

#locked refresh rate
FPS = 60

#set velocity for ship movement
VEL = 5

#game bg color
BG = (250,150,200)
BLACK = (0,0,0)
#Set default ship size
SHIP_HEIGHT = 60
SHIP_WIDTH = 40

#get file path for yellow spaceship asset
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_blue.png"))
#rotate and resize
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH + 30, SHIP_HEIGHT + 30)), 90)

#get file path for red spaceship asset
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
#rotate and resize
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT )),90)

#updates and draw screen
def draw_window (red, yellow):
    WIN.fill(BG)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    #WIN.draw.text("HI-SCORE", 20,20)
    pygame.display.update()



#Handle User 2 input for ship
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x + VEL > BORDER.x: #LEFT P1 
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < WIDTH - 25:a #RIGHT P1 
        yellow.x += VEL 
    if keys_pressed[pygame.K_UP]and yellow.y - VEL > -10: #UP P1 dd
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT : #DOWN P1 
         yellow.y += VEL

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

#Main Program
def main():
    red = pygame.Rect(100,300,SHIP_WIDTH, SHIP_HEIGHT)
    yellow = pygame.Rect(700,300,SHIP_WIDTH, SHIP_HEIGHT)
    


    run = True
    clock = pygame.time.Clock()


#while user is playing run through this 60 times per second
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            #check if user quit
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)



        draw_window(red, yellow)
        

    pygame.quit()

if __name__ == "__main__":
    main()
