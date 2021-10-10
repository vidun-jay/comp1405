#Vishva Vidun Jayakody, 101224988
import sys

#defining cli arguments to letters and setting 'True' case
a = int(sys.argv[1]) == '1'
b = int(sys.argv[2]) == '1'
c = int(sys.argv[3]) == '1'
g = int(sys.argv[7]) == '1'
i = int(sys.argv[9]) == '1'
j = int(sys.argv[10]) == '1'
k = int(sys.argv[11]) == '1'

#first circuit
output1 = (((not b) or a) and c) and (not a)

#second circuit
output2 = ((((not j) or i) or k) and (not g))

#output result to console
print("<" + str(output1) + ">, <" + str(output2) + ">")