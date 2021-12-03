#Vishva Vidun Jayakody, 101224988
import random


def isSorted(list):
    length = len(list)

    #check if the value of every item in list is the last one plus one    
    for i in range(0, length-1):
        if list[i] > list[i+1]:
            return False
        else:
            pass
    return True           

#shuffle function
def shuffleList(list):
    length = len(list)

    for i in range (0, length):
        shuffled_index = random.randint(0, length-1)
        list[i], list[shuffled_index] = list[shuffled_index], list[i]

#bogosort
def bogoSort(list):
     
    while isSorted(list) == False:
         shuffleList(list)
    return list

#bozosort
def bozoSort(list):

    length = len(list)

    while isSorted(list) == False:
        #take two random indexes, and swap them
        index1 = random.randint(0, length-1)
        index2 = random.randint(0, length-1)
        list[index1], list[index2] = list[index2], list[index1]

        print(list)
    
    return list

def main():
    list = [3, 2, 1, 6, 100, 1, 4, 7, 9]
    print("\nOriginal list:", list)
    print('Sorted using Bogo Sort:', bogoSort(list))
    print('Sorted list Bozo Sort:', bozoSort(list), '\n')

if __name__ == "__main__":
    main()