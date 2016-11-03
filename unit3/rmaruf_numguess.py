import random 
k = random.randint(1,101)
num = int(input("I am thinking of a number between 1 and 100. can you guess it? "))

while (num != k):
    
    if num < k:
        print ("Too low!")
        num = int(input("Try again ^.^ "))
    
    elif num > k:
        print ("Too high!")
        num = int(input("Try again ^.^ "))
        
if num == k:
    print ("Great job! You got it! It was {}".format(k))
    
    

