from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    gpassword = "".join(password_list)
    pass_input.delete(0, END)
    pass_input.insert(0, string=gpassword)
    pyperclip.copy(gpassword)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_input.get()
    email = eu_input.get()
    password = pass_input.get()
    new_data = {
        website.title(): {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Field!", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as f:
                d = json.load(f)
        except FileNotFoundError:
            d = new_data
            with open("data.json", "w") as f:
                json.dump(d, f, indent=4)
        else:
            d.update(new_data)
            with open("data.json", "w") as f:
                json.dump(d, f, indent=4)
        finally:
            website_input.delete(0, END)
            eu_input.delete(0, END)
            pass_input.delete(0, END)
            messagebox.showinfo(title="Success", message="Password Saved!")
# ---------------------------- SEARCH --------------------------------- #
def search():
    search_query = website_input.get()
    try:
        with open("data.json", "r") as f:
            d = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No passwords have been saved yet!")
    else:
        if search_query.title() in d:
            username = d.get(f"{search_query.title()}", {}).get('email')
            spassword = d.get(f"{search_query.title()}", {}).get('password')
            pyperclip.copy(spassword)
            messagebox.showinfo(title=f"{search_query.title()}", message=f"Email: {username} \nPassword: {spassword}\n\nPassword has been copied to clipboard!")
        else:
            messagebox.showinfo(title="Not Found", message="There are no passwords saved for this website")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_file)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1)

eu_label = Label(text="Email/Username:")
eu_label.grid(column=0, row=2)

eu_input = Entry(width=35)
eu_input.insert(0, "chakib@chakib.com")
eu_input.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)


pass_input = Entry(width=21)
pass_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()