#Vishva Vidun Jayakody, 101224988
import pygame
import math

#pi value for radians values
pi = math.pi

#initialize pygame
pygame.init()

#sets display dimensions
window = pygame.display.set_mode((600, 600))

#sets background to red
window.fill((170,76,49))

while True:
    #program close definition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    #blue segment
    pygame.draw.arc(window, (67,129,183), [150,150,300,300], (3*pi)/2, (pi/2)+0.01, 50)
    #white segment
    pygame.draw.arc(window, (221,212,200), [150,150,300,300], pi/2, (3*pi/2)+0.01, 50)
    #yellow segment
    pygame.draw.arc(window, (227,180,85), [200,200,200,200], (3*pi)/2, (pi/2)+0.009, 50)
    #pink segment
    pygame.draw.arc(window, (227,166,151), [250,250,100,100], (3*pi)/2, (pi/2)+0.009, 50)
    #black segment
    pygame.draw.arc(window, (30,30,30), [200,200,200,200], pi/2, (3*pi/2)+0.01, 100)

    pygame.display.update()