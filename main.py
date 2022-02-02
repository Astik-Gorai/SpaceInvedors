# import pygame library

import pygame
from pygame.locals import *
import random
import math
from pygame import mixer

# initialize the pygame

pygame.init ()
# adding background
background = pygame.image.load ( "background.jpg" )
 # background music
mixer.music.load("background.wav")
mixer.music.play(-1)
# Set icon and name of our game window

pygame.display.set_caption ( "Space Invader" )
icon = pygame.image.load ( "ufo.png" )
pygame.display.set_icon ( icon )

# creating window in pygame

screen = pygame.display.set_mode ( (900, 600) )
# Adding player
rocket = pygame.image.load ( "rocket.png" )
rx, ry = 210, 500
rx_change = 0
ry_change = 0



alien = pygame.image.load("alien3.png")
alienX = random.randint(0,760)
alienY = random.randint(50,450)
alienX_change = 0.4
alienY_change = 20
# Adding Bullets
# ready State:  we cant see the bullet
# fire State: The bullet is moving in upwards direction

bullet = pygame.image.load ( "bullet.png" )
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

# score
score = 0
font =pygame.font.Font('freesansbold.ttf', 32)
testX = 10
testY = 10
over_font =pygame.font.Font('freesansbold.ttf', 96)
def show_score(x, y, score):
    score = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score, (x, y))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit ( bullet, (x + 16, y + 10) )


def Rocket(x, y):
    screen.blit ( rocket, (x, y) )


def Alien():
    screen.blit ( alien, (alienX,alienY) )


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt ( (math.pow ( (alienX - bulletX), 2 )) + math.pow ( (alienY - bulletY), 2 ) )
    if distance <= 40:
        return True
    return False
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Game Loop
running = True
while running:
    # rx+=0.2
    screen.fill ( (44, 89, 23) )
    screen.blit ( background, (0, 0) )
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            running = False
            #  pass
        # if keystroke is pressed check is it left or right
        if event.type == pygame.KEYDOWN:  # keydown is for releasing the keystroke
            if event.key == pygame.K_LEFT:
                # print ( "left arrow is pressed" )
                rx_change -= 0.8
            if event.key == pygame.K_RIGHT:
                # print ( "right arrow is pressed" )
                rx_change += 0.8
            if event.key == pygame.K_SPACE:
                # bullet sound
                bullet_Sound = mixer.Sound( "laser.wav" )
                bullet_Sound.play ()
                bulletX = rx
                bullet_fire ( bulletX, bulletY )
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rx_change = 0
        # if event.type == pygame.KEYDOWN:
        #     screen.fill((77,89,45))
        #     pygame.display.update()
    # outside the for loop
    rx += rx_change
    ry += ry_change
    if rx <= 0:
        rx = 0
    elif rx >= 836:
        rx = 836
    # for i in range(no_of_elien):
    # movement of the alien
    # Game Over
    if alienY >450:
        alienY= 1200
        game_over_text()
    alienX += alienX_change
    if alienX <= 0:
        alienX_change = 0.3
        alienY += alienY_change
    elif alienX >= 830:
        alienX_change = -0.3
        alienY += alienY_change
    collision = isCollision ( alienX, alienY, bulletX, bulletY  )
    if collision:
        # collision sound
        collision_sound = mixer.Sound("explosion.wav")
        collision_sound.play()
        bulletY = 500
        score += 1
        bullet_state = "ready"
        alienX = random.randint ( 0, 836 )
        alienY = random.randint ( 50, 200)
    Alien()
    show_score ( testX, testY,score )
    # for creating multiple bullets

    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    # collision

    if bullet_state == "fire":
        bullet_fire ( bulletX, bulletY )
        bulletY -= bulletY_change
    Rocket ( rx, ry )

    pygame.display.update ()
