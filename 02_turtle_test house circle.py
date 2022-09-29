import turtle as turtle
# from turtle import *

# naming the program
turtle.title("my program")

# commando's turtle
# square, circle
turtle.shape("turtle")


# als import turtle is dan kan je gewoon title("my program") maar wordt niet gebruikt omdat 
# er in de verschillende libraries wel title zal bestaan


def hooks(x):
    for n in range(x):
        # movements
        turtle.forward(100)
        turtle.fillcolor("red")

        # change not position but the facing
        turtle.right(360/x)

def house():
    hooks(4)

    turtle.left(45)
    turtle.forward(30)

    turtle.right(45)
    turtle.forward(60)

    turtle.right(45)
    turtle.forward(30)

def circle(x):
    for n in range(x):
        turtle.forward(1)
        turtle.fillcolor("red")
        # change not position but the facing
        turtle.right(360/x)

def teken_driehoek(lengte):
    for n in range(lengte):
        turtle.forward
    

# hooks()
# house()
circle(500)
print(turtle.position())

# turtle.done()
turtle.mainloop()

