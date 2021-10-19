#Vishva Vidun Jayakody, 101224988
import pygame
import random
import sys

#gets image path from cli
image_path = sys.argv[0]
# image_path = '/Users/vidunjayakody/Desktop/comp1405/assignment-5/1image.jpeg'

#loads original image from path and gets size of image
image = pygame.image.load_extended(image_path)
img_dim = image.get_size()

#initialize pygame
pygame.init()

#sets display dimensions to 8x original image
window = pygame.display.set_mode((img_dim[0]*8, img_dim[1]*8))
print((img_dim[0]*8))
print((img_dim[1]*8))

#sets background to black
window.fill((0,0,0))

#program close definition
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        exit()

#nested for loop to read every color on original image
for i in range(img_dim[0]):
    for j in range(img_dim[1]):
        color = image.get_at((i, j)) #get the color of every pixel on original image

        #floor divide by 50 to get nice and neat values between 0-5 for rgb valuese
        red = color[0] // 50
        green = color[1] // 50
        blue = color[2] // 50

        #print the appropriate number of points 
        for k in range(red):
            scaled_x = random.randint(i*8, (i+2)*8)
            scaled_y = random.randint(j*8, (j+2)*8)
            pygame.draw.circle(window, (255, 0, 0), (scaled_x, scaled_y), 1)
        for k in range(green):
            scaled_x = random.randint(i*8, (i+2)*8)
            scaled_y = random.randint(j*8, (j+2)*8)                
            pygame.draw.circle(window, (0, 255, 0), (scaled_x, scaled_y), 1)
        for k in range(blue):
            scaled_x = random.randint(i*8, (i+2)*8)
            scaled_y = random.randint(j*8, (j+2)*8)
            pygame.draw.circle(window, (0, 0, 255), (scaled_x, scaled_y), 1)

#exit definitions
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()