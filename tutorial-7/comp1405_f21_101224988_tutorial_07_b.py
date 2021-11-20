#Vishva Vidun Jayakody, 101224988

#isValid function from part a)
def isValidMatrix(matrix):
    lengths = list(map(len, matrix))
    first_length = lengths[0]

    for length in lengths:
        if first_length != length:
            isValid = False
        else:
            isValid = True
    
    if isValid:
        for row in matrix:
            for element in row:
                if not isinstance(element, int) and not isinstance(element, float):
                    isValid = False
        if isValid:
            for row in matrix:
                if not isinstance(row, list):
                    isValid = False

    return isValid

def addMatrices(addend1, addend2):

    #if dimensions are the same, compute
    if len(addend1) == len(addend2) and len(addend1[0]) == len(addend2[0]):
        rows = len(addend1)
        columns = len(addend1[0])

        #create a new matrix (of correct size) to store sum values
        sum_matrix = [[0 for i in range(columns)] for j in range(rows)]

        #check if they're both valid matrices
        if isValidMatrix(addend1) and isValidMatrix(addend2):
            #perform matrix addition and add to sum matrix
            for i in range(rows):
                for j in range(columns):
                    sum_matrix[i][j] = addend1[i][j] + addend2[i][j]

        #if not a valid matrix, return empty list
        else:
            sum_matrix = []    

    #if dimensions not the same, return empty list
    else:
        sum_matrix = []
        
    return sum_matrix

def main():
    matrix1 = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]]

    matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    #implement addMatrices function
    sum_matrix = addMatrices(matrix1, matrix2)
    
    #print out the matrix nice and neatly
    if len(sum_matrix) == 0:
        print(sum_matrix)
    else:
        for i in range(len(sum_matrix)):
            print(sum_matrix[i])

if __name__ == "__main__":
    main()