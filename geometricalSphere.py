import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black") #sets the background color to black
fero = turtle.Turtle() #creates a turtle object
fero.speed(10) #sets the time for the turtle object "fero"

colors = ["yellow", "orange", "green", "red", "purple"]
for x in range(100):
    fero.color(random.choice(colors)) #invokes random module and chooses acolor randomly
    for i in range(5):
        fero.left(72)
        fero.forward(175) #creates a pentagon
    fero.right(25) #shifts the rotation the place next pentagon with an angle

wn.mainloop() #keeps the graphic window open