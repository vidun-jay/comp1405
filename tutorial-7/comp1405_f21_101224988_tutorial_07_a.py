#Vishva Vidun Jayakody, 101224988

def isValidMatrix(matrix):
    
    #check if it is rectangular
    lengths = list(map(len, matrix))

    first_length = lengths[0]
    for length in lengths:
        if first_length != length:
            isValid = False
        else:
            isValid = True

    if isValid: #if it passes the rectangle check
        
        #check if all items are numeric
        for row in matrix:
            for element in row:
                if not isinstance(element, int) and not isinstance(element, float):
                    isValid = False
    
        if isValid: #if it passes both tests, check if it's a list of lists
            for row in matrix:
                if not isinstance(row, list):
                    isValid = False

    return isValid

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    print(isValidMatrix(matrix))

if __name__ == "__main__":
    main()