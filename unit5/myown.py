import random
print("Welcome to my maze!! Use 1 = go forward, 2 = go backwards, 3 = go right, 4 = go left.")
plotpoint = random.randint(15,25)
print ("You start off at tile " + str(plotpoint))
def starting_the_maze(plotpoint,c):
    c = int(input("Which direction would you like to go? Pick a number. "))
    if c == 1:
        print ("You are now at tile " + str(plotpoint-1))
    elif c == 2:
        plotpoint - 1
        return ("You are now at tile " + str(plotpoint+1))
    elif c == 3:
        plotpoint + 2
        print ("You are now at tile " + str(plotpoint-2))
    elif c == 4:
        plotpoint - 2
        print ("You are now at tile " + str(plotpoint+2))
    while c != 0:
        f = random.randint(1,4)
        if f == 1:
            int(input("Would you like to go right(3) or left(4)? "))
        elif f == 2:
            int(input("Would you like to go forward(1) or backwards(2)? "))
        elif f == 3:
            int(input("Would you like to go right(3) or backwards(2)? "))
        elif f == 4:
            int(input("Would you like to go left(4) or forward(1)? "))
        return(plotpoint)

c = 0
starting_the_maze(plotpoint,c)
plotpoint = starting_the_maze(plotpoint,c)
    # if plotpoint <= 0:
    #     print ("You have made it out the maze yay." + str(plotpoint))
        
#I tried, I dont know how to work this
        
    
    