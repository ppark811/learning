import tkinter

def button_clicked():
    string = text_input.get()
    my_label.config(text=string)


# Window
window = tkinter.Tk()
window.title("GUI project")
window.minsize(width=500, height =300)

# Label
my_label = tkinter.Label(text="New Text", font=("Arial", 24, "bold"))
my_label.grid(column=0, row = 0)

# Entry
text_input = tkinter.Entry(width=18)
text_input.grid(column=3, row = 2)

# Button
button = tkinter.Button(text="click me", command=button_clicked) #calls button_clicked()
button.grid(column=1, row=1)

# new button
new_button = tkinter.Button(text="new button")
new_button.grid(column=2, row=0)


window.mainloop()