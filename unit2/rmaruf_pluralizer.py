n = int(input("Pick a number...:) "))
w = input(" Pick a noun...:) ")
p1 = w[-1:]
p2 = w[-2:]
s1 = "oy"
s2 = "ey"
s3 = "uy"
s4 = "ay"
s5 = "y"

if n == 1:
    print ((str(n)) + "\n" + (w))
elif p2 == "fe":
    print ((str(n)) + "\n" + (str(w[0:-2])) +"ves")
elif p2 == "ch":
    print ((str(n)) + "\n" + (w) +"es")
elif p2 == "sh":
    print ((str(n)) + "\n" + (w) +"es")
elif p2 == s1:
    print ((str(n)) + "\n" + (w) +"s")
elif p2 == s2:
    print ((str(n)) + "\n" + (w) +"s")
elif p2 == s3:
    print ((str(n)) + "\n" + (w) +"s")
elif p2 == s4:
    print ((str(n)) + "\n" + (w) +"s")
elif p1 == s5 and p1 != s1 and p1 != s2 and p1 != s3 and p1 != s4:
    print ((str(n)) + "\n" + (str(w[0:-1])) +"ies")
elif p2 == "us":
    print ((str(n)) + "\n" + (str(w[0:-2])) +"i")
else:
    print ((str(n)) + "\n" + (w) + "s")