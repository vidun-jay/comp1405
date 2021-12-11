#Vishva Vidun Jayakody, 101224988

def iteration(int_list):
    odd_plus_ten = []
    #check every index, if odd add 10
    for number in int_list:
        if number % 2 != 0:
            number += 10
        odd_plus_ten.append(number)
    return odd_plus_ten

def recursion(int_list, destination):
    odds = destination

    #if odd add 10
    if int_list[0] % 2 == 1:
        odds.append(int_list[0] + 10)
    
    #if not don't change
    else:
        odds.append(int_list[0])

    #as long as list is bigger than 0 (which is the base case), call itself
    if len(int_list) > 1:
        recursion(int_list[1:], odds)
    
    return odds

def main():
    odds = []
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Using iteration:", iteration(int_list))
    print("Using recursion:", recursion(int_list, odds))

if __name__ == "__main__":
    main()