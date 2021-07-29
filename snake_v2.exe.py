import pygame
import time
#creation of variables, pygame, and functions
import random
from pygame.locals import *
piclock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((600,600))
blue=(244,0,132)
grey=(100,100,100)
x=300
y=300
cookies=pygame.image.load("cookies.png")
cookies=pygame.transform.rotozoom(cookies,0,0.21)

score=0
black=(0,0,0)
RIGHT=0
LEFT=0
UP=0
DOWN=0
rand1=random.randint(1,39)*15
rand2=random.randint(1,39)*15
width=15
length=15
snakelist=[[x,y]]
entrypoint=0
scoreposition=(40,40)
textposition=(200,60)
text='get to 15 points for milk and cookies'
def show_text(text,position):

    fontobj= pygame.font.SysFont('freesans',30)
    msgobj = fontobj.render(str(text),False,blue)
    screen.blit(msgobj,position)
while True:
    
    snakelist.insert(0,[x,y])
    snakelist.pop()
    screen.fill(black)
    #portals+grid lines
    pygame.draw.rect(screen,grey,(240,345,15,15))
    pygame.draw.rect(screen,grey,(135,375,15,15))

    if x== 240 and y==345:
        x=135
        y=375
      
    elif x==135  and y==375:
        x=240
        y=345
 
#grid lines and 48 lines separated ny ten pixels each
    for linex in range(0,600,15):
        pygame.draw.line(screen, grey,(linex,600),(linex,0))
    for liney in range(0,600,15):
        pygame.draw.line(screen, grey,(0,liney),(600,liney))
  #allows snake to be drawn      
    for s in snakelist:
        pygame.draw.rect(screen,blue,s+[15,15],0)
    piclock.tick(12)
    #Allows smooth motion for the snake
    if UP == 1:
        y=y-15
    if DOWN==1:
        y=y+15
    if RIGHT==1:
        x=x+15
    if LEFT==1:
        x=x-15
        #makes the food in a random position
    pygame.draw.rect(screen,blue,(rand1,rand2,15,15),0)
    for event in pygame.event.get():
       #allows snake to move with arrow keys
        if event.type==KEYDOWN:
            if event.key==K_UP:
                UP=1
                LEFT=RIGHT=DOWN=0
            if event.key==K_DOWN:
                DOWN=1
                LEFT=RIGHT=UP=0
            if event.key==K_RIGHT:
                LEFT=DOWN=UP=0
                RIGHT=1
            if event.key==K_LEFT:
                RIGHT=UP=DOWN=0
                LEFT=1
            # to quit the game
        if event.type==QUIT:
            pygame.quit()
            exit()
            #Allows teleportation on the side walls
    if x>585:
        x=0
    if x<0:
        x=585
    if y<0:
        y=585
    if y>585:
        y=0
        # Allows snake to eat the food and teleport the food into another random location
    show_text(score,scoreposition)
    show_text(text,textposition)
    if (x,y) ==(rand1,rand2):
        rand1=random.randint(1,39)*15
        rand2=random.randint(1,39)*15
        #adds new coordinates to the list that makes the snake grow
        snakelist.append([x,y])
        str(score)
        score=score+1
    if score== 15:
        screen.blit(cookies,(0,0))
        time.sleep(5)
        score=0
    pygame.display.update()

        
        
    pygame.display.update()
