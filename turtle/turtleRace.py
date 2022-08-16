from cgitb import text
from turtle import Turtle, Screen, colormode
import random
import turtle
sc = Screen()
colormode(255)
colour = [ "red", "blue", "green", "yellow", "purple", "orange" ]
sc.setup(width=500, height=400)
user_bet= sc.textinput(title='Your Bet?', prompt="Which Turtle will win the race, Enter the color: ")
turtle_pos = [-70, -40, -10, 20, 50, 80]
new_turtles =[]
def randomColor():
    r= random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color= (r, g, b)
    return random_color
for tutle_index in range(0,6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(random.choice(colour))
    tim.goto(x=-230, y= turtle_pos[tutle_index])
    new_turtles.append(tim)
# tom = Turtle(shape='turtle') 
# timmy = Turtle(shape='turtle')
# tommy = Turtle(shape='turtle')
# timinder = Turtle(shape='turtle')

# timmy.penup()
# tom.penup()
# tommy.penup()
# timinder.penup()
# 
# tom.goto(x=-230, y= -100)
# timmy.goto(x=-230, y= -70)
# tommy.goto(x=-230, y= -40)
# timinder.goto(x=-230, y= -10)
if user_bet:
    race_on = True

while race_on:
    for turtle in new_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle ==user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost, The {winning_turtle} turtle is the winner")


            
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
   
sc.exitonclick()