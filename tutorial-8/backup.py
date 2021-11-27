#Vishva Vidun Jayakody, 101224988
import pygame
#initialize pygame
pygame.init()
#sets display dimensions
window = pygame.display.set_mode((64*6, 64*8))
#sets background to white
window.fill((255,255,255))
pygame.display.set_caption('Tile Map')

def clean(lines):
    new_list = []

    for i in lines:
        i = i.split(',')
        new_list.append(i)

    return new_list

def findIndex(element, matrix):
    coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                coordinates.append((i, j))
    
    return coordinates

def drawTile(coordinates, file_num):

    image = pygame.image.load('/Users/vidunjayakody/Desktop/comp1405/tutorial-8/images/desert_'+ str(file_num) + '.gif')
    window.blit(image, coordinates)

def main():

    map = open("tiles.map", "r")

    lines = clean(map.readlines())
    elmnts = []

    for item in lines:
        elmnts.append(item)
    
    elmnts = [x[:-1] for x in elmnts]
    
    for list in elmnts:
        print (list)

    for list in elmnts:
        for item in list:
            if item == '0':
                drawTile((0, 0), 0)
            # elif item == '1':
            #     drawTile((0, 0), 1)
            # elif item == '2':
            #     drawTile((0, 0), 2)
            # elif item == '3':
            #     drawTile((0, 0), 3)
            # elif item == '4':
            #     drawTile((0, 0), 1)

    while True:
        #program close definition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
       

        pygame.display.update()


if __name__ == "__main__":
    main()