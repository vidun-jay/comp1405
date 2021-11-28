#Vishva Vidun Jayakody, 101224988
import random

#function that takes in a length and returns a list of random items of that length seperated by ","
def rowGenerator(length):
    row = [str(random.randint(0,4)) for i in range(length)]
    return ','.join(row)

def main():

    #create configuration file
    tile_map_txt = open("tiles.conf", "w")

    #prompt the user for the prefix
    prefix = input("Tiles: ")
    
    #make the first line the prefix
    tile_map_txt.write("tiles: " + prefix + "\n\n")

    #make a new row for 8 columns (creating the 6x8 grid)
    for i in range (8):
        tile_map_txt.write((str(rowGenerator(6)) + ",\n"))
    
    #inform user of success creating config file
    print("Configuration file created!")
    tile_map_txt.close()

if __name__ == "__main__":
    main()
