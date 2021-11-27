#Vishva Vidun Jayakody, 101224988
import pygame
#initialize pygame
pygame.init()
#sets display dimensions
window = pygame.display.set_mode((64*6, 64*8))
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
                coordinates.append((i-2, j))
    
    return coordinates

def drawTile(coordinates, file_num):

    image = pygame.image.load('./images/desert_'+ str(file_num) + '.gif')
    window.blit(image, coordinates)

def coordinatesList(num, elements):

    coordinates = findIndex(str(num), elements)
    for item in coordinates:
        if item[0]*64 == 0 and item[1]*64 == 0:
            drawTile((item[0]*64, item[1]*64), num)
        else:
            drawTile((item[1]*64, item[0]*64), num)

def main():   

    valid = False
    while valid == False:
        map_location = input("Enter the location of a .map file: ")
        try:
            map = open(map_location, "r")
            valid = True
        except Exception:
            print("No file found. Try again: ")
            valid = False

    lines = clean(map.readlines())
    elmnts = []

    for item in lines:
        elmnts.append(item)
    
    elmnts = [x[:-1] for x in elmnts]
    
    for list in elmnts:
        print (list)

    while True:
        #sets background to white
        window.fill((255,255,255))
        #program close definition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        coordinatesList(0, elmnts)
        coordinatesList(1, elmnts)
        coordinatesList(2, elmnts)
        coordinatesList(3, elmnts)
        coordinatesList(4, elmnts)

        pygame.display.update()

if __name__ == "__main__":
    main()