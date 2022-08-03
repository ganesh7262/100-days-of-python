import tkinter


from pyparsing import rest_of_line
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    reps=0
    window.after_cancel(timer)
    canvas.itemconfig(count_down_text,text="00:00")
    label.config(text="Timer",fg=GREEN)
    
# ---------------------------- TIMER MECHANISM ------------------------------- #


def call_count_down():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps == 7:
        reps=0
        label.config(fg=RED,text="Break")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(fg=GREEN,text="Work")
        count_down(work_sec)
    else:
        label.config(fg=YELLOW,text="Break")
        count_down(short_break_sec)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min = count//60
    sec = count % 60
    txt = f"{min}:{sec}"
    canvas.itemconfig(count_down_text, text=txt)
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = tkinter.PhotoImage(
    file=r"100 days of python\projects\pomodoro\tomato.png")
canvas.create_image(100, 112, image=tomato_png)
count_down_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = tkinter.Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 25, "bold"), highlightthickness=0, bg=YELLOW)
label.grid(row=0, column=1)


start_button = tkinter.Button(text="Start", command=call_count_down)
start_button.grid(row=2, column=0)


reset_button = tkinter.Button(text="Reset",command=reset)
reset_button.grid(row=2, column=2)


window.mainloop()
