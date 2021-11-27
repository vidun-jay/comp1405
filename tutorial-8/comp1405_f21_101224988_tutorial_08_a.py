#Vishva Vidun Jayakody, 101224988
import random

def rowGenerator(length):
    row = [str(random.randint(0,4)) for i in range(length)]
    return ','.join(row)

def main():
    tile_map = []
    tile_map_txt = open("tiles.map", "w")

    prefix = input("Tiles: ")
    # prefix = "desert"
    
    if prefix == "desert":
        tile_map_txt.write("tiles: desert\n\n")

        for i in range (8):
            tile_map_txt.write((str(rowGenerator(6)) + ",\n"))

if __name__ == "__main__":
    main()