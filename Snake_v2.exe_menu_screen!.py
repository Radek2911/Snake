import pygame
import time
import random
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((600,600))
points1=pygame.image.load("15points.png")
points1=pygame.transform.rotozoom(points1,0,2)
points2=pygame.image.load("30points.png")
points2=pygame.transform.rotozoom(points2,0,2)
while True:
    screen.blit(points1,(20,200))
    screen.blit(points2,(350,200))
    pygame.display.update()
    for event in pygame.event.get():

        if event.type==QUIT:
            pygame.quit()
            exit()
    

