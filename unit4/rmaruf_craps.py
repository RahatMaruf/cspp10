#make funtion where the dice will roll randomly

import random

#the players bank needs to start off with $100


playersbank = 100

#the bank has an unlimited amount of money 

bank = 10000000000000000000000

#write a function that asks the user for their bet and takes away the amount they bet from their bank

def bet():
    dabet = int(input("How much would you ike to bet from your bank"))
    return (dabet)

#make a function that let"s the computer pick out two number betwwn 1 and 6

def dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1 + dice2
    
    
def loss_or_win():
    
    if dice1 + dice2 == 2 or dice1 + dice2 == 3 or dice1 + dice2 == 12:
        return ("You lost. You now have $" + str(dabet - playersbank))
    elif dice1 + dice2 == 7 or dice1 + dice2 == 11:
        return ("You win. You have $" + str(dabet + playersbank))
        
def get_phase3():
    
    if





#OPTION 2
# function name: roll_result
#   purpose: get the result of the roll
#   arguments: 
#       roll - the sum of the two dice rolled
#       is_first_roll - true/false depending on which roll it is
#   returns: the result
#       if player wins: return "win"
#       if player lost: return "lose"


