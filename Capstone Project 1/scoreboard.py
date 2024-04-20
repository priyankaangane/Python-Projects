from turtle import Turtle


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.level = 1
    self.goto(0, 140)  # Position the scoreboard
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Level: {self.level}",
               align="center",
               font=("Courier", 40, "normal"))

  def increase_level(self):
    self.level += 1
    self.update_scoreboard()

  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write("Game Over", align="center", font=("Courier", 40, "normal"))
