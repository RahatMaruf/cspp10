
#make funtion where the dice will roll randomly

import random

#the players bank needs to start off with $100


playersbank = 100

#the bank has an unlimited amount of money 

bank = 10000000000000000000000

#write a function that asks the user for their bet and takes away the amount they bet from their bank

def bet():
    dabet = int(input("You have $100 in your bank. How much would you like to bet from your bank"))
    return (dabet)

#make a function that let"s the computer pick out two number betwwn 1 and 6

def roll2dice():
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
            
            
def get_phase3(point_number):
        roll = roll2dice()
        while(roll != 7 and roll != point_number):
            return roll
            if point_number == 7:
                return ("You lose!")
            elif point_number
        
        
        
        
        