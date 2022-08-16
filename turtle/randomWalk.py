from operator import truediv
from turtle import Turtle, Screen, backward, forward 
import random
tim = Turtle()
sc = Screen()
path = [0, 90, 180, 270]
colour = [ "red", "blue", "green", "yellow", "purple", "orange", "pink", "black" ]
size = [30, 15 , 10, 20]
timismoving = True
for _ in range(300):
    tim.color(random.choice(colour))
    tim.pensize(random.choice(size))
    tim.forward(30)
    tim.setheading(random.choice(path))
    tim.speed(0)

sc.exitonclick()