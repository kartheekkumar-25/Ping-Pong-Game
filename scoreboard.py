from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.ls=0
        self.rs=0
        self.penup()
        self.color("black")
        self.goto(0,290)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.ls}  :  {self.rs}",align="center",font=("Arial",35,"bold"))

    def pad1win(self):
        self.goto(0,0)
        self.color("maroon")
        self.write(f"L Player WON", align="center", font=("Arial", 25, "bold"))

    def pad2win(self):
        self.goto(0,0)
        self.color("maroon")
        self.write(f"R Player WON", align="center", font=("Arial", 25, "bold"))