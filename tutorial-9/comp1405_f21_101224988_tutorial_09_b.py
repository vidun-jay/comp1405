#Vishva Vidun Jayakody, 101224988
import random
import time

#function to determine if a list is sorted or not
def isSorted(list):
    length = len(list)
    
    for i in range(0, length-1):
        if list[i] > list[i+1]:
            return False
        else:
            pass
    return True           

#shuffle method
def shuffleList(list):
    length = len(list)

    for i in range (0, length):
        shuffled_index = random.randint(0, length-1)
        list[i], list[shuffled_index] = list[shuffled_index], list[i]

#bogo sort
def bogoSort(list):
     
    while isSorted(list) == False:
         shuffleList(list)
    return list

#bozo sort
def bozoSort(list):

    length = len(list)

    while isSorted(list) == False:
        index1 = random.randint(0, length-1)
        index2 = random.randint(0, length-1)
        list[index1], list[index2] = list[index2], list[index1]

        print(list)
    
    return list

#function to find average given a list
def average(values):
    sum = 0
    for i in values:
        sum += i
    return (sum/len(values))

def main():

    #seperate lists for the scores (to calculate average later)
    bogo_scores = []
    bozo_scores = []
    matrix = []

    #counter controlled loop to increase size of random list generated
    for i in range (5):
        # generate random list
        list = [random.randint(1, 5) for i in range(i+1)]
        original = list.copy()
        matrix.append(list)
        # print (matrix)
        print("\nOriginal list:", original)
        print("Sorted list: ", bogoSort(list))

        bogo_scores = []

        #counter controlled loop for multiple trials (bogo)
        for i in range (5):
            start = time.time()
            bogoSort(list)
            end = time.time()
            score = end - start
            bogo_scores.append(score)

        #counter controlled loop for multiple trials (bozo)
        for i in range (5):
            start = time.time()
            bozoSort(list)
            end = time.time()
            score = end - start
            bozo_scores.append(score)

        #output average results
        print(f"BogoSort sorted in: {average(bogo_scores)} seconds on average.")
        print(f"BozoSort sorted in: {average(bozo_scores)} seconds on average.\n")
        
if __name__ == "__main__":
    main()