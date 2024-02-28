from tkinter import *

# initiating tkinter object, without tkinter. because we've imported every method above
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=350)

# creating a Label (**kwargs) key word arguments - optional arguments
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
# pack(), place(), or grid()
# my_label.pack()  # pack the Label from top to down, or left to right, and so on
# my_label.place(x=10, y=10)  # starts from top-left and only turns up
my_label.grid(row=0, column=0)


# 2 ways to configure, setting new value directly or calling .config method
my_label["text"] = "New text"  # setting new value tudo text parameter
# my_label.config(font=("Arial", 12))  # setting new value to font parameter

# Entry
input_entry = Entry(width=10)
input_entry.insert(END, string="Some text to begin with")
# input_entry.pack()
input_entry.grid(row=0, column=2)

# setting new value to the my_label["text"] when called on command parameter of the button
def button_click():
    my_label["text"] = input_entry.get()


# Button - without tkinter. because we've imported every method above
button = Button(text="Click me", command=button_click)  # command call the previous function
# button.pack()
button.grid(row=0, column=4)

# Textbox
text = Text(width=30, height=5)
text.focus()  # puts cursor in textbox
text.insert(END, "Example of multi-line text entry")  # text to begin with
print(text.get("1.0", END))  # gets current value in texbox at line 1, character 0
# text.pack()
text.grid(row=2, column=0)


# Spinbox
def spinbox_used():
    # gets the current value in spinbox and print
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
spinbox.grid(row=2, column=2)


# Scale
def scale_used(value):  # Called with current scale value
    print(value)  # prints the current value


scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
scale.grid(row=2, column=4)


# Checkbutton
def checkbutton_used():  # Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()  # IntVar() is a class from tkinter
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
# checkbutton.pack()
checkbutton.grid(row=4, column=0)


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
radiobutton1.grid(row=4, column=2)
radiobutton2.grid(row=5, column=2)


# Listbox
def listbox_used(event):  # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
listbox.grid(row=4, column=4)

# maintain the window opened
window.mainloop()
