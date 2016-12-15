
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
    return dice1 + dice2
    
    

    
    
def loss_or_win(dice1, dice2, dabet, playersbank):
    
    if dice1 + dice2 == 2 or dice1 + dice2 == 3 or dice1 + dice2 == 12:
        return ("You lost. You now have $" + str(dabet - playersbank))
    elif dice1 + dice2 == 7 or dice1 + dice2 == 11:
        return ("You win. You have $" + str(dabet + playersbank))
    else:
        return (dice1 + dice2)
            
            
def get_phase3(point_number):
        roll = roll2dice()
        while(roll != 7 and roll != point_number):
            roll2dice()
        
        
        
        
        
        
craps()        