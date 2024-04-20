from turtle import Turtle

class TurtleMotion:
    def __init__(self, color="pink", shape="turtle", position=(0, -180)):
        self.turtle = Turtle()
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.setpos(position)
        self.turtle.setheading(90)  

    def move_up(self):  
        y = self.turtle.ycor()
        y += 20
        self.turtle.sety(y)

    def move(self):  
        pass  
