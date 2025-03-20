from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website_name = website_entry.get().title()
    try:
        with open("data.json", mode="r") as password_file:
            password_data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website_name in password_data:
            messagebox.showinfo(title=website_name, message=f"Email: {password_data[website_name]["email"]}"
                                                            f"\nPassword: {password_data[website_name]["password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_name} exists.")
    finally:
        website_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_or_username = email_or_username_entry.get()
    password = password_entry.get()
    new_password_data = {
        website: {
            "email": email_or_username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(file="data.json", mode="r") as password_file:
                data = json.load(password_file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as password_file:
                json.dump(new_password_data, password_file, indent=4)
        else:
            data.update(new_password_data)
            with open(file="data.json", mode="w") as password_file:
                json.dump(data, password_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=26)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2)

email_or_username_label = Label(text="Email/Username:")
email_or_username_label.grid(row=2, column=0)

email_or_username_entry = Entry(width=44)
email_or_username_entry.grid(row=2, column=1, columnspan=2)
email_or_username_entry.insert(END, "kojolihamza@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
