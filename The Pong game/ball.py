from turtle import Turtle

class Ball:
    def __init__(self, color="white", shape="circle", stretch_wid=1, stretch_len=1, position=(0, 0)):
        self.ball = Turtle()
        self.ball.shape(shape)
        self.ball.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
        self.ball.penup()
        self.ball.setpos(position)
        self.ball.color(color)
        self.x_move = 0.5
        self.y_move = 0.5

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.setpos(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_1(self):
        self.x_move *= -1

    def reset_position(self):
        self.ball.goto(0, 0)
        self.bounce()
     