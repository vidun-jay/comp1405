#Vishva Vidun Jayakody, 101224988

#ask for name, current year, and birth year
name = str(input("Enter your name: "))
current_year = int(input("What is the current year? "))
birth_year = int(input("In what year were you born? "))

#calculate age
age1 = current_year - birth_year
age2 = (current_year - birth_year) - 1
leap = (current_year - birth_year) // 4

#print age
print("Hello", name + ", you are either", age2, "or", str(age1) + ". Unless you were actually born on a leap day, in which case you'd be", leap, "years old.")