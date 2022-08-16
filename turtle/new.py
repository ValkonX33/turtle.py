import colorsys
import random
from turtle import Turtle, Screen 

tim = Turtle()
colour = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]

sc = Screen()

def draw(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        tim.forward(100)
        
        tim.right(angle)
       

for n in range(3,11):
    tim.color(random.choice(colour))
    draw(n)


sc.exitonclick()