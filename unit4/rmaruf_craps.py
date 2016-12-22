
#make funtion where the dice will roll randomly

import random

#the players bank needs to start off with $100

def bank(playersbank):
    playersbank = 100



def bet(dabet):
    dabet = int(input("You have $100 in your bank. How much would you like to bet, if any from your bank? "))
    if dabet < 0:
        return ("Only positive amount of money!")
    else:
        return (dabet)



def roll2dice(dice1, dice2, point_number):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    point_number = dice1 + dice2
    return point_number


    

    
    
def loss_or_win(dice1, dice2, dabet, playersbank, point_number):
    
    
    if point_number == 2 or point_number == 3 or point_number == 12:
        return ("You lost. You now have $" + str(dabet - playersbank))
    elif point_number == 7 or point_number == 11:
        return ("You win. You have $" + str(dabet + playersbank))
    else:
        return (point_number)

            
            
def get_phase3(point_number, dabet, playersbank):
        roll = roll2dice()
        while(roll != 7 and roll != point_number):
            return roll
            
        if roll == 7:
            return ("You lose! You now have $" + str(dabet - playersbank))
        elif roll == point_number:
            return ("You Win! You now have $" + str(dabet + playersbank))

      
                

    
    
        
        
        
        