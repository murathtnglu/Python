import math

degree = 10

while degree!=-1:
    degree = eval(input("Enter degree : "))

    def converter(degree):
        radiant = degree*(math.pi/180)
        return radiant

    x = converter(degree)
    print(x)

