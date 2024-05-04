from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 8
reps = 0
tick = "✔"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
  if timer:
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label4.config(text="")
    my_label1.config(text="Timer")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
  global reps
  reps += 1
  work = WORK_MIN * 60
  short_break = SHORT_BREAK_MIN * 60
  long_break = LONG_BREAK_MIN * 60
  if reps % 2 == 0:
    countdown(short_break)
    my_label1.configure(text="Short Break", foreground="red")
  elif reps % 8 == 0:
    countdown(long_break)
    my_label1.configure(text="Long Break", foreground="blue")
  else:
    countdown(work)
    my_label1.configure(text="Beast Mode", foreground="pink")
  # countdown(1*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
  global tick
  global timer
  count_min = math.floor(count / 60)  #ROUNDING A NUMBER
  count_sec = count % 60
  if count_sec < 0:  #int
    count_sec = f"0{count_sec}"  #str

  canvas.itemconfig(timer_text,
                    text=f"{count_min}:{count_sec}")  #That was so smart(logic)
  if count > 0:
    timer = screen.after(1000, countdown, count - 1)
  else:
    start_timer()
    if reps == 4:
      my_label4.configure(text=tick + str(tick))


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("POMODORO")
screen.configure(bg="black")
canvas = Canvas(width=400, height=400)
img = PhotoImage(file="1.png")

# def sa_somth(thing):
#   print("hi")
# screen.after(1000,sa_somth,"hello")
canvas.create_image(150, 200, image=img)  # Adjust the coordinates here

canvas.create_text(70, 200, text="To the stars!", font=(FONT_NAME, 10, "bold"))
timer_text = canvas.create_text(70,
                                130,
                                text="00:00",
                                font=(FONT_NAME, 20, "bold"))
canvas.grid(row=7, column=1)

title = Label(text="Pomodoro App")
title.grid(column=0, row=0)
title.configure(foreground="white",
                background="Black",
                font=(FONT_NAME, 10, "bold"))

# components
my_label1 = Label(text="TIMER!")
my_label1.grid(row=0, column=1)
my_label1.configure(foreground="peachpuff",
                    background="Black",
                    font=(FONT_NAME, 35, "bold"))

# my_label2=Label(text="00:00")
# my_label2.grid(row=2,column=1)
# my_label2.configure(foreground="peachpuff",background="Black",font=(FONT_NAME,35,"bold"))

button1 = Button(text="START", font=(FONT_NAME), command=start_timer)
button1.grid(row=3, column=1)

my_label3 = Label(text="OR")
my_label3.grid(row=4, column=1)
my_label3.configure(foreground="peachpuff",
                    background="Black",
                    font=(FONT_NAME, 15, "bold"))

button2 = Button(text="STOP", font=(FONT_NAME), command=reset)
button2.grid(row=5, column=1)

my_label4 = Label(text=tick)
my_label4.grid(row=6, column=1)
my_label4.configure(background="black",
                    foreground="pink",
                    font=(FONT_NAME, 15, "bold"))

canvas.grid()
screen.mainloop()  #EVENT HANDLE
