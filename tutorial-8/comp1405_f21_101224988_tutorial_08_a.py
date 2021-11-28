#Vishva Vidun Jayakody, 101224988
import random

def rowGenerator(length):
    row = [str(random.randint(0,4)) for i in range(length)]
    return ','.join(row)

def main():
    tile_map = []
    tile_map_txt = open("tiles.conf", "w")

    prefix = input("Tiles: ")
    
    tile_map_txt.write("tiles: " + prefix + "\n\n")

    for i in range (8):
        tile_map_txt.write((str(rowGenerator(6)) + ",\n"))
    print("Configuration file created!")
    tile_map_txt.close()

if __name__ == "__main__":
    main()