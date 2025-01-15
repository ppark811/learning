import tkinter, random, json

WHITE = "#FFFFFF"

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def searchItem():
    input_website = website_textbox.get("1.0", "end-1c")
    
    if len(input_website) > 0:
        
        try:
            with open("./data.json", "r") as file:
                data = json.load(file)
                search_email = data[input_website]["email"]
                search_pass = data[input_website]["password"]
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            tkinter.messagebox.showwarning(title="No Data File", message="No Data File")
        except KeyError:
            tkinter.messagebox.showwarning(title="No Match", message=f"No match for website: {input_website}")
        else:
            tkinter.messagebox.showinfo(title=input_website, message=f"Email:       {search_email}\n"
                                                                     f"Password:    {search_pass}")
    else:
        tkinter.messagebox.showwarning(title="Empty Search", message="Please provide a website")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genPass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    password_list1 = [random.choice(letters) for item in range(nr_letters)]
    password_list2 = [random.choice(symbols) for item in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for item in range(nr_numbers)]
    
    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)
    
    password = "".join(password_list)
        
    password_textbox.delete("1.0", tkinter.END)
    password_textbox.insert("1.0", password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveEntries():

    input_website = website_textbox.get("1.0", "end-1c")
    input_email = email_user_textbox.get("1.0", "end-1c")
    input_pass = password_textbox.get("1.0", "end-1c")
    
    new_data = {
        input_website: {
            "email": input_email,
            "password": input_pass}
        }
    
    
    if len(input_website) == 0 or len(input_pass) == 0 or len(input_email) == 0:
        tkinter.messagebox.showwarning(title="Error", message="Ensure all fields are filled")
    else:    
        is_ok = tkinter.messagebox.askyesno(title=input_website, message=f"These are the details entered:"
                                            f"\nEmail:  {input_email}"
                                            f"\nPass:   {input_pass}"
                                            "\nProceed?")
        if is_ok:
            try:
                with open("./data.json", "r") as file:
                    data = json.load(file) # read old data
            except (json.decoder.JSONDecodeError, FileNotFoundError): # Error if file is empty or does not exist
                with open("./data.json", "w") as file:
                    json.dump(new_data, file, indent=4) # saving updated data
            else:
                data.update(new_data) # updating old data with new data
                with open("./data.json", "w") as file:
                    json.dump(new_data, file, indent=4) # saving updated data
            finally:
                website_textbox.delete("1.0", tkinter.END)
                password_textbox.delete("1.0", tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

# Lock Image
canvas = tkinter.Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_image = tkinter.PhotoImage(file="./logo.png")
canvas.create_image(100,100, image=lock_image)
canvas.grid(column=1, row=0)

# Text labels
website_label = tkinter.Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1, sticky=tkinter.W)
email_user_label = tkinter.Label(text="Email/Username:", bg=WHITE)
email_user_label.grid(column=0, row=2, sticky=tkinter.W)
password_label = tkinter.Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3, sticky=tkinter.W)

# Text boxes
website_textbox = tkinter.Text(height=1, width=25)
website_textbox.grid(column=1, row=1, sticky=tkinter.W)
website_textbox.focus()
email_user_textbox = tkinter.Text(height=1, width=25)
email_user_textbox.grid(column=1, row=2, columnspan=2, sticky=tkinter.W)
email_user_textbox.insert(tkinter.END, "default@email.com")
password_textbox = tkinter.Text(height=1, width=25)
password_textbox.grid(column=1, row=3, sticky=tkinter.W)

# Buttons
search = tkinter.Button(text="Search", width=15, command=searchItem)
search.grid(column=2, row=1, sticky=tkinter.W)
gen_pass = tkinter.Button(text="Generate Password", command=genPass)
gen_pass.grid(column=2, row=3, sticky=tkinter.W)
add_but = tkinter.Button(text="Add", width=44, command=saveEntries)
add_but.grid(column=1, row=4, columnspan=2, sticky=tkinter.W)

window.mainloop()
