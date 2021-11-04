#Vishva Vidun Jayanody, 101224988
import random

#get the users choice
def user_turn():
    user_hand = int(input("\nWhat would you like to play?\n1. Rock\n2. Paper\n3. Scissors\nEnter a number: "))
    
    if user_hand == 1:
        return 0
    elif user_hand == 2:
        return 1
    elif user_hand == 3:
        return 2

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
        print(f'You play {map(user)} and CPU plays {map(cpu)}. The game is a tie!')
    elif minimum_distance == 1:
        print(f'You play {map(user)} but CPU plays {map(cpu)}. You lose.')
    elif minimum_distance == 2:
        print(f'You play {map(user)} and CPU plays {map(cpu)}. You win!')

#main function
def main():
    while True:
        user = user_turn()
        cpu = cpu_turn()
        winner(user, cpu)

if __name__ == "__main__":
    main()