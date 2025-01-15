import tkinter, math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
rep = 0
check_mark_counter = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rep, check_mark_counter, timer
    window.after_cancel(timer)    
    rep = 0
    check_mark_counter = 0
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep, check_mark_counter
    
    rep += 1
    
    # If repetition is a certain number, make the time length be relative to what we want
    if rep in [1,3,5,7]:
        timer_label.config(text="Work",fg=GREEN)
        count_down(WORK_MIN*60)
    elif rep in [2,4,6]:
        timer_label.config(text="Break",fg=PINK)  
        check_mark_counter += 1
        check_mark.config(text=CHECK_MARK*check_mark_counter)
        count_down(SHORT_BREAK_MIN*60)
    elif rep == 8:
        timer_label.config(text="Break",fg=RED)
        count_down(LONG_BREAK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else: # If timer hits zero, go to next repetition and continue timer
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

#Timer Label
timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

# Tomato image
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check marks 
check_mark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
check_mark.grid(column=1, row=3)



window.mainloop()
