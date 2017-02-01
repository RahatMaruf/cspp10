import random
print ("Hello, welcome to the maze! You're stuck in here until you find a way out.")
plotpoint = random.randint(5,10)
def starting_the_maze():
    c = int(input("Which direction would you like to go? 1 = go forward, 2 = go backwards, 3 = go right, 4 = go left. Pick a number. "))
    while plotpoint != 0:
        if c == 1:
            plotpoint + 1
        elif c == 2:
            plotpoint - 1
        elif c == 3:
            plotpoint + 2
        elif c == 4:
            plotpoint - 2
    if plotpoint <= 0:
        print ("You have made it out the maze yay.")
starting_the_maze()    
    