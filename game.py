import pygame
import os

#important var, screen size, title, fps and ship vel
WIDTH , HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SUPER BETA!")
FPS = 60
VEL = 5

#game bg color
BLUE = (0,150,200)

#Set default ship size
SHIP_HEIGHT = 60
SHIP_WIDTH = 40

#get file path for yellow spaceship asset
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
#rotate and resize
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 90)

#get file path for red spaceship asset
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
#rotate and resize
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT )),270)

#updates and draw screen
def draw_window (red, yellow):
    WIN.fill(BLUE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()



#Handle User 2 input for ship
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT]: #LEFT P1 
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT]: #RIGHT P1 
        yellow.x += VEL
    if keys_pressed[pygame.K_UP]: #UP P1 
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN]: #DOWN P1 
         yellow.y += VEL

#Handle User 1 input for ship
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a]: #LEFT P1 
        red.x -= VEL
    if keys_pressed[pygame.K_d]: #RIGHT P1 
        red.x += VEL
    if keys_pressed[pygame.K_w]: #UP P1 
        red.y -= VEL
    if keys_pressed[pygame.K_s]: #DOWN P1 
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
