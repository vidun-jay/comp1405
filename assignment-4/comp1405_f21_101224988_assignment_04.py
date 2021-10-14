#Vishva Vidun Jayakody, 101224988

"""
### UNIQUE MOVIE IDENTIFIERS ###

"Demon Slayer - The Movie: Mugen Train"
- Main character uses sword technique called "concentration breathing"

"Your Name"
- Plot includes a comet called "Comet Tiamat"

"Boruto: Naruto the Movie"
- About the son of a man with a nine-tailed fox demon inside him =

"Sword Art Online The Movie: Ordinal Scale"
- Characters play in a virtual reality world

"My Neighbor Totoro"
- Has a giant, dark gray animal with rabbit-like ears

"Akira"
- Akira is a post-apocalyptic cyberpunk action film

"A Silent Voice"
- Main female character is deaf

"Spirited Away"
- Main character wanders into a world ruled by gods, witches and spirits

"Princess Mononoke"
- Main character is accompanied by a large wolf

"Grave of the Fireflies"
- Needs no identifier, if answer to previous question is no, this is only possible anime movie left

"Cinderella"
- Fits into a glass slipper

"Aladdin"
- Rides a magic carpet

"Beauty and the Beast"
- Talking furniture and silverware

"Snow White"
- Has 7 dwarves

"The Little Mermaid"
- Main character desires legs

"Peter Pan"
- Antagonist has a hook for a hand

"Mulan"
- Main character has to convince everyone she's a man

"Tangled"
- Ridiculously long hair. Must take hours just to brush through.

"Frozen"
- Was turned into a massive marketing scheme. Everyone and everything was selling frozen merch and playing frozen
songs everywhere.

"Pinocchio"
- Needs no identifier, if answer to previous question is no, this is only possible fairy tale movie left
"""

#ask user if they need instructions and print them if they do
instr = input("\nDo you need instructions on how to play? (yes/no): ")
if(instr.lower() == "yes"):
    print("""+------------------------------------------------------------+
|                        Instructions                        |
+------------------------------------------------------------+
| Choose a movie from the ones below:                        |
| – Demon Slayer - The Movie: Mugen Train                    |
| - Your Name                                                |
| - Boruto: Naruto the Movie                                 |
| - Sword Art Online The Movie: Ordinal Scale                |
| - My Neighbor Totoro                                       |
| - Akira                                                    |
| - A Silent Voice                                           |
| - Spirited Away                                            |
| - Princess Mononoke                                        |
| - Grave of the Fireflies                                   |
| - Cinderella                                               |
| - Aladdin                                                  |
| - Beauty and the Beast                                     |
| - Snow White                                               |
| - The Little Mermaid                                       |
| - Peter Pan                                                |
| - Mulan                                                    |
| - Tangled                                                  |
| - Frozen                                                   |
| - Pinocchio                                                |
| Then, simply answer the questions by typing "yes" or "no"! |
+------------------------------------------------------------+""")

    #pretty much only accept "yes" as an answer
    ready = ""
    while(ready != "yes"):
        ready = input("Are you ready to go? (yes/no) ")

### ANIME ###
#ask user which subgenre to select
subgenre = input('Which subgenre would you like to consult? (anime/fairy tale) ')

#only allow either "anime" or "subgenre"
while(subgenre != "anime" and subgenre != "fairy tale"):
    subgenre = input('Incorrect subgenre entered, please enter either "anime" or "fairy tale": ')

