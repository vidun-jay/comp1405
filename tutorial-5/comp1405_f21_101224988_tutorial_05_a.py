#Vishva Vidun Jayanody, 101224988

#function that checks if number is prime
def isPrime(num):
    isPrime = False
    #1 is not prime, so start from 1+
    if num > 1:
        #counter-controlled for loop to determine if a number is prime or not
        for i in range(2, num):
            if (num % i) == 0:
                isPrime = False
                break
            else:
                isPrime = True
    else:
        isPrime = False
    return isPrime

#main function
def main():
    repeat = True
    while repeat == True:
        user_num = int(input("\nEnter a number and find out if it's prime: "))
        print(isPrime(user_num))
        
        #give user option to quit
        repeat_prompt = input("Would you like to ask again? (y/n)? ")
        if repeat_prompt.lower() == "y":
            pass
        else:
            repeat = False

if __name__ == "__main__":
    main()