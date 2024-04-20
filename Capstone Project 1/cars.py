from turtle import Turtle
import random


class Cars:
  colors = [
      "lightcoral", "lightskyblue", "lightgreen", "lightyellow", "lavender",
      "peachpuff"
  ]

  def __init__(self, num_cars, stretch_wid=1, stretch_len=2):
    self.cars = []
    self.num_cars = num_cars
    self.stretch_wid = stretch_wid
    self.stretch_len = stretch_len
    self.create_cars()

  def create_cars(self):
    for i in range(self.num_cars):
      new_car = Turtle("square")
      new_car.penup()
      new_car.shapesize(stretch_wid=self.stretch_wid,
                        stretch_len=self.stretch_len)
      new_car.color(random.choice(self.colors))
      new_car.goto(-180, -180 + i * 40)
      self.cars.append(new_car)

  def move_cars_forward(self):
    for car in self.cars:
      speed = random.uniform(-0.5, 0.7)
      car.forward(speed)
