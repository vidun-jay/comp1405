#Vishva Vidun Jayakody, 101224988

#prompt for all the grades and store to their respective variables
tut = float(input("Enter overall grade recieved for tutorials: "))
quiz = float(input("Enter overall grade recieved for quizzes: "))
ass = float(input("Enter overall grade recieved for assignments: "))
final = float(input("Enter overall grade recieved for the final: "))

#calculate grade
grade = (tut*0.1) + (quiz*0.3) + (ass*0.4) + (final*0.2)

#determine which letter grade the grade is
if(grade >= 90):
    print("Your final grade is an A+")
elif(grade >= 85 and grade <= 89):
    print("Your final grade is an A")
elif(grade >= 80 and grade <= 84):
    print("Your final grade is an A-")
elif(grade >= 77 and grade <= 79):
    print("Your final grade is an B+")
elif(grade >= 73 and grade <= 76):
    print("Your final grade is an B")
elif(grade >= 70 and grade <= 72):
    print("Your final grade is an B-")
elif(grade >= 67 and grade <= 69):
    print("Your final grade is an C+")
elif(grade >= 63 and grade <= 66):
    print("Your final grade is an C")
elif(grade >= 60 and grade <= 62):
    print("Your final grade is an C-")
elif(grade >= 57 and grade <= 59):
    print("Your final grade is an D+")
elif(grade >= 53 and grade <= 56):
    print("Your final grade is an D")
elif(grade >= 50 and grade <= 52):
    print("Your final grade is an D-")
elif(grade <= 49):
    print("You fail. :(")