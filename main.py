from turtle import Screen, Turtle
from score import Score


line = Turtle()
screen = Screen()



# setting up screen

screen.setup(width=1200, height=800)
screen.colormode(255)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
line.color("white")
line.hideturtle()
line.penup()
line.goto(0, 400)
line.pensize(5)
line.setheading(270)

# drawing middle line

for step in range(16):
    line.pendown()
    line.forward(25)
    line.penup()
    line.forward(25)
    screen.update()

score = Score()
screen.update()

screen.exitonclick()



