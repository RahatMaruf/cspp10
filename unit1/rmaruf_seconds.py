s = int(float(input("How many seconds would you like to see in hours,minutes and seconds?")))
s2 = s%60
m = (s/60)%60
h = m/3600
print (str(s) + " seconds is " + (str(h)) + " hours, " + (str(m)) + " minute, and " + (str(s2)) + " seconds.")