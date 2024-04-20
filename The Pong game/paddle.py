import turtle

class Paddle:
    def __init__(self, color="white", shape="square", stretch_wid=5, stretch_len=1, position=(350, 0)):
        self.turtle = turtle.Turtle()
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
        self.turtle.penup()
        self.turtle.setposition(position)

    def paddle_up(self):
        # Function to move the paddle up
        y = self.turtle.ycor()
        y += 20
        self.turtle.sety(y)

    def paddle_down(self):
        # Function to move the paddle down
        y = self.turtle.ycor()
        y -= 20
        self.turtle.sety(y)
