from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.penup()
        self.speed(7)
        self.setheading(randint(-60,60))

    def move(self):
        self.forward(10)

    def wallbounce(self):
        self.setheading(-self.heading())

    def paddlebounce(self):
        self.setheading(180-self.heading())
        self.forward(10)