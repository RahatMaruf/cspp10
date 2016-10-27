f = input("How may the calculator assist you? ")
c = f[1]
#this checks the mathematic term used such as addition
num1 = int(f[0])
num2 = int(f[2])

if c == "+":
    print ("The result is {} " .format(num1 + num2))
elif c == "-":
    print ("The result is {} " .format(num1 - num2))
elif c == "/":
    print ("The result is {} " .format(num1 / num2))
elif c == "*":
    print ("The result is {} " .format(num1 * num2))
elif c == "%":
    print ("The result is {} " .format(num1 % num2)) 