from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_session = WORK_MIN * 60
    rest_session = SHORT_BREAK_MIN * 60
    long_break_session = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_session)
    elif reps % 2 == 0:
        title_label.config(text="BREAK", fg=PINK)
        count_down(rest_session)
    else:
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_session)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        global reps
        if reps % 2 == 0:
            checkmark.config(text=CHECK * math.floor(reps / 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Counter")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
title_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 29, "bold"))
canvas.grid(row=1, column=1)

start_bttn = Button(text="Start", bg=YELLOW, border=0, font=(FONT_NAME, 10, "normal"), command=start_timer)
start_bttn.grid(row=2, column=0)

reset_bttn = Button(text="Reset", bg=YELLOW, border=0, font=(FONT_NAME, 10, "normal"), command=reset_timer)
reset_bttn.grid(row=2, column=2)

checkmark = Label(bg=YELLOW, fg=GREEN)
checkmark.grid(row=3, column=1)



window.mainloop()