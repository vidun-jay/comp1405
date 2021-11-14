#Vishva Vidun Jayanody, 101224988

#create the list
list = []

while True:

    #ask user if they want to add something, remove something, or leave
    choice = input("\nWhat would you like to do?\n1. Add something to the list\n2. Remove the last value from the list\n3. Exit\n\nEnter a number: ")

    #only accept integer
    try:
        choice = int(choice)
    except ValueError:
        print("\nPlease enter either 1, 2, or 3")
        continue

    if int(choice) == 1:
        append = input("What word would you like to add? ")
        list.append(append) #add string to list
    elif int(choice) == 2:
        list.pop() #remove latest item from list
    elif int(choice) == 3:
        exit() #exit condition
    elif int(choice) != 1 or int(choice) != 2 or int(choice) != 3:
        print("\nPlease enter either 1, 2, or 3")
        continue
    
    print("\nYour updated list contains:", list)