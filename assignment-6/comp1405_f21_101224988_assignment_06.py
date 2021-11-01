#Vishva Vidun Jayakody, 101224988
import pygame
import random
import time

#initialize pygame and load font
pygame.init()
pygame.display.set_caption('Race to 56')
font = pygame.font.Font('freesansbold.ttf', 15)

#the length (and width I guess) of one square
square_dim = 80

#sets display dimensions to 8 'squares'
window = pygame.display.set_mode((square_dim*8, square_dim*7))

#dice roll function, generates number between 1-6
def roll():
    return random.randint(1, 6)

def checkerboard():
    #initiates tile counter    
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

#program close definition
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        exit()

#Player starting positions
p1_pos = [40, 40]
p2_pos = [40, 40]

#Let player 1 go first
p1_turn = True
p2_turn = False

#main loop
while True:
    ### PLAYER 1 MOVEMENT ###
    if(p1_turn == True): #if it's player 1s turn
        #roll the dice
        p1_roll = roll()
        
        #output dice roll to command line
        print("Player 1 rolled a", p1_roll)

        #move p1_roll many squares forward
        for i in range (p1_roll):

            #as long as it's not at the last square, go ___ many squares to the right
            if p1_pos[0] <= 520:
                p1_pos[0] += 80
            
            #winning case
            elif p1_pos[0] >= 520 and p1_pos[1] >= 520:
                pygame.time.delay(1000)
                print("Player 1 wins!")
                exit()                
            
            #if at the last square, start from the first square of the next row
            else:
                p1_pos[0] = 40
                p1_pos[1] += 80
            
            #update position of player1, w/ a 300ms delay
            checkerboard()
            pygame.display.update()
            pygame.time.delay(300)

    #next person's turn
    p1_turn = False 
    p2_turn = True

    #wait a second before next person's turn
    pygame.time.delay(1000)

    ### PLAYER 2 MOVEMENT ###
    if(p2_turn == True): #if it's player 2s turn
        #roll the dice
        p2_roll = roll()
        
        #output dice roll to command line
        print("Player 2 rolled a", p2_roll, "\n")
        
        #move p2_roll many squares forward
        for i in range (p2_roll):      

            #as long as it's not at the last square, go ___ many squares to the right
            if p2_pos[0] <= 520:
                p2_pos[0] += 80

            #winning case
            elif p2_pos[0] >= 520 and p2_pos[1] >= 520:
                print("Player 2 wins!")
                exit()
            
            #if at the last square, start from the first square of the next row
            else:
                p2_pos[0] = 40
                p2_pos[1] += 80

            #update position of player1, w/ a 300ms delay                
            checkerboard()
            pygame.display.update()
            pygame.time.delay(300)

    #next person's turn
    p1_turn = True
    p2_turn = False

    #wait a second and a half before next person's turn
    pygame.time.delay(1000)