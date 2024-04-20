from turtle import Screen
from turtlemotion import TurtleMotion
from cars import Cars
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.title("The Turtle Race")
screen.setup(height=400, width=400)
screen.tracer(0)

turtles = TurtleMotion()
scoreboard = Scoreboard()
cars = Cars(num_cars=8, stretch_len=2, stretch_wid=1)


screen.listen()
screen.onkey(turtles.move_up, 'Up')

# Main game loop
game_on = True
while game_on:
  screen.update()
  turtles.move()
  cars.move_cars_forward()

  
  for car in cars.cars:
    if turtles.turtle.distance(car) < 20:  
      scoreboard.game_over()
      game_on = False
      break  

screen.exitonclick()
