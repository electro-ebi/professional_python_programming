# import required packages

import pygame
import math
import sys

# initialize pygame and create window

pygame.init()
width=1200
height=700
screen_size=(width,height)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption("Ellipse project")
clock=pygame.time.Clock()



while (True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    xradius=500
    yradius=200

    for degree in range(0,360,1):
        x1=int(math.cos(degree*2*(math.pi/360))*xradius)+(width/2)
        y1=int(math.sin(degree*2*(math.pi/360))*yradius)+(height/2)
        # print(degree,x1,y1)

        screen.fill((255,255,255))
        pygame.draw.circle(screen,(255,0,0),[600,350],100)
        pygame.draw.ellipse(screen,(0,0,0),[(((width)-(xradius*2))/2),(((height)-(yradius*2))/2),(xradius*2),(yradius*2)],1)
        pygame.draw.circle(screen,(0,0,255),[x1,y1],40)
        pygame.display.flip()
        clock.tick(50)
