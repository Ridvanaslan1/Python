from tkinter import *
import tkinter.ttk as ttk
import math

GREEN = '#90A17D'
FONT_NAME = 'Courier'
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
BG_COLOR = '#404258'
reps = 0
timer = None
# ------ Function --------- #


# reset

def reset_timer():
    global reps, timer

    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', background=BG_COLOR,
                       foreground='white', font=(FONT_NAME, 40, 'bold'))
    reps = 0
    start_btn['state'] = NORMAL


# start timer


def start_timer():
    global reps, timer
    start_btn['state'] = DISABLED

    reps += 1
    print(reps)

    if reps % 2 == 0:
        if reps == 8:
            long_break_sec = LONG_BREAK_MIN * 60
            title_label.config(text='Long Break', background=BG_COLOR,
                               foreground='white', font=(FONT_NAME, 40, 'bold'))
            count_down(long_break_sec)
            reps = 0
        else:
            shor_break_sec = SHORT_BREAK_MIN * 60
            title_label.config(text='Short Break', background=BG_COLOR,
                               foreground='white', font=(FONT_NAME, 40, 'bold'))
            count_down(shor_break_sec)
    else:
        title_label.config(text='Work!', background=BG_COLOR,
                           foreground='white', font=(FONT_NAME, 40, 'bold'))
        work_sec = WORK_MIN * 60
        count_down(work_sec)


# count down
def count_down(count):
    global reps, timer
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = root.after(1000, count_down, count-1)
    else:
        start_timer()


# ------ UI SETUP --------- #
root = Tk()
root.title('POMODORO APP')
root.geometry('780x700')
root.resizable(False, False)
root.config(background=BG_COLOR, padx=45, pady=50)

# Icon
image_icon = PhotoImage(file='Timer_icon.png')
root.iconphoto(False, image_icon)


# Labels
title_label = ttk.Label(text='Timer', background=BG_COLOR,
                        foreground='white', font=(FONT_NAME, 40, 'bold'))
title_label.grid(column=1, row=0)

# Canvas setup
canvas = Canvas(width=512, height=512, bg=BG_COLOR, highlightthickness=0)
bg_image = PhotoImage(file='Image_bg.png')
canvas.create_image(256, 256, image=bg_image)
timer_text = canvas.create_text(
    256, 310, text='00:00', fill='#6B728E', font=(FONT_NAME, 50, 'bold'))
canvas.grid(column=1, row=1)

# Buttons
start_btn = ttk.Button(text='Start', command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = ttk.Button(text='Reset', command=reset_timer)
reset_btn.grid(column=2, row=2)

root.mainloop()
