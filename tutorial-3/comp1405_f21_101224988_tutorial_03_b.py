#Vishva Vidun Jayakody, 101224988

#prompt user for a background
print("Many kinds of people made the trip to Oregon.\nYou may be:\n")
print("1. Banker from Boston")
print("2. Carpenter from Ohio")
print("3. Farmer from Illinois\n")
background = int(input("What is your choice? "))

#sets the initial balances
if(background == 1):
    starting_balance = 800
elif(background == 2):
    starting_balance = 600
elif(background == 3):
    starting_balance = 500

#prints the menu and starting balance
print("""
+========================+
|  Matt's General Store  |
| Independence, Missouri |
+========================+
| 1. Oxen                |
+------------------------+
| 2. Food                |
+------------------------+
| 3. Clothing            |
+------------------------+
""")
print("Amount you have: $" + str(starting_balance))

#asks user all the questions
yoke = float(input("\nThere are 2 oxen in a yoke; I recommend at least 3 yoke. I charge $40.00 a yoke.\nHow many yoke do you want? "))
food = float(input("\nYou’ll need flour, sugar, bacon, and coffee. My price is 20 cents a pound.\nHow many pounds of food do you want? "))
clothes = float(input("\nYou'll need warm clothing in the mountains. Each set is $10.00.\nHow many sets of clothes do you want? "))

#calculates total bill
bill = yoke*40 + food*0.2 + clothes*10

#prints total bill and remaining balance
print("\nYour total bill is $" + str(bill))
print("\nYou have $" + str(starting_balance - bill) + " remaining.\n")