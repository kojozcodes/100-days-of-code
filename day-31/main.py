from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn_dict = {}
# ----------------------- DATA ----------------------------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn_dict = original_data.to_dict(orient="records")
else:
    to_learn_dict = data.to_dict(orient="records")


# ---------------------- CARD FUNCTION ------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    canvas.itemconfig(flash_card_img, image=fc_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(flash_card_img, image=fc_back_img)
    canvas.itemconfig(language_label, fill="white", text="English")
    canvas.itemconfig(word_label, fill="white", text=current_card["English"])


def is_known():
    to_learn_dict.remove(current_card)
    new_data = pandas.DataFrame(to_learn_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ----------------------- UI -------------------------
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)

fc_front_img = PhotoImage(file="./images/card_front.png")
fc_back_img = PhotoImage(file="./images/card_back.png")
flash_card_img = canvas.create_image(400, 263, image=fc_front_img)

language_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
