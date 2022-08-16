
from turtle import Turtle, Screen, colormode
import random
import turtle
sc = Screen()
tim = Turtle()
colormode(255)
def randomColor():
    r= random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color= (r, g, b)
    return random_color

# tim.shape('circle')
def spirograph(size):
    for _ in range(int(360/size)):  

        tim.speed(0)
        tim.color(randomColor())
        tim.circle(100)
       
        tim.setheading(tim.heading() +size)

spirograph(5)

    #     tim.tilt(40)
    #     tim.circle(60)
sc.exitonclick()