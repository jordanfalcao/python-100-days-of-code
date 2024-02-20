from tkinter import *

# initiating the window
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=400, height=250)

# creating 'is equal' Label
is_equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(row=2, column=1)  # grid (1, 3) (1, 3)
is_equal_label.config(padx=60, pady=20)

# miles label
miles_label = Label(text=" Miles", font=("Arial", 12, "bold"))
miles_label.grid(row=1, column=3)  # grid (1, 3) (1, 3)
miles_label.config(padx=20, pady=20)

# km label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(row=2, column=3)  # grid (1, 3) (1, 3)
km_label.config(padx=20, pady=20)

# result label
conversion_label = Label(text="0", font=("Arial", 12, "bold"))
conversion_label.grid(row=2, column=2)  # grid (1, 3) (1, 3)
conversion_label.config(padx=20, pady=20)

# Entry - set the mile to convert
input_entry = Entry(width=8)
input_entry.focus()
input_entry.grid(row=1, column=2)  # grid (1, 3) (1, 3)


# setting new value to the conversion_label["text"] when called on command parameter of the button
def button_click():
    conversion_label["text"] = round(float(input_entry.get()) * 1.60934, 2)


# Button to call method created before and convert
button = Button(text="Calculate", command=button_click)  # command call the previous function
button.grid(row=3, column=2)  # grid (1, 3) (1, 3)

# maintain the window opened
window.mainloop()
