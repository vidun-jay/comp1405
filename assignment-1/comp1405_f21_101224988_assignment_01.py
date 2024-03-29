#Vishva Vidun Jayakody, 101224988
import pygame

#initialize pygame
pygame.init()

#sets display dimensions
window = pygame.display.set_mode((480, 640))

#sets background to white
window.fill((255,255,255))

#while loop to prevent pygame from instantly closing
while True:
    #program close definition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #draw blue polygon
    pygame.draw.polygon(window, (79,90,150), [
        [250, 100],
        [325, 0],
        [400, 100],
        [400, 230],
        [320,100]], 0)

    #draw green polygon
    pygame.draw.polygon(window, (56,146,44), [
        [320, 430],
        [400, 430],
        [400, 530],
        [300, 690],
        [150, 690],
        [150, 530],
        [320, 530]], 0)

    #outputs the file to working directory
    pygame.image.save( window, 'assigned_image_for_101224988.png')

    #closes app after 1 second
    pygame.display.update()
    pygame.time.wait(1000)
    pygame.quit()