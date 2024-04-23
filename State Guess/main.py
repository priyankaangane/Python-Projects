import turtle
from turtle import Screen
import pandas as pd

screen = Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
  answer_state = screen.textinput(title=f"{len(guessed_state)}/50",
  prompt="Guess the next state?") #.title()

  if answer_state=="Exit":#new csv of missing states
     missing_state=[]
     for state in all_states:
      if state not in guessed_state:
        missing_state.append(state)
        new_data=pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

  
  if answer_state in all_states:
    guessed_state.append(answer_state)
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data=data[data['state']==answer_state]
    t.goto(int(state_data.x),int(state_data.y))
    t.write(answer_state)




# screen.mainloop()