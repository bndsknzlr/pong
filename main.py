from turtle import Screen, Turtle
from score import Score
from ball import Ball
import time
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
ball = Ball()

screen.update()

screen.listen()

screen.onkey(fun=player_1.up, key="w")
screen.onkey(fun=player_2.up, key="o")
screen.onkey(fun=player_1.down, key="s")
screen.onkey(fun=player_2.down, key="l")


game_on = True

while game_on:
    screen.update()
    screen.listen()
    ball.move_ball()
    border_ball = ball.ycor()
    out_ball = ball.xcor()
    if border_ball >= 330 or border_ball <= - 330:
        ball.bounce_ball(ball.heading())
    elif out_ball >= 620 or out_ball <= - 620:
        game_on = False

    time.sleep(0.03)


screen.exitonclick()
