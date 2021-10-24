#Vishva Vidun Jayakody, 101224988

#post-condition loop ensuring value is 0-9 exclusive
while True:
    num = int(input("Enter a number between 1-8: "))
    if(num == 0 or num >= 9):
        pass
    else:
        break

#nested counter-controlled loop
for i in range(1, num+1):
    for j in range(1, i+1):
        print(i, end="")
    print("")