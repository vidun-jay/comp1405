#Vishva Vidun Jayakody, 101224988
import pygame
import math

#pi value for radians values
pi = math.pi

#initialize pygame
pygame.init()

#sets display dimensions
window = pygame.display.set_mode((600, 600))

#sets background to blue
window.fill((188,221,238))

while True:
    #program close definition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    #head
    pygame.draw.circle(window, (0, 0, 0), (250, 150), 50)

    #torso
    pygame.draw.circle(window, (0, 0, 0), (250, 255), 50)
    pygame.draw.polygon(window, (0,0,0), [
        [300, 255],
        [200, 255],
        [200,400],
        [300,400]], 0)

    #left arm
    pygame.draw.arc(window, (0,0,0), [170,225,150,300], 2*pi/3, pi, 7)
    pygame.draw.circle(window, (0,0,0), (173, 380), 10)

    #right arm
    pygame.draw.arc(window, (0,0,0), [170,165,250,100], 3*pi/2, 0, 7)
    
    #trident
    pygame.draw.line(window, (233,174,1), (420, 45), (420, 430), 5)
    pygame.draw.circle(window, (0,0,0), (420, 215), 10) #hand needs to be over trident
    pygame.draw.arc(window, (233,174,1), [371, 30, 100, 100], pi, 0, 5)

    #left leg
    pygame.draw.arc(window, (0,0,0), [210, 315, 100, 300], 5*pi/6, 7*pi/6, 7)

    #right leg
    pygame.draw.arc(window, (0,0,0), [190, 315, 100, 300], 11*pi/6, pi/6, 7)

    #face
    pygame.draw.arc(window, (188,221,238), [220,85, 100, 100], 4*pi/3, 5*pi/3, 3) #smile
    pygame.draw.circle(window, (188,221,238), (280, 140), 5) #left eye
    pygame.draw.circle(window, (0,0,0), (310, 130), 5) #right eye
    pygame.draw.circle(window, (0,0,0), (300, 160), 10) #nose

    #left foot
    pygame.draw.polygon(window, (0,0,0), [
        [220, 530],
        [180, 555],
        [220, 545],
    ])

    #right foot
    pygame.draw.polygon(window, (0,0,0), [
        [278, 539],
        [278, 550],
        [320, 545],
    ])

    pygame.display.update()