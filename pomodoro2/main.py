#Pomodoro GUI Application

#import modules
from tkinter import *
import math

# ---------------------------- CONSTANTS -----------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#006400"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ---------------------------#
def reset_timer():
    window.after_cancel(timer)
    #change timer_text to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #change the label back to TIMER
    title_label.config(text="TIMER")
    #reset the checkmarks
    check_marks.config(text="")
    #update the reps
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM -----------------------#
def start_timer():
    global REPS
    REPS += 1
    #calculate the time in seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    #if the 1st/3rd/5th/7th rep: (work time)
    # if the 2nd/4th/6th rep: (short break time)
    # if the 8th rep: (long break time)
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="LONG BREAK", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)

# ----------------------- COUNTDOWN MECHANISM ------------------------#
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    #dynamic typing
    if count_sec < 10:
        count_sec =f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        #mark for number of work sessions
        marks= ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ----------------------------- #
window = Tk()
window.title("Pomodoro Project")
window.config(padx=100, pady=50, bg=YELLOW)

#timer label
title_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=("Diary Of A Wimpy Kid Font", 30, "bold"))
title_label.grid(column=1, row=0)

#tkinter canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

#add text over the image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
#checkmarks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
