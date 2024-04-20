from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("The Pong Game!")
screen.setup(height=600, width=800)
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))

screen.listen()
screen.onkey(r_paddle.paddle_up, 'Up')
screen.onkey(r_paddle.paddle_down, 'Down')
screen.onkey(l_paddle.paddle_up, 'w')
screen.onkey(l_paddle.paddle_down, 's')

game_on = True
while game_on:
    screen.update()
    ball.move()
    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.bounce()
    if (ball.ball.distance(r_paddle.turtle.position()) < 50 and ball.ball.xcor() > 340) or \
       (ball.ball.distance(l_paddle.turtle.position()) < 50 and ball.ball.xcor() < -340):
        ball.bounce_1()
      
    if ball.ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.ball.xcor() < -380:
         ball.reset_position()
         scoreboard.r_point()
        

screen.exitonclick()
