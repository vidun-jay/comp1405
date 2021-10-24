#Vishva Vidun Jayakody, 101224988
import random

#generate pseudorandom number between 1-100 inclusive
num = random.randint(1, 100)

count = 0 #initiate the counter to 0
#post-condition loop
while (count < 10): #only allow 10 tries
    #ask user for their guess
    guess = int(input('What is your guess? '))

    #provide feedback and increase count if not on last chance
    if(guess > num and count != 9):
        print('Incorrect. Try a lower number.')
        count += 1
    #provide feedback and increase count if not on last chance
    elif(num > guess and count != 9):
        print('Incorrect. Try a higher number.')
        count += 1
    #if guess is generated number, tell player they won the game and end game
    elif(num == guess):
        print("You won! The number was", str(num))
        break #exit condition 1: terminate if guess is right
    #if player is on last guess and get it wrong, tell them they lost and end game
    elif(count == 9 and num != guess):
        print('You lost. Better luck next time!')
        break #exit condition 2: terminate if 10 guesses are up (and guess is not right)