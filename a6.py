#Fatima Ferdous 
#101227971
#Assignment 6
#5/11/2021

import pygame
import random

pygame.init()

w = 7
h = 8

dim = 100

blue = (173,216,230)
white = (255,255,255)
black = (0,0,0)
red = (250,128,114)
green = (190,229,176)

current_colour = white

window = pygame.display.set_mode((w * dim, h * dim))

num_font = pygame.font.SysFont('constantia', 15, bold = True, italic = False)
number = 0

for y in range(h):
	for x in range(w):

		pygame.draw.rect(window, current_colour, (x * dim, y * dim, dim, dim))
		number += 1
		window.blit(num_font.render(str(number), 100, black), (8+(x*dim), 8+(y*dim)))
		pygame.display.update()

		if current_colour == white:
			current_colour = blue
		else:
			current_colour = white

#dice = random.randint(1,6)

player1 = pygame.draw.rect(window, red, (40,18,18,18))
print("Player 1 is a rectangle")
(p1_x,p1_y) = (40,18)

player2 = pygame.draw.circle(window, green, (48,55),12)
print("player 2 is a circle")
(p2_x,p2_y) = (48,55)

pygame.display.update()

p1_turn = True 
p2_turn = False

while True:
	if p1_turn == True:
		#move_p1 = dice
		#move_p1 += dice
		move_p1 = random.randint(1,6)
		move_p1 += random.randint(1,6)
		pygame.time.delay(1000)

		for i in range(move_p1):
			p1_x += 100
			pygame.draw.rect(window, red, (p1_x,p1_y,18,18)) 

			pygame.display.update()
			pygame.time.delay(1000)

			if p1_x >= 740:
				if p1_x == 640 and p1_y == 718:
					print("player 1 wins")
					break
				else:
					p1_x = -60 
					p1_y += 100
		if p1_x == 640 and p1_y == 718:
			break

		p1_turn = False 
		p2_turn = True

	if p2_turn == True:
		#move_p2 = dice 
		#move_p2 += dice
		move_p2 = random.randint(1,6) 
		move_p2 += random.randint(1,6)
		pygame.time.delay(1000)

		for j in range(move_p2):
			p2_x += 100
			pygame.draw.circle(window, green, (p2_x,p2_y),12) 
			
			pygame.display.update()
			pygame.time.delay(1000)

			if p2_x >= 648:
				if p2_x == 648 and p2_y == 755:
					print("player 2 wins")
					break
				else:
					p2_x = -52
					p2_y += 100

		if p2_x == 648 and p2_y == 755:
			break

		p1_turn = True 
		p2_turn = False

		pygame.time.delay(3000)


#100*7+48 or 40 for x co-ord 
    
		
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

