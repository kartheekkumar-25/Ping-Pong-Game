from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.x=x
        self.createpaddle()

    def createpaddle(self):
        self.color("black")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.goto(self.x, 0)

    def up(self):
        y=self.ycor()+40
        if y!=320:
            self.goto(self.xcor(),y)

    def down(self):
        y = self.ycor() - 40
        if y!=-320:
            self.goto(self.xcor(), y)


