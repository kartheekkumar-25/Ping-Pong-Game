from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(1000,700)
screen.bgcolor("beige")
screen.title("PING PONG")
screen.tracer(0)


pad1=Paddle(-460)
pad2=Paddle(460)

screen.update()
screen.listen()

#paddle controls
screen.onkey(pad2.up,"Up")
screen.onkey(pad2.down,"Down")
screen.onkey(pad1.up,"w")
screen.onkey(pad1.down,"s")

scoreboard=Scoreboard()

ball=Ball()
game_on=True
i=0
time.sleep(2)

# Main game loop
while game_on:
    #increases ball speed
    if i>=100:
        if ball.speed()!=10:
            ball.speed(ball.speed()+1)
            i=0
    i+=1
    ball.move()
    screen.update()
    x_cor=ball.xcor()
    y_cor=ball.ycor()

    #ball collision with top/bottom wall
    if 340<=y_cor or y_cor<=-340:
        ball.wallbounce()

    pad1_yc=pad1.ycor()
    pad2_yc=pad2.ycor()

    #ball collision with paddles
    if (430<x_cor<460 and pad2_yc-60<y_cor<pad2_yc+60) or (-460<x_cor<-430 and pad1_yc-60<y_cor<pad1_yc+60):
        ball.paddlebounce()

    #scores increment
    if x_cor>460:
        scoreboard.ls+=1
        ball.setheading(ball.heading()+180)
        ball.goto(0,0)
        pad1.goto(-460,0)
        pad2.goto(460,0)
        scoreboard.refresh()
        ball.speed(3)

    if x_cor<-460:
        scoreboard.rs+=1
        ball.setheading(ball.heading()+180)
        ball.goto(0,0)
        pad1.goto(-460,0)
        pad2.goto(460,0)
        scoreboard.refresh()
        ball.speed(3)

    #win condition
    if scoreboard.ls==3:
        scoreboard.pad1win()
        game_on=False
    elif scoreboard.rs==3:
        scoreboard.pad2win()
        game_on=False

    time.sleep(0.03)

screen.exitonclick()