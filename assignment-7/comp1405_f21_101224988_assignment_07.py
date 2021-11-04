#Vishva Vidun Jayakody, 101224988
import pygame

#initialize pygame
pygame.init()

#ask user for image path
img_path = input('Enter the path of an image: ')
img = pygame.image.load_extended(img_path)

#get dimensions of image and create window with that size
img_dim = img.get_size()
window = pygame.display.set_mode(img_dim)
pygame.display.set_caption('Color Inverter')

#draw image on window
window.blit(img, (0,0))
pygame.display.update()

#loop to repeatedly get input, apply the effect and update display
exit_flag = False
while not exit_flag:

    #check if the (left) mouse button has been pressed
    mouse_press = pygame.mouse.get_pressed()
    if mouse_press[0]:
        
        #clock for fps to slow the loop down
        clock = pygame.time.Clock()
        mouse_pos = pygame.mouse.get_pos() #get position of mouse 
        
        #if the full rectangle can be drawn
        if mouse_pos[0] >= 200 and mouse_pos[1] >= 100:
            area_x = mouse_pos[0] - 200
            area_y = mouse_pos[1] - 100
        #if it's less than the width of the rect, use 0 instead of mouse_pos (can't have -ve pixels)
        elif mouse_pos[0] < 200:
            area_x = 0
            area_y = mouse_pos[1] - 100
        elif mouse_pos[1] < 100:
            area_x = mouse_pos[0] - 200
            area_y = 0
        #top left case, draw rectangle from (0, 0) (also because can't have -ve pixels)
        elif mouse_pos[0] < 200 and mouse_pos[1] < 100:
            mouse_pos[0] = 0
            mouse_pos[1] = 0
            area_x = 0
            area_y = 0
        
        #'draw' the rectangle
        for i in range(area_y, mouse_pos[1]):
            for j in range(area_x, mouse_pos[0]):
                #handling index out of bounds error, can't have -ve pixels
                if i >= 0 and j >= 0:
                    rgb = window.get_at((j, i))
                else:
                    rgb = window.get_at((0, 0))
                window.set_at((j,i), (255-rgb[0], 255-rgb[1], 255-rgb[2]))
        pygame.display.update() #update display
        clock.tick(4) #slowing down the loop

    for e in pygame.event.get(): 
        if e.type == pygame.QUIT:
          exit_flag = True