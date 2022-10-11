from tkinter import *
from tkinter import simpledialog, messagebox
import string
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_new_password():

    source = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password_list = ""
    for _ in range(15):
        password_list = password_list + random.choice(source)
    password_input.insert(0, password_list)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data_to_txt():
    # answer = simpledialog.askstring("Answer The Dialog", f"Your Website is {website_input.get()} \n Your Password is:{password_input.get()}", parent=window)
    # if answer is not None:
    #     print("You have Confirmed That we are good to go")

    if website_input.get() == "" or email_input.get()== "" or password_input.get() == "":
        messagebox.showinfo(title="Error", message="You have Left Some Fields empity")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"This are The details:\n Email:{email_input.get()}\n Password:{password_input.get()} \n Is it Ok to save.")
        if is_ok:
            with open("data.txt", "a") as save_data:
                save_data.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()} \n")
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
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.insert(0, "amaedris1@gmail.com")

email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input=Entry(width=21)
password_input.grid(row=3, column=1)
generate_button = Button(text="Generate Password", command=generate_new_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_data_to_txt)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
