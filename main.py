from turtle import Screen, Turtle
from score import Score
from ball import Ball
import time
from players import Paddle


line = Turtle()
screen = Screen()


# setting up screen

screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("red")
screen.title("PONG")
screen.mode("standard")
screen.tracer(0)
line.color("white")
# line.hideturtle()
line.penup()
line.goto(0, 300)
line.pensize(5)
line.setheading(270)
start_pl1 = (-360, 0)
start_pl2 = (350, 0)

# drawing middle line

for step in range(15):
    line.pendown()
    line.forward(25)
    line.penup()
    line.forward(25)
    screen.update()

# setting up borders

# border_top = Turtle()
# border_top.color("white")
# border_top.goto(0, 300)
# border_top.shape("square")
# border_top.shapesize(stretch_len=40, stretch_wid=0.2)
#
# border_bot = Turtle()
# border_bot.color("white")
# border_bot.goto(0, -290)
# border_bot.shape("square")
# border_bot.shapesize(stretch_len=40, stretch_wid=0.2)


score = Score()
player_1 = Paddle(start_pl1)
player_2 = Paddle(start_pl2)
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
    ball.move_ball()
    border_ball = ball.ycor()
    out_ball = ball.xcor()
    head_ball = ball.heading()
    if border_ball > 200 or border_ball < -200:
        ball.bounce_ball_wall()
    else:
        pass
    # if ball.distance(border_top) < 15 or ball.distance(border_bot) < 15:
    #     ball.bounce_ball(head_ball)
    # elif out_ball >= 620 or out_ball <= - 620:
    #     game_on = False

    time.sleep(0.08)


screen.exitonclick()
