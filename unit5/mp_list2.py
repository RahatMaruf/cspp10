numero = []
actions = input("What would you like to do with the list? ").lower
while actions != "exit":
    users_input_choice = int(input("Choose a number. "))
    
    if users_input_choice >= 0:
        numero.insert(0, users_input_choice)
    
    elif actions == "sum":
        sum(numero)
    
    elif actions == "clear":
         numero.remove(users_input_choice)

    elif actions == "print":
        print (numero)
        
    elif actions == "length":
        print (len(numero))

if actions == "exit":
    print ("exited")
    
        