#all the logic for the anime movies
if(subgenre.lower() == "anime"):
    demon_slayer = input('Does the main character in your movie use a sword technique called "concentration breathing"? ')
    if(demon_slayer.lower() == "yes"):
        print('Your movie is "Demon Slayer - The Movie: Mugen Train"')
    elif(demon_slayer.lower() == "no"):
        your_name = input('Does the plot of this movie include a comet called "Comet Tiamat"? ')
        if(your_name.lower() == "yes"):
            print('Your movie is "Your Name"')
        elif(your_name.lower() == "no"):
            boruto = input('Is this movie about the son of a man with a nine-tailed fox demon inside him? ')
            if(boruto.lower() == "yes"):
                print('Your movie is "Boruto: Naruto the Movie"')
            elif(boruto.lower() == "no"):
                sao = input('Do the characters in this movie find themselves in a virtual reality world? ')
                if(sao.lower() == "yes"):
                    print('Your movie is "Sword Art Online The Movie: Ordinal Scale"')
                elif(sao.lower() == "no"):
                    totoro = input('Does your movie have a large, dark gray animal with rabbit-like ears? ')
                    if(totoro.lower() == "yes"):
                        print('Your movie is "My Neighbor Totoro"')
                    elif(totoro.lower() == "no"):
                        akira = input('Is your movie a post-apocalyptic cyberpunk action film? ')
                        if(akira.lower() == "yes"):
                            print('Your movie is "Akira"')
                        elif(akira.lower() == "no"):
                            silent_voice = input('Does your movie have a main character with a disability? ')
                            if(silent_voice.lower() == "yes"):
                                print('Your movie is "A Silent Voice"')
                            elif(silent_voice.lower() == "no"):
                                silent_voice = input('Does the main character of your movie wander into a world ruled by gods, witches, and spirits? ')
                                if(silent_voice.lower() == "yes"):
                                    print('Your movie is "Spirited Away"')
                                elif(silent_voice.lower() == "no"):
                                    final1 = input('Is the main character of the movie often accompanied by a large wolf? ')
                                    if(final1.lower() == "yes"):
                                        print('Your movie is "Princess Mononoke"')
                                    elif(final1.lower() == "no"):
                                        print('Your movie is "Grave of the Fireflies"')

### FAIRY TALE ###
#all the logic for the fairy tale movies
elif(subgenre.lower() == "fairy tale"):
    cinderella = input('Would the character the movie is named after fit in a glass slipper? ')
    if(cinderella.lower() == "yes"):
        print('Your movie is "Cinderella"')
    elif(cinderella.lower() == "no"):
        aladdin = input('Does the main character of your movie ride a magic carpet? ')
        if(aladdin.lower() == "yes"):
            print('Your movie is "Aladdin"')
        elif(aladdin.lower() == "no"):
            batb = input('Do the furniture and silverware speak in your movie? ')
            if(batb.lower() == "yes"):
                print('Your movie is "Beauty and the Beast"')
            elif(batb.lower() == "no"):
                snow_white = input('Does your movie contain dwarves? ')
                if(snow_white.lower() == "yes"):
                    print('Your movie is "Snow White"')
                elif(snow_white.lower() == "no"):
                    little_mermaid = input('Does the main character in your movie desire human legs? ')
                    if(little_mermaid.lower() == "yes"):
                        print('Your movie is "The Little Mermaid"')
                    elif(little_mermaid.lower() == "no"):
                        peter_pan = input('Does the antagonist in this movie have a hook for a hand? ')
                        if(peter_pan.lower() == "yes"):
                            print('Your movie is "Peter Pan"')
                        elif(peter_pan.lower() == "no"):
                            mulan = input('Does your main character have to convince everyone she is a man? ')
                            if(mulan.lower() == "yes"):
                                print('Your movie is "Mulan"')
                            elif(mulan.lower() == "no"):
                                tangled = input('Does one of the main characters have ridiculously long hair? ')
                                if(tangled.lower() == "yes"):
                                    print('Your movie is "Tangled"')
                                elif(tangled.lower() == "no"):
                                    final2 = input('Was your movie turned into a global marketing scheme targeting children that probably earned more in sales than it did in movie revenue? ')
                                    if(final2.lower() == "yes"):
                                        print('Your movie is “Frozen”')
                                    elif(final2.lower() == "no"):
                                        print('Your movie is "Pinocchio”')