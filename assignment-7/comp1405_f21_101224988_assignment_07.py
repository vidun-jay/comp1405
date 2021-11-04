#Vishva Vidun Jayakody, 101224988
import pygame

#initialize pygame
pygame.init()

#ask user for image path
img_path = '/Users/vidunjayakody/Desktop/comp1405/assignment-7/image.jpg'
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

    mouse_press = pygame.mouse.get_pressed()

    if mouse_press[0]:

        mouse_pos = pygame.mouse.get_pos()   
        print(mouse_pos) ### FOR TESTING, REMEMBER TO DELETE ###
        
        if mouse_pos[0] >= 200 and mouse_pos[1] >= 100:
            area_x = mouse_pos[0] - 200
            area_y = mouse_pos[1] - 100

        elif mouse_pos[0] < 200:
            area_x = 0
            area_y = mouse_pos[1] - 100

        elif mouse_pos[1] < 100:
            area_x = mouse_pos[0] - 200
            area_y = 0

        elif mouse_pos[0] < 200 and mouse_pos[1] < 100:
            mouse_pos[0] = 0
            mouse_pos[1] = 0
            area_x = 0
            area_y = 0
        
        for i in range(area_y, mouse_pos[1]):
            for j in range(area_x, mouse_pos[0]):
                if i >= 0 and j >= 0:
                    rgb = window.get_at((j, i))
                else:
                    rgb = window.get_at((0, 0))
                
                window.set_at((j,i), (255-rgb[0], 255-rgb[1], 255-rgb[2]))
        pygame.display.update()

    for e in pygame.event.get(): 
        if e.type == pygame.QUIT:
          exit_flag = True