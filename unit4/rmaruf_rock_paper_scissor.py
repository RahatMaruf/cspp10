import random


#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    #code here
    choice = input("Rock, paper, or scissor? ")
    if choice == "rock":
        print ("r")
    elif choice == "paper":
        print ("p")
    elif choice == "scissor":
        print ("s")

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    compchoice = random.randint(1,4)
    1 = "r"
    2 = "p"
    3 = "s"
get_comp_move()
    
    

