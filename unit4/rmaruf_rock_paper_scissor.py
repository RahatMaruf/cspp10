import random


#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    #code here
    choice = input("Rock, paper, or scissor? ")
    if choice == "rock":
        return ("r")
    elif choice == "paper":
        return ("p")
    elif choice == "scissor":
        return ("s")

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    compchoice = random.randint(1,4)
    if compchoice == 1:
        return ("r")
    elif compchoice == 2:
        return ("p")
    elif compchoice == 3:
        return ("s")

    
    

