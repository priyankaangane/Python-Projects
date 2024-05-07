from tkinter import *

FONT_NAME = "Courier"
from tkinter import messagebox
import random

screen = Tk()
screen.title("Password Manager")
screen.configure(background="black")
screen.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=img)
canvas.config(background="black")

#Password Generator Project

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  # Using list comprehension to generate password_list
  password_list = [random.choice(letters) for _ in range(nr_letters)]
  password_list += [random.choice(symbols) for _ in range(nr_symbols)]
  password_list += [random.choice(numbers) for _ in range(nr_numbers)]
  random.shuffle(password_list)

  # Using join to concatenate characters in password_list
  password = "".join(password_list)
  # print(f"Your password is: {password}")
  entry3.insert(END, password)


# -------------------------------Save in docs--------------------------------------#
def add():
  info = []
  info.append(entry1.get())
  info.append(entry2.get())
  info.append(entry3.get())
  if len(entry1.get()) == 0 and len(entry3.get()) == 0:
    messagebox.showinfo(title="Warning",
                        message="You haven't entered your details")
  else:

    is_ok = messagebox.askokcancel(
        title="POP-UP",
        message=f"These are the details entered:\n{info}\nIs it ok to save?")

    is_ok = True
    with open("info_docs.txt", "a") as file:
      for item in info:
        file.write("|".join(info) + "\n")
        entry1.delete(0, END)
        entry3.delete(0, END)


# -------------------------------Message box-------------------------------------#

# -------------------------------COMPONENTS/UI DESIGN--------------------------------------#
label = Label(text="Password Generator!!")
label.configure(background="black", foreground="white")
label.grid(row=0, column=1)  #columnspan

label2 = Label(text="Website:")
label2.configure(background="black", foreground="white", padx=20, pady=20)
label2.grid(row=2, column=0)

entry1 = Entry(width=35)
entry1.focus()
entry1.insert(END, string="")
entry1.grid(row=2, column=1, columnspan=3)

label3 = Label(text="Email/username:")
label3.configure(background="black", foreground="white")
label3.grid(row=3, column=0)

entry2 = Entry(width=35)
entry2.insert(END, string="")
entry2.grid(row=3, column=1, columnspan=3)
entry2.insert(0, "priyanka18@gmail.com")

label4 = Label(text="Password")
label4.configure(background="black", foreground="white", pady=20, padx=10)
label4.grid(row=4, column=0)

entry3 = Entry(width=21)
entry3.insert(END, string="")
# entry3.insert(0,password)
entry3.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
# print(entry3.get())

button2 = Button(text="Generate Password", command=generate_password)
button2.config(width=11, background="peachpuff")
button2.grid(row=4, column=3)

button1 = Button(text="ADD", command=add)
button1.config(width=36, background="peachpuff")
button1.grid(row=5, column=1, columnspan=3, padx=2, pady=5)

# --------------------------------------------------------------------------------
canvas.grid(row=1, column=1)
screen.mainloop()
