#Vishva Vidun Jayakody, 101224988
import pygame

#initialize pygame
pygame.init()

#takes in an array of lines, removes ","s, and outputs a list of characters in config file
def clean(lines):
    new_list = []

    for i in lines:
        i = i.split(',')
        new_list.append(i)

    return new_list

#returns a list of all indices in which a element appears in a given matrix
def findIndex(element, matrix):
    coordinates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                coordinates.append((i-2, j))
    
    return coordinates

#function to draw the tiles to their respective coordinates using pygame
def drawTiles(window, tile_dimensions, prefix, num, elements):

    coordinates = findIndex(str(num), elements)
    image = pygame.image.load('./images/' + prefix + '_' + str(num) + '.gif')
    
    for item in coordinates:    
        if item[0]*tile_dimensions == 0 and item[1]*tile_dimensions == 0:
            window.blit(image, (item[0]*tile_dimensions, item[1]*tile_dimensions))
        else:
            window.blit(image, (item[1]*tile_dimensions, item[0]*tile_dimensions))

def main():

    #prompt the user for a map file, repeat until valid one is given
    valid = False
    while valid == False:
        map_location = input("Enter the location of a tiles.conf file: ")
        try:
            map = open(map_location, "r")
            valid = True
        except Exception:
            print("No file found. Try again: ")
            valid = False

    #reads every line of tiles.conf file, calls clean() to turn it into a neat list of characters
    lines = clean(map.readlines())
    print(lines)
    
    #list comprehension to only take the "desert" from "tiles: desert"
    temp = [i[7:-1] for i in lines[0]]
    prefix = temp[0]
    
    elmnts = []

    #adds all the characters to a list of lists by line
    for item in lines:
        elmnts.append(item)
    
    #remove "\n" from every line
    elmnts = [x[:-1] for x in elmnts]
    
    #output what the matrix looks like
    for list in elmnts:
        print (list)

    #if the name in tiles.conf specifies a file name that isn't in the /images/ folder, clean exit
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

        #draw every tile in it's respective coordinate
        drawTiles(window, dim[0], prefix, 0, elmnts)
        drawTiles(window, dim[0], prefix, 1, elmnts)
        drawTiles(window, dim[0], prefix, 2, elmnts)
        drawTiles(window, dim[0], prefix, 3, elmnts)
        drawTiles(window, dim[0], prefix, 4, elmnts)

        pygame.display.update()

if __name__ == "__main__":
    main()
