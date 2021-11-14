#Vishva Vidun Jayanody, 101224988
import random

#function to check whether input is an integer
def isInt(x):
    try:
        x = int(x)
        return True
    except ValueError:
        return False

#replace function, takes list, original item in set, and new string as inputs
def replace(list, original, replaced):
    for i in range (len(list)):
        if list[i] == int(original):
            list[i] = replaced

#frequency of string, takes list and keyword as input and returns final count
def count(list, word):
    count = 0
    for i in range(len(list)):
        if list[i] == word:
            count += 1
    return count

def main():
    #ask the user for a list size and only positive integers
    while True:
        list = []
        n = input("\nEnter an integer: ")
        if isInt(n) and int(n) > 0:

            #populate list
            for i in range(int(n)):
                list.append(random.randint(0, 5))

            print("Your list has the following", n, "items:", list, "\n")
            break
        
        else:
            print("Invalid integer detected. Please try again.")
            continue

    while True: #event controlled loop
        original = input("Enter a integer to replace: ")

        #if the integer they select is actually in the list, keep going
        if isInt(original) and int(original) in list:
            new_value = input("What would you like to replace "+str(original)+" with? ")
            replace(list, original, new_value) #counter controlled loop
            break #exit node
        #if the integer they select is not in the list, tell the user and prompt again
        else:
            print('It looks like "'+str(original)+'" is not in the list. Try again.\n')
            continue

    print("\nYour updated list contains: ", list)
    keyword = input("\nEnter a String to search for: ")
    print('\nYour list contains "' + keyword + '"', count(list, keyword), "times.")

if __name__ == "__main__":
    main()