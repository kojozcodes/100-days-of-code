from tkinter import *


def button_clicked():
    user_text = input_field.get()
    my_label.config(text=user_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

# Button 1
button_1 = Button(text="Click Me", command=button_clicked)
button_1.grid(row=1, column=1)

# Button 2
button_2 = Button(text="Button 2", command=button_clicked)
button_2.grid(row=0, column=2)

# Entry
input_field = Entry(width=10)
input_field.grid(row=2, column=3)

window.mainloop()
