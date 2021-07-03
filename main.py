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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text ="TIMER")
    tick_mark.config(text = "")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN *60
    if reps == 8:
        countdown(long_break_secs)
        timer_label.config(text = "BREAK", fg = RED)
    elif reps%2 > 0:
        timer_label.config(text = "WORK", fg = GREEN)
        countdown(work_secs)

    else :
        timer_label.config(text = "BREAK", fg = PINK)
        countdown(short_break_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "/"
        tick_mark.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg =YELLOW)

canvas = Canvas(width = 200,height = 224, bg =YELLOW, highlightthickness = 0)
img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = img)
timer_text = canvas.create_text(100, 120, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)


timer_label = Label(text = "TIMER", font = (FONT_NAME, 35, "bold"), fg=GREEN, bg= YELLOW )
timer_label.grid(row = 0, column = 1)

start_button = Button(text = "START", highlightthickness = 0, command= start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "RESET", highlightthickness = 0, command = reset_timer)
reset_button.grid(row = 2, column = 2)

tick_mark = Label(text = "✔️", fg =GREEN, bg =YELLOW)
tick_mark.grid(row = 3, column = 1 )

window.mainloop()
