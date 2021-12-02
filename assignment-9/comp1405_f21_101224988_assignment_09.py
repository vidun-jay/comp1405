#Vishva Vidun Jayakody, 101224988

def removePunctuation(phrase):
    
    #define what punctuations are
    punctuation_list = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    #turn input into list of characters
    phrase = list(phrase)

    #use list comprehension to only 'remove' puncuation
    phrase = [i for i in phrase if i not in punctuation_list]

    #turns the list back into a string for neat printing
    converted_string = ""
    for i in phrase:
        converted_string += i

    return converted_string

def leet(phrase):

    leet_index = (
        ('A', '4'),
        ('B', '8'),
        ('C', 'c'),
        ('D', 'd'),
        ('E', '3'),
        ('F', 'f'),
        ('G', '9'),
        ('H', 'h'),
        ('I', '1'),
        ('J', 'j'),
        ('K', 'k'),
        ('L', '1'),
        ('M', 'm'),
        ('N', 'n'),
        ('O', '0'),
        ('P', 'p'),
        ('Q', 'q'),
        ('R', 'r'),
        ('S', '5'),
        ('T', '7'),
        ('U', 'u'),
        ('V', 'v'),
        ('W', 'w'),
        ('X', 'x'),
        ('Y', 'y'),
        ('Z', 'z'))

    #convert to list of uppercase letters
    phrase = list(toUpper(phrase))
    
    #check to see if letters from the conversion index are in the string
    for original, leet in leet_index:
        #repeat for every letter in the given string
        for i in range (len(phrase)):
            #if the letter at index i is a letter from the conversion index, replace it with its leet
            if phrase[i] == original:
                phrase[i] = leet
    
    #turns the list back into a string for neat printing
    converted_string = ""
    for i in phrase:
        converted_string += i

    return converted_string

def toUpper(phrase):
    #initialize lowercase variable
    uppercase = ""

    #for every letter in the word
    for letter in phrase:
        #if it's an lowercase letter, add 32 to it's ASCII value (making it uppercase)
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        uppercase += letter
    
    return uppercase

def homoglyph(phrase):
    homoglyph_index = (
        ('A', '@'),
        ('B', '|3'),
        ('C', '<'),
        ('D', 'I>')
    )

    phrase = list(phrase)
    
    #check to see if letters from the conversion index are in the string
    for original, homoglyph in homoglyph_index:
        original = toUpper(original)
        #repeat for every letter in the given string
        for i in range (len(phrase)):
            #if the letter at index i is a letter from the conversion index, replace it with its leet
            if toUpper(phrase[i]) == original:
                phrase[i] = homoglyph
    
    #turns the list back into a string for neat printing
    converted_string = ""
    for i in phrase:
        converted_string += i

    return converted_string

def abbreviate(phrase):
    
    replacement_index = [
        ['by the way', 'BTW'],
        ['oh my god', 'OMG'],
        ['laughing out loud', 'LOL']]

    wordlist = removePunctuation(phrase).split()

    for i in range(len(wordlist)):

        if(wordlist[i].lower() == 'by' and wordlist[i+1].lower() == 'the' and wordlist[i+2].lower() == 'way'):
            wordlist[i] = 'BTW'
            wordlist[i+1] = ''
            wordlist[i+2] = ''

        elif(wordlist[i].lower() == 'oh' and wordlist[i+1].lower() == 'my' and wordlist[i+2].lower() == 'god'):
            wordlist[i] = 'OMG'
            wordlist[i+1] = ''
            wordlist[i+2] = ''

        elif(wordlist[i].lower() == 'laughing' and wordlist[i+1].lower() == 'out' and wordlist[i+2].lower() == 'loud'):
            wordlist[i] = 'LOL'
            wordlist[i+1] = ''
            wordlist[i+2] = ''

    #if any item in wordlist returns false (is a blank string), don't include in wordlist
    wordlist = [blank for blank in wordlist if blank]

    #turns the list back into a string for neat printing
    converted_string = ""
    for i in wordlist:
        converted_string += i + " "

    return converted_string

def main():

    print('\n### TESTING LEET FUNCTION ###\n')
    test1 = 'hello world'
    print('Input =', test1)
    leet_ver = leet(test1)
    print('Output =', leet_ver, "\n")

    print('\n### TESTING UPPERCASE FUNCTION ###\n')
    test2 = 'this sentence goes in all lowercase, and comes out all uppercase'
    print('Input =', test2)
    uppercase_ver = toUpper(test2)
    print('Output =', uppercase_ver, "\n")

    print('\n### TESTING HOMOGLYPHS FUNCTION ###\n')
    test3 = 'the quick brown fox jumps over the lazy dog'
    print('Input =', test3)
    homoglyph_ver = (homoglyph(test3))
    print('Output =', homoglyph_ver, "\n")

    print('\n### TESTING ABBREVIATIONS FUNCTION ###\n')
    test4 = 'Oh my god by the way I am totally laughing out loud right now'
    print('Input =', test4)
    abbreviated_ver = (abbreviate(test4))
    print('Output =', abbreviated_ver, "\n")

    print('\n### TESTING REMOVE PUNCTUATION FUNCTION ###\n')
    test5 = """the following items will be removed: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
    print('Input =', test5)
    removed_punc = removePunctuation(test5)
    print('Output =', removed_punc, "\n")

if __name__ == "__main__":
    main()