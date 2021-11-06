#Vishva Vidun Jayanody, 101224988
import random
import time

#get the users choice
def user_turn():

    #only accept integers 1-3 as valid inputs
    while True:
        user_hand = input("\nWhat would you like to play?\n1. Rock\n2. Paper\n3. Scissors\nEnter a number: ")
        try:
            if int(user_hand) == 1 or int(user_hand) == 2 or int(user_hand) == 3:

                if int(user_hand) == 1:
                    return 0
                elif int(user_hand) == 2:
                    return 1
                elif int(user_hand) == 3:
                    return 2
            else:
                print("\nInvalid input, please enter either 1, 2 or 3.")
                continue
        except ValueError:
            print("\nInvalid input, please enter either 1, 2 or 3.")

#get the CPUs choice
def cpu_turn():
    cpu_hand = random.randint(1, 3)

    if cpu_hand == 1:
        return 0
    elif cpu_hand == 2:
        return 1
    elif cpu_hand == 3:
        return 2

#function that maps numerical values to strings
def map(player):
    if player == 0:
        player = 'rock' 
    elif player == 1:
        player = 'paper'
    elif player == 2:
        player = 'scissors'
    return player

#determine winner based on minimum distance
def winner(user, cpu):

    minimum_distance = (cpu - user) % 3

    if minimum_distance == 0:
        print(f'\nYou play {map(user)} and CPU also plays {map(cpu)}. The game is a tie!\n')
    elif minimum_distance == 1:
        print(f'\nYou play {map(user)} but CPU plays {map(cpu)}. You lose.\n')
    elif minimum_distance == 2:
        print(f'\nYou play {map(user)} and CPU plays {map(cpu)}. You win!\n')

#main function
def main():

    #keep running as long as user selects yes to rematch
    rematch = True
    while rematch == True:
        print("Rock...")
        time.sleep(0.4)
        print("Paper...")
        time.sleep(0.4)
        print("Scissors...")
        time.sleep(0.4)
        print("Shoot!")

        user = user_turn()
        cpu = cpu_turn()
        winner(user, cpu)

        yes_no = input("Rematch? (y/n): ")
        if yes_no.lower() == "y":
            rematch = True
        else:
            rematch = False

if __name__ == "__main__":
    main()