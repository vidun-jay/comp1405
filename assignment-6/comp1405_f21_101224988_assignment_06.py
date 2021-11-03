# Vishva Vidun Jayakody, 101224988
import pygame
import random

#initialize pygame and load font for numbers
pygame.init()
pygame.display.set_caption('Race to 56')
font = pygame.font.Font('freesansbold.ttf', 15)

#define the length (and width) of one square
square_dim = 80

#sets display dimensions to 8x7 'squares'
window = pygame.display.set_mode((square_dim*8, square_dim*7))

#pygame program close definition
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        exit()

#dice roll function, generates number between 1-6
def roll():
    return random.randint(1, 6)

#checkerboard function to draw board and update pieces
def checkerboard():
    #initiate tile counter    
    num = 0

    #sets background to white
    window.fill((255,255,255))

    #draw checkerboard
    for i in range(0, square_dim*8, 160):
        for j in range(0, square_dim*8, 160):
            for k in range(80, square_dim*8, 160):
                for n in range(80, square_dim*8, 160):
                    pygame.draw.rect(window, (0, 0, 0), (i, j, 80, 80))
                    pygame.draw.rect(window, (0, 0, 0), (k, n, 80, 80))
    
    #number the tiles
    for i in range (0, square_dim*8, 80):
            for j in range(0, square_dim*8, 80):
                num += 1
                tile_num = font.render(str(num), True, (128, 128, 128))
                window.blit(tile_num, (j+5, i+5))

    #if you land on an occupied tile, make space for both
    if p1_pos == p2_pos:
        pygame.draw.circle(window, (255, 0, 0), (p1_pos[0], p1_pos[1]-20), 10)
        pygame.draw.circle(window, (0, 255, 0), (p1_pos[0], p1_pos[1]+20), 10)
    else:
        #draw the latest dot on top of the new checkerboard (clearing old dots)
        pygame.draw.circle(window, (255, 0, 0), p1_pos, 10)
        pygame.draw.circle(window, (0, 255, 0), p2_pos, 10)

#player starting positions
p1_pos = [40, 40]
p2_pos = [40, 40]

#randomly decide who goes first 
first = random.randint(1, 2)
if first == 1:
    turn = False
    print("Player 1 goes first!")
else:
    turn = True
    print("Player 2 goes first!")

#main loop
while True:
    ### PLAYER 1 MOVEMENT ###
    if(turn == False): #if it's player 1s turn (player 1 = False, player 2 = True)
        #roll the dice
        p1_roll = roll()

        #output dice roll to command line
        print("Player 1 rolled a", p1_roll)

        #move "p1_roll" many squares forward
        for i in range (p1_roll):

            #check if either player has already won and end game if they have
            if p1_pos[0] >= 600 and p1_pos[1] >= 520:
                pygame.time.delay(500)
                print("\nPlayer 1 wins!")
                exit()
            elif p2_pos[0] >= 600 and p2_pos[1] >= 520:
                pygame.time.delay(500)
                print("Player 2 wins!")
                exit()                 

            #as long as it's not at the last square, go ___ many squares to the right
            if p1_pos[0] <= 520:
                p1_pos[0] += 80             
            
            #if at the last square, start from the first square of the next row
            else:
                p1_pos[0] = 40
                p1_pos[1] += 80
            
            #update position of player1, w/ a 300ms delay
            checkerboard()
            pygame.display.update()
            pygame.time.delay(300)

    #next person's turn
    turn = True

    #wait a second before next person's turn
    pygame.time.delay(1000)

    ### PLAYER 2 MOVEMENT ###
    if(turn == True): #if it's player 2s turn
        #roll the dice
        p2_roll = roll()
        
        #output dice roll to command line
        print("Player 2 rolled a", p2_roll, "\n")
        
        #move p2_roll many squares forward
        for i in range (p2_roll):

            #check if either player has already won and end game if they have
            if p1_pos[0] >= 600 and p1_pos[1] >= 520:
                pygame.time.delay(1000)
                print("Player 1 wins!")
                exit()
            elif p2_pos[0] >= 600 and p2_pos[1] >= 520:
                pygame.time.delay(1000)
                print("Player 2 wins!")
                exit()               

            #as long as it's not at the last square, go ___ many squares to the right
            if p2_pos[0] <= 520:
                p2_pos[0] += 80
            
            #if at the last square, start from the first square of the next row
            else:
                p2_pos[0] = 40
                p2_pos[1] += 80

            #update position of player1, w/ a 300ms delay                
            checkerboard()
            pygame.display.update()
            pygame.time.delay(300)

    #next person's turn
    turn = False

    #wait a second and a half before next person's turn
    pygame.time.delay(1000)