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

    
    #function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    #code here
    rounds = int(input("How many rounds would you like to play? Only 1-9 rounds available! "))
    return (rounds)
    

#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move, cmove):
    #code here
    if cmove == "r" and p1move == "s":
        print ("Computer Wins!Player Loses!")
        return "computer"
    elif cmove == "s" and p1move == "r":
        print ("Player Wins!Computer Loses!")
        return "player"
    elif cmove == "r" and p1move == "p":
        print ("Player Wins! Computer Loses!")
        return "player"
    elif cmove == "p" and p1move == "s":
        print ("Player Wins!Computer Loses!")
        return "player"
    elif cmove == "s" and p1move == "p":
        print ("Computer Wins!Player Loses!")
        return "computer"
    elif cmove == "p" and p1move == "r":
        print ("Computer Wins!Player Loses!")
        return "computer"
    else:
        print ("It's a tie")
        

#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    #code here
    choice = shortmove 
    compchoice = shortmove
    if shortmove == "r":
        return ("Rock")
    elif shortmove == "s":
        return ("Scissor")
    elif shortmove == "p":
        return ("Paper")
        
#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, ties):
    #code here
    print("Player Score: {}".format(pscore))
    print("Computer Score: {}".format(cscore))
    print("Tie Score: {}".format(ties))

#function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
#   returns: none
def rps():
    #code here
    rounds = get_rounds()
    cmove = get_comp_move()
    p1move = get_p1_move()
     
    print("Player choice {}".format(get_full_move(p1move) ))
    print("Computer chose {}".format(get_full_move(cmove) ))
    
    winner = get_round_winner(p1move,cmove)
    if winner == "player":
        print("Player won!")
    elif winner == "computer":
        print("Computer won!")
    else:
        print("It's a tie!")
    for rounds in range(0,10):
        

#function name: tests
#   arguments: none
#   purpose: a place for you to write your tests.  replace 'rps' below
#               with 'tests' to run this function instead of the game loop
#   returns: none


rps()

