#Vishva Vidun Jayakody, 101224988

pi = 3.14159 #define pi for degrees measures

#eyes function, no inputs, no returns
def draw_eyes():
    #eye outlines
    pygame.draw.circle(win_sfc, (0, 0, 0), (110, 220), 25)
    pygame.draw.circle(win_sfc, (0, 0, 0), (190, 220), 25)

    #eyes
    pygame.draw.circle(win_sfc, (255, 255, 255), (110, 220), 23)
    pygame.draw.circle(win_sfc, (255, 255, 255), (190, 220), 23)

    #pupil
    pygame.draw.circle(win_sfc, (0, 0, 0), (110, 230), 10)
    pygame.draw.circle(win_sfc, (0, 0, 0), (190, 230), 10)

    #eyebrows
    pygame.draw.arc(win_sfc, (0,0,0), [85,180,50,50], pi/3, 5*pi/6, 3)
    pygame.draw.arc(win_sfc, (0,0,0), [165,180,50,50], pi/6, 2*pi/3, 3)

#hat function, no inputs, returns 'irish tophat'
def draw_hat():

    pygame.draw.rect(win_sfc, (50, 90, 55), [200, 60, 100, 140]) #hat base
    pygame.draw.rect(win_sfc, (50, 90, 55), [150, 200, 200, 70]) #hat base
    pygame.draw.rect(win_sfc, (0, 0, 0), [150, 225, 200, 20]) #black belt
    pygame.draw.rect(win_sfc, (247, 206, 100), [230, 215, 40, 40]) #gold square
    pygame.draw.rect(win_sfc, (0, 0, 0), [235, 220, 30, 30]) #black square inside gold square

    return "irish tophat"

#mouth function, inputs x and y coordinates (ints), no returns
def draw_mouth(x, y):
    pygame.draw.ellipse(win_sfc, (0, 0, 0), (x-40, y+30, 80, 50)) #inside of mouth
    pygame.draw.ellipse(win_sfc, (255, 0, 0), (x-8, y+59, 35, 20)) #tongue
    pygame.draw.rect(win_sfc, (255, 255, 255), [x-20, y+35, 30, 10]) #teeth
    pygame.draw.ellipse(win_sfc, (0, 0, 0), (x-40, y+30, 80, 50), 5) #outline