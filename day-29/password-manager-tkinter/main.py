from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '.']

    # create a list using letters, numbers and symbols
    password_list = [
                        choice(letters) for _ in range(randint(8, 10))
                    ] + [
                        choice(symbols) for _ in range(randint(2, 4))
                    ] + [
                        choice(numbers) for _ in range(randint(2, 4))
                    ]

    shuffle(password_list)  # random.shuffle method
    password = "".join(password_list)  # .join method in any string

    password_entry.insert(0, password)  # insert generated password into 'password_entry'
    pyperclip.copy(password)  # automatically copy the created password - to after paste ctrl+v


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # if ant entry is empty, get a message error
    if website == "" or password == "" or email == "":
        messagebox.showerror("Oops", "Please, don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUser: {email}"
                                                              f"\nPassword: {password}")
        # if click 'ok', then:
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
            # delete method to erase the entries
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# # # # # # # # # # # # LABELS # # # # # # # # # # #
# web label
web_label = Label(text="Website:")
web_label.grid(row=1, column=0, sticky="E")

# email label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E")

# password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

# # # # # # # # # # # # ENTRIES # # # # # # # # # # #
# web entry
web_entry = Entry()
web_entry.grid(row=1, column=1, columnspan=2, sticky="EW")  # sticky holds East/West side
web_entry.focus()  # set the cursor on web entry

# email entry
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "jordan@gmail.com")  # initial value

# password entry
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# # # # # # # # # # # # BUTTONS # # # # # # # # # # #
# password button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

# add button
add_button = Button(text="Add", width=30, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
