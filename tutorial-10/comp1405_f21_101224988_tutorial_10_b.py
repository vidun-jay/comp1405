#Vishva Vidun Jayakody, 101224988

#checks each item in list, if its a e i o or u then make it uppercase and print new list
def iteration(char_list):
    upper_vowels = []
    
    for char in char_list:
        if char in 'aeiou':
            upper_vowels.append(str(char).upper())
        else:
            upper_vowels.append(char)

    return upper_vowels

#change the value of selected index to uppercase if its a e i o or u, call itself as many times as needed to finish list
def recursion(char_list, destination):
    upper_vowels = destination

    if char_list[0] in 'aeiou':
        upper_vowels.append(str(char_list[0]).upper())
    
    else:
        upper_vowels.append(char_list[0])

    if len(char_list) > 1:
        recursion(char_list[1:], upper_vowels)
    
    return upper_vowels

def main():
    uppercase_vowels = []

    char_list = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'abcdel']
    print("Using iteration:", iteration(char_list))
    print("Using recursion:", recursion(char_list, uppercase_vowels))

if __name__ == "__main__":
    main()