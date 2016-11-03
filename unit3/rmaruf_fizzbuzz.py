dude = int(input("What number would you like to go up to that's less than 1000?" ))
for x in range(1,dude):
    if x%3 and x%5== 0:
        print ("FizzBuzz")
    elif x%5 == 0:
        print ("Buzz")
    elif x%3== 0:
        print ("Fizz")
    else:
        print (x)