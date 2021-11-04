#Vishva Vidun Jayanody, 101224988

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

def main():
    while True:
        user_num = int(input("\nEnter a number and find out if it's prime: "))
        print(isPrime(user_num))

if __name__ == "__main__":
    main()