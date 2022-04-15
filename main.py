from turtle import Screen, Turtle
from score import Score

from players import Player1, Player2

line = Turtle()
screen = Screen()

# setting up screen

screen.setup(width=1200, height=800)
screen.colormode(255)
screen.bgcolor("red")
screen.title("PONG")
screen.mode("standard")
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
player_1 = Player1()
player_2 = Player2()

screen.update()

screen.listen()

screen.onkey(fun=player_1.up, key="w")
screen.onkey(fun=player_2.up, key="o")
screen.onkey(fun=player_1.down, key="S")
screen.onkey(fun=player_2.down, key="L")

# player_1.move()

screen.update()


game_on = True

# while game_on:
#     player_1.move()

screen.exitonclick()



