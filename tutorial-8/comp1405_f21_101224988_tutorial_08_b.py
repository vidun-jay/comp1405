#Vishva Vidun Jayakody, 101224988
import pygame

#initialize pygame
pygame.init()

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

def coordinatesList(window, tile_dimensions, prefix, num, elements):

    coordinates = findIndex(str(num), elements)
    image = pygame.image.load('./images/' + prefix + '_' + str(num) + '.gif')
    # print('./images/' + str(prefix) + '_' + str(num) + '.gif')
    
    for item in coordinates:    
        # print('./images/' + prefix + '_' + str(num) + '.gif')
        if item[0]*tile_dimensions == 0 and item[1]*tile_dimensions == 0:
            window.blit(image, (item[0]*tile_dimensions, item[1]*tile_dimensions))
        else:
            window.blit(image, (item[1]*tile_dimensions, item[0]*tile_dimensions))

def main():

    valid = False
    while valid == False:
        map_location = input("Enter the location of a tiles.conf file: ")
        try:
            map = open(map_location, "r")
            valid = True
        except Exception:
            print("No file found. Try again: ")
            valid = False

    lines = clean(map.readlines())
    
    temp = [i[7:-1] for i in lines[0]]
    prefix = temp[0]
    
    elmnts = []

    for item in lines:
        elmnts.append(item)
    
    elmnts = [x[:-1] for x in elmnts]
    
    for list in elmnts:
        print (list)

    try:
        dim = pygame.image.load('./images/' + prefix + '_0.gif').get_rect().size
    except Exception:
        print("Error: The tile name specified in 'tiles.conf' does not exist in the /images/ directory.")
        exit()
    #sets display dimensions
    window = pygame.display.set_mode((dim[0]*6, dim[1]*8))
    pygame.display.set_caption('Tile Map')

    while True:
        #program close definition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        coordinatesList(window, dim[0], prefix, 0, elmnts)
        coordinatesList(window, dim[0], prefix, 1, elmnts)
        coordinatesList(window, dim[0], prefix, 2, elmnts)
        coordinatesList(window, dim[0], prefix, 3, elmnts)
        coordinatesList(window, dim[0], prefix, 4, elmnts)

        pygame.display.update()

if __name__ == "__main__":
    main()