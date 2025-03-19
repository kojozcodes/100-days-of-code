from tkinter import *


def convert_miles_to_km():
    mile_value = float(miles_value.get())
    km_value_label.config(text='{0:.2f}'.format(mile_value * 1.609344))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

miles_value = Entry(width=5)
miles_value.grid(row=0, column=1)
miles_value.config(font=("Courier", 15, "bold"))

miles_label = Label(text="Miles", font=("Courier", 15, "bold"))
miles_label.grid(row=0, column=2)
miles_label.grid(padx=5, pady=5)

equal_to_label = Label(text="is equal to", font=("Courier", 15, "bold"))
equal_to_label.grid(row=1, column=0)
equal_to_label.grid(padx=5, pady=5)

km_value_label = Label(text="0", font=("Courier", 15, "bold"))
km_value_label.grid(row=1, column=1)
km_value_label.grid(padx=5, pady=5)

km_label = Label(text="Km", font=("Courier", 15, "bold"))
km_label.grid(row=1, column=2)
km_label.grid(padx=5, pady=5)

calculate_button = Button(text="Calculate", font=("Courier", 15, "bold"), command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)
calculate_button.grid(padx=5, pady=5)

window.mainloop()
