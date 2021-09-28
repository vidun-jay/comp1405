#Vishva Vidun Jayakody, 101224988
import sys

"""
Take the command line argument, divide it by 3 
and round the result down, add it to the integer that 
is one more than itself, subtract 3 from it, add the return 
value from the input function call to it, multiply it by 7.181918, 
convert it to an integer, and finally convert it to a character.
"""

input = int(input("Enter a number: "))

cmd_line_arg = int(sys.argv[1])

#divide by 3 and round result down
running_total = cmd_line_arg // 3

#add it to the integer that is one more than itself
running_total = running_total + (cmd_line_arg + 1)

#subtract 3
running_total -= 3

#add the return value from input function call
running_total += input

#multiply it by 7.181918
running_total = running_total * 7.181918

#convert it to an integer
running_total = int(running_total)

#convert it to a character
running_total = chr(running_total)
print(running_total)