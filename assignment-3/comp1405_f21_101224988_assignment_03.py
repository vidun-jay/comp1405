#Vishva Vidun Jayakody, 101224988
import sys

#defining cli arguments to letters A-L
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])
e = int(sys.argv[5])
f = int(sys.argv[6])
g = int(sys.argv[7])
h = int(sys.argv[8])
i = int(sys.argv[9])
j = int(sys.argv[10])
k = int(sys.argv[11])
l = int(sys.argv[12])

"""
Note: variables are named using the following convention:
c + <circuit number> + <gate type (n, o, a)> + <gate number> + <order from left to right>

ex. circuit 1, not gate 1 = c1n1
"""

# +------------+
# | Circuit #1 |
# +------------+

#First NOT gate
if b == 0: 
    c1n1_output = True #if B is false, make it true
elif b == 1: 
    c1n1_output = False #if B is true, make it false

#First OR gate
if a == 1 or c1n1_output == True: 
    c1o1_output = True #if either A or the previous output is true, output true
else:
    c1o1_output = False #otherwise output false

#First AND gate
if c1o1_output == True and c == 1:
    c1a1_output = True #if both the previous output and C are true, output true
else:
    c1a1_output = False #otherwise output false

#Second NOT gate
if a == 0:
    c1n2_output = True #if A is false, make it true
elif a == 1:
    c1n2_output = False #if A is true, make it false

#final gate for circuit 1
if c1a1_output == True and c1n2_output == True:
    final_gate1 = True #if both last "AND" and "NOT" outputs are true, output true
else:
    final_gate1 = False #otherwise output false

# +------------+
# | Circuit #2 |
# +------------+

#first NOT gate
if j == 0:
    c2n1_output = True #if J is false, make it true
elif j == 1:
    c2n1_output = False #if J is true, make it false

#first OR gate
if c2n1_output == True or i == 1:
    c2o1_output = True #if either previous output or I is true, output true
else:
    c2o1_output = False #otherwise output false

#second OR gate
if c2o1_output == True or k == 1:
    c2o2_output = True #if either previous output or K is true, output true
else:
    c2o2_output = False #otherwise output false

#second NOT gate
if g == 0:
    c2n2_output = True #if G is false, make it true
elif g == 1:
    c2n2_output = False #if G is true, make it false

#final gate for circuit 2
if c2o2_output == True and c2n2_output == True:
    final_gate2 = True #if both last "OR" and "NOT" outputs are true, output true
else:
    final_gate2 = False #otherwise output false

#output results to terminal
print("<" + str(final_gate1) + ">,", "<" + str(final_gate2) + ">")