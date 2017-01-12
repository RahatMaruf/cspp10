numero = []
choice = 1
while choice != 0:
    choice = int(input("Enter a number: "))
    numero.insert(0,choice)
    if choice == 0:
        break
    if choice < 0:
        if (choice * -1) in numero:
            numero.remove(choice * -1)
            numero.remove(choice)
    print(numero)
   