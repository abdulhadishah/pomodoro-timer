import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, REPS
    window.after_cancel(timer)
    timer = None
    REPS = 0
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro_timer():
    global REPS

    work_duration_sec = WORK_MIN * 60
    short_break_duration_sec = SHORT_BREAK_MIN * 60
    long_break_duration_sec = LONG_BREAK_MIN * 60

    REPS += 1

    if REPS % 8 == 0:
        start_countdown(long_break_duration_sec)
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        start_countdown(short_break_duration_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        start_countdown(work_duration_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_countdown(remaining_seconds):
    minutes = math.floor(remaining_seconds / 60)
    seconds = remaining_seconds % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if remaining_seconds > 0:
        global timer
        timer = window.after(1000, start_countdown, remaining_seconds - 1)
    else:
        start_pomodoro_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_pomodoro_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(font=(FONT_NAME, 18, "normal"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
