from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import random
import json
import os


def find_password():
    web_name = enter_web.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Oops', message="No Data File Found")
    else:
        if web_name in data:
            email = data[web_name]["email"]
            password = data[web_name]["password"]
            messagebox.showinfo(title="I found it", message=f"Website: {web_name}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Sorry", message="No details for the website exists.")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    random_password = "".join(password_list)
    enter_pass.insert(0, random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web_entered = enter_web.get()
    email_entered = enter_email.get()
    password_entered = enter_pass.get()
    new_data = {
        web_entered: {
            "email": email_entered,
            "password": password_entered,
        }
    }

    if not web_entered or not email_entered or not password_entered:
        messagebox.showerror(title='Oops', message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_entered, message=f'There are the details entered:\nEmail: {email_entered}\nPassword: {password_entered}\nIs it ok to save?')
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                enter_web.delete(0, 'end')
                enter_pass.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


window = Tk()
window.title('Password Manager')
window.config(padx=25, pady=25, bg=_from_rgb((0, 73, 101)))

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=_from_rgb((0, 73, 101)))

current_dir = os.path.dirname(os.path.abspath(__file__))
key_img = PhotoImage(file=os.path.join(current_dir, 'logo.png'))

canvas.create_image(100, 100, image=key_img)
canvas.grid(column=0, row=0, columnspan=3)

web = Label(text="Website:", fg="white", font=("Courier", 10, "bold"), bg=_from_rgb((0, 73, 101)))
web.grid(column=0, row=1, sticky='W')

email = Label(text="Email:", fg="white", font=("Courier", 10, "bold"), bg=_from_rgb((0, 73, 101)))
email.grid(column=0, row=2, sticky='W')

password = Label(text="Password:", fg="white", font=("Courier", 10, "bold"), bg=_from_rgb((0, 73, 101)))
password.grid(column=0, row=3, sticky='W')

enter_web = Entry(width=25)
enter_web.focus()
# enter_web.grid(column=1, row=1, sticky='W')
enter_web.grid(column=1, row=1)


enter_email = Entry(width=38)
# enter_email.grid(column=1, row=2, columnspan=2, sticky='W')
enter_email.grid(column=1, row=2, columnspan=2)

enter_email.insert(0, '@gmail.com')

enter_pass = Entry(width=25)
# enter_pass.grid(column=1, row=3, sticky='W')
enter_pass.grid(column=1, row=3)


generate_button = Button(text="Generate Password", width=14, bg='gray', highlightthickness=0, font=("Courier", 8, "bold"), command=generate_password)
generate_button.grid(column=2, row=3, sticky='W')

add_button = Button(text="Add", width=48, bg='gray', highlightthickness=0, font=("Courier", 8, "bold"), command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky='W')

search_button = Button(text="Search", width=14, bg='gray', highlightthickness=0, font=("Courier", 8, "bold"), command=find_password)
search_button.grid(column=2, row=1, sticky='W')

window.mainloop()
