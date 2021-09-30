#Vishva Vidun Jayakody, 101224988
import sys

"""
Take the command line argument, divide it by 3 
and round the result down, add it to the integer that 
is one more than itself, subtract 3 from it, add the return 
value from the input function call to it, multiply it by 7.181918, 
convert it to an integer, and finally convert it to a character.
"""

#prompt user for a  number
input = int(input("Enter a number: "))

#takes first command line argument
cmd_line_arg = int(sys.argv[1])

#divide by 3 and round result down
running_total = cmd_line_arg // 3
print(running_total, "- divide by 3 and round result down")

#add it to the integer that is one more than itself
running_total += running_total + 1
print(running_total, "- add to integer one more than itself")

#subtract 3
running_total -= 3
print(running_total, "- subtract 3")

#add the return value from input function call
running_total += input
print(running_total, "- add input function call")

#multiply it by 7.181918
running_total = running_total * 7.181918
print(running_total, "- multiply it by 7.181918")

#convert it to an integer
running_total = int(running_total)
print(running_total, "- convert to int")

#convert it to a character
running_total = chr(running_total)
print('<' + running_total + '>')