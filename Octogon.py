#octogan.py
# Chiedu Nduka-Eze
#Wednsesday, september 7
#this function creates 4 colored in octagons in different coordinates

import turtle

# This draws an octogon
def octagon():
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(100)
        turtle.left(45)
    turtle.end_fill()

#this moves the turtle pen without drawing a line
def move(x):
    turtle.penup()
    turtle.forward(x)
    turtle.pendown()

#This code moves the cursor and colors in the octogon
turtle.color('purple')
octagon()
turtle.left(180)
move(100)

#Second octogon
turtle.color('red')
octagon()
move(400)

#third octogon
turtle.color('blue')
octagon()
move(-1000)

#fourth octogon
turtle.color('orange')
octagon()


turtle.exitonclick()






