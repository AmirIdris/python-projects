from tkinter import *
from tkinter import simpledialog, messagebox
from random import choice, randint, shuffle
from string import ascii_lowercase, digits, punctuation
import pyperclip
import json
# ---------------------------- SEARCH PASSWORD ------------------------------- #


def find_password():
    website = website_input.get()
    if website == "":
        messagebox.showinfo(title="Error", message="You Cannot Search Empty String")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")

        else:
            try:
                result = data[website]
            except KeyError:
                messagebox.showinfo(title="Error", message="No Detail For The website")
            else:
                password = result["password"]
                user_email = result["email"]
                messagebox.showinfo(title="Dialog Info", message=f"Here is Your Password: {password}\n Here is Your Email: {user_email} \n")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_new_password():

    lowercase_letter_range = randint(8, 10)
    number_range = randint(2, 4)
    symbol_ranges = randint(2, 4)
    lowercase_letter_list = [choice(ascii_lowercase) for _ in range(lowercase_letter_range)]
    number_list = [choice(digits) for _ in range(number_range)]
    symbol_list = [choice(punctuation) for _ in range(symbol_ranges)]

    password_list = lowercase_letter_list + number_list + symbol_list
    shuffle(password_list)
    password = ""
    for char in password_list:
        password = password + char

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data_to_txt():
    email = email_input.get()
    website = website_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email":email,
            "password":password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Error", message="You have Left Some Fields empity")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This are The details:\n Email:{email}\n Password:{password} \n Is it Ok to save.")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:

                    # read the data from json file
                    data = json.load(data_file)
                    # update the old data with new data
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # dumping the new data to the json file
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # dumping the new data to the json file
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=120, height=160)
logo_img = PhotoImage(file="img_3.png")
canvas.create_image(80, 100, image=logo_img)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.insert(0, "amaedris1@gmail.com")

email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input=Entry(width=21)
password_input.grid(row=3, column=1)
# Search Button Creation
search = Button(text="Search", bg="Blue", command=find_password)
search.grid(row=1, column=2)
# generate button creation
generate_button = Button(text="Generate Password", command=generate_new_password)
generate_button.grid(row=3, column=2)
# Add Button Creation
add_button = Button(text="Add", width=36, command=save_data_to_txt)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
