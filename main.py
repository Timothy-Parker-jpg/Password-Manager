from tkinter import *
from tkinter import messagebox
import string
from random import choice
import pyperclip
import json
import tkinter.font as font

button_color = "#5F7A61"
bg_color = "#444941"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def search():
    data = file_read()
    website_name = website_entry.get()
    try:
        messagebox.showinfo(title="Website Credentials", message=f"Email/Username: {data[website_name]['email/username']}.\n"
                                                                 f"Password: {data[website_name]['password']}")
    except KeyError:
        messagebox.showinfo(title="Website Credentials",
                            message="No matching Credentials")

def generate_password():
    password_entry.delete(0, "end")
    letters_symbols = string.ascii_letters + string.punctuation
    password = []
    for i in range(15):
        character = choice(letters_symbols)
        password.append(character)
    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    return password
# ---------------------------- SAVE PASSWORD ------------------------------- #
def file_read():
    with open("data.json", "r") as f:
        data = json.load(f)
        return data
def file_write(new_data):
    with open("data.json", "w") as f:
        json.dump(new_data, f, indent=4)

def add_credentials():
    website_name = website_entry.get()
    username_email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email/username": username_email,
            "password": password
        }
    }
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message="Website and Password fields must be filled.")
    else:
        is_okay = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \n"
                                                                      f"Email: {username_email} \n"
                                                                      f"Password: {password}")
        if is_okay:
            try:
                data = file_read()
                data.update(new_data)
            except (FileNotFoundError, json.JSONDecodeError):
                file_write(new_data)
            else:
                file_write(new_data)
            finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)
window.configure(bg=bg_color)
font = font.Font(family="arial", weight="bold")
#LOGO
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=250, height=250, highlightthickness=0, bg=bg_color)
canvas.create_image(125, 150, image=logo)
canvas.grid(row=0, column=2)
#Buttons
generate_password_button = Button(text="Generate Password", width=14, command=generate_password, bg=button_color)
add_login_credentials_button = Button(text="Add", command=add_credentials, bg=button_color)
search_button = Button(text="Search", width=14, command=search, bg=button_color)
#labels
website_entry_label = Label(text="Website Name:", bg=bg_color, font=font)
email_username_entry_label = Label(text="Username/Email:", bg=bg_color, font=font)
password_entry_label = Label(text="Password:", bg=bg_color, font=font)
#Entry fields
website_entry = Entry(width=22, bg=button_color)
email_username_entry = Entry(width=40, bg=button_color)
password_entry = Entry(width=22, bg=button_color)
#Window Design
website_entry_label.grid(row=2, column=1)
website_entry.grid(row=2, column=2, sticky="w")
search_button.grid(row=2, column=2, sticky="e")
email_username_entry_label.grid(row=3, column=1)
email_username_entry.grid(row=3, column=2,sticky="ew")
generate_password_button.grid(row=4, column=2, sticky="e")
password_entry_label.grid(row=4, column=1)
password_entry.grid(row=4, column=2, sticky="w")
add_login_credentials_button.grid(row=5, column=2, sticky="ew")
#Functionality
website_entry.focus()
email_username_entry.insert(0, "Timothyparker1996@gmail.com")

window.mainloop()
