import math

def func(a,b,c):
    delta= b**2 - 4 * a * c

    if delta<0:
        print("No reel roots..")
        return

    x1 = (-1*b + math.sqrt(delta)/(2*a))
    x2 = (-1 * b - math.sqrt(delta) / (2 * a))

    return(x1,x2)




a = eval(input("Enter a :"))
b = eval(input("Enter b :"))
c = eval(input("Enter c :"))

print("Solutions are (x1,x2) : ",func(a,b,c))