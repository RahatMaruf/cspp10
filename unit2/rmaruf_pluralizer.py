n = input("Pick a number.  ")
w = input(" Pick a word. ")
p1 = w[-1]
p2 = w[-2]

if w[-2:] == "fe":
    print ((str(n) + (str(w[0:-2]) +"ves")))