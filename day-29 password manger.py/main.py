from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_passoword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # here we use list comphersion for following code
    password_letters = [choice(letters) for char in range(randint(0, 10))]

    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    Password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = Website_entry.get()
    email = Email_entry.get()
    password = Password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Opps!", message="please make sure you haven't left any feilds empty.")

    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"There are the details entered: \n email:{email} \n password:{password} \n is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} : {email} : {password}\n")
                Website_entry.delete(0, END)
                Password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# --------------------------------------------------------------------------------
# labels
Website_label = Label(text="Website:")
Website_label.grid(row=1, column=0)

Email_label = Label(text="Email:")
Email_label.grid(row=2, column=0)

Password_label = Label(text="Password:")
Password_label.grid(row=3, column=0)

# ----------------------------------------------------------------------------
# enteries
Website_entry = Entry(width=35)
Website_entry.grid(row=1, column=1, columnspan=2)
Website_entry.focus()

Email_entry = Entry(width=35)
Email_entry.grid(row=2, column=1, columnspan=2)
Email_entry.insert(0, "harshad9@gmail.com")

Password_entry = Entry(width=26)
Password_entry.grid(row=3, column=1)

# -----------------------------------------------------------------
# Buttons
generate_password_button = Button(
    text="Generate Password", command=generate_passoword)

generate_password_button.grid(row=3, column=2, columnspan=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
