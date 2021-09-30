#Vishva Vidun Jayakody, 101224988

#prompt user for phone number
number = int(input("Enter your seven-digit phone number: "))

#define first 3 and last 4 digits
f3_digits = number // 10000
line_number = number % 10000

#operations
step1 = f3_digits * 80
step2 = (step1 + 1)*250
step3 = step2 + (line_number*2)
step4 = int((step3 - 250) / 2)

#print to console
print("Your prefix is " + str(f3_digits) + ". Multiply this by 80, and the result is: " + str(step1))
print("Add 1 to that result and multiply it by 250, and the result is: " + str(step2))
print("Your line number is " + str(line_number) + ". Add this to the previous result twice, and the result is: " + str(step3))
print("Subtract 250 from that result and divide it by 2, and the result is: " + str(step4))