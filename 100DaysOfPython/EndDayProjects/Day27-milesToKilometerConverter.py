import tkinter

def miles_to_km():
    miles = float(miles_input.get())
    km = miles*1.60934
    km_num_label.config(text=km)


# Window
window = tkinter.Tk()
window.title("Mile to Km Converter")
#window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# is equal to label
text = tkinter.Label(text="is equal to")
text.grid(column=0, row=1)

# Miles Entry
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

# Miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# Km number label
km_num_label = tkinter.Label(text=0)
km_num_label.grid(column=1, row=1)

# Km label
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)


# Calculate Button
calculate_button = tkinter.Button(text="Calculate", command=miles_to_km) #calls button_clicked()
calculate_button.grid(column=1, row=3)

# # new button
# new_button = tkinter.Button(text="new button")
# new_button.grid(column=2, row=0)


window.mainloop()
