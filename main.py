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
line.hideturtle()
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


player_1 = Paddle(start_pl1)
player_2 = Paddle(start_pl2)


# screen.update()

screen.listen()

screen.onkey(fun=player_1.up, key="w")
screen.onkey(fun=player_2.up, key="o")
screen.onkey(fun=player_1.down, key="s")
screen.onkey(fun=player_2.down, key="l")

score = Score()
game_on = True
while game_on:
    score.clear()
    ball = Ball()
    fight_on = True
    while fight_on:
        screen.update()
        ball.move_ball()
        border_ball = ball.ycor()
        out_ball = ball.xcor()
        head_ball = ball.heading()
        if border_ball > 280 or border_ball < -280:
            ball.bounce_ball_wall()
        elif player_1.distance(ball) <= 25 and out_ball == -350 or player_2.distance(ball) <= 25 and out_ball >= 340:
            ball.bounce_ball_paddle()
        elif out_ball >= 390:
            fight_on = False
            time.sleep(1)
            score.track_score_pl1()
        elif out_ball <= -380:
            fight_on = False
            score.track_score_pl2()
            time.sleep(1)

        time.sleep(0.05)


screen.exitonclick()
